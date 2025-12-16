# 3DGS Reconstruction Quality Report: ktv_hevc_deblur035

**Overall Score**: 46.70/100

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

- **Quality Score**: 80.43/100

- **Mean Score**: 80.43

- **Std Dev**: 6.04


*No-reference quality metric based on natural scene statistics.*


---


## Vision Language Model Metrics


**Model**: gpt-5-nano


### Overall Quality Assessment

- **Quality Score**: 47.50/100

- **Mean Rating**: 4.75/10

- **Std Dev**: 0.60

- **Range**: [4.00, 6.00]


### Artifact Detection

- **Quality Score**: 40.83/100

- **Mean Severity**: 6.92/10

- **Std Dev**: 0.95


*Lower severity indicates fewer visual artifacts (ghosting, floating blobs, etc.).*


### Structural Quality

- **Quality Score**: 46.67/100

- **Mean Rating**: 4.67/10

- **Std Dev**: 0.62


*Higher rating indicates better structural integrity (no warped walls, misaligned edges, etc.).*


---


## Detailed View Analysis


### View 1 (0°)

![View 1](captured_views/ktv_hevc_deblur035/view_000_000deg.png)


**VLM Analysis**:

**Score**: 6/10


> *The rendering shows a plausible interior layout with reasonable room-scale cues, but suffers from notable geometric distortions (warped walls, misaligned edges) and depth inconsistencies. Textures are soft with ghosting and inconsistency across surfaces, indicating weaker 3DGS texture fidelity. Overall realism is moderate; it could be mistaken for a reconstruction with artifacts rather than a true photograph.*


**Detected Issues**:
- ⚠️ **Curved Or Warped Walls**: Left wall and ceiling appear irregularly warped with streaky texture, causing nonplanar geometry in the room perimeter.
- ⚠️ **Misaligned Edges**: Edges around the window frames and the round tabletop appear slightly misaligned or distorted relative to other architectural cues.
- ⚠️ **Depth Or Perspective Errors**: Depth cues and perspective between foreground table and background seating feel inconsistent, slightly flattening or exaggerating distances.
- 🎨 **Ghosting**: Subtle ghosting along high-contrast edges of curtains and windows.
- 🎨 **Over Blur**: Overall surfaces look smeared with soft blur, reducing fine texture fidelity on upholstery and tablecloth.
- 🎨 **Texture Inconsistency**: Texture quality varies across surfaces (ceiling vs. furniture) leading to inconsistent material appearance.


### View 2 (30°)

![View 2](captured_views/ktv_hevc_deblur035/view_001_030deg.png)


**VLM Analysis**:

**Score**: 5/10


> *The rendering shows a plausible indoor layout with recognizable geometry, but overall realism is compromised by heavy blur and painterly texturing that reduces fine-grained texture fidelity. Minor depth alignment issues exist near the windows and table edge, yet no severe geometric breakage is observed.*


**Detected Issues**:
- ⚠️ **Depth Or Perspective Errors**: Some depth cues and edge alignments appear slightly off, particularly around the window frames and table edge, giving a mild sense of perspective distortion.
- 🎨 **Over Blur**: Strong overall blur/painterly effect reduces fine texture fidelity and sharpness.
- 🎨 **Texture Inconsistency**: Inconsistent surface textures (sofa, table, walls) with irregular brush-like patterns across surfaces.


### View 3 (60°)

![View 3](captured_views/ktv_hevc_deblur035/view_002_060deg.png)


**VLM Analysis**:

**Score**: 5/10


> *The rendering has plausible layout and object arrangement, but severe blur and texture smearing degrade geometric clarity and depth cues. Minor geometric structure is intact, but overall realism as a real-world scene is compromised by perceptual artifacts and inconsistent texturing.*


**Detected Issues**:
- ⚠️ **Depth Or Perspective Errors**: Significant motion- or blur-induced depth distortion; edges and scale cues are softened, reducing reliable depth cues from the scene.
- 🎨 **Ghosting**: Overall smeared texture across surfaces, especially on walls and table, reducing surface fidelity.
- 🎨 **Over Blur**: Strong blur across most regions, obscuring fine details and texture variation.
- 🎨 **Texture Inconsistency**: Inconsistent texture sharpness between surfaces (e.g., wall vs. table) due to uneven rendering or post-processing.


### View 4 (90°)

![View 4](captured_views/ktv_hevc_deblur035/view_003_090deg.png)


**VLM Analysis**:

**Score**: 5/10


> *The rendering shows a plausible room layout but suffers from notable geometric distortions and texture artifacts that reduce realism. Structural cues (edges, depth) are inconsistently maintained, and surface textures lack sharpness, resulting in a scene that is recognizable but not convincingly photorealistic.*


**Detected Issues**:
- ⚠️ **Curved Or Warped Walls**: Large wall panel and ceiling surfaces appear unnaturally warped and stretched, suggesting distorted geometry.
- ⚠️ **Misaligned Edges**: Edges around furniture and cabinetry do not align cleanly with adjacent surfaces; noticeable edge mismatches.
- ⚠️ **Depth Or Perspective Errors**: Perspective cues and depth relations appear inconsistent (objects overlap oddly, depth cues flattened in places).
- 🎨 **Ghosting**: Faint ghost-like duplicates on some surfaces, especially near high-contrast areas.
- 🎨 **Floating Artifacts**: Small detached texture patches appear to float above surfaces in certain regions.
- 🎨 **Over Blur**: Regions lack sharp detail due to excessive blur, reducing perceived texture fidelity.


### View 5 (120°)

![View 5](captured_views/ktv_hevc_deblur035/view_004_120deg.png)


**VLM Analysis**:

**Score**: 5/10


> *The render captures the scene layout and major components, but geometric distortions (warped walls, misaligned edges, depth inconsistencies) and noticeable texture artifacts (ghosting, floating strands, over-blur) reduce realism. Overall still recognizable as a 3D reconstruction, but imperfections prevent it from closely matching a real photograph.*


**Detected Issues**:
- ⚠️ **Curved Or Warped Walls**: Wall panel and painting appear slightly wavy and stretched, not perfectly flat.
- ⚠️ **Misaligned Edges**: Edges of furniture and cabinetry look slightly offset and not crisply aligned with room geometry.
- ⚠️ **Depth Or Perspective Errors**: Foreground objects and distant wall plane show minor perspective inconsistency, reducing depth accuracy.
- 🎨 **Ghosting**: Subtle ghost-like edges around objects due to overlapping splats.
- 🎨 **Floating Artifacts**: Sagging strands and stray filaments around scaffolding appear detached from surfaces.
- 🎨 **Over Blur**: General scene looks softened; fine details (fabric, wood grain) are blurred.
- 🎨 **Texture Inconsistency**: Surface textures vary irregularly (some patches too smooth, others overly detailed) for a single material.


### View 6 (150°)

![View 6](captured_views/ktv_hevc_deblur035/view_005_150deg.png)


**VLM Analysis**:

**Score**: 5/10


> *The render shows a recognizable room layout but with noticeable geometric and texture inconsistencies. Curved and warped walls, misaligned edges, depth compression, and several texture artifacts (ghosting, over-blur, inconsistent texture) reduce realism. Overall, it resembles a plausible scene but with non-negligible reconstruction errors that veer toward a mid-range quality rather than photorealistic accuracy.*


**Detected Issues**:
- ⚠️ **Curved Or Warped Walls**: Walls and surfaces show pronounced curvature and bending, especially on the left wall and near the back panel.
- ⚠️ **Misaligned Edges**: Edges along furniture and wall panels do not align cleanly; some gaps and misregistrations are visible.
- ⚠️ **Depth Or Perspective Errors**: Depth cues and perspective are inconsistent (ceiling/floor interaction and chair alignment) producing a flat/warped sense of depth.
- 🎨 **Ghosting**: Subtle ghosting around high-contrast regions (red artwork) and near edges.
- 🎨 **Over Blur**: Regions appear overly blurred, reducing fine texture fidelity (chairs, wall panel).
- 🎨 **Texture Inconsistency**: Texture quality varies across surfaces; some areas look smeared while others are sharp.


### View 7 (180°)

![View 7](captured_views/ktv_hevc_deblur035/view_006_180deg.png)


**VLM Analysis**:

**Score**: 5/10


> *The rendering shows a scene that roughly resembles the intended interior but suffers from notable geometric distortions and depth inconsistencies. Textures exhibit artifacts, ghosting, and uneven sharpness, leading to an overall perception of a plausible scene only at a rough level. Minor to moderate reconstruction errors dominate, making it clearly distinguishable from a real photograph.*


**Detected Issues**:
- ⚠️ **Curved Or Warped Walls**: Wall surfaces and shelving appear distorted with irregular, wavering contours, not corresponding to real geometry.
- ⚠️ **Misaligned Edges**: Edges along furniture and shelves do not align cleanly; lines appear skewed and inconsistent with room corners.
- ⚠️ **Depth Or Perspective Errors**: Depth cues and perspective seem inconsistent (e.g., furniture and wall depth do not consistently scale or converge).
- 🎨 **Ghosting**: Fine line artifacts over surfaces, especially walls and glass-like structures, resembling ghosting.
- 🎨 **Over Blur**: Some regions appear excessively smeared, reducing surface detail (e.g., upholstery and leaves).
- 🎨 **Texture Inconsistency**: Inconsistent texture granularity; some areas look overly smooth while others are highly detailed with noise.


### View 8 (210°)

![View 8](captured_views/ktv_hevc_deblur035/view_007_210deg.png)


**VLM Analysis**:

**Score**: 4/10


> *The rendering shows notable geometric distortions (warped walls, misaligned edges, depth inconsistencies) and inconsistent textures. Visual coherence is compromised by floating artifacts and over-blurred surfaces, resulting in only moderate realism for a 3D reconstruction of an interior.*


**Detected Issues**:
- ⚠️ **Curved Or Warped Walls**: Left dark wall appears strongly curved and irregular rather than flat, indicating warped geometry.
- ⚠️ **Misaligned Edges**: Edges between wall panels and furniture show slight misalignment and non-joinable seams.
- ⚠️ **Depth Or Perspective Errors**: Depth cues and perspective appear inconsistent (shelving and furniture do not align properly with the room).
- 🎨 **Floating Artifacts**: Numerous thin strands and lines float around shelves, indicating occlusion or depth inconsistencies.
- 🎨 **Over Blur**: Overall scene exhibits excessive blur in some surfaces, reducing texture sharpness.
- 🎨 **Texture Inconsistency**: Texture quality varies abruptly across surfaces (wall vs. furniture vs. decor) with mismatched detail levels.


### View 9 (240°)

![View 9](captured_views/ktv_hevc_deblur035/view_008_240deg.png)


**VLM Analysis**:

**Score**: 4/10


> *The rendering shows notable geometric and textural inconsistencies typical of aggressive 3DGS/NeRF-style reconstructions. Warped walls, misaligned edges, depth distortions, and uneven texture quality indicate unreliability for accurate real-world reconstruction without further refinement.*


**Detected Issues**:
- ⚠️ **Curved Or Warped Walls**: Large, irregular warping evident on the left wall and floor transition, giving a non-planar surface rather than real geometry.
- ⚠️ **Misaligned Edges**: Edges and seams do not align coherently between surfaces, especially near the boundary between the dark wall and lighter area on the right.
- ⚠️ **Depth Or Perspective Errors**: Depth cues are inconsistent; perspective seems distorted with skewed foreshortening and objects that do not recede realistically.
- 🎨 **Ghosting**: Subtle ghosting around high-contrast edges, particularly near wall textures.
- 🎨 **Over Blur**: Regions appear blurred relative to scene details, reducing texture sharpness.
- 🎨 **Texture Inconsistency**: Texture quality varies abruptly between regions, with mismatched granularity and lighting.


### View 10 (270°)

![View 10](captured_views/ktv_hevc_deblur035/view_009_270deg.png)


**VLM Analysis**:

**Score**: 4/10


> *The rendering shows a noisy, highly textured wall with significant depth and boundary inconsistencies. There are misaligned edges and depth cues that do not align with a coherent real-world geometry, along with overall blur and texture inconsistency that reduce realism. Minor geometry appears intact, but the scene lacks reliable multi-surface coherence and sharp texture fidelity necessary for a high-quality reconstruction.*


**Detected Issues**:
- ⚠️ **Misaligned Edges**: Visible seam and misalignment near the right boundary where the dark wall meets the lighter area.
- ⚠️ **Depth Or Perspective Errors**: Strong perspective distortion and abrupt boundary transitions, inconsistent depth cues across the scene.
- 🎨 **Over Blur**: General softness on the textured wall, reducing fine detail.
- 🎨 **Texture Inconsistency**: Texture quality varies between wall regions and boundary area; abrupt changes in detail level.


### View 11 (300°)

![View 11](captured_views/ktv_hevc_deblur035/view_010_300deg.png)


**VLM Analysis**:

**Score**: 4/10


> *The rendering has a very noisy, densely patterned surface that challenges depth interpretation, leading to weak depth cues and inconsistent shading. There is a prominent synthetic overlay (white ring) that disrupts realism. Overall geometry is plausible but the texture coherence and depth perception are compromised, resulting in a below-average realism score for a real-world scene reconstruction.*


**Detected Issues**:
- ⚠️ **Depth Or Perspective Errors**: Weak depth cues and inconsistent perspective across the dense dark surface; difficulty resolving foreground vs background due to uniform texture.
- 🎨 **Floating Artifacts**: A bright circular overlay (white ring) obscures part of the texture, which looks inserted rather than part of the scene.
- 🎨 **Texture Inconsistency**: Highly variable micro-geometry within the surface (dense hair-like strands) creates inconsistent shading and roughness, reducing photorealism.


### View 12 (330°)

![View 12](captured_views/ktv_hevc_deblur035/view_011_330deg.png)


**VLM Analysis**:

**Score**: 5/10


> *The render shows a dense, hair-like structure with a near-uniform mass on the right and a beige left wall. Overall geometry is plausible but depth and shading cues are inconsistent, leading to a noticeable sense of depth ambiguity. Texture is dense but exhibits local inconsistencies in density and tone. Minor reconstruction artifacts affect overall realism but do not completely break the scene structure.*


**Detected Issues**:
- ⚠️ **Depth Or Perspective Errors**: Partial depth cue inconsistency; background strands and wall transition suggestOK depth but some portions lack coherent perspective cues.
- 🎨 **Texture Inconsistency**: Inhomogeneous hair-like texture density and shading across the mass; abrupt tonal shifts near the left wall region.
