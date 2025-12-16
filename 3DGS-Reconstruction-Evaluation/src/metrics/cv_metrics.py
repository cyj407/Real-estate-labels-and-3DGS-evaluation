"""
Computer Vision-based metrics for 3DGS reconstruction quality evaluation.
Includes blur detection, edge consistency, BRISQUE, and LPIPS metrics.
"""

import cv2
import numpy as np
from pathlib import Path
from typing import Dict, List, Union
from PIL import Image
import logging

# MANIQA import
try:
    import pyiqa, torch
    MANIQA_AVAILABLE = True
except ImportError:
    MANIQA_AVAILABLE = False
    logging.warning("pyiqa not available. MANIQA metric will be unavailable.")

# BRISQUE imports
try:
    from skimage.metrics import structural_similarity as ssim
    import scipy.ndimage
    BRISQUE_AVAILABLE = True
except ImportError:
    BRISQUE_AVAILABLE = False
    logging.warning("scikit-image not available. BRISQUE metric will be limited.")

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class BlurDetector:
    """Detects blur in images using Laplacian variance."""
    
    def __init__(self, threshold: float = 100.0):
        """
        Initialize blur detector.
        
        Args:
            threshold: Laplacian variance threshold (lower = more blurred)
        """
        self.threshold = threshold
    
    def compute_blur_score(self, image_path: Union[str, Path]) -> float:
        """
        Compute blur score using Laplacian variance.
        
        Args:
            image_path: Path to image file
            
        Returns:
            Blur score (higher = sharper, lower = more blurred)
        """
        image = cv2.imread(str(image_path))
        if image is None:
            raise ValueError(f"Could not load image: {image_path}")
        
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        laplacian_var = cv2.Laplacian(gray, cv2.CV_64F).var()
        
        return float(laplacian_var)
    
    def evaluate_views(self, view_paths: List[Union[str, Path]]) -> Dict:
        """
        Evaluate blur across multiple views.
        
        Args:
            view_paths: List of image paths
            
        Returns:
            Dictionary with blur statistics
        """
        scores = []
        
        for path in view_paths:
            try:
                score = self.compute_blur_score(path)
                scores.append(score)
            except Exception as e:
                logger.error(f"Error processing {path}: {e}")
        
        if not scores:
            return {"error": "No valid scores computed"}
        
        scores_array = np.array(scores)
        
        return {
            "metric": "blur_laplacian",
            "mean": float(np.mean(scores_array)),
            "std": float(np.std(scores_array)),
            "min": float(np.min(scores_array)),
            "max": float(np.max(scores_array)),
            "median": float(np.median(scores_array)),
            "num_views": len(scores),
            "threshold": self.threshold,
            "quality_score": self._normalize_score(np.mean(scores_array))
        }
    
    def _normalize_score(self, raw_score: float) -> float:
        """
        Normalize blur score to 0-100 scale.
        
        Args:
            raw_score: Raw Laplacian variance
            
        Returns:
            Normalized score (0-100, higher is better)
        """
        # Typical good images: 500-2000, blurred: <100
        # Normalize to 0-100 scale
        normalized = min(100, (raw_score / 20))
        return float(normalized)


class EdgeConsistencyMetric:
    """Evaluates edge density and consistency across views."""
    
    def __init__(self, canny_low: int = 50, canny_high: int = 150):
        """
        Initialize edge consistency metric.
        
        Args:
            canny_low: Lower threshold for Canny edge detection
            canny_high: Upper threshold for Canny edge detection
        """
        self.canny_low = canny_low
        self.canny_high = canny_high
    
    def compute_edge_density(self, image_path: Union[str, Path]) -> float:
        """
        Compute edge density using Canny edge detection.
        
        Args:
            image_path: Path to image file
            
        Returns:
            Edge density (percentage of edge pixels)
        """
        image = cv2.imread(str(image_path))
        if image is None:
            raise ValueError(f"Could not load image: {image_path}")
        
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(gray, self.canny_low, self.canny_high)
        
        edge_density = np.sum(edges > 0) / edges.size
        return float(edge_density)
    
    def evaluate_views(self, view_paths: List[Union[str, Path]]) -> Dict:
        """
        Evaluate edge consistency across multiple views.
        
        Args:
            view_paths: List of image paths
            
        Returns:
            Dictionary with edge consistency statistics
        """
        densities = []
        
        for path in view_paths:
            try:
                density = self.compute_edge_density(path)
                densities.append(density)
            except Exception as e:
                logger.error(f"Error processing {path}: {e}")
        
        if not densities:
            return {"error": "No valid densities computed"}
        
        densities_array = np.array(densities)
        
        # Lower std = more consistent edges across views
        consistency_score = 100 * (1 - min(1.0, np.std(densities_array) / 0.05))
        
        return {
            "metric": "edge_consistency",
            "mean_density": float(np.mean(densities_array)),
            "std_density": float(np.std(densities_array)),
            "min_density": float(np.min(densities_array)),
            "max_density": float(np.max(densities_array)),
            "consistency_score": float(consistency_score),
            "num_views": len(densities),
            "quality_score": float(consistency_score)
        }


class BRISQUEMetric:
    """
    Blind/Referenceless Image Spatial Quality Evaluator.
    Uses pyiqa implementation.
    """
    
    def __init__(self):
        """Initialize BRISQUE metric."""
        if not MANIQA_AVAILABLE: # Reusing the pyiqa availability check
            raise ImportError("BRISQUE via pyiqa requires pyiqa package")
        
        self.device = torch.device("cpu")
        try:
            self.model = pyiqa.create_metric('brisque', device=self.device)
            logger.info(f"BRISQUE initialized on {self.device} (via pyiqa)")
        except Exception as e:
            logger.error(f"Failed to initialize BRISQUE: {e}")
            raise

    def compute_quality_score(self, image_path: Union[str, Path]) -> float:
        """
        Compute BRISQUE score for a single image.
        
        Args:
            image_path: Path to image file
            
        Returns:
            Quality score (0-100, higher is better)
        """
        try:
            # pyiqa handles image loading
            # BRISQUE returns a score typically 0-100, where 0 is best and 100 is worst.
            score = self.model(str(image_path))
            
            if torch.is_tensor(score):
                score = score.item()
                
            # Invert for "higher is better" consistency with other metrics
            # 0 (best) -> 100, 100 (worst) -> 0
            quality_score = max(0.0, 100.0 - float(score))
            
            return quality_score
            
        except Exception as e:
            logger.error(f"Error computing BRISQUE for {image_path}: {e}")
            return 0.0
    
    def evaluate_views(self, view_paths: List[Union[str, Path]]) -> Dict:
        """
        Evaluate quality across multiple views.
        
        Args:
            view_paths: List of image paths
            
        Returns:
            Dictionary with quality statistics
        """
        scores = []
        
        for path in view_paths:
            try:
                score = self.compute_quality_score(path)
                scores.append(score)
            except Exception as e:
                logger.error(f"Error processing {path}: {e}")
        
        if not scores:
            return {"error": "No valid scores computed"}
        
        scores_array = np.array(scores)
        
        return {
            "metric": "brisque_quality",
            "mean": float(np.mean(scores_array)),
            "std": float(np.std(scores_array)),
            "min": float(np.min(scores_array)),
            "max": float(np.max(scores_array)),
            "median": float(np.median(scores_array)),
            "num_views": len(scores),
            "quality_score": float(np.mean(scores_array))
        }


def evaluate_all_cv_metrics(view_paths: List[Union[str, Path]], config: Dict) -> Dict:
    """
    Run all enabled CV metrics on a set of views.
    
    Args:
        view_paths: List of image paths
        config: Configuration dictionary
        
    Returns:
        Dictionary with all metric results
    """
    cv_config = config.get("cv_metrics", {})
    results = {}
    
    # Blur detection
    if cv_config.get("blur", {}).get("enabled", True):
        logger.info("Computing blur metrics...")
        blur_detector = BlurDetector(
            threshold=cv_config.get("blur", {}).get("threshold", 100)
        )
        results["blur"] = blur_detector.evaluate_views(view_paths)
    
    # Edge consistency
    if cv_config.get("edge_consistency", {}).get("enabled", True):
        logger.info("Computing edge consistency...")
        edge_metric = EdgeConsistencyMetric(
            canny_low=cv_config.get("edge_consistency", {}).get("canny_low", 50),
            canny_high=cv_config.get("edge_consistency", {}).get("canny_high", 150)
        )
        results["edge_consistency"] = edge_metric.evaluate_views(view_paths)
    
    # BRISQUE
    if cv_config.get("brisque", {}).get("enabled", True):
        logger.info("Computing BRISQUE quality...")
        brisque_metric = BRISQUEMetric()
        results["brisque"] = brisque_metric.evaluate_views(view_paths)
    
    # MANIQA
    if cv_config.get("maniqa", {}).get("enabled", True) and MANIQA_AVAILABLE:
        logger.info("Computing MANIQA quality...")
        try:
            maniqa_metric = MANIQAMetric()
            results["maniqa"] = maniqa_metric.evaluate_views(view_paths)
        except Exception as e:
            logger.error(f"MANIQA evaluation failed: {e}")
            results["maniqa"] = {"error": str(e)}
    
    return results


class MANIQAMetric:
    """
    Multi-dimension Attention Network for No-Reference Image Quality Assessment.
    Uses pyiqa implementation.
    """
    
    def __init__(self):
        """Initialize MANIQA metric."""
        if not MANIQA_AVAILABLE:
            raise ImportError("MANIQA requires pyiqa package")
        
        self.device = torch.device("cpu")
        try:
            self.model = pyiqa.create_metric('maniqa', device=self.device)
            logger.info(f"MANIQA initialized on {self.device}")
        except Exception as e:
            logger.error(f"Failed to initialize MANIQA: {e}")
            raise

    def compute_quality_score(self, image_path: Union[str, Path]) -> float:
        """
        Compute MANIQA score for a single image.
        
        Args:
            image_path: Path to image file
            
        Returns:
            Quality score (normalized to 0-100)
        """
        try:
            # pyiqa handles image loading
            score = self.model(str(image_path))
            
            # MANIQA output is typically raw score, convert to float
            if torch.is_tensor(score):
                score = score.item()
                
            # Normalize: MANIQA scores roughly 0-1, verify scaling
            # Typically higher is better
            return float(score * 100)
            
        except Exception as e:
            logger.error(f"Error computing MANIQA for {image_path}: {e}")
            raise

    def evaluate_views(self, view_paths: List[Union[str, Path]]) -> Dict:
        """
        Evaluate MANIQA quality across multiple views.
        
        Args:
            view_paths: List of image paths
            
        Returns:
            Dictionary with quality statistics
        """
        scores = []
        
        for path in view_paths:
            try:
                score = self.compute_quality_score(path)
                scores.append(score)
            except Exception as e:
                logger.error(f"Error processing {path}: {e}")
        
        if not scores:
            return {"error": "No valid scores computed"}
        
        scores_array = np.array(scores)
        
        return {
            "metric": "maniqa",
            "mean": float(np.mean(scores_array)),
            "std": float(np.std(scores_array)),
            "min": float(np.min(scores_array)),
            "max": float(np.max(scores_array)),
            "median": float(np.median(scores_array)),
            "num_views": len(scores),
            "quality_score": float(np.mean(scores_array))
        }


if __name__ == "__main__":
    # Test with sample images
    import yaml
    from pathlib import Path
    
    config_path = Path(__file__).parent.parent.parent / "config.yaml"
    with open(config_path) as f:
        config = yaml.safe_load(f)
    
    # Test blur detection
    print("Testing CV metrics...")
    print("Note: Run view capture first to generate test images")
