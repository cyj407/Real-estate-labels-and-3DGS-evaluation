# 3DGS Reconstruction Quality Report: ktv_hevc

**Overall Score**: 49.49/100

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

- **Quality Score**: 84.85/100

- **Mean Score**: 84.85

- **Std Dev**: 10.60


*No-reference quality metric based on natural scene statistics.*


---


## Vision Language Model Metrics


**Model**: gpt-5-nano


### Overall Quality Assessment

- **Quality Score**: 49.17/100

- **Mean Rating**: 4.92/10

- **Std Dev**: 0.95

- **Range**: [3.00, 6.00]


### Artifact Detection

- **Quality Score**: 42.50/100

- **Mean Severity**: 6.75/10

- **Std Dev**: 0.72


*Lower severity indicates fewer visual artifacts (ghosting, floating blobs, etc.).*


### Structural Quality

- **Quality Score**: 51.67/100

- **Mean Rating**: 5.17/10

- **Std Dev**: 0.69


*Higher rating indicates better structural integrity (no warped walls, misaligned edges, etc.).*


---


## Detailed View Analysis


### View 1 (0°)

![View 1](captured_views/ktv_hevc/view_000_000deg.png)


**VLM Analysis**:

**Score**: 5/10


> *The render shows a largely plausible room layout, but significant geometric and texture inconsistencies degrade realism. A large left-side void suggests missing geometry, depth cues are inconsistent near windows, and textures exhibit blur and inconsistency, reducing overall fidelity to a real scene.*


**Detected Issues**:
- ⚠️ **Curved Or Warped Walls**: Large black void on the left where wall geometry appears missing or severely occluded, leading to impossible continuation of geometry.
- ⚠️ **Misaligned Edges**: Window frames and curtains show subtle misalignment with surrounding surfaces; edges do not perfectly align with floor/ceiling geometry.
- ⚠️ **Depth Or Perspective Errors**: Depth cues are inconsistent near the window area; some planes appear stretched or foreshortened oddly, suggesting depth errors.
- 🎨 **Floating Artifacts**: Unanchored texture patches near the left wall and ceiling regions; surfaces look like they float or smear away from geometry.
- 🎨 **Over Blur**: Excessive blur on large flat surfaces (table, floor) reducing fine texture fidelity.
- 🎨 **Texture Inconsistency**: Inconsistent texture sharpness across surfaces (curtains vs. upholstery vs. floor) suggesting uneven mip/denoise or rendering bands.


### View 2 (30°)

![View 2](captured_views/ktv_hevc/view_001_030deg.png)


**VLM Analysis**:

**Score**: 6/10


> *The scene is broadly plausible as a dining room reconstruction, with coherent geometry and perspective. However, noticeable texture softness, blurring, and blending artifacts reduce realism. Minor texture inconsistencies and ghosting are present across multiple surfaces, suggesting rendering limitations typical of 3D Gaussian splatting or similar reconstructions. Overall, the image reads as a credible but imperfect real-world scene, with moderate artifacts that prevent a photo-real 10.*


**Detected Issues**:
- 🎨 **Ghosting**: Subtle ghosting and smeared transitions on large surfaces (table top, wall cabinet) indicating blending artifacts.
- 🎨 **Over Blur**: Overall softening of textures, especially on fabric seating and flowers.
- 🎨 **Texture Inconsistency**: Inconsistent texture granularity between surfaces (wood table vs. fabric chairs vs. wall panels).


### View 3 (60°)

![View 3](captured_views/ktv_hevc/view_002_060deg.png)


**VLM Analysis**:

**Score**: 6/10


> *The scene shows a largely coherent interior layout with plausible geometry and perspective. However, pronounced rendering artifacts characteristic of 3D Gaussian splatting (ghosting on shiny surfaces, smeared textures, and minor texture inconsistencies) reduce realism. Overall it reads as a believable reconstruction with noticeable but not catastrophic defects, primarily in texture fidelity and artifact presence.*


**Detected Issues**:
- 🎨 **Ghosting**: Subtle ghosting-like trails and smear artifacts across glossy surfaces (table, vase area) typical of 3DGS rendering.
- 🎨 **Texture Inconsistency**: Inconsistencies in surface textures (leather chairs, wall art) with smeared or stretched appearance.


### View 4 (90°)

![View 4](captured_views/ktv_hevc/view_003_090deg.png)


**VLM Analysis**:

**Score**: 6/10


> *The scene presents a generally coherent interior with plausible geometry and layout. Minor texture inconsistencies and reduced sharpness on some surfaces indicate residual reconstruction artifacts typical of 3DGS/NeRF renders. No severe geometric distortions or depth-structure failures are evident, but surface textures could be more faithful and edge sharpness improved to achieve higher realism.*


**Detected Issues**:
- 🎨 **Over Blur**: Broad soft focus on some surfaces (e.g., table top and distant wall areas) that slightly reduces sharpness.
- 🎨 **Texture Inconsistency**: Inconsistent surface textures across materials (wood, fabric, and walls) with occasional patchy realism.


### View 5 (120°)

![View 5](captured_views/ktv_hevc/view_004_120deg.png)


**VLM Analysis**:

**Score**: 6/10


> *The scene has plausible layout and perspective with generally coherent geometry, but visible 3DGS/NeRF-like texture artifacts (notably fine line ghosting across surfaces) reduce realism. Overall structure remains recognizable as a room with chairs and a large artwork, yet texture fidelity and artifact visibility prevent a near-photograph level of realism.*


**Detected Issues**:
- 🎨 **Ghosting**: Numerous fine line artifacts and irregular scraggly strokes across surfaces, especially on the left shelving area and around the circular table, indicating splat/point-based texture inconsistencies.


### View 6 (150°)

![View 6](captured_views/ktv_hevc/view_005_150deg.png)


**VLM Analysis**:

**Score**: 5/10


> *The rendering shows a plausible indoor layout but exhibits significant geometric distortions (warped walls, misaligned edges, depth inconsistencies) and texture blending artifacts. Overall realism is moderate, with geometry and texture solidity compromised by notable reconstruction flaws.*


**Detected Issues**:
- ⚠️ **Curved Or Warped Walls**: Left wall and shelving appear noticeably curved and warped, breaking strict rectilinear geometry.
- ⚠️ **Misaligned Edges**: Edges of furniture and paneling do not align cleanly; some lines seem stretched or skewed.
- ⚠️ **Depth Or Perspective Errors**: Depth cues look inconsistent (objects at similar depths have conflicting scaling), suggesting perspective errors.
- 🎨 **Over Blur**: Overall softness and smear across surfaces reduce sharpness of textures.
- 🎨 **Texture Inconsistency**: Inconsistent surface textures (e.g., furniture vs. walls) hint at post-processing artifacts or reconstruction blending.


### View 7 (180°)

![View 7](captured_views/ktv_hevc/view_006_180deg.png)


**VLM Analysis**:

**Score**: 5/10


> *The rendering shows noticeable geometric distortions and depth inconsistencies, with artifacts around fine structures and inconsistent textures. Overall realism is moderate but not near-photographic; minor geometry and texture fidelity issues undermine structural integrity.*


**Detected Issues**:
- ⚠️ **Curved Or Warped Walls**: Wall and shelving appear subtly curved or warped, not aligning with straight architectural planes.
- ⚠️ **Misaligned Edges**: Edges of the shelving unit and mounting frames do not align cleanly with adjacent walls and surfaces.
- ⚠️ **Depth Or Perspective Errors**: Perspective cues are inconsistent (depth lines and relative scale look off), suggesting distortion in depth rendering.
- 🎨 **Floating Artifacts**: Stray, hair-like artifacts float around the shelving and plant areas, not tied to real geometry.
- 🎨 **Texture Inconsistency**: Textures on walls, shelves, and furniture vary unnaturally, indicating inconsistent surface mapping.


### View 8 (210°)

![View 8](captured_views/ktv_hevc/view_007_210deg.png)


**VLM Analysis**:

**Score**: 5/10


> *The rendering shows a plausible interior but with notable geometric distortions and depth inconsistencies. The warped wall and misaligned edges reduce realism, and texture uniformity is uneven with overblurring in certain areas. Overall, it resembles a reconstruction but not robustly accurate to a real scene.*


**Detected Issues**:
- ⚠️ **Curved Or Warped Walls**: Left dark wall shows heavy warping and irregular pattern, breaking straight geometry.
- ⚠️ **Misaligned Edges**: Shelf frame and glass edges appear skewed and not meeting walls cleanly.
- ⚠️ **Depth Or Perspective Errors**: Overall perspective feels inconsistent across the scene, with depth cues not aligning coherently.
- 🎨 **Over Blur**: Regions near edges and textured patterns appear overly blurred, reducing sharpness.
- 🎨 **Texture Inconsistency**: Texture quality varies (wall, furniture, flowers) leading to nonuniform realism.


### View 9 (240°)

![View 9](captured_views/ktv_hevc/view_008_240deg.png)


**VLM Analysis**:

**Score**: 4/10


> *The rendering shows significant geometric issues: warped wall geometry, misaligned edges, and inconsistent depth cues. Textures are uneven, with noticeable blur and surface texture inconsistencies across surfaces. Overall, it resembles a rough reconstruction with several structural and appearance flaws that reduce realism and structural plausibility.*


**Detected Issues**:
- ⚠️ **Curved Or Warped Walls**: A large wall on the left appears noticeably warped and non-planar, with a nonuniform curvature across the surface.
- ⚠️ **Misaligned Edges**: Visible gaps/ misalignments at the junction between the textured wall and the white surface; edges do not meet cleanly.
- ⚠️ **Depth Or Perspective Errors**: Depth cues and perspective are inconsistent, leading to a sense of impossible geometry (e.g., wall-plane to scaffold transitions).
- 🎨 **Over Blur**: Regions appear overly smooth/blurry, reducing fine texture fidelity.
- 🎨 **Texture Inconsistency**: Texture quality varies sharply between surfaces (dark textured wall vs. smooth white areas and scaffolding), indicating inconsistent sampling.


### View 10 (270°)

![View 10](captured_views/ktv_hevc/view_009_270deg.png)


**VLM Analysis**:

**Score**: 4/10


> *The rendering exhibits noticeable geometric distortions (curved/warped wall) and depth inconsistencies. Texture fidelity is degraded by blur and artifact patterns, resulting in modest overall realism. Improvements needed in geometric fidelity, depth cues, and texture consistency to approach photorealistic reconstruction.*


**Detected Issues**:
- ⚠️ **Curved Or Warped Walls**: The wall texture appears warped and curved rather than flat, suggesting distorted geometry.
- ⚠️ **Depth Or Perspective Errors**: Depth cues are inconsistent; foreground detail dominates and background lacks coherent perspective.
- 🎨 **Floating Artifacts**: Fine stray strands/lines in the texture that do not align with real geometry.
- 🎨 **Over Blur**: Overall softness reduces sharpness and edge definition.
- 🎨 **Texture Inconsistency**: Repetitive pattern with uneven shading/lighting across the surface.


### View 11 (300°)

![View 11](captured_views/ktv_hevc/view_010_300deg.png)


**VLM Analysis**:

**Score**: 4/10


> *The rendering shows substantial texture-related artifacts (dense, repetitive mesh pattern) and depth inconsistency that hinder reliable geometric interpretation. No obvious geometric collapse, but perspective cues are compromised by texture; overall realism is limited and reconstruction reliability is moderate at best.*


**Detected Issues**:
- ⚠️ **Depth Or Perspective Errors**: Perceived depth cues are inconsistent due to dense texture and occlusion, making geometry hard to interpret and giving a sense of distorted perspective in the central region.
- 🎨 **Ghosting**: Highly repetitive, woven-like texture across large areas, creating a ghosted/mesh appearance.
- 🎨 **Texture Inconsistency**: Texture quality varies by region; some surfaces appear sharper while others are dominated by the dense pattern, reducing overall coherence.


### View 12 (330°)

![View 12](captured_views/ktv_hevc/view_011_330deg.png)


**VLM Analysis**:

**Score**: 3/10


> *The rendering shows clear structural and texture inconsistencies: a noticeable misalignment at the boundary between surfaces, significant depth/perspective errors, and highly inconsistent right-side texture. Overall realism is compromised with pronounced artifacts that reveal reconstruction limitations.*


**Detected Issues**:
- ⚠️ **Misaligned Edges**: Visible seam along the vertical boundary between the light left wall and the dark right surface; edges do not align cleanly.
- ⚠️ **Depth Or Perspective Errors**: Severe depth cues are inconsistent, with a pronounced seam and abrupt transition between regions, suggesting depth/pose misalignment.
- 🎨 **Texture Inconsistency**: Highly noisy, spiky texture on the right side contrasts with the smooth left wall; overall texture coherence is poor.
