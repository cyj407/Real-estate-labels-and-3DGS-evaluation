"""
Report generation for 3DGS reconstruction quality evaluation.
Creates markdown reports with visualizations and comparisons.
"""

import json
from pathlib import Path
from typing import Dict, List
import logging
import os

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class ReportGenerator:
    """Generates comprehensive evaluation reports."""
    
    def __init__(self, results_dir: str = "results"):
        """
        Initialize report generator.
        
        Args:
            results_dir: Directory containing evaluation results
        """
        self.results_dir = Path(results_dir)
    
    def generate_report(self, render_name: str, results: Dict) -> str:
        """
        Generate markdown report for a single render.
        
        Args:
            render_name: Name of the render
            results: Evaluation results dictionary
            
        Returns:
            Markdown report content
        """
        report = []
        
        # Header
        report.append(f"# 3DGS Reconstruction Quality Report: {render_name}\n")
        report.append(f"**Overall Score**: {results.get('overall_score', 0):.2f}/100\n")
        report.append(f"**Number of Views Evaluated**: {results.get('num_views', 0)}\n")
        report.append(f"**Render URL**: {results.get('render_url', 'N/A')}\n")
        report.append("\n---\n")
        
        # CV Metrics Section
        report.append("\n## Computer Vision Metrics\n")
        cv_results = results.get("cv_metrics", {})
        
        if "blur" in cv_results:
            blur = cv_results["blur"]
            report.append("\n### Blur Detection (Laplacian Variance)\n")
            report.append(f"- **Quality Score**: {blur.get('quality_score', 0):.2f}/100\n")
            report.append(f"- **Mean Laplacian**: {blur.get('mean', 0):.2f}\n")
            report.append(f"- **Std Dev**: {blur.get('std', 0):.2f}\n")
            report.append(f"- **Range**: [{blur.get('min', 0):.2f}, {blur.get('max', 0):.2f}]\n")
            report.append(f"\n*Higher Laplacian variance indicates sharper images.*\n")
        
        if "edge_consistency" in cv_results:
            edge = cv_results["edge_consistency"]
            report.append("\n### Edge Consistency\n")
            report.append(f"- **Consistency Score**: {edge.get('consistency_score', 0):.2f}/100\n")
            report.append(f"- **Mean Edge Density**: {edge.get('mean_density', 0):.4f}\n")
            report.append(f"- **Std Dev**: {edge.get('std_density', 0):.4f}\n")
            report.append(f"\n*Lower standard deviation indicates more consistent edges across views.*\n")
        
        if "brisque" in cv_results:
            brisque = cv_results["brisque"]
            report.append("\n### BRISQUE Quality Assessment\n")
            report.append(f"- **Quality Score**: {brisque.get('quality_score', 0):.2f}/100\n")
            report.append(f"- **Mean Score**: {brisque.get('mean', 0):.2f}\n")
            report.append(f"- **Std Dev**: {brisque.get('std', 0):.2f}\n")
            report.append(f"\n*No-reference quality metric based on natural scene statistics.*\n")
        
        # VLM Metrics Section
        report.append("\n---\n")
        report.append("\n## Vision Language Model Metrics\n")
        vlm_results = results.get("vlm_metrics", {})
        
        if isinstance(vlm_results, dict) and "model" in vlm_results:
            report.append(f"\n**Model**: {vlm_results.get('model', 'N/A')}\n")
            
            if "quality" in vlm_results:
                quality = vlm_results["quality"]
                report.append("\n### Overall Quality Assessment\n")
                report.append(f"- **Quality Score**: {quality.get('quality_score', 0):.2f}/100\n")
                report.append(f"- **Mean Rating**: {quality.get('mean', 0):.2f}/10\n")
                report.append(f"- **Std Dev**: {quality.get('std', 0):.2f}\n")
                report.append(f"- **Range**: [{quality.get('min', 0):.2f}, {quality.get('max', 0):.2f}]\n")
            
            if "artifacts" in vlm_results:
                artifacts = vlm_results["artifacts"]
                report.append("\n### Artifact Detection\n")
                report.append(f"- **Quality Score**: {artifacts.get('quality_score', 0):.2f}/100\n")
                report.append(f"- **Mean Severity**: {artifacts.get('mean_severity', 0):.2f}/10\n")
                report.append(f"- **Std Dev**: {artifacts.get('std_severity', 0):.2f}\n")
                report.append(f"\n*Lower severity indicates fewer visual artifacts (ghosting, floating blobs, etc.).*\n")
            
            if "structural" in vlm_results:
                structural = vlm_results["structural"]
                report.append("\n### Structural Quality\n")
                report.append(f"- **Quality Score**: {structural.get('quality_score', 0):.2f}/100\n")
                report.append(f"- **Mean Rating**: {structural.get('mean', 0):.2f}/10\n")
                report.append(f"- **Std Dev**: {structural.get('std', 0):.2f}\n")
                report.append(f"\n*Higher rating indicates better structural integrity (no warped walls, misaligned edges, etc.).*\n")
        
        
        # Detailed View Analysis
        report.append("\n---\n")
        report.append("\n## Detailed View Analysis\n")
        views = results.get("views", [])
        
        if views:
            for i, view in enumerate(views):
                path = Path(view["screenshot_path"])
                if path.exists():
                    # Calculate relative path for markdown
                    try:
                        # Use path relative to project root
                        # User requested format: captured_views/ktv75/view_000_000deg.png
                        project_root = Path(__file__).parent.parent
                        rel_path = os.path.relpath(path.absolute(), project_root.absolute())
                    except Exception:
                        rel_path = path.absolute()
                        
                    report.append(f"\n### View {i+1} ({view.get('angle', 0):.0f}°)\n")
                    report.append(f"![View {i+1}]({rel_path})\n")
                    
                    # VLM Analysis
                    vlm_data = view.get("vlm_analysis")
                    if vlm_data:
                        report.append("\n**VLM Analysis**:\n")
                        
                        # Score
                        q = vlm_data.get("overall_score")
                        if q is not None:
                             report.append(f"**Score**: {q}/10\n\n")

                        if vlm_data.get("summary"):
                            report.append(f"> *{vlm_data.get('summary')}*\n\n")
                        
                        # Defects
                        defects = vlm_data.get("structural_defects") or {}
                        artifacts = vlm_data.get("texture_artifacts") or {}
                        
                        issues = []
                        for k, v in defects.items():
                            if isinstance(v, dict) and v.get("present"):
                                 desc = v.get("description", "")
                                 issues.append(f"- ⚠️ **{k.replace('_', ' ').title()}**: {desc}")
                        
                        for k, v in artifacts.items():
                            if isinstance(v, dict) and v.get("present"):
                                 desc = v.get("description", "")
                                 issues.append(f"- 🎨 **{k.replace('_', ' ').title()}**: {desc}")

                        if issues:
                            report.append("**Detected Issues**:\n" + "\n".join(issues) + "\n")
                        else:
                            report.append("No significant defects detected.\n")
        
        return "\n".join(report)
    
    def generate_comparison_report(self, all_results: Dict[str, Dict]) -> str:
        """
        Generate comparative report across all renders.
        
        Args:
            all_results: Dictionary of all evaluation results
            
        Returns:
            Markdown comparison report
        """
        report = []
        
        # Header
        report.append("# 3DGS Reconstruction Quality Comparison\n")
        report.append(f"**Number of Renders Evaluated**: {len(all_results)}\n")
        report.append("\n---\n")
        
        # Overall ranking
        report.append("## Overall Ranking\n")
        
        # Sort by overall score
        sorted_results = sorted(
            [(name, res) for name, res in all_results.items() if "error" not in res],
            key=lambda x: x[1].get("overall_score", 0),
            reverse=True
        )
        
        report.append("| Rank | Render Name | Overall Score | Views |")
        report.append("|------|-------------|---------------|-------|")
        
        for i, (name, res) in enumerate(sorted_results):
            score = res.get("overall_score", 0)
            num_views = res.get("num_views", 0)
            report.append(f"| {i+1} | {name} | {score:.2f}/100 | {num_views} |")
        
        # Detailed comparison table
        report.append("---\n")
        report.append("## Detailed Metric Comparison\n")
        
        # Build comparison table
        report.append("| Render | Blur | Edge | BRISQUE | VLM Quality | VLM Artifacts | VLM Structural |")
        report.append("|--------|------|------|---------|-------------|---------------|----------------|")
        
        for name, res in sorted_results:
            cv = res.get("cv_metrics", {})
            vlm = res.get("vlm_metrics", {})
            
            blur_score = cv.get("blur", {}).get("quality_score", 0)
            edge_score = cv.get("edge_consistency", {}).get("quality_score", 0)
            brisque_score = cv.get("brisque", {}).get("quality_score", 0)
            vlm_quality = vlm.get("quality", {}).get("quality_score", 0) if isinstance(vlm, dict) else 0
            vlm_artifacts = vlm.get("artifacts", {}).get("quality_score", 0) if isinstance(vlm, dict) else 0
            vlm_structural = vlm.get("structural", {}).get("quality_score", 0) if isinstance(vlm, dict) else 0
            
            report.append(f"| {name} | {blur_score:.1f} | {edge_score:.1f} | {brisque_score:.1f} | {vlm_quality:.1f} | {vlm_artifacts:.1f} | {vlm_structural:.1f} |")
        
        # Insights
        report.append("---\n")
        report.append("## Key Insights\n")
        
        if sorted_results:
            best_name, best_res = sorted_results[0]
            worst_name, worst_res = sorted_results[-1]
            
            report.append(f"\n### Best Performing Render: **{best_name}**\n")
            report.append(f"- Overall Score: {best_res.get('overall_score', 0):.2f}/100\n")
            
            # Identify strengths
            cv = best_res.get("cv_metrics", {})
            vlm = best_res.get("vlm_metrics", {})
            
            strengths = []
            if cv.get("blur", {}).get("quality_score", 0) > 70:
                strengths.append("Sharp images (high blur score)")
            if cv.get("edge_consistency", {}).get("quality_score", 0) > 70:
                strengths.append("Consistent edges across views")
            if isinstance(vlm, dict) and vlm.get("quality", {}).get("quality_score", 0) > 70:
                strengths.append("High VLM quality rating")
            
            if strengths:
                report.append(f"\n**Strengths**: {', '.join(strengths)}\n")
            
            if len(sorted_results) > 1:
                report.append(f"\n### Lowest Performing Render: **{worst_name}**\n")
                report.append(f"- Overall Score: {worst_res.get('overall_score', 0):.2f}/100\n")
        
        return "\n".join(report)
    
    def save_all_reports(self, all_results: Dict[str, Dict]):
        """
        Generate and save all reports.
        
        Args:
            all_results: Dictionary of all evaluation results
        """
        # Individual reports
        for name, results in all_results.items():
            if "error" in results:
                continue
            
            report_content = self.generate_report(name, results)
            report_path = self.results_dir / f"{name}_report.md"
            
            with open(report_path, "w") as f:
                f.write(report_content)
            
            logger.info(f"Report saved: {report_path}")
        
        # Comparison report
        comparison_content = self.generate_comparison_report(all_results)
        comparison_path = self.results_dir / "comparison_report.md"
        
        with open(comparison_path, "w") as f:
            f.write(comparison_content)
        
        logger.info(f"Comparison report saved: {comparison_path}")


if __name__ == "__main__":
    # Test report generation
    results_dir = Path("results")
    
    if not results_dir.exists():
        print("No results directory found. Run evaluation first.")
    else:
        generator = ReportGenerator(str(results_dir))
        
        # Load all results
        all_results = {}
        for result_file in results_dir.glob("*_results.json"):
            with open(result_file) as f:
                data = json.load(f)
                all_results[data["render_name"]] = data
        
        if all_results:
            generator.save_all_reports(all_results)
            print("Reports generated successfully!")
        else:
            print("No results found.")
