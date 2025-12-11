"""
Region adapter for cross-region semantic label adaptation.
Provides training-free adaptation for Taiwan, Japan, and US markets.
"""

from typing import List, Dict, Set
import yaml


class RegionAdapter:
    """Adapt semantic labels for different geographic regions."""
    
    def __init__(self, config_path: str = "../config.yaml"):
        with open(config_path, 'r') as f:
            self.config = yaml.safe_load(f)
        
        self.region_vocab = self.config['regions']['region_vocab']
        self.default_region = self.config['regions']['default']
        
        # Define region-specific synonym mappings
        self.region_synonyms = {
            'japan': {
                'entrance': 'genkan entrance',
                'bathroom': 'unit bath',
                'flooring': 'tatami flooring',
            },
            'us': {
                'storage': 'walk-in closet',
                'countertops': 'granite countertops',
            },
            'taiwan': {
                'balcony': 'balcony with laundry area',
            }
        }
    
    def detect_region(self, property_metadata: Dict) -> str:
        """
        Detect property region from metadata.
        
        Args:
            property_metadata: Property metadata dict with 'city' field
        
        Returns:
            Region code ('taiwan', 'japan', 'us')
        """
        city = property_metadata.get('city', '').lower()
        
        # Simple heuristic based on city names
        # In production, would use more sophisticated location detection
        if any(jp_city in city for jp_city in ['tokyo', '東京', 'osaka', '大阪', 'kyoto']):
            return 'japan'
        elif any(us_city in city for us_city in ['new york', 'los angeles', 'chicago', 'houston']):
            return 'us'
        else:
            # Default to Taiwan for current dataset
            return 'taiwan'
    
    def get_region_vocabulary(self, region: str) -> List[str]:
        """Get region-specific vocabulary additions."""
        return self.region_vocab.get(region, [])
    
    def adapt_labels(
        self, 
        labels: List[str], 
        region: str,
        add_region_specific: bool = True
    ) -> List[str]:
        """
        Adapt labels for a specific region.
        
        Args:
            labels: List of semantic labels
            region: Target region ('taiwan', 'japan', 'us')
            add_region_specific: Whether to add region-specific vocabulary
        
        Returns:
            Adapted label list
        """
        adapted_labels = labels.copy()
        
        # Apply synonym replacements for region
        if region in self.region_synonyms:
            synonyms = self.region_synonyms[region]
            for i, label in enumerate(adapted_labels):
                for generic_term, region_term in synonyms.items():
                    if generic_term in label.lower():
                        # Replace with region-specific term
                        adapted_labels[i] = label.replace(generic_term, region_term)
        
        return adapted_labels
    
    def enrich_with_region_context(
        self, 
        labels: List[str],
        property_metadata: Dict
    ) -> Dict[str, any]:
        """
        Enrich labels with region-specific context.
        
        Returns:
            Dictionary with original labels, region, and adapted labels
        """
        region = self.detect_region(property_metadata)
        adapted_labels = self.adapt_labels(labels, region)
        
        return {
            'original_labels': labels,
            'region': region,
            'adapted_labels': adapted_labels,
            'region_vocabulary': self.get_region_vocabulary(region)
        }
    
    def create_region_aware_prompts(self, base_label: str, region: str) -> str:
        """
        Create region-aware prompt for CLIP.
        
        Args:
            base_label: Base label text
            region: Target region
        
        Returns:
            Region-contextualized prompt
        """
        region_contexts = {
            'taiwan': 'in a Taiwanese apartment',
            'japan': 'in a Japanese apartment',
            'us': 'in an American home'
        }
        
        context = region_contexts.get(region, '')
        if context:
            return f"a photo of {base_label} {context}"
        else:
            return f"a photo of {base_label}"


if __name__ == "__main__":
    # Test region adapter
    adapter = RegionAdapter()
    
    # Test labels
    test_labels = [
        "modern kitchen",
        "spacious living room",
        "bathroom with shower",
        "entrance hallway",
        "balcony"
    ]
    
    # Test metadata
    test_metadata = {
        'city': '高雄市',
        'district': '楠梓區'
    }
    
    print("Testing Region Adapter")
    print("="*60)
    
    result = adapter.enrich_with_region_context(test_labels, test_metadata)
    
    print(f"\nDetected Region: {result['region']}")
    print(f"\nOriginal Labels:")
    for label in result['original_labels']:
        print(f"  - {label}")
    
    print(f"\nAdapted Labels:")
    for label in result['adapted_labels']:
        print(f"  - {label}")
    
    print(f"\nRegion Vocabulary:")
    for vocab in result['region_vocabulary']:
        print(f"  - {vocab}")
