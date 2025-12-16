#!/usr/bin/env python3
"""
CLI for 3DGS Reconstruction Quality Evaluation System.

Usage:
    python evaluate.py                          # Evaluate all renders from config
    python evaluate.py --run 1                  # Evaluate specific run (1-indexed)
    python evaluate.py --config custom.yaml     # Use custom config
    python evaluate.py --skip-capture           # Use existing captured views
    python evaluate.py --metrics cv             # Use only CV metrics
    python evaluate.py --metrics vlm            # Use only VLM metrics
"""

import argparse
import asyncio
import os
import sys
from pathlib import Path
import logging

# Add src to path
sys.path.insert(0, str(Path(__file__).parent))

from src.evaluator import ReconstructionEvaluator
from src.report_generator import ReportGenerator

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def parse_args():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description="3DGS Reconstruction Quality Evaluation System",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
        Examples:
        # Evaluate all renders
        python evaluate.py
        
        # Evaluate specific run
        python evaluate.py --run 1
        
        # Use custom configuration
        python evaluate.py --config my_config.yaml
        
        # Skip view capture (use existing images)
        python evaluate.py --skip-capture
        
        # Use only CV metrics
        python evaluate.py --metrics cv
        
        # Use only VLM metrics (requires OPENAI_API_KEY)
        python evaluate.py --metrics vlm
        
        # Evaluate specific URL
        python evaluate.py --url https://example.com/viewer --name "My Render"
        """
    )
    
    parser.add_argument(
        "--config",
        type=str,
        default="config.yaml",
        help="Path to configuration file (default: config.yaml)"
    )
    
    parser.add_argument(
        "--run",
        type=int,
        help="Evaluate specific run number (1-indexed)"
    )
    
    parser.add_argument(
        "--url",
        type=str,
        help="Evaluate a specific 3DGS viewer URL directly"
    )

    parser.add_argument(
        "--name",
        type=str,
        help="Name for the direct URL evaluation (default: extracted or 'custom_render')"
    )
    
    parser.add_argument(
        "--skip-capture",
        action="store_true",
        help="Skip view capture and use existing images"
    )
    
    parser.add_argument(
        "--metrics",
        choices=["all", "cv", "vlm"],
        default="all",
        help="Which metrics to run (default: all)"
    )
        
    parser.add_argument(
        "--output-dir",
        type=str,
        help="Override output directory from config"
    )
    
    parser.add_argument(
        "--no-report",
        action="store_true",
        help="Skip report generation"
    )
    
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Enable verbose logging"
    )
    
    return parser.parse_args()


import http.server
import socketserver
import threading
from contextlib import contextmanager

@contextmanager
def serve_file(file_path: Path):
    """Serve a file directory temporarily."""
    port = 8086
    dirname = file_path.parent
    
    class Handler(http.server.SimpleHTTPRequestHandler):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, directory=str(dirname), **kwargs)
            
        def log_message(self, format, *args):
            pass  # Silence logs
            
    httpd = socketserver.TCPServer(("", port), Handler)
    server_thread = threading.Thread(target=httpd.serve_forever, daemon=True)
    server_thread.start()
    
    try:
        url = f"http://localhost:{port}/{file_path.name}"
        yield url
    finally:
        httpd.shutdown()
        httpd.server_close()


async def main():
    """Main CLI entry point."""
    args = parse_args()
    
    # Set logging level
    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)
    
    # Check config file
    config_path = Path(args.config)
    if not config_path.exists():
        logger.error(f"Configuration file not found: {config_path}")
        return 1
    
    # Modify config based on args
    import yaml
    with open(config_path) as f:
        config = yaml.safe_load(f)
    
    # Disable metrics based on selection
    if args.metrics == "cv":
        config["vlm_metrics"]["enabled"] = False
        logger.info("VLM metrics disabled (CV only mode)")
    elif args.metrics == "vlm":
        config["cv_metrics"]["blur"]["enabled"] = False
        config["cv_metrics"]["edge_consistency"]["enabled"] = False
        config["cv_metrics"]["brisque"]["enabled"] = False
        config["cv_metrics"]["maniqa"]["enabled"] = False

        logger.info("CV metrics disabled (VLM only mode)")
    
    # Override output dir
    if args.output_dir:
        config["output"]["results_dir"] = args.output_dir
    
    # Save modified config temporarily
    temp_config_path = Path("temp_config.yaml")
    with open(temp_config_path, "w") as f:
        yaml.dump(config, f)
    
    try:
        # Initialize evaluator
        logger.info("Initializing evaluator...")
        evaluator = ReconstructionEvaluator(
            config_path=str(temp_config_path)
        )
        
        # Evaluate
        if args.url:
            # Evaluate direct URL
            from urllib.parse import urlparse
            
            # Determine name
            if args.name:
                name = args.name
            else:
                # Try to extract from URL or query params
                parsed = urlparse(args.url)
                # Logic to extract something meaningful or default
                name = "custom_render"
                
            logger.info(f"Evaluating direct URL: {name}")
            
            results = await evaluator.evaluate_render(
                name,
                args.url,
                skip_capture=args.skip_capture
            )
            
            all_results = {name: results}
            
        elif args.run is not None:
            # Evaluate specific run
            renders = config.get("renders", [])
            if args.run < 1 or args.run > len(renders):
                logger.error(f"Invalid run number: {args.run}. Must be 1-{len(renders)}")
                return 1
            
            render = renders[args.run - 1]
            logger.info(f"Evaluating run {args.run}: {render['name']}")
            
            results = await evaluator.evaluate_render(
                render["name"],
                render["url"],
                skip_capture=args.skip_capture
            )
            
            all_results = {render["name"]: results}
        else:
            # Evaluate all runs
            logger.info("Evaluating all renders...")
            all_results = await evaluator.evaluate_all_renders(
                skip_capture=args.skip_capture
            )
        
        # Generate reports
        if not args.no_report:
            logger.info("\nGenerating reports...")
            report_gen = ReportGenerator(evaluator.output_dir)
            report_gen.save_all_reports(all_results)
        
        logger.info("\n" + "="*60)
        logger.info("EVALUATION COMPLETE")
        logger.info("="*60)
        logger.info(f"Results saved to: {evaluator.output_dir}")
        
        # Print summary
        print("\n" + "="*60)
        print("SUMMARY")
        print("="*60)
        for name, results in all_results.items():
            if "error" in results:
                print(f"❌ {name}: ERROR - {results['error']}")
            else:
                score = results.get("overall_score", 0)
                print(f"✓ {name}: {score:.2f}/100")
        print("="*60 + "\n")
        
        return 0
        
    finally:
        # Clean up temp config
        if temp_config_path.exists():
            temp_config_path.unlink()


if __name__ == "__main__":
    exit_code = asyncio.run(main())
    sys.exit(exit_code)
