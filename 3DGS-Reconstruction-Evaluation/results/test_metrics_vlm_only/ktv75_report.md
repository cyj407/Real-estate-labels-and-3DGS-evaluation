# 3DGS Reconstruction Quality Report: ktv75

**Overall Score**: 45.62/100

**Number of Views Evaluated**: 12

**Render URL**: https://3d-tour-demo-scene.vercel.app/?model=https://storage.googleapis.com/3dgs-homee/ktv50.glb&splat=https://storage.googleapis.com/3dgs-homee/ktv75.ksplat&px=-3.357&py=0.082&pz=0.38&tx=-2.56&ty=0.007&tz=-0.218


---


## Computer Vision Metrics


---


## Vision Language Model Metrics


**Model**: gpt-5-nano


### Overall Quality Assessment

- **Quality Score**: 49.17/100

- **Mean Rating**: 4.92/10

- **Std Dev**: 1.11

- **Range**: [3.00, 7.00]


### Artifact Detection

- **Quality Score**: 40.83/100

- **Mean Severity**: 6.92/10

- **Std Dev**: 1.04


*Lower severity indicates fewer visual artifacts (ghosting, floating blobs, etc.).*


### Structural Quality

- **Quality Score**: 47.50/100

- **Mean Rating**: 4.75/10

- **Std Dev**: 1.16


*Higher rating indicates better structural integrity (no warped walls, misaligned edges, etc.).*


---


## Detailed View Analysis


### View 1 (0°)

![View 1](captured_views/ktv75/view_000_000deg.png)


**VLM Analysis**:

**Score**: 3/10


> *The rendering shows major geometric and texture inconsistencies: warped foreground structures, misaligned edges, unstable depth relations, and pervasive blur/ghosting artifacts. Overall realism is limited; the scene is not a reliable reconstruction of a real 3D environment.*


**Detected Issues**:
- ⚠️ **Curved Or Warped Walls**: Large foreground structures appear heavily curved and stretched, not matching real-world planar walls.
- ⚠️ **Misaligned Edges**: Edges between floor and wall/sofa show noticeable misalignment and jagged transitions.
- ⚠️ **Depth Or Perspective Errors**: Severe depth cues are inconsistent; foreground dominates with abrupt transitions to background black area, depth cues unreliable.
- 🎨 **Ghosting**: Soft duplications and smeared textures near the large foreground blur.
- 🎨 **Floating Artifacts**: Isolated bright streaks and patches not anchored to geometry.
- 🎨 **Over Blur**: Extensive blur obscures fine details, especially in the foreground.
- 🎨 **Texture Inconsistency**: Inconsistent surface textures between floor, chair, and wall regions.


### View 2 (30°)

![View 2](captured_views/ktv75/view_001_030deg.png)


**VLM Analysis**:

**Score**: 5/10


> *The rendering shows a plausible room layout but with strong geometric distortions and pervasive texture artifacts. Warped walls, smeared edges, depth inconsistencies, and ghosted textures prevent it from being a faithful reconstruction of a real scene. Improvements should focus on correcting perspective geometry, reducing excessive blur, and stabilizing texture transitions to restore spatial coherence.*


**Detected Issues**:
- ⚠️ **Curved Or Warped Walls**: Walls and ceiling exhibit pronounced bending and warping, particularly near the corners and along the ceiling lines.
- ⚠️ **Misaligned Edges**:  Edges of furniture and architectural elements appear slightly misaligned or smeared, especially around doorway frames and cabinet fronts.
- ⚠️ **Depth Or Perspective Errors**: Overall depth cues are inconsistent; some surfaces appear stretched or compressed altering perceived distance.
- 🎨 **Ghosting**:  faint trailing/ghost-like artifacts around edges and high-contrast transitions.
- 🎨 **Floating Artifacts**:  small disconnected patches of texture appear detached from surfaces, giving a floating look.
- 🎨 **Over Blur**:  excessive blur smears fine details across large areas such as walls and furniture.
- 🎨 **Texture Inconsistency**:  inconsistent texturing across surfaces (varying sharpness and grain) without physical justification.


### View 3 (60°)

![View 3](captured_views/ktv75/view_002_060deg.png)


**VLM Analysis**:

**Score**: 7/10


> *The scene presents a structurally coherent dining room with plausible geometry and layout. Minor depth/perspective cues are slightly inconsistent, and the overall texture is intentionally stylized, causing reduced sharpness and some texture inconsistency across surfaces. No major geometric defects detected, but depth cues and surface detail fidelity are somewhat compromised by the rendering style.*


**Detected Issues**:
- ⚠️ **Depth Or Perspective Errors**: Slight parallax/perspective inconsistencies near the window edges and along the table depth, affecting precise depth cues.
- 🎨 **Over Blur**: Overall painterly blur/softening across surfaces, reducing fine texture sharpness.
- 🎨 **Texture Inconsistency**: Inconsistent surface textures (soft painterly look on walls vs. sharper foreground objects) typical of stylized renderings.


### View 4 (90°)

![View 4](captured_views/ktv75/view_003_090deg.png)


**VLM Analysis**:

**Score**: 6/10


> *The scene is recognizable as a dining room reconstruction with coherent layout and object placement. However, geometric depth cues show minor inconsistencies and several texture-related artifacts reduce realism (ghosting, over-blur, and texture inconsistency). Overall structure is plausible, but not perfectly indistinguishable from a real photograph.*


**Detected Issues**:
- ⚠️ **Depth Or Perspective Errors**: Subtle depth/perspective inconsistencies around the table and chairs, and some perspective warp near the back wall where the artwork meets the cabinet.
- 🎨 **Ghosting**:  faint ghost-like trails/ghosting in high-contrast regions and around edges.
- 🎨 **Over Blur**: overall soft focus/over-blurring of fine textures, especially on furniture and walls.
- 🎨 **Texture Inconsistency**: inconsistent surface textures between materials (wood/table vs. upholstery) leading to unrealistic transitions.


### View 5 (120°)

![View 5](captured_views/ktv75/view_004_120deg.png)


**VLM Analysis**:

**Score**: 6/10


> *The rendering presents a recognizably indoor conference-room scene with plausible furniture layout and lighting. However, geometric distortions (curved/warped walls and misaligned edges) and pervasive soft blur reduce realism and affect structural accuracy. Textures are generally well represented but lack of sharpness and minor inconsistencies reduce perceptual fidelity. Overall, a mostly realistic reconstruction with notable geometric and texture quality limitations.*


**Detected Issues**:
- ⚠️ **Curved Or Warped Walls**: Notable curvature and irregularities along the left wall and ceiling area, giving a distorted geometry impression.
- ⚠️ **Misaligned Edges**: Slight misalignment at some panel edges and seams, especially near the back wall and wall decorations.
- 🎨 **Over Blur**: Overall soft focus/blur in many regions, reducing sharpness of textures.


### View 6 (150°)

![View 6](captured_views/ktv75/view_005_150deg.png)


**VLM Analysis**:

**Score**: 6/10


> *The rendering forms a recognizable interior scene with plausible layout and lighting, but exhibits notable geometric irregularities in surfaces (notably left-side walls), along with texture inconsistencies and overall blur. These factors reduce realism and indicate reconstruction artifacts that diverge from a true real-world capture.*


**Detected Issues**:
- ⚠️ **Curved Or Warped Walls**: Left wall/nearby surfaces show irregular, non-rectilinear warping and jagged edge treatment.
- 🎨 **Ghosting**: Subtle ghosting around high-contrast edges and seams.
- 🎨 **Over Blur**: Overall soft blur reduces sharpness, especially on mid and far surfaces.
- 🎨 **Texture Inconsistency**: Inconsistent texture detail across walls and furniture; some areas look smeared.


### View 7 (180°)

![View 7](captured_views/ktv75/view_006_180deg.png)


**VLM Analysis**:

**Score**: 5/10


> *The rendering shows a plausible interior scene but exhibits notable geometric distortions (curved/warped walls and depth inconsistencies) and texture artifacts (blur, ghosting, and uneven texture fidelity). These issues reduce realism and indicate moderate reconstruction errors typical of aggressive 3D Gaussian Splatting results. Minor geometry and alignment issues prevent it from being indistinguishable from a real scene.*


**Detected Issues**:
- ⚠️ **Curved Or Warped Walls**: Prominent warping along the left wall and door region; vertical straight lines appear distorted, suggesting curved geometry or perspective distortion.
- ⚠️ **Depth Or Perspective Errors**: Overall depth cues are inconsistent in some areas (foreground furniture edges not aligning cleanly with background). Some parts appear stretched due to aggressive processing.
- 🎨 **Ghosting**: Subtle ghosting around high-contrast edges, especially on the black wall panel and near the doorway.
- 🎨 **Over Blur**: Significant blur on mid-ground furniture and wall textures, reducing sharpness of details.
- 🎨 **Texture Inconsistency**: Inconsistent texture fidelity across surfaces (wood, fabric, and paint show varying granularity) with some smeared areas.


### View 8 (210°)

![View 8](captured_views/ktv75/view_007_210deg.png)


**VLM Analysis**:

**Score**: 4/10


> *The rendering exhibits strong geometric instability with warped walls, misaligned edges, and depth inconsistencies that undermine spatial coherence. Texture details are inconsistent and smeared, resulting in noticeable artifacts that reduce realism and multi-surface consistency.*


**Detected Issues**:
- ⚠️ **Curved Or Warped Walls**: Multiple wall planes appear curved and warped, especially along the vertical wall segments; geometry does not align with a typical rectilinear room.
- ⚠️ **Misaligned Edges**: Edges near doorway and wall joints do not meet cleanly; noticeable tearing/offsets along panel edges.
- ⚠️ **Depth Or Perspective Errors**: Depth cues are inconsistent; foreground and background planes do not maintain stable perspective, contributing to a skewed spatial interpretation.
- 🎨 **Floating Artifacts**: Unclear speckled/line artifacts floating over surfaces, not attached to geometry.
- 🎨 **Over Blur**: Significant blur smears detail across large regions, reducing texture fidelity.
- 🎨 **Texture Inconsistency**: Texture quality varies abruptly between adjacent surfaces, with inconsistent shading and detail.


### View 9 (240°)

![View 9](captured_views/ktv75/view_008_240deg.png)


**VLM Analysis**:

**Score**: 4/10


> *The rendering shows notable geometric and textural inconsistencies typical of challenging 3DGS reconstructions: warped walls, misaligned edges, and depth errors combine with multiple texture artifacts (ghosting, floating strokes, over-blur). Overall realism is limited; reconstruction fails to convincingly replicate real-world spatial geometry, though some scene elements remain recognizable.*


**Detected Issues**:
- ⚠️ **Curved Or Warped Walls**: Several wall planes appear warped and skewed, with distorted straight lines (e.g., vertical panels and doorway edges) suggesting geometry misalignment.
- ⚠️ **Misaligned Edges**: Edges where wall panels and furniture meet do not align cleanly; noticeable gaps and misfits along vertical/horizontal seams.
- ⚠️ **Depth Or Perspective Errors**: Depth cues are inconsistent; perspective lines do not converge realistically, giving a warped sense of space.
- 🎨 **Ghosting**: Subtle ghost-like duplicates along textures, particularly on large flat surfaces.
- 🎨 **Floating Artifacts**: Random stray strokes/lines appear detached from surfaces, floating in space.
- 🎨 **Over Blur**: Regions show excessive blur smearing texture details, reducing sharpness.
- 🎨 **Texture Inconsistency**: Inconsistent texture resolution across surfaces; some areas look smeared while others are detailed.


### View 10 (270°)

![View 10](captured_views/ktv75/view_009_270deg.png)


**VLM Analysis**:

**Score**: 4/10


> *The rendering shows noticeable geometric distortions and depth inconsistencies, with mixed texture fidelity and visible fusion-related artifacts. Overall it behaves like a rough reconstruction with several structural and textural irregularities, not yet convincing as a real-world indoor scene.*


**Detected Issues**:
- ⚠️ **Curved Or Warped Walls**: Many walls appear irregular and rubbery with visible distortions around the vertical surfaces, suggesting warped geometry.
- ⚠️ **Misaligned Edges**: Edges of doorways and panels do not align cleanly; some corners appear skewed or offset.
- ⚠️ **Depth Or Perspective Errors**: Depth cues are inconsistent; perspective lines diverge oddly, giving a non-realistic depth relationship between foreground and background.
- 🎨 **Ghosting**: Faint translucent echoes around large flat surfaces and along edges, typical of multi-view fusion artifacts.
- 🎨 **Over Blur**: Certain regions appear overly smooth, reducing fine texture details (e.g., walls and floor).
- 🎨 **Texture Inconsistency**: Texture quality varies across surfaces; some areas look blurred while others retain edges, inconsistent with lighting.


### View 11 (300°)

![View 11](captured_views/ktv75/view_010_300deg.png)


**VLM Analysis**:

**Score**: 4/10


> *The render exhibits severe geometric distortions (curved, misaligned walls; distorted depth cues) and noticeable texture/appearance artifacts (ghosting, over-blur, inconsistent textures). These issues significantly reduce realism and structural reliability as a real-scene reconstruction. Minor surface details are present, but overall quality is insufficient for accurate 3D reconstruction assessment.*


**Detected Issues**:
- ⚠️ **Curved Or Warped Walls**: Numerous walls and vertical panels show pronounced curvature and bending, especially near the right-side wall and doorway frames.
- ⚠️ **Misaligned Edges**: Edges of walls and door frames appear misaligned and jagged, contributing to a non-realistic geometry.
- ⚠️ **Depth Or Perspective Errors**: Depth cues are inconsistent; perspective appears skewed likely from artifacts rather than true scene geometry.
- 🎨 **Ghosting**: Subtle ghosting around high-contrast edges and circular marker, indicative of multi-view blending artifacts.
- 🎨 **Over Blur**: Overall softness and motion-like blur reduce sharpness of textures, especially on foreground surfaces.
- 🎨 **Texture Inconsistency**: Texture continuity is erratic; surfaces look stretched or smeared in multiple regions.


### View 12 (330°)

![View 12](captured_views/ktv75/view_011_330deg.png)


**VLM Analysis**:

**Score**: 5/10


> *The rendering shows recognizable interior structure but with noticeable geometric distortions and inconsistent textures. Warped walls, misaligned edges, and depth inconsistencies reduce realism. A prominent central ring artifact and overall blur contribute to the sense of a flawed reconstruction rather than a faithful real scene.*


**Detected Issues**:
- ⚠️ **Curved Or Warped Walls**: Numerous subtle warps and scribble-like distortions across walls and near door frames, giving a warped geometry impression.
- ⚠️ **Misaligned Edges**: Edges at doorway frames and panel boundaries do not align cleanly, contributing to a jumbled silhouette.
- ⚠️ **Depth Or Perspective Errors**: Depth cues are inconsistent in transitional areas (e.g., hallway to room) leading to a questionable sense of scale and perspective.
- 🎨 **Floating Artifacts**: A prominent circular white ring in the center and stray scribbles/lines give the impression of floating markers or overlays.
- 🎨 **Over Blur**: Overall softness and motion-like blur reduces texture sharpness, especially on walls and floor.
- 🎨 **Texture Inconsistency**: Varied texture density across surfaces (some very smooth, some highly scribbled) indicate inconsistent reconstruction textures.
