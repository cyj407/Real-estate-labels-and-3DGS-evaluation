# 3DGS Reconstruction Quality Report: ktv_hevc

**Overall Score**: 49.74/100

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

- **Quality Score**: 50.00/100

- **Mean Rating**: 5.00/10

- **Std Dev**: 0.58

- **Range**: [4.00, 6.00]


### Artifact Detection

- **Quality Score**: 45.00/100

- **Mean Severity**: 6.50/10

- **Std Dev**: 0.76


*Lower severity indicates fewer visual artifacts (ghosting, floating blobs, etc.).*


### Structural Quality

- **Quality Score**: 49.17/100

- **Mean Rating**: 4.92/10

- **Std Dev**: 1.04


*Higher rating indicates better structural integrity (no warped walls, misaligned edges, etc.).*


---


## Detailed View Analysis


### View 1 (0°)

![View 1](captured_views/ktv_hevc/view_000_000deg.png)


**VLM Analysis**:

**Score**: 5/10


> *The scene is recognizable as an interior dining/living area with plausible geometry and lighting, but there are clear artifacts: a large black void region suggesting missing data or occlusion, depth/perspective inconsistencies near the window area, and overall blur/texture mismatches that reduce realism. Minor geometry appears intact, but texture stability and multi-surface coherence are compromised.*


**Detected Issues**:
- ⚠️ **Depth Or Perspective Errors**: Notable black void on the left side and some perspective/edge inconsistencies near the window area suggesting missing data or misalignment in the reconstruction.
- 🎨 **Over Blur**: Overall soft focus and motion-like blur, especially across the table surface and edges.
- 🎨 **Texture Inconsistency**: Inconsistent material reproduction (very dark void area and uneven reflections on the table/floor) indicating texture/material mismatches.


### View 2 (30°)

![View 2](captured_views/ktv_hevc/view_001_030deg.png)


**VLM Analysis**:

**Score**: 5/10


> *The rendering shows a plausible interior layout with correct spatial arrangement, but exhibits notable geometric and texture inconsistencies typical of 3DGS/NeRF outputs. Some wall/ceiling areas appear curved or smeared, and overall texture is softened with occasional inconsistencies between materials, reducing realism. No severe topology breaks detected, but the scene is not indistinguishable from a real photograph.*


**Detected Issues**:
- ⚠️ **Curved Or Warped Walls**: Ceiling/plaster edges and transitions appear smeared and slightly curved, notably around the ceiling beam and wall joints, giving a non-planar feel.
- 🎨 **Over Blur**: Overall softness and painterly look reduces sharpness across textures, especially on table surface and flower centerpiece.
- 🎨 **Texture Inconsistency**: Inconsistent texture fidelity between materials (wood, fabric, and glass) with some surfaces appearing oversmoothed compared to others.


### View 3 (60°)

![View 3](captured_views/ktv_hevc/view_002_060deg.png)


**VLM Analysis**:

**Score**: 6/10


> *The scene shows a coherent room layout with plausible geometry and perspective, but the rendering exhibits noticeable texture inconsistencies and ghosting artifacts typical of 3D Gaussian Splatting reconstructions. Overall realism is moderate; geometric structure remains credible, while texture fidelity and artifact presence reduce perceptual accuracy.*


**Detected Issues**:
- 🎨 **Ghosting**: visible ghosting/line artifacts across surfaces (table, wall panel, bouquet) typical of 3DGS rendering.
- 🎨 **Texture Inconsistency**: inconsistent surface textures on chairs and cabinetry, slight mismatch in shading/reflectivity.


### View 4 (90°)

![View 4](captured_views/ktv_hevc/view_003_090deg.png)


**VLM Analysis**:

**Score**: 6/10


> *The scene is recognizable as a dining/sofa area with plausible geometry and layout. Minor depth/perspective ambiguities and noticeable texture inconsistencies reduce realism. Overall, the reconstruction is functional but exhibits small geometric and texture fidelity gaps typical of 3DGS renders.*


**Detected Issues**:
- ⚠️ **Depth Or Perspective Errors**: Subtle depth/perspective misalignment between foreground table/chair region and the background wall area; scene depth cues do not perfectly converge, causing a minor fictitious flattening in some zones.
- 🎨 **Texture Inconsistency**: Inconsistent or smeared textures on wood paneling and upholstery; visible brush-like strokes and irregularities typical of 3DGS renderings, affecting perceived material fidelity.


### View 5 (120°)

![View 5](captured_views/ktv_hevc/view_004_120deg.png)


**VLM Analysis**:

**Score**: 5/10


> *The scene shows reasonable overall structure with recognizable room layout, but the reconstruction exhibits depth inconsistencies and prominent rendering artifacts (ghosting, floating strands, texture inconsistency) that reduce realism. Minor geometry remains plausible, but multi-surface coherence is affected by artifacts and depth misalignment.*


**Detected Issues**:
- ⚠️ **Depth Or Perspective Errors**: Distorted depth cues and slight perspective mismatches between foreground chairs and background elements; depth scaling appears inconsistent.
- 🎨 **Ghosting**: Visible fine line artifacts across surfaces, especially around edges and near the artwork frame.
- 🎨 **Floating Artifacts**: Stray lines and wispy strands appear disconnected from real geometry, floating around the shelves and table area.
- 🎨 **Texture Inconsistency**: Inconsistent surface detail between cabinetry, walls, and upholstery; some textures look unnaturally smooth or smeared.


### View 6 (150°)

![View 6](captured_views/ktv_hevc/view_005_150deg.png)


**VLM Analysis**:

**Score**: 5/10


> *The rendering shows a mostly plausible interior layout but exhibits notable geometric distortions and texture inconsistencies. Warped/curved surfaces, misaligned edges, and depth misalignments reduce realism. Texture artifacts include floating strands and overall over-blur, impacting surface fidelity. Overall, it is a moderate reconstruction with several noticeable defects that prevent high realism.*


**Detected Issues**:
- ⚠️ **Curved Or Warped Walls**: Subtle warping and irregularities along the wall and shelving edges, especially near the left side of the scene.
- ⚠️ **Misaligned Edges**: Some edges (e.g., window frame and panel lines) do not align cleanly with adjacent geometry, suggesting stitching or reconstruction misalignment.
- ⚠️ **Depth Or Perspective Errors**: Inconsistent depth cues in the seating area and foreground objects; perspective does not perfectly match scene scale.
- 🎨 **Floating Artifacts**: Sparse stray strands/lines appear detached from surfaces, giving a floating artifact impression.
- 🎨 **Over Blur**: Overall softening and motion-like blur reduces texture fidelity on seating and wall textures.
- 🎨 **Texture Inconsistency**: Visible mismatches in texture sharpness between foreground chairs and wall/flowing decorative panels.


### View 7 (180°)

![View 7](captured_views/ktv_hevc/view_006_180deg.png)


**VLM Analysis**:

**Score**: 5/10


> *The reconstruction shows noticeable geometric distortions and depth inconsistencies, with blurred textures and conflicting material appearances. Overall realism is moderate but clearly deviates from a real scene in structure and texture fidelity.*


**Detected Issues**:
- ⚠️ **Curved Or Warped Walls**: Wall and shelving appear distorted with irregular curves, especially along the glass cabinet and adjacent walls.
- ⚠️ **Misaligned Edges**: Edges between the shelf unit and surrounding walls/fixtures do not align cleanly, giving a skewed geometry.
- ⚠️ **Depth Or Perspective Errors**: Perspective cues are inconsistent (tilted lines and warped depth), causing depth cues to feel unrealistic.
- 🎨 **Over Blur**: Areas around edges of furniture and shelves appear smeared, reducing sharpness.
- 🎨 **Texture Inconsistency**: Texture granularity varies across surfaces (glass, metal, fabric) in a way that seems incongruent with real materials.


### View 8 (210°)

![View 8](captured_views/ktv_hevc/view_007_210deg.png)


**VLM Analysis**:

**Score**: 5/10


> *The rendering shows several structural and texture inconsistencies typical of 3DGS reconstructions: warped walls, misaligned edges, and depth/perspective distortions reduce realism. Some artifacting around fine strands and inconsistent texture distribution further lowers fidelity. Overall, the scene is recognizable but not convincingly indistinguishable from a real photograph; improvements in geometry consistency and texture stabilization would be needed.*


**Detected Issues**:
- ⚠️ **Curved Or Warped Walls**: Left dark patterned wall appears warped with irregular curvature rather than flat.
- ⚠️ **Misaligned Edges**: Shelf frames and vertical edges do not align cleanly, creating slight skew in geometry.
- ⚠️ **Depth Or Perspective Errors**: Depth cues and perspective look inconsistent (distorted scale and skewed vanishing points).
- 🎨 **Floating Artifacts**: Thin stray strands or fibers around shelves and decor appear detached from surfaces.
- 🎨 **Texture Inconsistency**: Textural patterns (wall, furniture, and decorative elements) lack coherent spacing, causing uneven realism.


### View 9 (240°)

![View 9](captured_views/ktv_hevc/view_008_240deg.png)


**VLM Analysis**:

**Score**: 5/10


> *The rendering shows notable geometric and textural inconsistencies that reduce realism. Warped wall geometry, misaligned edges, and depth distortions disrupt structural coherence. Texture artifacts (ghosting, floating strands, and uneven detail) further diminish fidelity. While some surface areas hint at plausible geometry, overall scene consistency is limited and would benefit from improved surface reconstruction, better edge alignment, and more stable texturing.*


**Detected Issues**:
- ⚠️ **Curved Or Warped Walls**: Large warped/plastic-looking wall surface on the left with irregular curvature and jagged tessellation visible.
- ⚠️ **Misaligned Edges**: Edges between wall and floor/ceiling appear misaligned and inconsistent with real geometry; some seams look unrealistically thick.
- ⚠️ **Depth Or Perspective Errors**: Foreground/background depth cues appear inconsistent; perspective compression and distorted foreshortening around the central seam create depth ambiguity.
- 🎨 **Ghosting**: Subtle ghost-like repetitions in textured regions, particularly the dark wall area.
- 🎨 **Floating Artifacts**: Sparse stray strands and line-like artifacts floating over surfaces, not anchored to geometry.
- 🎨 **Over Blur**: Overall softness in large flat areas reduces fine texture fidelity; some regions look overly smoothed.
- 🎨 **Texture Inconsistency**: Inconsistent texture density across surfaces; some textures look different in nearby regions, indicating stitching artifacts.


### View 10 (270°)

![View 10](captured_views/ktv_hevc/view_009_270deg.png)


**VLM Analysis**:

**Score**: 4/10


> *The rendering shows notable geometric and textural inconsistencies: warped patterns, misaligned edges, depth/perspective errors, and non-uniform texture tiling. These issues reduce realism, indicating a reconstruction with structural and appearance artifacts rather than a faithful real-world scene.*


**Detected Issues**:
- ⚠️ **Curved Or Warped Walls**: Pattern appears stretched/warped across the main wall surface, suggesting non-rigid or misaligned mesh tiling.
- ⚠️ **Misaligned Edges**: Edges near the frame and vertical features do not align cleanly with adjacent surfaces, indicating potential stitching artifacts or depth mismatch.
- ⚠️ **Depth Or Perspective Errors**: Depth cues are inconsistent; scale and perspective do not convincingly align across the scene (foreground vs background misprojection).
- 🎨 **Over Blur**: Overall softening/blurrier regions reduce sharpness of fine details, not typical of a real scene.
- 🎨 **Texture Inconsistency**: Tiling and repetitive patterns show abrupt changes; texture consistency across surfaces is not uniform.


### View 11 (300°)

![View 11](captured_views/ktv_hevc/view_010_300deg.png)


**VLM Analysis**:

**Score**: 5/10


> *The rendering shows noticeable geometric distortions with warped walls, misaligned edges, and inconsistent depth cues. Texture exhibits heavy blurring and inconsistent patterns with sparse, floating artifact-like elements. Overall realism is moderate but artifacts prevent convincing reconstruction of a real scene.*


**Detected Issues**:
- ⚠️ **Curved Or Warped Walls**: Large, irregular warping and bending visible across the vertical surfaces, giving a distorted room-like enclosure.
- ⚠️ **Misaligned Edges**: Edges between planes appear mismatched and jagged, not aligning cleanly with adjacent surfaces.
- ⚠️ **Depth Or Perspective Errors**: Depth cues are inconsistent; some surfaces appear unnaturally flat or foreshortened, reducing real-world depth fidelity.
- 🎨 **Floating Artifacts**: Repeated hair-like textures dominate the scene, giving the impression of floating clusters rather than a stable surface.
- 🎨 **Over Blur**: Overall softness and lack of fine detail, especially on edge regions, suggesting excessive blur in shading/texture.
- 🎨 **Texture Inconsistency**: Texture density and pattern vary abruptly across surfaces, lacking consistent material appearance.


### View 12 (330°)

![View 12](captured_views/ktv_hevc/view_011_330deg.png)


**VLM Analysis**:

**Score**: 4/10


> *The rendering exhibits notable geometric and depth inconsistencies, particularly along a central seam between left and right surfaces. Texturing shows ghosting and inconsistent detail, with over-smoothed areas. Overall realism is limited; artifacts indicate reconstruction errors in geometry and texture stability.*


**Detected Issues**:
- ⚠️ **Curved Or Warped Walls**: Prominent vertical seam and warping along the boundary between the light left wall and the dark right surface, suggesting misalignment or deformed geometry.
- ⚠️ **Misaligned Edges**: Edges near the seam appear jagged and inconsistent with expected planar walls, indicating edge misalignment.
- ⚠️ **Depth Or Perspective Errors**: Unclear depth cues on the boundary region; perspective appears inconsistent with surrounding surfaces, hinting at depth errors.
- 🎨 **Ghosting**: Overlaid translucent artifacts across the dark textured surface, reducing clarity.
- 🎨 **Over Blur**: Wide regions appear overly smoothed, diminishing fine texture details.
- 🎨 **Texture Inconsistency**: Texture density and shading vary abruptly across the scene, inconsistent with a coherent surface.
