# 3DGS Reconstruction Quality Report: ktv75

**Overall Score**: 43.62/100

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

- **Quality Score**: 67.64/100

- **Mean Score**: 67.64

- **Std Dev**: 10.43


*No-reference quality metric based on natural scene statistics.*


---


## Vision Language Model Metrics


**Model**: gpt-5-nano


### Overall Quality Assessment

- **Quality Score**: 49.17/100

- **Mean Rating**: 4.92/10

- **Std Dev**: 0.86

- **Range**: [4.00, 6.00]


### Artifact Detection

- **Quality Score**: 45.00/100

- **Mean Severity**: 6.50/10

- **Std Dev**: 0.96


*Lower severity indicates fewer visual artifacts (ghosting, floating blobs, etc.).*


### Structural Quality

- **Quality Score**: 48.33/100

- **Mean Rating**: 4.83/10

- **Std Dev**: 1.14


*Higher rating indicates better structural integrity (no warped walls, misaligned edges, etc.).*


---


## Detailed View Analysis


### View 1 (0°)

![View 1](captured_views/ktv75/view_000_000deg.png)


**VLM Analysis**:

**Score**: 4/10


> *The rendering shows significant structural and textural inconsistencies that reduce realism: warped foreground geometry, misaligned edges, abrupt depth transitions, and noticeable blur/ghosting. Overall, the scene fails to convincingly represent a coherent real-world environment; geometric integrity and multi-surface consistency are only marginally acceptable.*


**Detected Issues**:
- ⚠️ **Curved Or Warped Walls**: Foreground column/edge appears distorted with pronounced curvature and warped transitions between surfaces.
- ⚠️ **Misaligned Edges**: Visible misalignment between floor and walls near the foreground; edge breaks do not form clean right angles.
- ⚠️ **Depth Or Perspective Errors**: Depth cues are inconsistent (very shallow foreground blur with abrupt black background), leading to unusable perspective in portions of the scene.
- 🎨 **Ghosting**: Soft ghost-like artifacts around high-contrast transitions, especially near the large blurred foreground.
- 🎨 **Over Blur**: Strong blur in the near foreground obscures geometry and contributes to depth confusion.
- 🎨 **Texture Inconsistency**: Inconsistent texture detail across surfaces (sharp on some areas, smeared on others) indicating patchy reconstruction.


### View 2 (30°)

![View 2](captured_views/ktv75/view_001_030deg.png)


**VLM Analysis**:

**Score**: 5/10


> *The rendering shows a plausible interior layout but suffers from pronounced geometric distortions and depth inconsistencies. Surface textures are variably sharp with deliberate blur and occasional floaty artifacts, reducing realism. Overall, it reads as a roughly reconstructed space with notable but not catastrophic defects; improvements should target rectifying perspective, wall alignments, and texture coherence to approach a photo-realistic realism.*


**Detected Issues**:
- ⚠️ **Curved Or Warped Walls**: Walls and ceiling exhibit notable warping and bending geometry, especially along the edges and corners, giving a non-rectilinear appearance.
- ⚠️ **Misaligned Edges**: Some door frames, furniture edges, and floor transitions appear slightly misaligned or skewed relative to the scene plane.
- ⚠️ **Depth Or Perspective Errors**: Depth cues are inconsistent; some objects appear oversized or misplaced in depth, suggesting perspective errors.
- 🎨 **Floating Artifacts**: Small translucent artifacts hover near surfaces, giving a floaty look in some regions.
- 🎨 **Over Blur**: Widespread motion-like blur reduces surface sharpness, smoothing fine details.
- 🎨 **Texture Inconsistency**: Surface textures vary abruptly between adjacent areas, lacking consistent material cues.


### View 3 (60°)

![View 3](captured_views/ktv75/view_002_060deg.png)


**VLM Analysis**:

**Score**: 6/10


> *The scene presents a recognizable dining room layout with coherent geometry and plausible lighting. However, the rendering exhibits noticeable over-blurring and painterly texture smoothing typical of 3DGS reconstructions, leading to slightly inconsistent materials and minor depth/perspective anomalies around windows and far surfaces. Overall structure is sound, but texture fidelity and multi-surface coherence could be improved to reach higher realism.*


**Detected Issues**:
- ⚠️ **Depth Or Perspective Errors**: Subtle perspective inconsistencies around window frames and chair alignments; slight depth mismatch in background elements relative to foreground.
- 🎨 **Over Blur**: Overall painterly/softed shading and edge diffusion reduce sharpness of textures on furniture and floor.
- 🎨 **Texture Inconsistency**: Inconsistent material quality across surfaces (table vs. chairs vs. walls) with unnatural smoothing.


### View 4 (90°)

![View 4](captured_views/ktv75/view_003_090deg.png)


**VLM Analysis**:

**Score**: 6/10


> *Overall geometry appears coherent with plausible room layout and depth cues. Minor texture inconsistencies and global blur reduce realism slightly, but structural integrity is maintained and the scene remains believable as a real interior reconstruction.*


**Detected Issues**:
- 🎨 **Over Blur**: General softening across surfaces, likely due to rendering/upsampling.
- 🎨 **Texture Inconsistency**: Inconsistent texture fidelity on large flat surfaces (e.g., wall paneling and table) with painterly transitions.


### View 5 (120°)

![View 5](captured_views/ktv75/view_004_120deg.png)


**VLM Analysis**:

**Score**: 6/10


> *The rendering shows a plausible room layout with coherent seating arrangement and depth, but notable geometric distortion on the left wall and overall softness indicate reconstruction artifacts. The scene is recognizable as a real room, yet not fully geometry-consistent or texture-stable due to warped surfaces and strong blur.*


**Detected Issues**:
- ⚠️ **Curved Or Warped Walls**: Left wall panel appears warped and scribbled, giving a distorted geometry.
- 🎨 **Over Blur**: Overall softness suggests heavy post-processing or 3DGS blur, reducing edge sharpness.


### View 6 (150°)

![View 6](captured_views/ktv75/view_005_150deg.png)


**VLM Analysis**:

**Score**: 6/10


> *The scene presents a plausible interior layout with chairs, tables, and decor, but exhibits moderate geometric distortions (curved/warped walls and perspective biases) and texture inconsistencies. Overall realism is acceptable but not indistinguishable from a real photograph; minor artifacts reduce the overall fidelity.*


**Detected Issues**:
- ⚠️ **Curved Or Warped Walls**: Left wall and doorway area show slight curvature and irregular edges suggesting warped geometry.
- ⚠️ **Depth Or Perspective Errors**: Overall depth cues and wall/ceiling intersections appear mildly distorted, particularly near the back wall and table edge, affecting perspective consistency.
- 🎨 **Over Blur**: General softness especially on furniture and walls, reducing sharpness and depth cues.
- 🎨 **Texture Inconsistency**: Inconsistent texture quality across surfaces (e.g., mural wall vs. surrounding walls, and decorative items) leading to mismatched realism.


### View 7 (180°)

![View 7](captured_views/ktv75/view_006_180deg.png)


**VLM Analysis**:

**Score**: 4/10


> *The rendering exhibits notable geometric distortions and misalignments (curved/warped walls, jagged edges) with smeared textures and incoherent surface details. Depth is mostly plausible, but the overall scene lacks structural reliability and photorealism due to pervasive artifacting and topology issues. Improvements needed in geometry regularization and texture consistency to approach a real-world scene.*


**Detected Issues**:
- ⚠️ **Curved Or Warped Walls**: Multiple surfaces show heavy scribble-like distortion and bending, notably along the white wall and near the door frame.
- ⚠️ **Misaligned Edges**: Edges at the door and wall junction appear misaligned and jagged, indicating inconsistent topology.
- 🎨 **Over Blur**: Overall surfaces appear smeared, reducing fine details on furniture and wall textures.
- 🎨 **Texture Inconsistency**: Texture quality varies across surfaces (floor, walls, furniture) with abrupt changes and lacking coherence.


### View 8 (210°)

![View 8](captured_views/ktv75/view_007_210deg.png)


**VLM Analysis**:

**Score**: 4/10


> *The rendering shows a recognizable scene structure but suffers from noticeable depth/perspective inconsistencies and edge misalignments. Textures are inconsistently applied with overall blur, leading to a reconstruction that is only moderately realistic and could be confused with a distorted 3DGS/NeRF result.*


**Detected Issues**:
- ⚠️ **Misaligned Edges**: Noticeable misalignment along wall seam/edge near the central column; gaps and edge contours do not line up cleanly with adjacent surfaces.
- ⚠️ **Depth Or Perspective Errors**: Depth cues appear inconsistent (foreground vs background geometry wobble; caps and edges don't align with expected perspective).
- 🎨 **Over Blur**: Overall surface textures look smeared or overly soft in several regions, reducing sharpness.
- 🎨 **Texture Inconsistency**: Texture quality varies across surfaces (some areas look smooth while others are heavily smeared or irregular).


### View 9 (240°)

![View 9](captured_views/ktv75/view_008_240deg.png)


**VLM Analysis**:

**Score**: 4/10


> *The rendering exhibits notable geometric distortions (warped walls, misaligned edges) and depth inconsistencies that reduce realism as a real-world 3D reconstruction. Texture fidelity is compromised by ghosting and surface-texture mismatches, leading to an overall moderate-to-poor assessment with only limited structural cues appearing plausible.*


**Detected Issues**:
- ⚠️ **Curved Or Warped Walls**: Wall panels and vertical surfaces show noticeable curvature and irregular warping, especially along the central brown surface.
- ⚠️ **Misaligned Edges**: Some edges do not align with adjacent geometry (floor/ceiling lines appear offset), contributing to a disjointed appearance.
- ⚠️ **Depth Or Perspective Errors**: Depth cues and perspective appear inconsistent (anomalous scale, odd foreshortening), hindering real-world spatial interpretation.
- 🎨 **Ghosting**:  faint duplicate surfaces and overlaid strokes, typical of reconstruction artifacts.
- 🎨 **Texture Inconsistency**: Textures (wood, wall, floor) do not match across surfaces; abrupt changes suggest stitching rather than real material continuity.


### View 10 (270°)

![View 10](captured_views/ktv75/view_009_270deg.png)


**VLM Analysis**:

**Score**: 5/10


> *The rendering shows recognizable spatial structure but with noticeable geometric distortions and texture inconsistencies. Surface warp, edge misalignment, and depth errors reduce realism. Texture artifacts (ghosting, over-blur, and inconsistency) further diminish fidelity. Overall, it is a plausible reconstruction but not convincingly photorealistic; minor artifacts significantly impact perceived accuracy.*


**Detected Issues**:
- ⚠️ **Curved Or Warped Walls**: Multiple surface imperfections and wavy distortions across wall-like surfaces, suggesting depth warp from splat-based reconstruction.
- ⚠️ **Misaligned Edges**: Doorways and edges appear slightly offset or smeared relative to surrounding geometry, indicating misalignment.
- ⚠️ **Depth Or Perspective Errors**: Overall perspective seems skewed; vertical/horizontal cues not consistent with real-world geometry, suggesting depth imprecision.
- 🎨 **Ghosting**: Faint duplicates and ghost-like edges around high-contrast regions, typical of NeRF/3DGS composites.
- 🎨 **Over Blur**: Significant blur across large surfaces, reducing texture sharpness and detail fidelity.
- 🎨 **Texture Inconsistency**: Inconsistent texture quality between foreground cardboard and background walls; patches of varying detail and color.


### View 11 (300°)

![View 11](captured_views/ktv75/view_010_300deg.png)


**VLM Analysis**:

**Score**: 5/10


> *The rendering shows notable geometric and textural inconsistencies typical of a coarse 3DGS/NeRF reconstruction. Warped walls, slight edge misalignments, and depth errors reduce realism. Texture sharpness is compromised with blurred regions and inconsistent material cues. Overall, the scene resembles a plausible corridor but with clear reconstruction artifacts that prevent it from being indistinguishable from a real photograph.*


**Detected Issues**:
- ⚠️ **Curved Or Warped Walls**: Visible warping and bending in wall planes and door frames; slight curvature artifacts across the corridor surfaces.
- ⚠️ **Misaligned Edges**: Some edges and corners appear misaligned or miscoincident, especially near doorway junctions.
- ⚠️ **Depth Or Perspective Errors**: Depth cues are inconsistent in several regions; perspective compression around the doorway and far wall reduces depth realism.
- 🎨 **Over Blur**: General blur reduces texture sharpness; fine details are smeared across surfaces, especially near edges.
- 🎨 **Texture Inconsistency**: Inconsistent material appearance (wood panels vs. wall surfaces) and mismatched reflectivity across surfaces.


### View 12 (330°)

![View 12](captured_views/ktv75/view_011_330deg.png)


**VLM Analysis**:

**Score**: 4/10


> *The rendering exhibits significant geometric and depth inconsistencies with warped walls, misaligned edges, and distorted perspective. Textures are smeared with ghosting and inconsistent surface details, reducing realism. Overall, the scene is not a reliable reconstruction of a real 3D interior; artifacts are prominent and affect structural interpretation.*


**Detected Issues**:
- ⚠️ **Curved Or Warped Walls**: Numerous jagged and warped edge lines throughout walls and surfaces, especially near doorways and corners.
- ⚠️ **Misaligned Edges**: Edges of panels and doors appear misaligned or skewed relative to surrounding geometry.
- ⚠️ **Depth Or Perspective Errors**: Overall perspective feels distorted with inconsistent depth cues and unusual foreshortening in hallway areas.
- 🎨 **Ghosting**: Fine scribble-like artifacts and overlaid strokes across surfaces.
- 🎨 **Over Blur**: General scene appears smeared; edges lack crispness especially on vertical structures.
- 🎨 **Texture Inconsistency**: Textures vary abruptly between surfaces; some areas look painterly rather than physical.
