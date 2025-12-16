# 3DGS Reconstruction Quality Report: ktv75

**Overall Score**: 39.05/100

**Number of Views Evaluated**: 12

**Render URL**: https://3d-tour-demo-scene.vercel.app/?model=https://storage.googleapis.com/3dgs-homee/ktv50.glb&splat=https://storage.googleapis.com/3dgs-homee/ktv75.ksplat&px=-3.357&py=0.082&pz=0.38&tx=-2.56&ty=0.007&tz=-0.218


---


## Computer Vision Metrics


### Blur Detection (Laplacian Variance)

- **Quality Score**: 12.49/100

- **Mean Laplacian**: 249.89

- **Std Dev**: 98.06

- **Range**: [120.54, 407.77]


*Higher Laplacian variance indicates sharper images.*


### Edge Consistency

- **Consistency Score**: 52.46/100

- **Mean Edge Density**: 0.0565

- **Std Dev**: 0.0238


*Lower standard deviation indicates more consistent edges across views.*


### BRISQUE Quality Assessment

- **Quality Score**: 41.60/100

- **Mean Score**: 41.60

- **Std Dev**: 2.79


*No-reference quality metric based on natural scene statistics.*


---


## Vision Language Model Metrics


**Model**: gpt-5-nano


### Overall Quality Assessment

- **Quality Score**: 49.17/100

- **Mean Rating**: 4.92/10

- **Std Dev**: 0.76

- **Range**: [4.00, 6.00]


### Artifact Detection

- **Quality Score**: 41.67/100

- **Mean Severity**: 6.83/10

- **Std Dev**: 0.69


*Lower severity indicates fewer visual artifacts (ghosting, floating blobs, etc.).*


### Structural Quality

- **Quality Score**: 46.67/100

- **Mean Rating**: 4.67/10

- **Std Dev**: 0.94


*Higher rating indicates better structural integrity (no warped walls, misaligned edges, etc.).*


---


## Sample Views


### View 1 (0°)

![View 1](/Users/yujiechen/homee_assignment/3DGS-Reconstruction-Evaluation/captured_views/ktv75/view_000_000deg.png)


### View 2 (30°)

![View 2](/Users/yujiechen/homee_assignment/3DGS-Reconstruction-Evaluation/captured_views/ktv75/view_001_030deg.png)


### View 3 (60°)

![View 3](/Users/yujiechen/homee_assignment/3DGS-Reconstruction-Evaluation/captured_views/ktv75/view_002_060deg.png)
