# 3DGS Reconstruction Quality Report: ktv_hevc

**Overall Score**: 50.21/100

**Number of Views Evaluated**: 12

**Render URL**: https://3d-tour-demo-scene.vercel.app/?model=https://storage.googleapis.com/3dgs-homee/ktv_h264hevc.glb&splat=https://storage.googleapis.com/3dgs-homee/ktv_hevc.ksplat&px=-3.357&py=0.082&pz=0.38&tx=-2.56&ty=0.007&tz=-0.218


---


## Computer Vision Metrics


---


## Vision Language Model Metrics


**Model**: gpt-5-nano


### Overall Quality Assessment

- **Quality Score**: 50.83/100

- **Mean Rating**: 5.08/10

- **Std Dev**: 1.04

- **Range**: [3.00, 7.00]


### Artifact Detection

- **Quality Score**: 49.17/100

- **Mean Severity**: 6.08/10

- **Std Dev**: 0.76


*Lower severity indicates fewer visual artifacts (ghosting, floating blobs, etc.).*


### Structural Quality

- **Quality Score**: 50.83/100

- **Mean Rating**: 5.08/10

- **Std Dev**: 1.32


*Higher rating indicates better structural integrity (no warped walls, misaligned edges, etc.).*


---


## Detailed View Analysis


### View 1 (0°)

![View 1](captured_views/ktv_hevc/view_000_000deg.png)


**VLM Analysis**:

**Score**: 6/10


> *The scene shows plausible room geometry and a coherent layout, but depth cues are inconsistent (notably a large black void on the left), and textures appear softened with some artifact-like inconsistencies. Overall, a mostly realistic reconstruction with noticeable depth and texture deficiencies that reduce realism.*


**Detected Issues**:
- ⚠️ **Depth Or Perspective Errors**: Significant depth gaps and a large black void on the left side suggest inconsistent depth cues and possible missing geometry near the wall/scene boundary.
- 🎨 **Over Blur**: Some global softening and blur, particularly on high-contrast edges like table surface and curtains, reduces sharpness.
- 🎨 **Texture Inconsistency**: Irregular surface textures (table/sofa) appear slightly plastic or smeared in places, suggesting inconsistent material layout.


### View 2 (30°)

![View 2](captured_views/ktv_hevc/view_001_030deg.png)


**VLM Analysis**:

**Score**: 6/10


> *The scene has a plausible layout with correct spatial arrangement, but overall realism is hindered by noticeable blur and texture/edge artifacts typical of 3DGS renderings. Minor geometry appears consistent, yet the image lacks sharp texture fidelity and shows ghosting, reducing photorealism.*


**Detected Issues**:
- 🎨 **Ghosting**: Subtle ghosted edges and overlaps on high-contrast textures (flowers and tabletop) indicative of rendering/denoising artifacts.
- 🎨 **Over Blur**: Overall softening and motion-like blur across surfaces, reducing sharpness.


### View 3 (60°)

![View 3](captured_views/ktv_hevc/view_002_060deg.png)


**VLM Analysis**:

**Score**: 7/10


> *Overall a mostly plausible interior reconstruction with correct spatial layout and lighting. The main issues are minor texture inconsistencies and surface warping artifacts that reduce realism slightly, but geometric structure and depth are largely coherent.*


**Detected Issues**:
- 🎨 **Texture Inconsistency**: Subtle texture inconsistencies and surface warping visible on large wooden table and upholstery, giving a slightly plastic look in places.


### View 4 (90°)

![View 4](captured_views/ktv_hevc/view_003_090deg.png)


**VLM Analysis**:

**Score**: 6/10


> *The scene shows a plausible interior layout with coherent geometry and perspective. Minor texture inconsistencies and subtle surface artifacts reduce realism slightly. Overall, geometry is sound, but texture fidelity and rare artifact traces prevent a higher realism score.*


**Detected Issues**:
- 🎨 **Texture Inconsistency**: Visible inconsistencies in surface textures and some repeating sheen/line artifacts on large flat panels and near the table; overall texture stability is imperfect.


### View 5 (120°)

![View 5](captured_views/ktv_hevc/view_004_120deg.png)


**VLM Analysis**:

**Score**: 5/10


> *The scene has plausible room geometry and layout with coherent perspective, but pervasive wireframe/ scribble artifacts reduce realism. No major geometric distortions detected, yet surface textures show visible artifacting that disrupts texture fidelity. Overall closeness to a real scene is moderate; improvements needed in artifact suppression to reach photographic realism.*


**Detected Issues**:
- 🎨 **Ghosting**: Fine scribble-like lines overlaying surfaces (wireframe-like artifacts) across furniture and walls.


### View 6 (150°)

![View 6](captured_views/ktv_hevc/view_005_150deg.png)


**VLM Analysis**:

**Score**: 5/10


> *The render shows a recognizable interior layout with plausible geometry, but several structural and texturing cues indicate reconstruction artifacts. Warped geometric elements, depth inconsistencies, and ghosting/texture mismatches reduce realism and spatial coherence. Overall still readable as a room but not a faithful real-world reconstruction.*


**Detected Issues**:
- ⚠️ **Curved Or Warped Walls**: Visible warping and bending in metal shelf/frame structures and glass cabinet components, not consistent with rigid real geometry.
- ⚠️ **Depth Or Perspective Errors**: Some depth cues (perspective lines and object sizing) appear inconsistent, suggesting slight misalignment between surfaces and their positions in space.
- 🎨 **Ghosting**: Fine streaks and smeared lines across surfaces typical of 3DGS/texturing artifacts.
- 🎨 **Texture Inconsistency**: Inconsistent surface textures between materials (chairs, wall, floor) resembling splatted or interpolated textures.


### View 7 (180°)

![View 7](captured_views/ktv_hevc/view_006_180deg.png)


**VLM Analysis**:

**Score**: 5/10


> *The render shows recognizable real-world room geometry but exhibits notable geometric distortions (warped shelf/glass, misaligned edges, inconsistent depth). Textures are broadly plausible but with texture inconsistencies and slight blur in places. Overall realism is moderate with clear reconstruction artefacts affecting structural integrity and spatial coherence.*


**Detected Issues**:
- ⚠️ **Curved Or Warped Walls**: Distorted shelving frame and glass panels appear warped, bending unnaturally relative to room geometry.
- ⚠️ **Misaligned Edges**: Edges of the shelf and adjacent furniture do not align cleanly with walls, producing subtle misalignment along vertical/horizontal lines.
- ⚠️ **Depth Or Perspective Errors**: Depth cues inconsistent (shelf front/back and chairs appear at conflicting scales), causing odd perspective distortions.
- 🎨 **Texture Inconsistency**: Pattern consistency on wall panels and upholstery is irregular; some textures read as smeared or stretched due to reconstruction noise.


### View 8 (210°)

![View 8](captured_views/ktv_hevc/view_007_210deg.png)


**VLM Analysis**:

**Score**: 5/10


> *The rendering shows recognizable interior geometry but exhibits notable structural and perspective inconsistencies. Warped walls, edge misalignments, and depth errors reduce realism. Texture fidelity is uneven with some artifacts (floating artefacts, over-blurring, and texture mismatches). Overall, the scene is moderately convincing but not a faithful reconstruction of a real room; improvements needed in geometry coherence and texture stability.*


**Detected Issues**:
- ⚠️ **Curved Or Warped Walls**: Left textured wall appears noticeably warped and distorted, not matching a flat planar surface.
- ⚠️ **Misaligned Edges**: Edges around the shelving units and frame appear slightly misaligned with adjacent geometry, suggesting geometry drift.
- ⚠️ **Depth Or Perspective Errors**: Overall perspective and scale feel inconsistent, with depth cues and object sizes not coherently aligning.
- 🎨 **Floating Artifacts**: Some stray high-frequency artefacts float near the shelving frame and metal textures.
- 🎨 **Over Blur**: Significant blur on fine textures (woven patterns, glass) reducing sharpness.
- 🎨 **Texture Inconsistency**: Textures vary in quality across surfaces (wall pattern vs. furniture fabric) creating noticeable mismatch.


### View 9 (240°)

![View 9](captured_views/ktv_hevc/view_008_240deg.png)


**VLM Analysis**:

**Score**: 4/10


> *The rendering exhibits notable geometric distortions and depth inconsistencies that undermine structural realism. Textures show ghosting, floating artifacts, and uneven fidelity across surfaces. Overall, the reconstruction is distinguishable from a real scene due to warped geometry and inconsistent appearances, scoring low on realism while still retaining some recognizable structural elements.*


**Detected Issues**:
- ⚠️ **Curved Or Warped Walls**: Significant warping and bending of vertical surfaces, especially where the wall meets the floor and near the boundary with the dark textured panel.
- ⚠️ **Misaligned Edges**: Edges along the wall/board transition appear jagged and misaligned with neighboring geometry.
- ⚠️ **Depth Or Perspective Errors**: Unrealistic perspective cues and inconsistent depth cues across the scene (e.g., foreground vs. background scaling and tunnel-like distortions).
- 🎨 **Ghosting**: Faint duplicate edges and semi-transparent layers on repeating textures.
- 🎨 **Floating Artifacts**: Unanchored fibrous strands and lines appear to float above surfaces.
- 🎨 **Over Blur**: Some surfaces look excessively blurred, reducing fine texture fidelity.
- 🎨 **Texture Inconsistency**: Inconsistent texturing between adjacent surfaces (left dark wall vs. right scaffolding) with abrupt transitions.


### View 10 (270°)

![View 10](captured_views/ktv_hevc/view_009_270deg.png)


**VLM Analysis**:

**Score**: 4/10


> *The rendering exhibits noticeable geometric and depth inconsistencies, with warped wall surfaces and misaligned perspective. Texture fidelity is compromised by an unnatural repeating pattern and an obtrusive overlay element, reducing realism and spatial coherence. Overall, it resembles a flawed 3D reconstruction with several non-physical artifacts.*


**Detected Issues**:
- ⚠️ **Curved Or Warped Walls**: Large wall surface shows noticeable curvature and warped texture flow, not matching a flat real-world wall.
- ⚠️ **Depth Or Perspective Errors**: Unstable perspective cues and inconsistent depth across surfaces; edges do not align coherently with a plausible camera viewpoint.
- 🎨 **Floating Artifacts**: Prominent white circular overlay (likely an annotation) obscures scene and reduces texture fidelity.
- 🎨 **Texture Inconsistency**: High-frequency repetitive lattice texture with unnatural uniformity; looks artificial and inconsistent with real material.


### View 11 (300°)

![View 11](captured_views/ktv_hevc/view_010_300deg.png)


**VLM Analysis**:

**Score**: 3/10


> *The rendering exhibits severe geometric ambiguity with warped surfaces and poor depth cues. Textures show strong tiling, drift, and over-blurring, leading to a scene that is not convincingly anchored in real-world geometry. Overall realism is limited; artifacts undermine structural integrity and spatial consistency.*


**Detected Issues**:
- ⚠️ **Curved Or Warped Walls**: Wavy, non-planar surface visible across the texture; shapes appear bent rather than flat walls.
- ⚠️ **Misaligned Edges**: Edges do not align cleanly at borders; abrupt transitions and misregistrations near the left and right boundaries.
- ⚠️ **Depth Or Perspective Errors**: Depth cues are inconsistent; foreground and background blend with no clear occlusion, making geometry ambiguous.
- 🎨 **Floating Artifacts**: Dense repeating pattern appears to float over the scene, not anchored to recognizable geometry.
- 🎨 **Over Blur**: Overall softness reduces edge sharpness, especially on fine details.
- 🎨 **Texture Inconsistency**: Tiling-like repetition and inconsistent shading across the surface indicate non-uniform texture mapping.


### View 12 (330°)

![View 12](captured_views/ktv_hevc/view_011_330deg.png)


**VLM Analysis**:

**Score**: 5/10


> *The rendering shows notable structural and textural inconsistencies: a visible seam with possible depth misalignment between two large surfaces, uneven texture quality across regions, and minor blur on one side. Overall realism is moderate but not convincing as a faithful real-world reconstruction.*


**Detected Issues**:
- ⚠️ **Misaligned Edges**: Clear seam/edge mismatch where the light-colored wall meets the dark textured surface.
- ⚠️ **Depth Or Perspective Errors**: Slight depth misalignment near the seam; perspective cues do not unify across surfaces.
- 🎨 **Over Blur**: Softening/blur on the left wall region compared to the highly detailed right surface.
- 🎨 **Texture Inconsistency**: Strong contrast between smooth wall texture and dense noisy surface texture, suggesting inconsistent reconstruction quality across surfaces.
