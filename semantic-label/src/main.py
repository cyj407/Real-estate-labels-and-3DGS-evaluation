"""
Main pipeline for real-estate semantic labeling system.
Orchestrates end-to-end processing with latency tracking.
"""

import json
import time
from pathlib import Path
from typing import Dict, List
import yaml
import numpy as np

from data_loader import PropertyDataLoader
from clip_classifier import ClipSceneClassifier
from siglip_classifier import SigLIPSceneClassifier
from label_generator import LabelGenerator
from siglip_label_generator import SigLIPLabelGenerator
from openai_label_generator import OpenAILabelGenerator
from region_adapter import RegionAdapter
from evaluator import LabelEvaluator


class SemanticLabelingPipeline:
    """End-to-end pipeline for property semantic labeling."""
    
    def __init__(self, config_path: str = "../config.yaml"):
        with open(config_path, 'r') as f:
            self.config = yaml.safe_load(f)
        
        self.device = self.config['model']['device']
        self.results_dir = Path(self.config['output']['results_dir'])
        self.results_dir.mkdir(parents=True, exist_ok=True)
        
        # Initialize components
        print("Initializing pipeline components...")
        self.data_loader = PropertyDataLoader(
            dataset_dir="../dataset",
            cache_dir=self.config['optimization']['image_cache_dir']
        )
        
        # Initialize scene classifier based on config
        classifier_type = self.config.get('scene_classifier', {}).get('type', 'clip')
        
        if classifier_type == 'siglip':
            print("Using SigLIP scene classifier")
            siglip_model = self.config['scene_classifier'].get('siglip_model', 'google/siglip2-base-patch16-224')
            self.scene_classifier = SigLIPSceneClassifier(
                model_name=siglip_model,
                device=self.device
            )
        else:
            print("Using CLIP scene classifier")
            self.scene_classifier = ClipSceneClassifier(
                model_name=self.config['model']['name'],
                pretrained=self.config['model']['pretrained'],
                device=self.device
              )
        
        # Initialize label generator based on config
        self.generator_type = self.config.get('labeling', {}).get('generator_type', 'clip')
        
        if self.generator_type == 'siglip':
            print("Using SigLIP label generator")
            siglip_model = self.config['scene_classifier'].get('siglip_model', 'google/siglip2-base-patch16-224')
            self.label_generator = SigLIPLabelGenerator(
                config_path=config_path,
                model_name=siglip_model,
                device=self.device
            )
        elif self.generator_type == 'openai':
            print("Using OpenAI label generator")
            self.label_generator = OpenAILabelGenerator(
                config=self.config,
                device=self.device
            )
        else: # CLIP
            print("Using CLIP label generator")
            self.label_generator = LabelGenerator(
                config_path=config_path,
                model_name=self.config['model']['name'],
                pretrained=self.config['model']['pretrained'],
                device=self.device
            )
        
        self.region_adapter = RegionAdapter(config_path=config_path)
        self.evaluator = LabelEvaluator(
            config_path=config_path,
            model_name=self.config['model']['name'],
            pretrained=self.config['model']['pretrained'],
            device=self.device
        )
        
        print("Pipeline initialized successfully!\n")
    
    def process_property(
        self, 
        property_data: Dict, 
        image_paths: List[str]
    ) -> Dict:
        """
        Process a single property through the complete pipeline.
        
        Returns:
            Dictionary with labels, metadata, and timing information
        """
        start_time = time.time()
        
        property_id = self.data_loader.get_property_id(property_data)
        metadata = self.data_loader.get_property_metadata(property_data)
        
        print(f"\n{'='*60}")
        print(f"Processing Property: {property_id}")
        print(f"Title: {metadata['title']}")
        print(f"Total Images: {len(image_paths)}")
        
        # Stage 1: Filter interior images
        stage1_start = time.time()
        interior_paths, classification_stats = self.scene_classifier.filter_interior_images(
            image_paths,
            batch_size=self.config['model']['batch_size']
        )
        stage1_time = time.time() - stage1_start
        
        # Stage 2: Generate semantic labels & Apply region adaptation
        stage2_start = time.time()
        label_result = self.label_generator.generate_labels(
            interior_paths,
            # top_k_total=self.config['labeling']['top_k_labels']
        )
        
        if self.generator_type != 'openai':
            label_result = self.region_adapter.enrich_with_region_context(
                label_result['labels'],
                metadata
            )
        stage2_time = time.time() - stage2_start
        
        # Stage 3: Evaluate labels
        stage3_start = time.time()
        evaluation_metrics = self.evaluator.evaluate_property(
            label_result['adapted_labels'] if self.generator_type != 'openai' else label_result['labels'],
            interior_paths
        )
        error_analysis = self.evaluator.analyze_errors(
            label_result['adapted_labels'] if self.generator_type != 'openai' else label_result['labels'],
            interior_paths
        )
        stage3_time = time.time() - stage3_start
        
        total_time = time.time() - start_time
        
        # Compile results
        result = {
            'property_id': property_id,
            'metadata': metadata,
            'labels': label_result['labels'] if isinstance(label_result, dict) and 'labels' in label_result else label_result,
            # 'labels_with_scores': label_result['labels_with_scores'],
            'image_stats': {
                'total_images': len(image_paths),
                'interior_images': len(interior_paths),
                'exterior_images': len(image_paths) - len(interior_paths),
                'interior_ratio': classification_stats['interior_ratio']
            },
            'evaluation': evaluation_metrics,
            'error_analysis': error_analysis,
            'timing': {
                'total_seconds': total_time,
                'stage1_classification': stage1_time,
                'stage2_labeling': stage2_time,
                'stage3_evaluation': stage3_time
            }
        }
        
        # Print summary
        print(f"\n✓ Processing Complete ({total_time:.2f}s)")
        print(f"  Interior Images: {len(interior_paths)}/{len(image_paths)}")
        print(f"  Generated Labels: {len(result['labels'])}")
        # print(f"  Region: {region_result['region']}")
        # print(f"\n  Top Labels:")
        # for item in label_result['labels_with_scores'][:5]:
        #     print(f"    - {item['label']} ({item['score']:.3f})")
        
        return result
    
    def process_all_properties(self) -> Dict:
        """
        Process all properties in the dataset.
        
        Returns:
            Aggregated results with metrics and timing statistics
        """
        print("="*60)
        print("REAL-ESTATE SEMANTIC LABELING PIPELINE")
        print("="*60)
        
        # Load all properties
        properties = self.data_loader.load_all_properties()
        
        num_runs = self.config.get('evaluation', {}).get('num_runs', 1)
        if num_runs > 1:
            print(f"Running {num_runs} iterations for latency benchmarking...")
            
        # Process each property
        all_results = []
        for property_data, image_paths in properties:
            # Run multiple times if configured
            property_latencies = []
            final_result = None
            
            for i in range(num_runs):
                if num_runs > 1:
                    print(f"  Run {i+1}/{num_runs} for property {property_data.get('property_id')}")
                    
                result = self.process_property(property_data, image_paths)
                property_latencies.append(result['timing']['total_seconds'])
                final_result = result
            
            # Use result from last run, but enrich with latency stats
            final_result['image_paths'] = image_paths  # For evaluation
            final_result['latency_stats'] = {
                'runs': num_runs,
                'mean_seconds': float(np.mean(property_latencies)),
                'p95_seconds': float(np.percentile(property_latencies, 95)),
                'min_seconds': float(np.min(property_latencies)),
                'max_seconds': float(np.max(property_latencies)),
                'raw_latencies': property_latencies
            }
            all_results.append(final_result)
        
        # Compute aggregate metrics
        print(f"\n{'='*60}")
        print("COMPUTING AGGREGATE METRICS")
        print("="*60)
        
        aggregate_metrics = self.evaluator.evaluate_all_properties(all_results)
        
        # Compute latency statistics
        latencies = [r['timing']['total_seconds'] for r in all_results]
        latency_stats = {
            'mean_seconds': np.mean(latencies),
            'median_seconds': np.median(latencies),
            'p95_seconds': np.percentile(latencies, 95),
            'min_seconds': np.min(latencies),
            'max_seconds': np.max(latencies),
            'details': [
                {
                    'property_id': r['property_id'],
                    'stats': r['latency_stats']
                } for r in all_results
            ]
        }
        
        # Compile final results
        final_results = {
            'summary': {
                'total_properties': len(all_results),
                'timestamp': time.strftime('%Y-%m-%d %H:%M:%S'),
                'config': {
                    'model': self.config['model']['name'],
                    'device': self.device,
                    'top_k_labels': self.config['labeling']['top_k_labels']
                }
            },
            'latency_statistics': latency_stats,
            'aggregate_metrics': aggregate_metrics,
            'properties': all_results
        }
        
        # Print summary
        print(f"\nLatency Statistics:")
        print(f"  Mean: {latency_stats['mean_seconds']:.2f}s")
        print(f"  Median: {latency_stats['median_seconds']:.2f}s")
        print(f"  P95: {latency_stats['p95_seconds']:.2f}s")
        print(f"  Range: [{latency_stats['min_seconds']:.2f}s, {latency_stats['max_seconds']:.2f}s]")
        
        print(f"\nAggregate Metrics:")
        print(f"  Coverage: {aggregate_metrics['mean_coverage']:.3f}")
        print(f"  Diversity: {aggregate_metrics['diversity']:.3f}")
        print(f"  Specificity: {aggregate_metrics['mean_specificity']:.3f}")
        print(f"  Redundancy: {aggregate_metrics['mean_redundancy']:.3f}")
        print(f"  CLIP Consistency: {aggregate_metrics['mean_clip_consistency']:.3f}")
        
        return final_results
    
    def save_results(self, results: Dict, filename: str = "results.json"):
        """Save results to JSON file."""
        output_path = self.results_dir / filename
        
        # Remove image_paths from results (too verbose for JSON)
        clean_results = results.copy()
        for prop in clean_results.get('properties', []):
            prop.pop('image_paths', None)
        
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(clean_results, f, indent=2, ensure_ascii=False)
        
        print(f"\n✓ Results saved to: {output_path}")
        return output_path


def main():
    """Main entry point."""
    import sys
    
    # Initialize pipeline
    pipeline = SemanticLabelingPipeline(config_path="../config.yaml")
    
    # Process all properties
    results = pipeline.process_all_properties()
    
    # Save results
    pipeline.save_results(results, filename="semantic_labels_results.json")
    
    print(f"\n{'='*60}")
    print("PIPELINE COMPLETE!")
    print("="*60)


if __name__ == "__main__":
    main()
