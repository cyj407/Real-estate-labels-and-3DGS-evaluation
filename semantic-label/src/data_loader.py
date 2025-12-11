"""
Data loader for real estate property images and metadata.
Handles JSON parsing, image downloading, and caching.
"""

import json
import os
from pathlib import Path
from typing import Dict, List, Tuple
from concurrent.futures import ThreadPoolExecutor, as_completed
import requests
from PIL import Image
from io import BytesIO
from tqdm import tqdm


class PropertyDataLoader:
    """Load and manage property data with image caching."""
    
    def __init__(self, dataset_dir: str, cache_dir: str = "cache/images"):
        self.dataset_dir = Path(dataset_dir)
        self.cache_dir = Path(cache_dir)
        self.cache_dir.mkdir(parents=True, exist_ok=True)
        
    def load_property_data(self, json_path: str) -> Dict:
        """Load property data from JSON file."""
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data
    
    def get_property_id(self, data: Dict) -> str:
        """Extract property ID from data."""
        return data['listing']['property_id']
    
    def download_image(self, url: str, save_path: Path) -> bool:
        """Download a single image from URL."""
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            
            # Open and save image
            img = Image.open(BytesIO(response.content))
            img = img.convert('RGB')  # Ensure RGB format
            img.save(save_path)
            return True
        except Exception as e:
            print(f"Failed to download {url}: {e}")
            return False
    
    def download_images(self, property_data: Dict, max_workers: int = 8) -> List[str]:
        """
        Download all images for a property with parallel processing.
        Returns list of local image paths.
        """
        property_id = self.get_property_id(property_data)
        image_urls = property_data['listing']['picture_list']
        
        # Create property-specific cache directory
        property_cache_dir = self.cache_dir / property_id
        property_cache_dir.mkdir(parents=True, exist_ok=True)
        
        downloaded_paths = []
        
        # Check which images are already cached
        download_tasks = []
        for idx, url in enumerate(image_urls):
            # Create filename from URL or use index
            filename = f"image_{idx:03d}.jpg"
            save_path = property_cache_dir / filename
            
            if save_path.exists():
                downloaded_paths.append(str(save_path))
            else:
                download_tasks.append((url, save_path, idx))
        
        # Download missing images in parallel
        if download_tasks:
            print(f"Downloading {len(download_tasks)} images for property {property_id}...")
            with ThreadPoolExecutor(max_workers=max_workers) as executor:
                futures = {
                    executor.submit(self.download_image, url, save_path): (save_path, idx)
                    for url, save_path, idx in download_tasks
                }
                
                for future in tqdm(as_completed(futures), total=len(futures), desc="Downloading"):
                    save_path, idx = futures[future]
                    if future.result():
                        downloaded_paths.append(str(save_path))
        
        # Sort by index to maintain order
        downloaded_paths.sort()
        return downloaded_paths
    
    def load_all_properties(self) -> List[Tuple[Dict, List[str]]]:
        """
        Load all properties from dataset directory.
        Returns list of (property_data, image_paths) tuples.
        """
        json_files = sorted(self.dataset_dir.glob("property_*.json"))
        
        if not json_files:
            raise ValueError(f"No property JSON files found in {self.dataset_dir}")
        
        print(f"Found {len(json_files)} properties")
        
        properties = []
        for json_path in json_files:
            print(f"\nLoading {json_path.name}...")
            property_data = self.load_property_data(json_path)
            image_paths = self.download_images(property_data)
            properties.append((property_data, image_paths))
            print(f"  Property ID: {self.get_property_id(property_data)}")
            print(f"  Images: {len(image_paths)}")
        
        return properties
    
    def get_property_metadata(self, property_data: Dict) -> Dict:
        """Extract useful metadata from property data."""
        listing = property_data['listing']
        return {
            'property_id': listing['property_id'],
            'title': listing['title'],
            'property_type': listing['property_type'],
            'city': listing['city'],
            'district': listing['district'],
            'num_bedroom': listing['num_bedroom'],
            'num_bathroom': listing['num_bathroom'],
            'interior_area': listing['interior_area'],
            'property_age': listing['property_age'],
        }


if __name__ == "__main__":
    # Test the data loader
    loader = PropertyDataLoader(
        dataset_dir="../dataset",
        cache_dir="../cache/images"
    )
    
    properties = loader.load_all_properties()
    print(f"\n{'='*60}")
    print(f"Successfully loaded {len(properties)} properties")
    
    for property_data, image_paths in properties:
        metadata = loader.get_property_metadata(property_data)
        print(f"\n{metadata['property_id']}: {metadata['title']}")
        print(f"  Type: {metadata['property_type']}, {metadata['num_bedroom']}BR/{metadata['num_bathroom']}BA")
        print(f"  Images: {len(image_paths)}")
