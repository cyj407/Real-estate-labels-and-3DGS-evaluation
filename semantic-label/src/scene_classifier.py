"""
Interior/Exterior scene classifier using CLIP zero-shot classification.
Filters images to identify interior photos only.
"""

import torch
import open_clip
from PIL import Image
from typing import List, Tuple, Dict
import numpy as np
from pathlib import Path


class SceneClassifier:
    """CLIP-based interior/exterior classifier."""
    
    def __init__(self, model_name: str = "ViT-B/32", pretrained: str = "openai", device: str = "cpu"):
        self.device = device
        print(f"Loading CLIP model: {model_name} ({pretrained}) on {device}...")
        
        self.model, _, self.preprocess = open_clip.create_model_and_transforms(
            model_name, pretrained=pretrained
        )
        self.tokenizer = open_clip.get_tokenizer(model_name)
        self.model.to(device)
        self.model.eval()
        
        # Define scene classification prompts
        self.scene_prompts = [
            "a photo of an interior room",
            "a photo of an exterior building facade",
            "a photo of outdoor scenery",
        ]
        
        # Pre-encode text prompts
        with torch.no_grad():
            text_tokens = self.tokenizer(self.scene_prompts).to(device)
            self.text_features = self.model.encode_text(text_tokens)
            self.text_features /= self.text_features.norm(dim=-1, keepdim=True)
    
    def classify_single_image(self, image_path: str) -> Tuple[str, float]:
        """
        Classify a single image as interior or exterior using positive interior features.
        Returns (label, confidence_score).
        """
        try:
            image = Image.open(image_path).convert('RGB')
            image_input = self.preprocess(image).unsqueeze(0).to(self.device)
            
            with torch.no_grad():
                image_features = self.model.encode_image(image_input)
                image_features /= image_features.norm(dim=-1, keepdim=True)
                
                # Calculate similarity scores
                similarity = (image_features @ self.text_features.T).squeeze(0)
                probs = similarity.softmax(dim=0).cpu().numpy()
            
            # Interior is index 0
            # Use a more lenient threshold - if interior score is reasonably high, classify as interior
            interior_score = float(probs[0])
            exterior_score = float(max(probs[1], probs[2]))
            
            # More permissive: classify as interior if it has ANY reasonable interior score
            # or if interior score is close to exterior score
            if interior_score > 0.25 or (interior_score > 0.15 and interior_score / (exterior_score + 0.01) > 0.7):
                label = "interior"
                confidence = interior_score
            else:
                label = "exterior"
                confidence = exterior_score
            
            return label, confidence
            
        except Exception as e:
            print(f"Error classifying {image_path}: {e}")
            return "unknown", 0.0
    
    def classify_batch(self, image_paths: List[str], batch_size: int = 16) -> List[Tuple[str, float]]:
        """
        Classify multiple images in batches for efficiency.
        Returns list of (label, confidence) tuples.
        """
        results = []
        
        for i in range(0, len(image_paths), batch_size):
            batch_paths = image_paths[i:i + batch_size]
            batch_images = []
            valid_indices = []
            
            # Load and preprocess batch
            for idx, path in enumerate(batch_paths):
                try:
                    image = Image.open(path).convert('RGB')
                    batch_images.append(self.preprocess(image))
                    valid_indices.append(idx)
                except Exception as e:
                    print(f"Error loading {path}: {e}")
                    results.append(("unknown", 0.0))
            
            if not batch_images:
                continue
            
            # Process batch
            batch_tensor = torch.stack(batch_images).to(self.device)
            
            with torch.no_grad():
                image_features = self.model.encode_image(batch_tensor)
                image_features /= image_features.norm(dim=-1, keepdim=True)
                
                # Calculate similarity scores
                similarity = image_features @ self.text_features.T
                probs = similarity.softmax(dim=-1).cpu().numpy()
            
            # Process results with same logic as classify_single_image
            batch_results = []
            for prob_vec in probs:
                interior_score = float(prob_vec[0])
                exterior_score = float(max(prob_vec[1], prob_vec[2]))
                
                # Same permissive logic as single image classification
                if interior_score > 0.25 or (interior_score > 0.15 and interior_score / (exterior_score + 0.01) > 0.7):
                    label = "interior"
                    confidence = interior_score
                else:
                    label = "exterior"
                    confidence = exterior_score
                batch_results.append((label, confidence))
            
            # Insert results at correct positions
            result_idx = 0
            for idx in range(len(batch_paths)):
                if idx in valid_indices:
                    results.append(batch_results[result_idx])
                    result_idx += 1
        
        return results
    
    def filter_interior_images(
        self, 
        image_paths: List[str], 
        threshold: float = 0.5,
        batch_size: int = 16
    ) -> Tuple[List[str], Dict[str, any]]:
        """
        Filter images to return only interior photos.
        
        Args:
            image_paths: List of image file paths
            threshold: Minimum confidence threshold for interior classification
            batch_size: Batch size for processing
        
        Returns:
            Tuple of (interior_image_paths, classification_stats)
        """
        print(f"Classifying {len(image_paths)} images...")
        classifications = self.classify_batch(image_paths, batch_size)
        
        interior_paths = []
        exterior_paths = []
        
        for path, (label, confidence) in zip(image_paths, classifications):
            if label == "interior" and confidence >= threshold:
                interior_paths.append(path)
            else:
                exterior_paths.append(path)
        
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
    from data_loader import PropertyDataLoader
    
    # Load one property for testing
    loader = PropertyDataLoader(
        dataset_dir="../dataset",
        cache_dir="../cache/images"
    )
    
    properties = loader.load_all_properties()
    if properties:
        property_data, image_paths = properties[0]
        property_id = loader.get_property_id(property_data)
        
        print(f"\nTesting classifier on property {property_id}")
        print(f"Total images: {len(image_paths)}")
        
        # Initialize classifier
        classifier = SceneClassifier(device="cpu")
        
        # Filter interior images
        interior_paths, stats = classifier.filter_interior_images(
            image_paths, 
            threshold=0.5,
            batch_size=16
        )
        
        print(f"\nClassification Results:")
        print(f"  Interior: {stats['interior_count']}")
        print(f"  Exterior: {stats['exterior_count']}")
        print(f"  Ratio: {stats['interior_ratio']:.1%}")
