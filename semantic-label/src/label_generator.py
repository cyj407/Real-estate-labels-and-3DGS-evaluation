"""
Semantic label generator using CLIP and hierarchical prompting.
Generates property-level keyword labels from interior images.
"""

import torch
import open_clip
from PIL import Image
from typing import List, Dict, Tuple
import numpy as np
from pathlib import Path
from collections import Counter
import yaml


class LabelGenerator:
    """Generate semantic labels for properties using CLIP."""
    
    def __init__(
        self, 
        config_path: str = "../config.yaml",
        model_name: str = "ViT-B/32", 
        pretrained: str = "openai", 
        device: str = "cpu"
    ):
        self.device = device
        
        # Load configuration
        with open(config_path, 'r') as f:
            self.config = yaml.safe_load(f)
        
        print(f"Loading CLIP model: {model_name} ({pretrained}) on {device}...")
        self.model, _, self.preprocess = open_clip.create_model_and_transforms(
            model_name, pretrained=pretrained
        )
        self.tokenizer = open_clip.get_tokenizer(model_name)
        self.model.to(device)
        self.model.eval()
        
        # Load label vocabularies from config
        self.room_types = self.config['labeling']['room_types']
        self.style_labels = self.config['labeling']['style_labels']
        self.feature_labels = self.config['labeling']['feature_labels']
        self.condition_labels = self.config['labeling']['condition_labels']
        
        # Pre-encode all label texts for efficiency
        self._encode_label_vocabularies()
    
    def _encode_label_vocabularies(self):
        """Pre-encode all label texts to embeddings."""
        print("Encoding label vocabularies...")
        
        self.label_embeddings = {}
        
        for category, labels in [
            ('room_types', self.room_types),
            ('style', self.style_labels),
            ('features', self.feature_labels),
            ('condition', self.condition_labels)
        ]:
            # Create prompts with context
            prompts = [f"a photo of {label}" for label in labels]
            
            with torch.no_grad():
                text_tokens = self.tokenizer(prompts).to(self.device)
                text_features = self.model.encode_text(text_tokens)
                text_features /= text_features.norm(dim=-1, keepdim=True)
            
            self.label_embeddings[category] = {
                'labels': labels,
                'embeddings': text_features
            }
        
        print(f"  Encoded {sum(len(v['labels']) for v in self.label_embeddings.values())} labels")
    
    def encode_images(self, image_paths: List[str], batch_size: int = 16) -> torch.Tensor:
        """Encode images to CLIP embeddings with batching."""
        all_features = []
        
        for i in range(0, len(image_paths), batch_size):
            batch_paths = image_paths[i:i + batch_size]
            batch_images = []
            
            for path in batch_paths:
                try:
                    image = Image.open(path).convert('RGB')
                    batch_images.append(self.preprocess(image))
                except Exception as e:
                    print(f"Error loading {path}: {e}")
            
            if batch_images:
                batch_tensor = torch.stack(batch_images).to(self.device)
                
                with torch.no_grad():
                    features = self.model.encode_image(batch_tensor)
                    features /= features.norm(dim=-1, keepdim=True)
                    all_features.append(features)
        
        if all_features:
            return torch.cat(all_features, dim=0)
        else:
            return torch.empty(0, self.model.visual.output_dim).to(self.device)
    
    def extract_labels_from_category(
        self, 
        image_features: torch.Tensor,
        category: str,
        top_k: int = 3,
        threshold: float = 0.25
    ) -> List[Tuple[str, float]]:
        """
        Extract top-k labels from a specific category.
        Returns list of (label, score) tuples.
        """
        category_data = self.label_embeddings[category]
        labels = category_data['labels']
        text_features = category_data['embeddings']
        
        # Calculate similarity between all images and all labels in category
        similarity = image_features @ text_features.T  # [num_images, num_labels]
        
        # Aggregate across images (mean similarity)
        mean_similarity = similarity.mean(dim=0).cpu().numpy()
        
        # Get top-k labels above threshold
        top_indices = np.argsort(mean_similarity)[::-1]
        
        results = []
        for idx in top_indices[:top_k]:
            score = float(mean_similarity[idx])
            if score >= threshold:
                results.append((labels[idx], score))
        
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
        
        print(f"Generating labels from {len(image_paths)} interior images...")
        
        # Encode all images
        image_features = self.encode_images(
            image_paths, 
            batch_size=self.config['model']['batch_size']
        )
        
        if image_features.shape[0] == 0:
            return {
                'labels': [],
                'labels_with_scores': [],
                'labels_by_category': {},
                'num_images': 0
            }
        
        # Extract labels from each category
        threshold = self.config['labeling']['confidence_threshold']
        max_per_category = self.config['labeling']['max_labels_per_category']
        
        labels_by_category = {
            'room_types': self.extract_labels_from_category(
                image_features, 'room_types', top_k=max_per_category, threshold=threshold
            ),
            'style': self.extract_labels_from_category(
                image_features, 'style', top_k=max_per_category, threshold=threshold
            ),
            'features': self.extract_labels_from_category(
                image_features, 'features', top_k=max_per_category * 2, threshold=threshold
            ),
            'condition': self.extract_labels_from_category(
                image_features, 'condition', top_k=2, threshold=threshold
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
        
        # Deduplicate similar labels
        top_labels = self._deduplicate_labels(top_labels)
        
        print(f"  Generated {len(top_labels)} labels")
        for item in top_labels[:5]:
            print(f"    - {item['label']} ({item['category']}, score: {item['score']:.3f})")
        
        return {
            'labels': [item['label'] for item in top_labels],
            'labels_with_scores': top_labels,
            'labels_by_category': labels_by_category,
            'num_images': len(image_paths)
        }
    
    def _deduplicate_labels(self, labels: List[Dict]) -> List[Dict]:
        """
        Remove redundant/overlapping labels.
        For now, simple deduplication by exact match.
        Could be enhanced with semantic similarity.
        """
        seen = set()
        deduplicated = []
        
        for item in labels:
            label = item['label']
            if label not in seen:
                seen.add(label)
                deduplicated.append(item)
        
        return deduplicated


if __name__ == "__main__":
    from data_loader import PropertyDataLoader
    from scene_classifier import SceneClassifier
    
    # Load data
    loader = PropertyDataLoader(
        dataset_dir="../dataset",
        cache_dir="../cache/images"
    )
    
    properties = loader.load_all_properties()
    
    if properties:
        # Test on first property
        property_data, image_paths = properties[0]
        property_id = loader.get_property_id(property_data)
        
        print(f"\nTesting label generation on property {property_id}")
        
        # Filter interior images
        classifier = ClipSceneClassifier(device="cpu")
        interior_paths, _ = classifier.filter_interior_images(image_paths)
        
        # Generate labels
        generator = LabelGenerator(device="cpu")
        result = generator.generate_labels(interior_paths, top_k_total=10)
        
        print(f"\n{'='*60}")
        print(f"Property: {property_id}")
        print(f"Interior Images: {result['num_images']}")
        print(f"\nTop Labels:")
        for item in result['labels_with_scores']:
            print(f"  - {item['label']} ({item['category']}, {item['score']:.3f})")
