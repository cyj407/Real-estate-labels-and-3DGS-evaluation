
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
        self.max_images = self.config.get('labeling', {}).get('openai_max_images', 10)
        
        self.system_prompt = \
        """
        You are an expert real estate agent and interior designer with global property knowledge.
        Your task is to analyze a set of interior photos of a property and generate at leasts 10 high-quality, fascinating, descriptive semantic tags.
        The system must work across multiple regions (e.g., Taiwan, Japan, United States) without retraining.

        The tags MUST:
        1. Cover specific room types present below: kitchen, balcony, living room, tatami room, basement.
        2. Describe architectural or interior style using region-neutral terms when possible, and region-specific terms when clearly identifiable.
        3. Highlight key features visible in the photos (e.g., natural lighting, built-in storage, floor-to-ceiling windows).
        4. Reflect the overall condition (e.g., newly renovated, well-maintained, dated but functional).

        Cross-region requirements:
        - Prefer globally understandable terminology.
        - When a region-specific concept is visually clear, use the correct regional term (e.g., “genkan”, “mansion (JP)”, “walk-up (US)”).
        - Avoid assumptions about region unless visual cues strongly indicate it.
        - Normalize similar concepts across regions (e.g., balcony / veranda / lanai → balcony).

        Output constraints:
        - Output at leasts 10 comma-separated tags.
        - Tags should be concise (1–3 words each).
        - Do NOT include explanations, sentences, or region names.
        """

    def _encode_image(self, image_path: str) -> str:
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
        if len(image_paths) > self.max_images:
            indices = [int(i * (len(image_paths) - 1) / (self.max_images - 1)) for i in range(self.max_images)]
            selected_paths = [image_paths[i] for i in indices]
            # Ensure unique in case of small list logic
            selected_paths = list(dict.fromkeys(selected_paths))

        print(f"  Sending {len(selected_paths)} images to OpenAI ({self.model})...")
        
        messages = [
            {"role": "developer", "content": self.system_prompt},
        ]
        
        user_content = [{"type": "input_text", "text": "Analyze these property images and provide semantic tags."}]
        
        for img_path in selected_paths:
            try:
                base64_image = self._encode_image(img_path)
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
