
import os
import base64
import json
from typing import List, Dict
from openai import OpenAI
import time

class OpenAILabelGenerator:
    """Generates semantic labels for properties using OpenAI's Vision API."""
    
    def __init__(self, config, device=None):
        """
        Initialize the OpenAI label generator.
        
        Args:
            config: Full configuration dictionary
            device: Ignored, kept for compatibility with other generators
        """
        self.config = config
        api_key = os.environ.get("OPENAI_API_KEY")
        if not api_key:
            print("WARNING: OPENAI_API_KEY environment variable not found.")
        
        self.client = OpenAI(api_key=api_key)
        self.model = self.config.get('labeling', {}).get('openai_model', 'gpt-5-nano')
        
        self.system_prompt = self.config.get('labeling', {}).get('system_prompt')
        if not self.system_prompt:
             print("WARNING: system_prompt not found in config. Using fallback default.")
             # Fallback default prompt if config is missing
             self.system_prompt = "You are an expert real estate agent. Analyze these interior photos and generate at least 10 descriptive semantic tags (e.g., room types, features, style)."

    def encode_image(self, image_path: str) -> str:
        """Encode image to base64 string."""
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode('utf-8')

    def generate_labels(self, image_paths: List[str]) -> Dict:
        """
        Generate tags for a property based on its interior images.
        
        Args:
            image_paths: List of paths to interior images
            
        Returns:
            Dictionary containing 'labels' and 'labels_with_scores'
        """
        if not image_paths:
            return {"labels": [], "labels_with_scores": []}
            
        # Select a subset of images to avoid payload limits/costs
        # We take evenly spaced images to get a good distribution
        selected_paths = image_paths

        print(f"  Sending {len(selected_paths)} images to OpenAI ({self.model})...")
        
        messages = [
            {"role": "developer", "content": self.system_prompt},
        ]
        
        user_content = [{"type": "input_text", "text": "Analyze these property images and provide semantic tags."}]
        
        for img_path in selected_paths:
            try:
                base64_image = self.encode_image(img_path)
                user_content.append({
                    "type": "input_image",
                    "image_url": f"data:image/jpeg;base64,{base64_image}",
                    "detail": "low" # Use low detail for speed and cost efficiency
                })
            except Exception as e:
                print(f"  Warning: Could not encode {img_path}: {e}")
                
        messages.append({"role": "user", "content": user_content})

        try:
            start_time = time.time()
            response = self.client.responses.create(
                model=self.model,
                input=messages,
                reasoning={ "effort": "low" },
                max_output_tokens=10000,
            )
            elapsed = time.time() - start_time
            print(f"  OpenAI response received in {elapsed:.2f}s")
           
            print(response)
            result_text = response.output_text
            print(f"  Raw response: {result_text}")
            
            # Parse comma-separated tags
            # Remove potential markdown code blocks if any
            clean_text = result_text
            if "```" in clean_text:
                clean_text = clean_text.replace("```json", "").replace("```", "").strip()
            
            # Split by comma
            tags = [tag.strip() for tag in clean_text.split(',')]
            # Remove empty strings
            tags = [t for t in tags if t]
            
            return {
                "labels": tags
            }
            
        except Exception as e:
            print(f"  ERROR calling OpenAI API: {e}")
            import traceback
            traceback.print_exc()
            return {"labels": []}


if __name__ == "__main__":
    # Test the generator
    import sys
    sys.path.append('..')
    
    from data_loader import PropertyDataLoader
    import yaml
    
    # Load test data
    loader = PropertyDataLoader(
        dataset_dir="../dataset",
        cache_dir="../cache/images"
    )

    with open('../config.yaml', 'r') as f:
        config = yaml.safe_load(f)

    # Initialize generator
    generator = OpenAILabelGenerator(config)
    
    properties = loader.load_all_properties()
    
    # Test on first property
    property_data, image_paths = properties[0]
    property_id = loader.get_property_id(property_data)
    
    print(f"\nTesting OpenAI label generator on property {property_id}")
    print(f"Total images: {len(image_paths)}")
    
    # Use first 5 images for testing
    test_images = image_paths[:5]
    
    result = generator.generate_labels(
        test_images
    )
    
    print(f"\n✓ Generated {len(result['labels'])} labels:")
    
    print(f"\nLabels:")
    for label in result['labels']:
        print(f"  - {label}")
