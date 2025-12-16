# 3DGS Reconstruction Quality Report: ktv_hevc_deblur035

**Overall Score**: 43.98/100

**Number of Views Evaluated**: 12

**Render URL**: https://3d-tour-demo-scene.vercel.app/?model=https://storage.googleapis.com/3dgs-homee/ktv_h264hevc.glb&splat=https://storage.googleapis.com/3dgs-homee/ktv_hevc_deblur035.ksplat&px=-3.5&py=0.082&pz=0.38&tx=-2.56&ty=0.007&tz=-0.218


---


## Computer Vision Metrics


### Blur Detection (Laplacian Variance)

- **Quality Score**: 24.09/100

- **Mean Laplacian**: 481.80

- **Std Dev**: 199.65

- **Range**: [185.25, 741.63]


*Higher Laplacian variance indicates sharper images.*


### Edge Consistency

- **Consistency Score**: 52.80/100

- **Mean Edge Density**: 0.1008

- **Std Dev**: 0.0236


*Lower standard deviation indicates more consistent edges across views.*


### BRISQUE Quality Assessment

- **Quality Score**: 45.98/100

- **Mean Score**: 45.98

- **Std Dev**: 2.72


*No-reference quality metric based on natural scene statistics.*


---


## Vision Language Model Metrics


**Model**: gpt-5-nano


### Overall Quality Assessment

- **Quality Score**: 48.33/100

- **Mean Rating**: 4.83/10

- **Std Dev**: 0.80

- **Range**: [3.00, 6.00]


### Artifact Detection

- **Quality Score**: 41.67/100

- **Mean Severity**: 6.83/10

- **Std Dev**: 0.80


*Lower severity indicates fewer visual artifacts (ghosting, floating blobs, etc.).*


### Structural Quality

- **Quality Score**: 46.67/100

- **Mean Rating**: 4.67/10

- **Std Dev**: 0.85


*Higher rating indicates better structural integrity (no warped walls, misaligned edges, etc.).*


---


## Sample Views


### View 1 (0°)

![View 1](/Users/yujiechen/homee_assignment/3DGS-Reconstruction-Evaluation/captured_views/ktv_hevc_deblur035/view_000_000deg.png)


### View 2 (30°)

![View 2](/Users/yujiechen/homee_assignment/3DGS-Reconstruction-Evaluation/captured_views/ktv_hevc_deblur035/view_001_030deg.png)


### View 3 (60°)

![View 3](/Users/yujiechen/homee_assignment/3DGS-Reconstruction-Evaluation/captured_views/ktv_hevc_deblur035/view_002_060deg.png)
