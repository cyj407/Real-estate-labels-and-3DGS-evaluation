# 3DGS Reconstruction Quality Report: ktv_hevc

**Overall Score**: 46.38/100

**Number of Views Evaluated**: 12

**Render URL**: https://3d-tour-demo-scene.vercel.app/?model=https://storage.googleapis.com/3dgs-homee/ktv_h264hevc.glb&splat=https://storage.googleapis.com/3dgs-homee/ktv_hevc.ksplat&px=-3.357&py=0.082&pz=0.38&tx=-2.56&ty=0.007&tz=-0.218


---


## Computer Vision Metrics


### Blur Detection (Laplacian Variance)

- **Quality Score**: 27.66/100

- **Mean Laplacian**: 553.24

- **Std Dev**: 143.08

- **Range**: [297.98, 714.67]


*Higher Laplacian variance indicates sharper images.*


### Edge Consistency

- **Consistency Score**: 50.02/100

- **Mean Edge Density**: 0.1250

- **Std Dev**: 0.0250


*Lower standard deviation indicates more consistent edges across views.*


### BRISQUE Quality Assessment

- **Quality Score**: 47.83/100

- **Mean Score**: 47.83

- **Std Dev**: 3.04


*No-reference quality metric based on natural scene statistics.*


---


## Vision Language Model Metrics


**Model**: gpt-5-nano


### Overall Quality Assessment

- **Quality Score**: 50.00/100

- **Mean Rating**: 5.00/10

- **Std Dev**: 0.91

- **Range**: [4.00, 6.00]


### Artifact Detection

- **Quality Score**: 47.50/100

- **Mean Severity**: 6.25/10

- **Std Dev**: 1.01


*Lower severity indicates fewer visual artifacts (ghosting, floating blobs, etc.).*


### Structural Quality

- **Quality Score**: 51.67/100

- **Mean Rating**: 5.17/10

- **Std Dev**: 1.21


*Higher rating indicates better structural integrity (no warped walls, misaligned edges, etc.).*


---


## Sample Views


### View 1 (0°)

![View 1](/Users/yujiechen/homee_assignment/3DGS-Reconstruction-Evaluation/captured_views/ktv_hevc/view_000_000deg.png)


### View 2 (30°)

![View 2](/Users/yujiechen/homee_assignment/3DGS-Reconstruction-Evaluation/captured_views/ktv_hevc/view_001_030deg.png)


### View 3 (60°)

![View 3](/Users/yujiechen/homee_assignment/3DGS-Reconstruction-Evaluation/captured_views/ktv_hevc/view_002_060deg.png)
