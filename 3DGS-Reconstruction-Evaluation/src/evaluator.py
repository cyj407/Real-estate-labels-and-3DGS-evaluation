"""
Main evaluation pipeline for 3DGS reconstruction quality assessment.
Orchestrates view capture, CV metrics, and VLM metrics.
"""

import json
import asyncio
from pathlib import Path
from typing import Dict, List, Optional
import logging
import yaml
import numpy as np

from src.capture.view_capturer import ViewCapturer
from src.metrics.cv_metrics import evaluate_all_cv_metrics
from src.metrics.vlm_metrics import evaluate_all_vlm_metrics

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class ReconstructionEvaluator:
    """
    Main evaluator for 3DGS reconstruction quality.
    Combines CV and VLM metrics for comprehensive assessment.
    """
    
    def __init__(self, config_path: str = "config.yaml"):
        """
        Initialize evaluator.
        
        Args:
            config_path: Path to configuration file
        """
        self.config_path = Path(config_path)
        
        # Load configuration
        with open(self.config_path) as f:
            self.config = yaml.safe_load(f)
        
        # Initialize components
        self.view_capturer = ViewCapturer(self.config)
        
        # Output directory
        self.output_dir = Path(self.config.get("output", {}).get("results_dir", "results"))
        self.output_dir.mkdir(parents=True, exist_ok=True)
        
        logger.info("ReconstructionEvaluator initialized")
    
    async def evaluate_render(
        self, 
        render_name: str, 
        render_url: str,
        skip_capture: bool = False
    ) -> Dict:
        """
        Evaluate a single 3DGS render.
        
        Args:
            render_name: Name of the render
            render_url: URL of the 3DGS viewer
            skip_capture: Skip view capture and use existing images
            
        Returns:
            Dictionary with all evaluation results
        """
        logger.info(f"\n{'='*60}")
        logger.info(f"Evaluating: {render_name}")
        logger.info(f"{'='*60}")
        
        # Capture views or load existing
        if skip_capture:
            logger.info("Skipping capture, loading existing views...")
            views = self.view_capturer.load_existing_views(render_name)
        else:
            logger.info("Capturing views...")
            views = await self.view_capturer.capture_views(render_name, render_url)
        
        if not views:
            logger.error(f"No views available for {render_name}")
            return {"error": "No views available"}
        
        view_paths = [v["screenshot_path"] for v in views]
        logger.info(f"Evaluating {len(view_paths)} views")
        
        # Run CV metrics
        logger.info("\n--- Running CV Metrics ---")
        cv_results = evaluate_all_cv_metrics(view_paths, self.config)
        
        # Run VLM metrics
        logger.info("\n--- Running VLM Metrics ---")
        vlm_results = evaluate_all_vlm_metrics(view_paths, self.config)
        
        # Merge VLM per-view details into views list
        if isinstance(vlm_results, dict) and "image_details" in vlm_results:
            # Create lookup by filename
            vlm_lookup = {d.get("image_path"): d for d in vlm_results["image_details"]}
            
            for view in views:
                try:
                    p = Path(view["screenshot_path"])
                    if p.name in vlm_lookup:
                        detail = vlm_lookup[p.name]
                        # Inject detailed analysis
                        view["vlm_analysis"] = {
                            "overall_score": detail.get("overall_score"),
                            "summary": detail.get("summary"),
                            "structural_defects": detail.get("structural_defects"),
                            "texture_artifacts": detail.get("texture_artifacts"),
                            "subscores": detail.get("subscores")
                        }
                except Exception as e:
                    logger.warning(f"Failed to merge VLM details for view: {e}")
        
        # Compute overall score
        overall_score = self._compute_overall_score(cv_results, vlm_results)
        
        # Compile results
        results = {
            "render_name": render_name,
            "render_url": render_url,
            "num_views": len(views),
            "cv_metrics": cv_results,
            "vlm_metrics": vlm_results,
            "overall_score": overall_score,
            "views": views
        }
        
        # Save results
        self._save_results(render_name, results)
        
        logger.info(f"\n{'='*60}")
        logger.info(f"Overall Score for {render_name}: {overall_score:.2f}/100")
        logger.info(f"{'='*60}\n")
        
        return results
    
    def _compute_overall_score(self, cv_results: Dict, vlm_results: Dict) -> float:
        """
        Compute weighted overall quality score.
        
        Args:
            cv_results: CV metric results
            vlm_results: VLM metric results
            
        Returns:
            Overall score (0-100)
        """
        weights = self.config.get("weights", {})
        scores = []
        
        # CV metric scores
        if "blur" in cv_results and "quality_score" in cv_results["blur"]:
            scores.append((cv_results["blur"]["quality_score"], weights.get("blur", 0.15)))
        
        if "edge_consistency" in cv_results and "quality_score" in cv_results["edge_consistency"]:
            scores.append((cv_results["edge_consistency"]["quality_score"], weights.get("edge_consistency", 0.15)))
        
        if "brisque" in cv_results and "quality_score" in cv_results["brisque"]:
            scores.append((cv_results["brisque"]["quality_score"], weights.get("brisque", 0.15)))
        
        if "maniqa" in cv_results and "quality_score" in cv_results["maniqa"]:
            scores.append((cv_results["maniqa"]["quality_score"], weights.get("maniqa", 0.15)))
        
        # VLM metric scores
        if isinstance(vlm_results, dict) and "quality" in vlm_results:
            scores.append((vlm_results["quality"]["quality_score"], weights.get("vlm_quality", 0.20)))
        
        if isinstance(vlm_results, dict) and "artifacts" in vlm_results:
            scores.append((vlm_results["artifacts"]["quality_score"], weights.get("vlm_artifacts", 0.10)))
        
        if isinstance(vlm_results, dict) and "structural" in vlm_results:
            scores.append((vlm_results["structural"]["quality_score"], weights.get("vlm_structural", 0.10)))
        
        if not scores:
            return 0.0
        
        # Compute weighted average
        total_weight = sum(w for _, w in scores)
        if total_weight == 0:
            return 0.0
        
        weighted_sum = sum(score * weight for score, weight in scores)
        overall = weighted_sum / total_weight
        
        return float(overall)
    
    def _save_results(self, render_name: str, results: Dict):
        """Save evaluation results to JSON file."""
        output_file = self.output_dir / f"{render_name}_results.json"
        
        with open(output_file, "w") as f:
            json.dump(results, f, indent=2)
        
        logger.info(f"Results saved to: {output_file}")
    
    async def evaluate_all_renders(self, skip_capture: bool = False) -> Dict[str, Dict]:
        """
        Evaluate all renders in configuration.
        
        Args:
            skip_capture: Skip view capture and use existing images
            
        Returns:
            Dictionary mapping render names to their results
        """
        renders = self.config.get("renders", [])
        all_results = {}
        
        for render in renders:
            name = render["name"]
            url = render["url"]
            
            try:
                results = await self.evaluate_render(name, url, skip_capture)
                all_results[name] = results
            except Exception as e:
                logger.error(f"Failed to evaluate {name}: {e}")
                all_results[name] = {"error": str(e)}
        
        # Generate comparative report
        self._generate_comparison(all_results)
        
        return all_results
    
    def _generate_comparison(self, all_results: Dict[str, Dict]):
        """
        Generate comparison report across all renders.
        
        Args:
            all_results: Dictionary of all evaluation results
        """
        comparison = {
            "renders": [],
            "ranking": []
        }
        
        for name, results in all_results.items():
            if "error" in results:
                continue
            
            comparison["renders"].append({
                "name": name,
                "overall_score": results.get("overall_score", 0),
                "num_views": results.get("num_views", 0)
            })
        
        # Sort by overall score (descending)
        comparison["renders"].sort(key=lambda x: x["overall_score"], reverse=True)
        
        # Create ranking
        for i, render in enumerate(comparison["renders"]):
            comparison["ranking"].append({
                "rank": i + 1,
                "name": render["name"],
                "score": render["overall_score"]
            })
        
        # Save comparison
        comparison_file = self.output_dir / "comparison.json"
        with open(comparison_file, "w") as f:
            json.dump(comparison, f, indent=2)
        
        logger.info(f"\nComparison saved to: {comparison_file}")
        
        # Print ranking
        logger.info("\n" + "="*60)
        logger.info("FINAL RANKING")
        logger.info("="*60)
        for item in comparison["ranking"]:
            logger.info(f"{item['rank']}. {item['name']}: {item['score']:.2f}/100")
        logger.info("="*60 + "\n")


async def main():
    """Main entry point for testing."""
    import os
    
    # Initialize evaluator
    evaluator = ReconstructionEvaluator()
    
    # Evaluate all renders
    results = await evaluator.evaluate_all_renders(skip_capture=False)
    
    print("\nEvaluation complete!")
    print(f"Results saved to: {evaluator.output_dir}")


if __name__ == "__main__":
    asyncio.run(main())
