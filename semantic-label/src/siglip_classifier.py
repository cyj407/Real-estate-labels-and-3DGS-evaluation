"""
SigLIP-based scene classifier for real estate images.
Uses google/siglip2-base-patch16-224 for interior/exterior classification.
"""

import torch
from transformers import pipeline
from PIL import Image
from pathlib import Path
from typing import List, Tuple, Dict


class SigLIPSceneClassifier:
    """Classify real estate images as interior or exterior using SigLIP."""
    
    def __init__(
        self,
        model_name: str = "google/siglip2-base-patch16-224",
        device: str = "cpu"
    ):
        """
        Initialize SigLIP classifier.
        
        Args:
            model_name: HuggingFace model identifier
            device: Device to run model on (cpu/cuda)
        """
        self.model_name = model_name
        self.device = 0 if device == "cuda" else -1  # pipeline uses 0 for cuda, -1 for cpu
        
        print(f"Loading SigLIP model: {model_name} on {device}...")
        
        try:
            # Initialize zero-shot image classification pipeline
            self.pipeline = pipeline(
                task="zero-shot-image-classification",
                model=model_name,
                device=self.device
            )
            
            # Define scene classification labels (same as CLIP)
            self.candidate_labels = [
                "a photo of an interior room",
                "a photo of amenity interior",
                "a photo of an exterior building",
                "a photo of outdoor scenery",
            ]
            
            print("✓ SigLIP model loaded successfully!")
            
        except Exception as e:
            print(f"❌ Error loading SigLIP: {e}")
            print("Make sure to install: pip install transformers pillow torch")
            raise
    
    def classify_single_image(self, image_path: str) -> Tuple[str, float]:
        """
        Classify a single image as interior or exterior.
        
        Args:
            image_path: Path to image file
            
        Returns:
            Tuple of (label, confidence)
        """
        try:
            # Load image
            image = Image.open(image_path).convert('RGB')
            
            # Run classification
            results = self.pipeline(image, candidate_labels=self.candidate_labels)
            
            # Get top prediction
            top_result = results[0]
            top_label_idx = self.candidate_labels.index(top_result['label'])
            
            # Interior if index 0 or 1 (same logic as CLIP)
            label = "interior" if top_label_idx <= 1 else "exterior"
            confidence = top_result['score']
            
            return label, confidence
            
        except Exception as e:
            print(f"Error classifying {image_path}: {e}")
            return "unknown", 0.0
    
    def classify_batch(
        self,
        image_paths: List[str],
        batch_size: int = 16
    ) -> List[Tuple[str, float]]:
        """
        Classify multiple images in batches.
        
        Args:
            image_paths: List of image file paths
            batch_size: Number of images to process at once
            
        Returns:
            List of (label, confidence) tuples
        """
        results = []
        
        for i in range(0, len(image_paths), batch_size):
            batch_paths = image_paths[i:i + batch_size]
            
            # Load images
            images = []
            valid_indices = []
            
            for idx, path in enumerate(batch_paths):
                try:
                    img = Image.open(path).convert('RGB')
                    images.append(img)
                    valid_indices.append(idx)
                except Exception as e:
                    print(f"Error loading {path}: {e}")
            
            if not images:
                # All images failed to load
                results.extend([("exterior", 0.0)] * len(batch_paths))
                continue
            
            # Process batch
            batch_results_raw = self.pipeline(
                images,
                candidate_labels=self.candidate_labels,
                batch_size=len(images)
            )
            
            # Process results
            batch_results = []
            for img_results in batch_results_raw:
                # Get top prediction for this image
                top_result = img_results[0]
                top_label_idx = self.candidate_labels.index(top_result['label'])
                
                # Interior if index 0 or 1
                label = "interior" if top_label_idx <= 1 else "exterior"
                confidence = top_result['score']
                batch_results.append((label, confidence))
            
            # Insert results at correct positions
            result_idx = 0
            for idx in range(len(batch_paths)):
                if idx in valid_indices:
                    results.append(batch_results[result_idx])
                    result_idx += 1
                else:
                    results.append(("exterior", 0.0))
        
        return results
    
    def filter_interior_images(
        self,
        image_paths: List[str],
        # threshold: float = 0.5,
        batch_size: int = 16
    ) -> Tuple[List[str], Dict]:
        """
        Filter images to return only interior photos.
        
        Args:
            image_paths: List of image file paths
            threshold: Minimum confidence threshold for interior classification
            batch_size: Batch size for processing
        
        Returns:
            Tuple of (interior_image_paths, classification_stats)
        """
        print(f"Classifying {len(image_paths)} images with SigLIP...")
        classifications = self.classify_batch(image_paths, batch_size)
        
        interior_paths = []
        exterior_paths = []
        
        for idx, (path, (label, confidence)) in enumerate(zip(image_paths, classifications)):
            if label == "interior":
                interior_paths.append(path)
            else:
                exterior_paths.append(path)
            print(f"  Debug: {Path(path).name} -> label={label}")


        stats = {
            'total_images': len(image_paths),
            'interior_count': len(interior_paths),
            'exterior_count': len(exterior_paths),
            'interior_ratio': len(interior_paths) / len(image_paths) if image_paths else 0,
            'classifications': [
                {'path': Path(p).name, 'label': l, 'confidence': c}
                for p, (l, c) in zip(image_paths, classifications)
            ]
        }
        
        print(f"  Interior: {len(interior_paths)} ({stats['interior_ratio']:.1%})")
        print(f"  Exterior: {len(exterior_paths)}")
        
        return interior_paths, stats


if __name__ == "__main__":
    # Test the classifier
    import sys
    sys.path.append('..')
    
    from data_loader import PropertyDataLoader
    
    # Load test data
    loader = PropertyDataLoader(
        dataset_dir="../dataset",
        cache_dir="../cache/images"
    )
    
    # Initialize classifier
    classifier = SigLIPSceneClassifier(device="cpu")
    
    properties = loader.load_all_properties()
    for property_data, image_paths in properties:
        property_id = loader.get_property_id(property_data)
        
        print(f"\nTesting SigLIP classifier on property {property_id}")
        print(f"Total images: {len(image_paths)}")
        
        # Filter interior images
        interior_paths, stats = classifier.filter_interior_images(
            image_paths, 
            batch_size=8
        )
        
        print(f"\nClassification Results:")
        print(f"  Interior: {len(interior_paths)}")
        print(f"  Exterior: {stats['exterior_count']}")
        print(f"  Ratio: {stats['interior_ratio']:.1%}")
