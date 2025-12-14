"""
SigLIP-based label generator for real estate properties.
Uses zero-shot image classification with probability-based filtering.
"""

import torch
from transformers import pipeline
from PIL import Image
from pathlib import Path
from typing import List, Dict, Tuple
import yaml
import numpy as np


class SigLIPLabelGenerator:
    """Generate semantic labels using SigLIP zero-shot classification."""
    
    def __init__(
        self,
        config_path: str = "../config.yaml",
        model_name: str = "google/siglip2-base-patch16-224",
        device: str = "cpu"
    ):
        """
        Initialize SigLIP label generator.
        
        Args:
            config_path: Path to config file
            model_name: HuggingFace model identifier
            device: Device to run model on
        """
        with open(config_path, 'r') as f:
            self.config = yaml.safe_load(f)
        
        self.device = 0 if device == "cuda" else -1
        self.model_name = model_name
        
        print(f"Loading SigLIP model for label generation: {model_name}...")
        
        # Initialize zero-shot classification pipeline
        self.pipeline = pipeline(
            task="zero-shot-image-classification",
            model=model_name,
            device=self.device
        )
        
        # Load label vocabularies from config
        self.label_vocab = {
            'room_types': self.config['labeling']['room_types'],
            'style': self.config['labeling']['style_labels'],
            'features': self.config['labeling']['feature_labels'],
            'condition': self.config['labeling']['condition_labels']
        }
        
        # Create full candidate label list
        self.all_labels = []
        self.label_to_category = {}
        
        for category, labels in self.label_vocab.items():
            for label in labels:
                self.all_labels.append(label)
                self.label_to_category[label] = category
        
        print(f"✓ Loaded {len(self.all_labels)} candidate labels from {len(self.label_vocab)} categories")
    
    def classify_image_with_labels(
        self,
        image_path: str,
        candidate_labels: List[str]
    ) -> List[Dict]:
        """
        Classify a single image with candidate labels.
        
        Args:
            image_path: Path to image
            candidate_labels: List of candidate label strings
            
        Returns:
            List of dicts with 'label' and 'score'
        """
        try:
            image = Image.open(image_path).convert('RGB')
            results = self.pipeline(image, candidate_labels=candidate_labels)
            return results
        except Exception as e:
            print(f"Error classifying {image_path}: {e}")
            return []
    
    def extract_labels_from_category(
        self,
        image_paths: List[str],
        category: str,
        top_k: int = 3,
        threshold: float = 0.2
    ) -> List[Tuple[str, float]]:
        """
        Extract top-k labels from a specific category across all images.
        
        Args:
            image_paths: List of interior image paths
            category: Category name ('room_types', 'style', 'features', 'condition')
            top_k: Maximum number of labels to return
            threshold: Minimum probability threshold
            
        Returns:
            List of (label, score) tuples
        """
        candidate_labels = self.label_vocab[category]
        
        if not candidate_labels:
            return []
        
        # Accumulate probabilities across all images
        label_scores = {label: [] for label in candidate_labels}
        
        for image_path in image_paths:
            results = self.classify_image_with_labels(image_path, candidate_labels)
            
            # Store scores for each label
            for result in results:
                label = result['label']
                score = result['score']
                if label in label_scores:
                    label_scores[label].append(score)
        
        # Calculate mean probability for each label
        mean_scores = {}
        for label, scores in label_scores.items():
            if scores:
                mean_scores[label] = np.mean(scores)
            else:
                mean_scores[label] = 0.0
        
        # Sort by mean score and filter by threshold
        sorted_labels = sorted(
            mean_scores.items(),
            key=lambda x: x[1],
            reverse=True
        )
        
        # Debug: show top scores
        print(f"    {category} - Top scores:")
        for label, score in sorted_labels[:5]:
            print(f"      {label}: {score:.4f}")
        
        # Take top-k above threshold
        results = []
        for label, score in sorted_labels[:top_k]:
            if score >= threshold:
                results.append((label, score))
        
        print(f"    {category} - Selected {len(results)} labels (threshold={threshold})")
        
        return results
    
    def generate_labels(
        self,
        image_paths: List[str],
        top_k_total: int = 10
    ) -> Dict[str, any]:
        """
        Generate semantic labels for a property from its interior images.
        
        Args:
            image_paths: List of interior image paths
            top_k_total: Maximum total number of labels to return
            
        Returns:
            Dictionary with labels by category and aggregated results
        """
        if not image_paths:
            return {
                'labels': [],
                'labels_with_scores': [],
                'labels_by_category': {},
                'num_images': 0
            }
        
        print(f"Generating labels from {len(image_paths)} interior images with SigLIP...")
        
        # Extract labels from each category
        # Note: SigLIP scores are much lower than CLIP, so we use a lower threshold
        threshold = 0.0005  # SigLIP scores are typically 0.001-0.01 range
        max_per_category = self.config['labeling']['max_labels_per_category']
        
        labels_by_category = {
            'room_types': self.extract_labels_from_category(
                image_paths, 'room_types', top_k=max_per_category, threshold=threshold
            ),
            'style': self.extract_labels_from_category(
                image_paths, 'style', top_k=max_per_category, threshold=threshold
            ),
            'features': self.extract_labels_from_category(
                image_paths, 'features', top_k=max_per_category * 2, threshold=threshold
            ),
            'condition': self.extract_labels_from_category(
                image_paths, 'condition', top_k=2, threshold=threshold
            ),
        }
        
        # Aggregate all labels and sort by score
        all_labels = []
        for category, label_list in labels_by_category.items():
            for label, score in label_list:
                all_labels.append({
                    'label': label,
                    'score': score,
                    'category': category
                })
        
        # Sort by score and take top-k
        all_labels.sort(key=lambda x: x['score'], reverse=True)
        top_labels = all_labels[:top_k_total]
        
        print(f"  Generated {len(top_labels)} labels")
        for item in top_labels[:5]:
            print(f"    - {item['label']} ({item['category']}, score: {item['score']:.3f})")
        
        return {
            'labels': [item['label'] for item in top_labels],
            'labels_with_scores': top_labels,
            'labels_by_category': labels_by_category,
            'num_images': len(image_paths)
        }


if __name__ == "__main__":
    # Test the generator
    import sys
    sys.path.append('..')
    
    from data_loader import PropertyDataLoader
    
    # Load test data
    loader = PropertyDataLoader(
        dataset_dir="../dataset",
        cache_dir="../cache/images"
    )
    
    # Initialize generator
    generator = SigLIPLabelGenerator(device="cpu")
    
    properties = loader.load_all_properties()
    
    # Test on first property
    property_data, image_paths = properties[0]
    property_id = loader.get_property_id(property_data)
    
    print(f"\nTesting SigLIP label generator on property {property_id}")
    print(f"Total images: {len(image_paths)}")
    
    # Use first 5 images for testing
    test_images = image_paths[:5]
    
    result = generator.generate_labels(
        test_images,
        top_k_total=10
    )
    
    print(f"\n✓ Generated {len(result['labels'])} labels:")
    for item in result['labels_with_scores']:
        print(f"  - {item['label']:<30} ({item['category']:<12} score: {item['score']:.3f})")
    
    print(f"\nLabels by category:")
    for category, labels in result['labels_by_category'].items():
        print(f"  {category}:")
        for label, score in labels:
            print(f"    - {label} ({score:.3f})")
