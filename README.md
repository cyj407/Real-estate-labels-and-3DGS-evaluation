# Real-Estate Semantic Labeling System and 3DGS Reconstruction Quality Evaluation
## Environment Setup
### 1. Prerequisites
- Python 3.9+
- `uv` package manager (recommended) or standard `pip`
```bash
pip install uv
```

### 2. Installation
1. **Install dependencies:**
```bash
uv sync
```
2. **Install Playwright browsers:**
```bash
uv run playwright install chromium
```
3. **Environment Variables:**
Export your OpenAI API key:
```bash
export OPENAI_API_KEY="sk-..."
```

## Task 1: Real-Estate Semantic Labeling System
### Pipeline
- Preprocess --> Scene Classification --> Label Generation --> Evaluation
  - preprocess: download images
  - scene classification: classify scene by SigLip2
  - label generation: generate semantic labels by OpenAI GPT-5-nano
  - evaluation: calculate latency, coverage, diversity, specificity, and redundancy

### Usage

Run the main pipeline to process properties:

```bash
cd semantic-label/src
uv run main.py
```
### Features
- **Scene Classification**: Automatically filters interior vs exterior images using **CLIP** (fast) or **SigLIP** (accurate).
- **Multi-Model Labeling**: Supports semantic label generation using **OpenAI GPT-5-nano**, **SigLIP**, or **CLIP**.
- **Performance Tracking**: Detailed latency monitoring for each pipeline stage.
- **Evaluation Metrics**: Automated calculation of coverage, diversity, specificity, and redundancy.

**Configuration**:
Edit `semantic-label/config.yaml` to switch models or adjust thresholds:
```yaml
scene_classifier:
  type: "siglip"  # Options: "clip", "siglip"

labeling:
  generator_type: "openai"  # Options: "clip", "siglip", or "openai"
```

### Output
- Results are saved in the [`semantic-label/src/results/semantic_labels_results.json`](semantic-label/src/results/semantic_labels_results.json).
- **Latency**: Average latency among all properties:
  ```json
  "mean_seconds": 11.883470129966735,
  "median_seconds": 11.260725021362305,
  "p95_seconds": 15.01300731897354,
  "min_seconds": 9.752989053726196,
  "max_seconds": 15.73918890953064,
  ```
  <details>

  <summary>Latency Per Property</summary>
  ```json
  {
    "details": [
      {
        "property_id": "GZ50364605",
        "stats": {
          "runs": 3,
          "mean_seconds": 12.753605763117472,
          "p95_seconds": 13.92692563533783,
          "min_seconds": 11.995177268981934,
          "max_seconds": 14.125452041625977,
          "raw_latencies": [
            12.140187978744507,
            11.995177268981934,
            14.125452041625977
          ]
        }
      },
      {
        "property_id": "TC08957218",
        "stats": {
          "runs": 3,
          "mean_seconds": 13.396948019663492,
          "p95_seconds": 17.06574490070343,
          "min_seconds": 11.071355104446411,
          "max_seconds": 17.69224500656128,
          "raw_latencies": [
            17.69224500656128,
            11.071355104446411,
            11.427243947982788
          ]
        }
      },
      {
        "property_id": "KS186226",
        "stats": {
          "runs": 3,
          "mean_seconds": 11.313208421071371,
          "p95_seconds": 11.881236481666566,
          "min_seconds": 10.310814142227173,
          "max_seconds": 11.897944211959839,
          "raw_latencies": [
            11.897944211959839,
            11.7308669090271,
            10.310814142227173
          ]
        }
      },
      {
        "property_id": "KS187345",
        "stats": {
          "runs": 3,
          "mean_seconds": 12.689109325408936,
          "p95_seconds": 13.627867937088013,
          "min_seconds": 10.848976135253906,
          "max_seconds": 13.632540941238403,
          "raw_latencies": [
            13.632540941238403,
            13.585810899734497,
            10.848976135253906
          ]
        }
      },
      {
        "property_id": "KS185237",
        "stats": {
          "runs": 3,
          "mean_seconds": 12.061180671056112,
          "p95_seconds": 14.130648231506347,
          "min_seconds": 10.508474111557007,
          "max_seconds": 14.453926801681519,
          "raw_latencies": [
            14.453926801681519,
            10.508474111557007,
            11.22114109992981
          ]
        }
      },
      {
        "property_id": "KS187126",
        "stats": {
          "runs": 3,
          "mean_seconds": 13.987332264582315,
          "p95_seconds": 15.47661371231079,
          "min_seconds": 13.109370946884155,
          "max_seconds": 15.73918890953064,
          "raw_latencies": [
            13.113436937332153,
            13.109370946884155,
            15.73918890953064
          ]
        }
      },
      {
        "property_id": "KS186928",
        "stats": {
          "runs": 3,
          "mean_seconds": 11.473570982615152,
          "p95_seconds": 12.362733316421508,
          "min_seconds": 10.841155052185059,
          "max_seconds": 12.505971908569336,
          "raw_latencies": [
            12.505971908569336,
            10.841155052185059,
            11.073585987091064
          ]
        }
      },
      {
        "property_id": "KS184357",
        "stats": {
          "runs": 3,
          "mean_seconds": 13.759162028630575,
          "p95_seconds": 14.771908378601074,
          "min_seconds": 13.035001039505005,
          "max_seconds": 14.934574842453003,
          "raw_latencies": [
            13.307910203933716,
            14.934574842453003,
            13.035001039505005
          ]
        }
      },
      {
        "property_id": "KS181499",
        "stats": {
          "runs": 3,
          "mean_seconds": 12.479379336039225,
          "p95_seconds": 15.1140887260437,
          "min_seconds": 10.599987030029297,
          "max_seconds": 15.537842035293579,
          "raw_latencies": [
            15.537842035293579,
            10.599987030029297,
            11.3003089427948
          ]
        }
      },
      {
        "property_id": "CW67133884",
        "stats": {
          "runs": 3,
          "mean_seconds": 11.138561089833578,
          "p95_seconds": 12.34354088306427,
          "min_seconds": 9.752989053726196,
          "max_seconds": 12.47158932685852,
          "raw_latencies": [
            11.191104888916016,
            12.47158932685852,
            9.752989053726196
          ]
        }
      }
    ]
  }
  ```
  </details>

- **Evaluation Metrics:** Average metrics across all properties.
  ```json
  "mean_coverage": 0.2704926997423172,
  "mean_specificity": 1.9603571428571427,
  "mean_redundancy": 0.7912824928760529,
  "mean_clip_consistency": 0.29532252848148344,
  "diversity": 0.8538550866277004,
  ```
  
  <details>
  
  <summary>Metrics Per Property</summary>
  
  ```json
  {
    "per_property": [
      {
        "coverage": 0.2748434245586395,
        "specificity": 2.066666666666667,
        "redundancy": 0.7785578370094299,
        "clip_consistency": 0.29473698139190674,
        "num_labels": 15,
        "num_images": 20,
        "property_id": "GZ50364605"
      },
      {
        "coverage": 0.2740125060081482,
        "specificity": 1.9285714285714286,
        "redundancy": 0.7695832252502441,
        "clip_consistency": 0.30551597476005554,
        "num_labels": 14,
        "num_images": 19,
        "property_id": "TC08957218"
      },
      {
        "coverage": 0.27422478795051575,
        "specificity": 1.7333333333333334,
        "redundancy": 0.7654905915260315,
        "clip_consistency": 0.3009018003940582,
        "num_labels": 15,
        "num_images": 20,
        "property_id": "KS186226"
      },
      {
        "coverage": 0.2741658687591553,
        "specificity": 1.6875,
        "redundancy": 0.8036534786224365,
        "clip_consistency": 0.29476189613342285,
        "num_labels": 16,
        "num_images": 20,
        "property_id": "KS187345"
      },
      {
        "coverage": 0.27246764302253723,
        "specificity": 2.0,
        "redundancy": 0.8115237951278687,
        "clip_consistency": 0.29205018281936646,
        "num_labels": 12,
        "num_images": 20,
        "property_id": "KS185237"
      },
      {
        "coverage": 0.2756105363368988,
        "specificity": 1.9333333333333333,
        "redundancy": 0.7994362115859985,
        "clip_consistency": 0.3002464771270752,
        "num_labels": 15,
        "num_images": 20,
        "property_id": "KS187126"
      },
      {
        "coverage": 0.25492069125175476,
        "specificity": 2.066666666666667,
        "redundancy": 0.7867103815078735,
        "clip_consistency": 0.2922825217247009,
        "num_labels": 15,
        "num_images": 20,
        "property_id": "KS186928"
      },
      {
        "coverage": 0.26711249351501465,
        "specificity": 2.0714285714285716,
        "redundancy": 0.8080320358276367,
        "clip_consistency": 0.2860683798789978,
        "num_labels": 14,
        "num_images": 20,
        "property_id": "KS184357"
      },
      {
        "coverage": 0.2677983045578003,
        "specificity": 2.1875,
        "redundancy": 0.7850239276885986,
        "clip_consistency": 0.2939707338809967,
        "num_labels": 16,
        "num_images": 20,
        "property_id": "KS181499"
      },
      {
        "coverage": 0.2697707414627075,
        "specificity": 1.9285714285714286,
        "redundancy": 0.8048134446144104,
        "clip_consistency": 0.29269033670425415,
        "num_labels": 14,
        "num_images": 19,
        "property_id": "CW67133884"
      }
    ]
  }

  <summary>Metrics Per Property</summary>

  ```json

  ```
  </details>

## Task 2: 3DGS Reconstruction Quality Evaluation
### Pipeline
- Preprocess --> Evaluation
  - preprocess: download the screenshots of renders
  - evaluation: calculate metrics

### Usage
Evaluate all renders defined in `config.yaml` using all enabled metrics.
```bash
cd 3DGS-Reconstruction-Evaluation/
uv run evaluate.py --skip-capture
```
*This will uses the views under `3DGS-Reconstruction-Evaluation/captured_views/`, and generate reports in [`3DGS-Reconstruction-Evaluation/results/`](3DGS-Reconstruction-Evaluation/results/).*

**Options:**
- `--skip-capture`: Reuse existing screenshots (faster for re-running metrics).
- `--no-report`: Skip generating Markdown reports.
- `--verbose`: Enable debug logging.
- `--metrics`: Specify which metrics to run (cv, vlm, or all).
- `--run`: Run a specific render (index in config.yaml).
- `--url`: Evaluate a single 3DGS URL.
- `--name`: Name for the evaluation run.

**Evaluate Direct URL:**
```bash
uv run evaluate.py --url <url> --name <name>
```

### Features
- **Automated View Capture**: Uses Playwright to capture standardized screenshots from 3DGS web viewers.
- **CV Metrics**: Blur detection, Edge Consistency, BRISQUE, and MANIQA (No-Reference Image Quality).
- **VLM Metrics**: Uses GPT-5-nano for semantic understanding of visual quality, artifacts, and structural integrity.
- **Parallel Processing**: Multithreaded VLM evaluation for speed.
- **Reporting**: Generates detailed Markdown reports and JSON results.

### Configuration (`3DGS-Reconstruction-Quality-Evaluation/config.yaml`)
- **`renders`**: List of 3DGS viewer URLs to evaluate.
- **`capture`**: Settings for screenshot resolution, count, and rotation sensitivity.
- **`cv_metrics`**: Enable/disable Blur, Edge, BRISQUE, MANIQA.
- **`vlm_metrics`**: Configure OpenAI model, workers, and prompts.
- **`weights`**: Adjust the influence of each metric on the final score.

### Output
Results are saved in the `3DGS-Reconstruction-Quality-Evaluation/results/` directory:
- [`comparison_report.md`](3DGS-Reconstruction-Evaluation/results/test_metrics_vlm_only/comparison_report.md): Comparative analysis/ranking of all evaluated renders.
- `*_results.json`: Raw metric data.
- `*_report.md`: Readable report for each render.