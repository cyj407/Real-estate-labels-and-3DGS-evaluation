"""
Vision Language Model-based metrics for 3DGS reconstruction quality evaluation.
Uses OpenAI Vision API (GPT-5-nano) for semantic quality assessment.
"""

import time
import base64
from pathlib import Path
from typing import Dict, List, Union, Optional
import logging
import re
import os

try:
    from openai import OpenAI
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False
    logging.warning("openai not available. VLM metrics will be disabled.")

import numpy as np

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class VLMEvaluator:
    """
    Evaluates 3DGS reconstruction quality using Vision Language Models.
    Provides quality scoring, artifact detection, and structural defect analysis.
    """
    
    def __init__(self, config: Dict):
        """
        Initialize VLM evaluator.
        
        Args:
            config: Configuration dictionary
        """
        if not OPENAI_AVAILABLE:
            raise ImportError("openai package required for VLM metrics")
        
        self.config = config
        self.vlm_config = config.get("vlm_metrics", {})
        
        self.client = OpenAI()
        
        self.model_name = self.vlm_config.get("model", "gpt-5-nano")
        self.max_retries = self.vlm_config.get("max_retries", 3)
        self.rate_limit_delay = self.vlm_config.get("rate_limit_delay", 1.0)
        
        self.system_prompt = \
        """
        You are a professional 3D reconstruction quality inspector specializing in 3D Gaussian Splatting (3DGS) renderings.

        Your task is to evaluate whether a given rendered image is visually consistent,
        structurally correct, and physically plausible as a real-world scene.

        You MUST:
        - Focus on geometric structure, spatial consistency, and texture fidelity
        - Ignore artistic style or aesthetic preferences
        - Base your judgment only on visual evidence in the image
        - Be strict and conservative: minor artifacts should reduce scores

        For each image, perform the following steps:
        Step 1: Overall Visual Consistency

        Answer the following question:

        "How visually consistent and realistic is this rendering as a reconstruction
        of a real 3D scene?"

        Give a single integer score from 1 to 10:
        - 10 = indistinguishable from a real photograph
        - 7–9 = mostly realistic, minor artifacts
        - 4–6 = noticeable reconstruction errors
        - 1–3 = severe artifacts, clearly broken geometry
        Output format:
        "overall_score": <integer 1-10>
        
        Step 2: Structural Integrity Check

        Carefully inspect the image for the following geometric defects.
        For each defect:
        - Answer YES or NO
        - If YES, briefly describe where it appears
        Output format:
        "structural_defects": {
        "curved_or_warped_walls": { "present": true/false, "description": "" },
        "misaligned_edges": { "present": true/false, "description": "" },
        "collapsed_or_melted_geometry": { "present": true/false, "description": "" },
        "depth_or_perspective_errors": { "present": true/false, "description": "" }
        }

        Step 3: Texture and Appearance Artifacts

        Inspect the image for rendering or texture-related artifacts commonly seen
        in 3DGS or NeRF reconstructions.
        Output format:
        "texture_artifacts": {
        "ghosting": { "present": true/false, "description": "" },
        "floating_artifacts": { "present": true/false, "description": "" },
        "over_blur": { "present": true/false, "description": "" },
        "texture_inconsistency": { "present": true/false, "description": "" }
        }

        Step 4: Subscores

        Provide the following subscores from 1 to 10:
        - geometry_score: structural correctness
        - texture_score: texture sharpness and stability
        - consistency_score: multi-surface and spatial coherence
        Output format:
        "subscores": {
        "geometry_score": <integer 1-10>,
        "texture_score": <integer 1-10>,
        "consistency_score": <integer 1-10>
        }

        Final output format:
        {
        "overall_score": 0,
        "structural_defects": { ... },
        "texture_artifacts": { ... },
        "subscores": { ... },
        "summary": "..."
        }
        """
        logger.info(f"VLM Evaluator initialized with {self.model_name}")
    
    def encode_image(self, image_path: Union[str, Path]) -> str:
        """Encode image to base64 string."""
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode('utf-8')

    def call_vlm(self, prompt: str, image_path: Union[str, Path], retries: int = 0) -> str:
        """
        Call VLM API with retry logic for a single image.
        
        Args:
            prompt: Text prompt
            image_path: Path to image
            retries: Current retry count
            
        Returns:
            Model response text
        """
        try:
            # Encode image
            base64_image = self.encode_image(image_path)
            
            # Prepare messages
            messages = [
                {
                    "role": "developer",
                    "content": self.system_prompt
                },
                {
                    "role": "user",
                    "content": [
                        {"type": "input_text", "text": prompt},
                        {
                            "type": "input_image",
                            "image_url": f"data:image/jpeg;base64,{base64_image}",
                            "detail": "high"
                        }
                    ]
                }
            ]
            
            # Generate response
            response = self.client.responses.create(
                model=self.model_name,
                input=messages,
                reasoning={ "effort": "low" },
                max_output_tokens=10000,
            )
            
            # Rate limiting
            time.sleep(self.rate_limit_delay)
            
            result_text = response.output_text
            # print(result_text) # Optional debug
            
            return result_text
            
        except Exception as e:
            if retries < self.max_retries:
                logger.warning(f"VLM call failed, retrying ({retries + 1}/{self.max_retries}): {e}")
                time.sleep(2 ** retries)
                return self.call_vlm(prompt, image_path, retries + 1)
            else:
                logger.error(f"VLM call failed after {self.max_retries} retries: {e}")
                raise

    def _extract_scores_from_json(self, response: str) -> Dict[str, any]:
        """
        Extract scores from JSON response for a single image.
        """
        import json
        
        try:
            # Find JSON block
            start = response.find('{')
            end = response.rfind('}') + 1
            if start != -1 and end != -1:
                json_str = response[start:end]
                # Fix potential JSON issues (e.g. trailing commas) if needed, 
                # but standard json.loads is usually strict.
                data = json.loads(json_str)
                return data
        except Exception as e:
            logger.warning(f"Failed to parse JSON scores: {e}. Response: {response}")
            
        return {}

    def evaluate_image_single(self, image_path: Union[str, Path]) -> Dict[str, any]:
        """
        Evaluate a single image for all metrics.
        
        Args:
            image_path: Path to image
            
        Returns:
            Dictionary with parsed results
        """
        prompt = """
        Analyze this 3D reconstruction image.
        Provide the full evaluation as specified in the system instructions.
        
        Respond with a JSON object.
        Example format:
        {
            "overall_score": 8,
            "structural_defects": {...},
            "texture_artifacts": {...},
            "subscores": {...},
            "summary": "Analysis..."
        }
        """
        
        try:
            response = self.call_vlm(prompt, image_path)
            # print(response)
            scores = self._extract_scores_from_json(response)
            return scores
        except Exception as e:
            logger.error(f"Single image evaluation failed for {image_path}: {e}")
            return {}

    def evaluate_views(self, view_paths: List[Union[str, Path]]) -> Dict:
        """
        Evaluate all VLM metrics across multiple views concurrently.
        
        Args:
            view_paths: List of image paths
            
        Returns:
            Dictionary with aggregated VLM metrics
        """
        if not self.vlm_config.get("enabled", True):
            return {"error": "VLM metrics disabled in config"}
        
        import concurrent.futures
        
        # Determine max workers (default to 5 or config)
        max_workers = self.vlm_config.get("max_workers", 5)
        logger.info(f"Evaluating {len(view_paths)} views with VLM (Concurrent, workers={max_workers})...")
        
        quality_scores = []
        artifact_scores = []
        structural_scores = []
        
        def process_view(path):
            try:
                logger.info(f"Processing view: {Path(path).name}")
                res = self.evaluate_image_single(path)
                
                # Extract scores (defaulting to 5.0 on error inside helper)
                q = float(res.get("overall_score", 5.0))
                
                sub = res.get("subscores", {})
                tex_score = float(sub.get("texture_score", 5.0))
                # Severity = 11 - texture_score approximately
                artifact_severity = max(1.0, 11.0 - tex_score)
                
                geo_score = float(sub.get("geometry_score", 5.0))
                
                return q, artifact_severity, geo_score
            except Exception as e:
                logger.error(f"Error processing {path}: {e}")
                return 5.0, 5.0, 5.0 # Fallback strict middle/bad score? Or ignore?
                # Using 5.0 as neutral fallback similar to previous code

        with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
            # map preserves order
            results = list(executor.map(process_view, view_paths))
            
        for q, a, s in results:
            quality_scores.append(q)
            artifact_scores.append(a)
            structural_scores.append(s)

        
        results = {
            "model": self.model_name,
            "num_views": len(view_paths)
        }
        
        # Helper to compute stats
        def compute_stats(score_list):
            if not score_list: return None
            arr = np.array(score_list)
            return {
                "mean": float(np.mean(arr)),
                "std": float(np.std(arr)),
                "min": float(np.min(arr)),
                "max": float(np.max(arr)),
                "median": float(np.median(arr)),
                "scores": [float(s) for s in score_list],
                "quality_score": float(np.mean(arr) / 10.0 * 100.0)
            }

        if quality_scores:
            results["quality"] = compute_stats(quality_scores)
            
        if artifact_scores:
            # Artifacts: we stored severity (low is good quality).
            # compute_stats calculates quality_score by mean/10*100.
            # But for artifacts, we want 11-mean.
            stats = compute_stats(artifact_scores)
            arr = np.array(artifact_scores)
            # Invert severity to get quality (10=best quality/no artifacts)
            inverted = 11.0 - arr
            stats["quality_score"] = float(np.mean(inverted) / 10.0 * 100.0)
            
            stats["mean_severity"] = stats.pop("mean")
            stats["std_severity"] = stats.pop("std")
            stats["min_severity"] = stats.pop("min")
            stats["max_severity"] = stats.pop("max")
            results["artifacts"] = stats

        if structural_scores:
            results["structural"] = compute_stats(structural_scores)
        
        return results


def evaluate_all_vlm_metrics(
    view_paths: List[Union[str, Path]], 
    config: Dict
) -> Dict:
    """
    Run all enabled VLM metrics on a set of views.
    
    Args:
        view_paths: List of image paths
        config: Configuration dictionary
        
    Returns:
        Dictionary with all VLM metric results
    """
    if not config.get("vlm_metrics", {}).get("enabled", True):
        logger.info("VLM metrics disabled in config")
        return {"enabled": False}
    
    try:
        evaluator = VLMEvaluator(config)
        results = evaluator.evaluate_views(view_paths)
        return results
    except Exception as e:
        logger.error(f"VLM evaluation failed: {e}")
        return {"error": str(e)}


if __name__ == "__main__":
    # Test VLM evaluator
    import yaml
    import os
    
    config_path = Path(__file__).parent.parent.parent / "config.yaml"
    with open(config_path) as f:
        config = yaml.safe_load(f)
    
    # Check for API key
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("Warning: OPENAI_API_KEY not set in environment")
    
    
    # load test images 
    img_paths = []  
    for img in os.listdir("captured_views/ktv_hevc_deblur035"):
        if img.endswith(".png"):
            img_path = os.path.join("captured_views/ktv_hevc_deblur035", img)
            img_paths.append(img_path)

        # break
    
    vlm_results = evaluate_all_vlm_metrics(img_paths, config)
    print(vlm_results)

    # {'model': 'gpt-5-nano', 'num_views': 12, 'quality': {'mean': 4.583333333333333, 'std': 0.6400954789890507, 'min': 3.0, 'max': 5.0, 'median': 5.0, 'scores': [3.0, 5.0, 5.0, 5.0, 5.0, 5.0, 4.0, 5.0, 4.0, 5.0, 5.0, 4.0], 'quality_score': 45.83333333333333}, 'artifacts': {'median': 7.0, 'scores': [9.0, 7.0, 5.0, 6.0, 7.0, 7.0, 7.0, 8.0, 8.0, 7.0, 6.0, 7.0], 'quality_score': 40.0, 'mean_severity': 7.0, 'std_severity': 1.0, 'min_severity': 5.0, 'max_severity': 9.0}, 'structural': {'mean': 4.583333333333333, 'std': 0.6400954789890507, 'min': 3.0, 'max': 5.0, 'median': 5.0, 'scores': [3.0, 5.0, 4.0, 5.0, 5.0, 5.0, 5.0, 4.0, 4.0, 5.0, 5.0, 5.0], 'quality_score': 45.83333333333333}}