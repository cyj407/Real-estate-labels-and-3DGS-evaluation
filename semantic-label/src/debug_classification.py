"""
Debug script to test interior/exterior classification on sample images.
"""

import sys
sys.path.append('..')

from scene_classifier import SceneClassifier
from data_loader import PropertyDataLoader
from PIL import Image

# Load data
loader = PropertyDataLoader(
    dataset_dir="../dataset",
    cache_dir="../cache/images"
)

# Load first property
properties = loader.load_all_properties()
if properties:
    property_data, image_paths = properties[0]
    property_id = loader.get_property_id(property_data)
    
    print(f"Testing classification on property {property_id}")
    print(f"Total images: {len(image_paths)}\n")
    
    # Initialize classifier
    classifier = SceneClassifier(device="cpu")
    
    # Test on first 5 images individually
    for i, img_path in enumerate(image_paths[:5]):
        label, confidence = classifier.classify_single_image(img_path)
        print(f"Image {i+1}: {label} (confidence: {confidence:.3f})")
        print(f"  Path: {img_path}")
        
        # Load and display image size
        try:
            img = Image.open(img_path)
            print(f"  Size: {img.size}")
        except:
            pass
        print()
