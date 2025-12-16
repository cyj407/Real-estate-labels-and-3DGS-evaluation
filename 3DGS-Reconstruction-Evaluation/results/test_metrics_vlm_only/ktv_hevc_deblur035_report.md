# 3DGS Reconstruction Quality Report: ktv_hevc_deblur035

**Overall Score**: 44.58/100

**Number of Views Evaluated**: 12

**Render URL**: https://3d-tour-demo-scene.vercel.app/?model=https://storage.googleapis.com/3dgs-homee/ktv_h264hevc.glb&splat=https://storage.googleapis.com/3dgs-homee/ktv_hevc_deblur035.ksplat&px=-3.5&py=0.082&pz=0.38&tx=-2.56&ty=0.007&tz=-0.218


---


## Computer Vision Metrics


---


## Vision Language Model Metrics


**Model**: gpt-5-nano


### Overall Quality Assessment

- **Quality Score**: 47.50/100

- **Mean Rating**: 4.75/10

- **Std Dev**: 0.72

- **Range**: [3.00, 6.00]


### Artifact Detection

- **Quality Score**: 40.83/100

- **Mean Severity**: 6.92/10

- **Std Dev**: 0.95


*Lower severity indicates fewer visual artifacts (ghosting, floating blobs, etc.).*


### Structural Quality

- **Quality Score**: 45.83/100

- **Mean Rating**: 4.58/10

- **Std Dev**: 0.95


*Higher rating indicates better structural integrity (no warped walls, misaligned edges, etc.).*


---


## Detailed View Analysis


### View 1 (0°)

![View 1](captured_views/ktv_hevc_deblur035/view_000_000deg.png)


**VLM Analysis**:

**Score**: 6/10


> *The rendering shows a largely plausible interior layout with plausible object placement and lighting. However, depth cues are slightly inconsistent and surface textures lack uniform sharpness, leading to a modest degradation in realism. Minor artifacts in texture coherence and overall depth perception prevent a near-photographic level of realism.*


**Detected Issues**:
- ⚠️ **Depth Or Perspective Errors**: Some depth cues appear inconsistent; perspective and scale feel slightly off around the window area, contributing to a flatter perception in parts of the scene.
- 🎨 **Over Blur**: Overall softness/blur is noticeable, especially on large flat surfaces like the table and floor, reducing crispness of textures.
- 🎨 **Texture Inconsistency**: Inconsistent texture detail across surfaces (e.g., curtains vs. floor vs. furniture) suggests non-uniform reconstruction quality.


### View 2 (30°)

![View 2](captured_views/ktv_hevc_deblur035/view_001_030deg.png)


**VLM Analysis**:

**Score**: 5/10


> *The rendering shows a plausible interior layout with correct multi-surface arrangement (table, chairs, windows), but geometry is noticeably warped and surfaces are smeared. Textures are inconsistent and blurred, leading to reduced realism. Overall, the scene is recognizable but not a faithful reconstruction of a real room; improvements needed in geometric fidelity and texture stability.*


**Detected Issues**:
- ⚠️ **Curved Or Warped Walls**: Overall surfaces appear smeared and wavy, particularly on the walls and table edges, giving a distorted geometry impression.
- 🎨 **Floating Artifacts**: Foreground furniture and central decoration show inconsistent depth cues with surrounding geometry, creating a sense of floating elements.
- 🎨 **Over Blur**: Overall image exhibits heavy motion-like blur and smeared textures, reducing clarity of surfaces.
- 🎨 **Texture Inconsistency**: Textures appear painterly and non-uniform (brushed walls, stretched fabrics), lacking consistent surface detail.


### View 3 (60°)

![View 3](captured_views/ktv_hevc_deblur035/view_002_060deg.png)


**VLM Analysis**:

**Score**: 5/10


> *The rendering shows recognizable room geometry but with notable geometric distortions and depth inconsistencies. Textures are variably sharp, with pronounced blur and texture mismatches across surfaces, leading to a result that is only moderately realistic as a real-world reconstruction.*


**Detected Issues**:
- ⚠️ **Curved Or Warped Walls**: Wall and ceiling surfaces appear smeared and slightly curved, reducing geometric straightness.
- ⚠️ **Misaligned Edges**: Edges of the table, window frames, and cabinetry do not align crisply; some lines look distorted.
- ⚠️ **Depth Or Perspective Errors**: Some depth cues and perspective lines appear inconsistent, especially near the window/background region.
- 🎨 **Over Blur**: Widespread motion-like blur smooths fine details, reducing sharpness of textures.
- 🎨 **Texture Inconsistency**: Texture quality varies across surfaces (wall, tabletop, fabrics) with abrupt changes.


### View 4 (90°)

![View 4](captured_views/ktv_hevc_deblur035/view_003_090deg.png)


**VLM Analysis**:

**Score**: 5/10


> *The rendering shows noticeable geometric distortion and depth inconsistencies, with warped walls, misaligned edges, and blurred textures that reduce realism. While some structural elements are recognizable, the scene does not convincingly represent a real room due to depth errors, texture ghosting, and overall spatial incoherence.*


**Detected Issues**:
- ⚠️ **Curved Or Warped Walls**: Wall surfaces appear warped and curved rather than flat; ceiling and window frames also show bending lines.
- ⚠️ **Misaligned Edges**: Edges along the furniture and cabinet line do not align consistently with other planes; overlaps appear jagged.
- ⚠️ **Depth Or Perspective Errors**: Depth cues are inconsistent; foreground table edges blur into the scene, reducing proper depth separation.
- 🎨 **Ghosting**: Residual ghost-like outlines around furniture and plants, indicating misregistered surfaces.
- 🎨 **Over Blur**: Significant blur across wide areas, reducing fine texture detail on upholstery and cabinet surfaces.
- 🎨 **Texture Inconsistency**: Inconsistent texture quality between wall art, upholstery, and window areas; patches look irregular.


### View 5 (120°)

![View 5](captured_views/ktv_hevc_deblur035/view_004_120deg.png)


**VLM Analysis**:

**Score**: 5/10


> *The scene shows recognizable room geometry but with notable geometric distortions and depth inconsistencies. Textures suffer from ghosting, blur, and uneven quality across surfaces, reducing realism and multi-surface coherence. Overall realism is moderate with several artifacts indicating reconstruction limitations.*


**Detected Issues**:
- ⚠️ **Curved Or Warped Walls**: Walls and panels exhibit noticeable bending and non-Manhattan geometry, especially near the left and back regions.
- ⚠️ **Misaligned Edges**: Edges between furniture and walls appear slightly misaligned; chafed seams around the cabinet and panel edges.
- ⚠️ **Depth Or Perspective Errors**: Depth cues are inconsistent; perspective warps around the foreground table and chairs create unrealistic depth perception.
- 🎨 **Ghosting**: Fine line ghosts and hairline strokes across surfaces (especially on walls and furniture) typical of 3DGS sampling.
- 🎨 **Over Blur**: Some regions show excessive blur, reducing texture clarity (e.g., chairs and foreground).
- 🎨 **Texture Inconsistency**: Inconsistent texture densities; some surfaces look smeared while others are sharper, causing mismatch.


### View 6 (150°)

![View 6](captured_views/ktv_hevc_deblur035/view_005_150deg.png)


**VLM Analysis**:

**Score**: 5/10


> *The rendering exhibits moderate geometric and textural inconsistencies characteristic of 3D Gaussian splatting reconstructions. The space is recognizable, but curved/warped walls, depth ambiguities, and ghosting artifacts reduce realism and spatial coherence. Improvements in edge alignment, depth accuracy, and texture stability would raise the reconstruction quality.*


**Detected Issues**:
- ⚠️ **Curved Or Warped Walls**: Noticeable warping and bending of wall surfaces and structural lines, especially along the left side and near the cabinets.
- ⚠️ **Misaligned Edges**: Edges and junctions appear slightly misaligned or skewed, contributing to an unnatural geometry impression.
- ⚠️ **Depth Or Perspective Errors**: Depth cues and perspective appear inconsistent in several regions, leading to an unstable sense of space.
- 🎨 **Ghosting**: Ghost-like trails and faint duplications around high-contrast boundaries (e.g., furniture edges and wall texture).
- 🎨 **Over Blur**: Localized blur smears texture details, particularly on furniture and wall surfaces.
- 🎨 **Texture Inconsistency**: Inconsistent texture fidelity across surfaces; some areas look painterly while others are more detailed.


### View 7 (180°)

![View 7](captured_views/ktv_hevc_deblur035/view_006_180deg.png)


**VLM Analysis**:

**Score**: 4/10


> *The rendering shows a plausible interior layout but suffers from significant geometric distortions and pervasive texture artifacts characteristic of 3D Gaussian Splatting reconstructions. Structural geometry is fragmented with curved/warped walls and misaligned edges, and depth cues are inconsistent. Texture fidelity is deteriorated by ghosting, floating strands, and global blur, reducing realism and multi-surface coherence. Overall, it is a recognizable reconstruction with notable reconstruction errors that prevent it from being convincingly real-world accurate.*


**Detected Issues**:
- ⚠️ **Curved Or Warped Walls**: Wall surfaces appear tuyed and warped, particularly on the left dark wall and the overall room walls showing non-planar distortions.
- ⚠️ **Misaligned Edges**: Edges of furniture and shelving do not align cleanly with walls; some verticals appear skewed relative to the room geometry.
- ⚠️ **Depth Or Perspective Errors**: Depth cues and perspective are inconsistent in several regions (e.g., shelf and seating area) leading to ambiguous scale and depth relations.
- 🎨 **Ghosting**: Fine fiber-like artifacts and motion-like trails across surfaces, especially on walls and shelves.
- 🎨 **Floating Artifacts**: Strand-like wisps float in front of and within scene surfaces, not anchored to geometry.
- 🎨 **Over Blur**: Broad blurring in large flat areas reduces texture fidelity and edge sharpness.
- 🎨 **Texture Inconsistency**: Inconsistent surface textures between adjacent surfaces (e.g., wall vs. paneling) and irregular noise patterns.


### View 8 (210°)

![View 8](captured_views/ktv_hevc_deblur035/view_007_210deg.png)


**VLM Analysis**:

**Score**: 5/10


> *The rendering shows noticeable geometric and texture inconsistencies typical of aggressive 3D Gaussian splatting reconstructions. Structural integrity is compromised by warped walls, misaligned edges, and depth/perspective errors. Texture fidelity is affected by ghosting, floating artifacts, and over-blur, reducing realism. Overall, this could be interpreted as a plausible interior layout but with clear reconstruction artifacts that prevent it from being mistaken for a real scene without additional refinement.*


**Detected Issues**:
- ⚠️ **Curved Or Warped Walls**: Several wall surfaces appear heavily bent and warped, particularly the left dark wall with numerous jagged lines, giving a non-planar geometry impression.
- ⚠️ **Misaligned Edges**: Edges between wall planes and furniture show misalignment and inconsistent junctions, not aligning cleanly with expected room geometry.
- ⚠️ **Depth Or Perspective Errors**: Depth cues are inconsistent; near objects struggle with proper perspective and occlusion, causing a flattened or skewed sense of space.
- 🎨 **Ghosting**: Texture bleed and faint duplicates are visible in some regions, especially along vertical structures.
- 🎨 **Floating Artifacts**: Stray line-like artifacts float within the scene, not tied to real geometry.
- 🎨 **Over Blur**: Overall softness and motion-like blur reduce sharpness of textures on furniture and walls.
- 🎨 **Texture Inconsistency**: Texture tiling and inconsistent roughness across surfaces; some materials look unnaturally uniform or mismatched.


### View 9 (240°)

![View 9](captured_views/ktv_hevc_deblur035/view_008_240deg.png)


**VLM Analysis**:

**Score**: 3/10


> *The rendering exhibits severe geometric distortions with warped walls, misaligned edges, and unreliable depth cues. Textures show ghosting, floating artifacts, and abrupt inconsistencies, making the scene clearly non-credible as a real-world reconstruction. Artifacts and depth errors significantly reduce realism and spatial coherence.*


**Detected Issues**:
- ⚠️ **Curved Or Warped Walls**: Large wall surface on left appears highly warped and non-planar; curvature disrupts geometry.
- ⚠️ **Misaligned Edges**: Edges between wall and floor/ceiling do not align; visible misplacements around the doorway/partition.
- ⚠️ **Depth Or Perspective Errors**: Forward elements and background depth seem inconsistent; perspective foreshortening is unreliable.
- 🎨 **Ghosting**: Translucent trailing artifacts across complex textures; outlines bleed into adjacent surfaces.
- 🎨 **Floating Artifacts**: Isolated geometry fragments float unnaturally, detached from main surfaces.
- 🎨 **Texture Inconsistency**: Textures alternate between dense pattern and smooth areas, lacking cohesion.


### View 10 (270°)

![View 10](captured_views/ktv_hevc_deblur035/view_009_270deg.png)


**VLM Analysis**:

**Score**: 4/10


> *The rendering shows a dense, irregular texture that does not convincingly form a correct real-world surface. Structural cues such as walls and edges are imperfect (slight curvature, edge misalignment, and depth inconsistencies). Texture exhibits artifacts (ghosting, over-blur, and inconsistent density) that reduce realism. Overall, the scene is locally plausible but contains noticeable geometric and texture flaws that prevent it from being strongly convincing as a real 3D reconstruction.*


**Detected Issues**:
- ⚠️ **Curved Or Warped Walls**: The large wall surface appears subtly curved and non-planar, not matching a flat real-world wall.
- ⚠️ **Misaligned Edges**: Edge where wall meets floor/adjacent plane shows misalignment and abrupt transition.
- ⚠️ **Depth Or Perspective Errors**: Depth cues look inconsistent; near/far relationships and perspective seem off, giving a disjointed sense of scale.
- 🎨 **Ghosting**: Subsurface ghost-like patterns across the wall texture, indicating multi-pass rendering artifacts.
- 🎨 **Over Blur**: Uniform blur reduces fine microstructure, leading to loss of sharpness in dense textures.
- 🎨 **Texture Inconsistency**: Texture density and shading vary inconsistently across the surface, suggesting patchy reconstruction.


### View 11 (300°)

![View 11](captured_views/ktv_hevc_deblur035/view_010_300deg.png)


**VLM Analysis**:

**Score**: 5/10


> *The rendering shows a dense, fiber-like surface with plausible mass and occlusion, but depth cues are weak and texture is inconsistently shaded with noticeable blur and ghosting. Overall geometry is moderately coherent, but the scene lacks reliable spatial grounding and has several texture reliability issues that reduce realism.*


**Detected Issues**:
- ⚠️ **Depth Or Perspective Errors**: Overall depth cues feel inconsistent; the dense fiber field lacks reliable perspective anchors, leading to uncertain depth perception.
- 🎨 **Ghosting**: Subtle ghost-like artifacts in dense hair/fiber regions; layering artifacts are visible.
- 🎨 **Over Blur**: Regions of fibers appear overly smoothed, reducing fine detail and sharpness.
- 🎨 **Texture Inconsistency**: Inconsistent surface shading across fibers; some areas look plastic or uniform while others are detailed.


### View 12 (330°)

![View 12](captured_views/ktv_hevc_deblur035/view_011_330deg.png)


**VLM Analysis**:

**Score**: 5/10


> *The render shows a dense, hair-like geometry with a smooth adjacent surface. While no explicit geometric collapses or misalignments are visible, depth cues are inconsistent across regions, and texture continuity is poor between surfaces. This yields a moderate realism but notable reconstruction artifacts that reduce overall plausibility.*


**Detected Issues**:
- ⚠️ **Depth Or Perspective Errors**: Significant depth cues are inconsistent across the dense, hair-like geometry; perspective alignment between the near beige surface and the dark textured region is unclear.
- 🎨 **Texture Inconsistency**: Abrupt change in texture quality between the smooth wall and the highly detailed hair-like surface; lighting/shading contrast appears inconsistent across regions.
