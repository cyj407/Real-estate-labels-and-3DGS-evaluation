"""
Automated view capture system for 3DGS renders using Playwright.
Captures multiple viewpoints by programmatically rotating the camera.
"""

import asyncio
import json
import math
from pathlib import Path
from typing import Dict, List, Optional
from playwright.async_api import async_playwright, Page, Browser
from PIL import Image
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class ViewCapturer:
    """Captures multiple views from 3DGS web viewer by rotating camera."""
    
    def __init__(self, config: Dict):
        """
        Initialize view capturer with configuration.
        
        Args:
            config: Configuration dictionary with capture settings
        """
        self.config = config
        self.capture_config = config.get("capture", {})
        self.num_views = self.capture_config.get("num_views", 12)
        self.wait_time = self.capture_config.get("wait_time", 3000)
        self.viewport_width = self.capture_config.get("viewport_width", 1920)
        self.viewport_height = self.capture_config.get("viewport_height", 1080)
        self.output_dir = Path(self.capture_config.get("output_dir", "captured_views"))
        self.timeout = self.capture_config.get("timeout", 60000)  # Default 60s timeout
        
    async def capture_views(
        self, 
        render_name: str, 
        url: str,
        output_subdir: Optional[str] = None
    ) -> List[Dict]:
        """
        Capture multiple views from a 3DGS render.
        
        Args:
            render_name: Name identifier for this render
            url: URL of the 3DGS viewer
            output_subdir: Optional subdirectory for outputs
            
        Returns:
            List of dictionaries containing view metadata and file paths
        """
        output_path = self.output_dir / (output_subdir or render_name)
        output_path.mkdir(parents=True, exist_ok=True)
        
        views = []
        
        async with async_playwright() as p:
            browser = await p.chromium.launch(
                headless=True,
                args=[
                    '--disable-web-security', 
                    '--disable-features=IsolateOrigins,site-per-process',
                    '--disable-gpu',
                    '--use-gl=swiftshader'
                ]
            )
            page = await browser.new_page(
                viewport={"width": self.viewport_width, "height": self.viewport_height}
            )
            
            try:
                logger.info(f"Loading {render_name} from {url}")
                await page.goto(url, wait_until="networkidle", timeout=self.timeout)
                
                # Wait for initial scene load
                await asyncio.sleep(self.wait_time / 1000)
                
                # Capture views at different rotation angles
                rotation_step = 360 / self.num_views
                
                for i in range(self.num_views):
                    angle = i * rotation_step
                    logger.info(f"Capturing view {i+1}/{self.num_views} at {angle}°")
                    
                    # Rotate camera if not the first view
                    if i > 0:
                        await self._rotate_camera(page, rotation_step)
                        await asyncio.sleep(1)  # Wait for scene to stabilize
                    
                    # Capture screenshot
                    screenshot_path = output_path / f"view_{i:03d}_{int(angle):03d}deg.png"
                    await page.screenshot(path=str(screenshot_path), full_page=False, timeout=self.timeout)
                    
                    # Store metadata
                    view_data = {
                        "view_index": i,
                        "angle": angle,
                        "render_name": render_name,
                        "screenshot_path": str(screenshot_path),
                        "url": url
                    }
                    views.append(view_data)
                    
                    logger.info(f"Saved: {screenshot_path}")
                
                # Save metadata
                metadata_path = output_path / "views_metadata.json"
                with open(metadata_path, "w") as f:
                    json.dump(views, f, indent=2)
                
                logger.info(f"Captured {len(views)} views for {render_name}")
                
            except Exception as e:
                logger.error(f"Error capturing views for {render_name}: {e}")
                raise
            finally:
                await browser.close()
        
        return views
    
    async def _rotate_camera(self, page: Page, degrees: float):
        """
        Rotate the camera by simulating mouse drag.
        
        Args:
            page: Playwright page object
            degrees: Degrees to rotate
        """
        # Calculate drag distance using configured sensitivity
        # Default 5.0 if not specified (previous 2.5/3.0 were too low)
        sensitivity = self.capture_config.get("rotation_sensitivity", 5.0)
        drag_distance = degrees * sensitivity
        
        # Get viewport center
        center_x = self.viewport_width / 2
        center_y = self.viewport_height / 2
        
        # Simulate horizontal drag to rotate
        await page.mouse.move(center_x, center_y)
        await page.mouse.down()
        await page.mouse.move(center_x + drag_distance, center_y, steps=10)
        await page.mouse.up()
    
    async def capture_all_renders(self, renders: List[Dict]) -> Dict[str, List[Dict]]:
        """
        Capture views from all renders in the configuration.
        
        Args:
            renders: List of render configurations
            
        Returns:
            Dictionary mapping render names to their view metadata
        """
        all_views = {}
        
        for render in renders:
            name = render["name"]
            url = render["url"]
            
            try:
                views = await self.capture_views(name, url)
                all_views[name] = views
            except Exception as e:
                logger.error(f"Failed to capture {name}: {e}")
                all_views[name] = []
        
        return all_views
    
    def load_existing_views(self, render_name: str) -> List[Dict]:
        """
        Load metadata for previously captured views.
        
        Args:
            render_name: Name of the render
            
        Returns:
            List of view metadata dictionaries
        """
        metadata_path = self.output_dir / render_name / "views_metadata.json"
        
        if not metadata_path.exists():
            logger.warning(f"No existing views found for {render_name}")
            return []
        
        with open(metadata_path, "r") as f:
            return json.load(f)


async def main():
    """Test the view capturer with a sample configuration."""
    import yaml
    
    # Load config
    config_path = Path(__file__).parent.parent.parent / "config.yaml"
    with open(config_path) as f:
        config = yaml.safe_load(f)
    
    capturer = ViewCapturer(config)
    
    # Test with first render
    render = config["renders"][0]
    views = await capturer.capture_views(render["name"], render["url"])
    
    print(f"\nCaptured {len(views)} views")
    for view in views[:3]:  # Show first 3
        print(f"  View {view['view_index']}: {view['angle']}° -> {view['screenshot_path']}")


if __name__ == "__main__":
    asyncio.run(main())
