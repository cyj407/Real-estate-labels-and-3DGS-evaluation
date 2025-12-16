"""
Evaluator for semantic labeling system.
Computes quantitative metrics and performs error analysis.
"""

import torch
import open_clip
from PIL import Image
import numpy as np
from typing import List, Dict, Tuple
from collections import Counter
from itertools import combinations
from sklearn.metrics.pairwise import cosine_similarity
import yaml


class LabelEvaluator:
    """Evaluate quality of generated semantic labels."""
    
    def __init__(
        self, 
        config_path: str = "../config.yaml",
        model_name: str = "ViT-B/32",
        pretrained: str = "openai",
        device: str = "cpu"
    ):
        self.device = device
        
        # Load config
        with open(config_path, 'r') as f:
            self.config = yaml.safe_load(f)
        
        # Load CLIP model for evaluation
        print(f"Loading CLIP model for evaluation...")
        self.model, _, self.preprocess = open_clip.create_model_and_transforms(
            model_name, pretrained=pretrained
        )
        self.tokenizer = open_clip.get_tokenizer(model_name)
        self.model.to(device)
        self.model.eval()
    
    def encode_text(self, texts: List[str]) -> torch.Tensor:
        """Encode text labels to embeddings."""
        with torch.no_grad():
            text_tokens = self.tokenizer(texts).to(self.device)
            text_features = self.model.encode_text(text_tokens)
            text_features /= text_features.norm(dim=-1, keepdim=True)
        return text_features
    
    def encode_images(self, image_paths: List[str]) -> torch.Tensor:
        """Encode images to embeddings."""
        images = []
        for path in image_paths:
            try:
                img = Image.open(path).convert('RGB')
                images.append(self.preprocess(img))
            except Exception as e:
                print(f"Error loading {path}: {e}")
        
        if not images:
            return torch.empty(0, 512).to(self.device)
        
        batch = torch.stack(images).to(self.device)
        with torch.no_grad():
            image_features = self.model.encode_image(batch)
            image_features /= image_features.norm(dim=-1, keepdim=True)
        
        return image_features
    
    def compute_coverage(
        self, 
        labels: List[str], 
        image_paths: List[str]
    ) -> float:
        """
        Coverage: How well labels cover the semantic content of images.
        Measured as mean max similarity between each label and all images.
        """
        if not labels or not image_paths:
            return 0.0
        
        label_features = self.encode_text([f"a photo of {label}" for label in labels])
        image_features = self.encode_images(image_paths)
        
        if image_features.shape[0] == 0:
            return 0.0
        
        # Similarity matrix: [num_labels, num_images]
        similarity = (label_features @ image_features.T).cpu().numpy()
        
        # For each label, find max similarity with any image
        max_similarities = similarity.max(axis=1)
        
        # Coverage is mean of these max similarities
        coverage = float(max_similarities.mean())
        
        return coverage
    
    def compute_specificity(self, labels: List[str]) -> float:
        """
        Specificity: Granularity of labels.
        Measured as average word count per label.
        Higher word count generally indicates more specific labels.
        """
        if not labels:
            return 0.0
        
        word_counts = [len(label.split()) for label in labels]
        specificity = np.mean(word_counts)
        
        return float(specificity)
    
    def compute_redundancy(self, labels: List[str]) -> float:
        """
        Redundancy: Degree of duplicate/overlapping labels.
        Measured as mean pairwise cosine similarity between label embeddings.
        Lower is better (less redundant).
        """
        if len(labels) < 2:
            return 0.0
        
        label_features = self.encode_text([f"a photo of {label}" for label in labels])
        label_features_np = label_features.cpu().numpy()
        
        # Compute pairwise similarities
        similarities = cosine_similarity(label_features_np)
        
        # Get upper triangle (excluding diagonal)
        n = len(labels)
        upper_triangle = similarities[np.triu_indices(n, k=1)]
        
        redundancy = float(upper_triangle.mean())
        
        return redundancy
    
    def compute_diversity(self, all_property_labels: List[List[str]]) -> float:
        """
        Diversity: How differentiated labels are across properties.
        Measured as mean Jaccard distance between property label sets.
        Higher is better (more diverse).
        """
        if len(all_property_labels) < 2:
            return 0.0
        
        # Convert to sets
        label_sets = [set(labels) for labels in all_property_labels]
        
        # Compute pairwise Jaccard distances
        distances = []
        for set1, set2 in combinations(label_sets, 2):
            intersection = len(set1 & set2)
            union = len(set1 | set2)
            
            if union > 0:
                jaccard_sim = intersection / union
                jaccard_dist = 1 - jaccard_sim
                distances.append(jaccard_dist)
        
        diversity = float(np.mean(distances)) if distances else 0.0
        
        return diversity
    
    def compute_clip_consistency(
        self, 
        labels: List[str], 
        image_paths: List[str]
    ) -> float:
        """
        CLIP Consistency: Label-image alignment.
        Measured as mean similarity between label and image embeddings.
        """
        if not labels or not image_paths:
            return 0.0
        
        label_features = self.encode_text([f"a photo of {label}" for label in labels])
        image_features = self.encode_images(image_paths)
        
        if image_features.shape[0] == 0:
            return 0.0
        
        # Mean label embedding
        mean_label_features = label_features.mean(dim=0, keepdim=True)
        mean_label_features /= mean_label_features.norm(dim=-1, keepdim=True)
        
        # Mean image embedding
        mean_image_features = image_features.mean(dim=0, keepdim=True)
        mean_image_features /= mean_image_features.norm(dim=-1, keepdim=True)
        
        # Cosine similarity
        consistency = float((mean_label_features @ mean_image_features.T).item())
        
        return consistency
    
    def evaluate_property(
        self, 
        labels: List[str], 
        image_paths: List[str]
    ) -> Dict[str, float]:
        """
        Evaluate labels for a single property.
        
        Returns:
            Dictionary of metric scores
        """
        metrics = {
            'coverage': self.compute_coverage(labels, image_paths),
            'specificity': self.compute_specificity(labels),
            'redundancy': self.compute_redundancy(labels),
            'clip_consistency': self.compute_clip_consistency(labels, image_paths),
            'num_labels': len(labels),
            'num_images': len(image_paths)
        }
        
        return metrics
    
    def evaluate_all_properties(
        self, 
        all_results: List[Dict]
    ) -> Dict[str, any]:
        """
        Evaluate across all properties.
        
        Args:
            all_results: List of dicts with 'labels' and 'image_paths' keys
        
        Returns:
            Aggregated metrics and per-property results
        """
        per_property_metrics = []
        all_labels = []
        
        for result in all_results:
            labels = result['labels']
            image_paths = result['image_paths']
            
            metrics = self.evaluate_property(labels, image_paths)
            metrics['property_id'] = result.get('property_id', 'unknown')
            per_property_metrics.append(metrics)
            
            all_labels.append(labels)
        
        # Compute diversity across all properties
        diversity = self.compute_diversity(all_labels)
        
        # Aggregate metrics
        aggregated = {
            'mean_coverage': np.mean([m['coverage'] for m in per_property_metrics]),
            'mean_specificity': np.mean([m['specificity'] for m in per_property_metrics]),
            'mean_redundancy': np.mean([m['redundancy'] for m in per_property_metrics]),
            'mean_clip_consistency': np.mean([m['clip_consistency'] for m in per_property_metrics]),
            'diversity': diversity,
            'total_properties': len(all_results),
            'per_property': per_property_metrics
        }
        
        return aggregated
    
    def analyze_errors(
        self, 
        labels: List[str], 
        image_paths: List[str]
    ) -> Dict[str, List[str]]:
        """
        Categorize potential errors in labels.
        
        Returns:
            Dictionary mapping error categories to example labels
        """
        errors = {
            'over_generic': [],
            'hallucination': [],
            'wrong_room_type': []
        }
        
        # 1. Over-generic checks
        generic_terms = {
            'room', 'space', 'area', 'nice', 'good', 'great', 'layout', 'design', 
            'style', 'view', 'feature', 'interior', 'exterior', 'building', 'home',
            'house', 'apartment', 'condo', 'property', 'unit'
        }
        
        # 2. Room type list for specific checking
        room_types = {
            'bedroom', 'living room', 'kitchen', 'kitchenette', 'bathroom', 'dining room', 
            'balcony', 'garage', 'hallway', 'study', 'office', 'gym', 'pool'
        }
        
        for label in labels:
            label_lower = label.lower()
            words = label_lower.split()
            
            # Check over-generic
            if label_lower in generic_terms:
                errors['over_generic'].append(label)
                continue
                


            # Check visual grounding (Hallucination / Wrong Room Type)
            if image_paths:
                label_features = self.encode_text([f"a photo of {label}"])
                image_features = self.encode_images(image_paths)
                
                if image_features.shape[0] > 0:
                    similarity = (label_features @ image_features.T).cpu().numpy()
                    max_sim = float(similarity.max())
                    
                    # Thresholds
                    # Room types usually have higher CLIP alignment than abstract features
                    if any(rt in label_lower for rt in room_types):
                        if max_sim < 0.22: # Stricter for room types
                            errors['wrong_room_type'].append(f"{label} ({max_sim:.3f})")
                    else:
                        if max_sim < 0.18: # Lower threshold for general features
                            errors['hallucination'].append(f"{label} ({max_sim:.3f})")
                            
        return errors


if __name__ == "__main__":
    # Test evaluator
    evaluator = LabelEvaluator(device="cpu")
    
    # Test labels
    test_labels = [
        "modern kitchen",
        "spacious living room",
        "hardwood flooring",
        "natural lighting",
        "contemporary design"
    ]
    
    print("Testing Evaluator")
    print("="*60)
    
    # Test metrics
    print(f"\nSpecificity: {evaluator.compute_specificity(test_labels):.3f}")
    print(f"Redundancy: {evaluator.compute_redundancy(test_labels):.3f}")
    
    # Test diversity
    test_property_labels = [
        ["modern kitchen", "hardwood flooring"],
        ["traditional bedroom", "carpet flooring"],
        ["luxury bathroom", "marble countertops"]
    ]
    print(f"Diversity: {evaluator.compute_diversity(test_property_labels):.3f}")
