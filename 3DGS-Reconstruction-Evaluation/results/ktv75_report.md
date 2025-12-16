# 3DGS Reconstruction Quality Report: ktv75

**Overall Score**: 43.46/100

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

- **Std Dev**: 1.11

- **Range**: [3.00, 7.00]


### Artifact Detection

- **Quality Score**: 43.33/100

- **Mean Severity**: 6.67/10

- **Std Dev**: 1.03


*Lower severity indicates fewer visual artifacts (ghosting, floating blobs, etc.).*


### Structural Quality

- **Quality Score**: 49.17/100

- **Mean Rating**: 4.92/10

- **Std Dev**: 1.26


*Higher rating indicates better structural integrity (no warped walls, misaligned edges, etc.).*


---


## Detailed View Analysis


### View 1 (0°)

![View 1](captured_views/ktv75/view_000_000deg.png)


**VLM Analysis**:

**Score**: 4/10


> *The rendering shows major geometric distortions and depth inconsistencies with severe foreground blur and edge misalignments. Textures are inconsistent and blurred, with ghosting artifacts suggesting imperfect surface fusion. Overall, this resembles a rough reconstruction with limited geometric fidelity to a real scene; not suitable as a reliable 3DGS/NeRF reconstruction without substantial corrections.*


**Detected Issues**:
- ⚠️ **Curved Or Warped Walls**: Large portions of the scene exhibit extreme curvature and warping, especially along the central column-like structure and left foreground, breaking straight-edged geometry.
- ⚠️ **Misaligned Edges**: Edges near the doorway/ledge and couch area do not align coherently with surrounding geometry, creating visible seams.
- ⚠️ **Depth Or Perspective Errors**: Ambiguous depth cues and inconsistent perspective; depth appears flattened or exaggerated in several regions, leading to unreliable spatial relationships.
- 🎨 **Ghosting**: Subtle ghosting around high-contrast edges, likely from multi-view blending artifacts.
- 🎨 **Over Blur**: Significant overall blur, especially in the foreground, reducing texture sharpness and details.
- 🎨 **Texture Inconsistency**: Inconsistent surface textures (mixed matte/shiny patches) without plausible lighting variation.


### View 2 (30°)

![View 2](captured_views/ktv75/view_001_030deg.png)


**VLM Analysis**:

**Score**: 4/10


> *The render shows a heavily distorted interior with significant geometric warping and depth inconsistencies. Textures are blurred and inconsistent, with ghosting artifacts affecting perception. Overall, it is recognizable as a room but far from a reliable photorealistic reconstruction; major structural and texture fidelity issues reduce realism and spatial coherence.*


**Detected Issues**:
- ⚠️ **Curved Or Warped Walls**: Large portions of walls and ceiling show pronounced bending and curving, especially along the left and right edges; geometry appears smeared and non-planar.
- ⚠️ **Misaligned Edges**: Edges between furniture and walls are inconsistent and jagged; vertical/horizontal alignments do not match real-world rectilinear constraints.
- ⚠️ **Depth Or Perspective Errors**: Depth cues are distorted; perspective compression and foreshortening look incorrect in several room regions, reducing spatial coherence.
- 🎨 **Ghosting**: Subtle ghosted outlines around large surfaces and furniture, indicating multi-surface blending artifacts.
- 🎨 **Over Blur**: Excessive blur across most surfaces, masking fine details and causing smeared textures.
- 🎨 **Texture Inconsistency**: Inconsistent surface textures; some areas appear overly smooth while others show irregular, painterly patterns.


### View 3 (60°)

![View 3](captured_views/ktv75/view_002_060deg.png)


**VLM Analysis**:

**Score**: 7/10


> *The scene presents a coherent dining room layout with plausible geometry and depth. Overall structure is solid with minor stylization-induced blur affecting texture sharpness. No major geometric defects observed; slight global smoothing reduces realism but preserves spatial coherence and multi-surface consistency.*


**Detected Issues**:
- 🎨 **Over Blur**: Overall soft, painterly blur across surfaces consistent with stylized rendering; sharp details are reduced.


### View 4 (90°)

![View 4](captured_views/ktv75/view_003_090deg.png)


**VLM Analysis**:

**Score**: 6/10


> *The scene is recognizable as a dining room reconstruction with coherent layout and depth. However, heavy smoothing and inconsistent texture details reduce realism, and there are minor texture coherence issues across surfaces. Geometry remains largely plausible with no obvious structural breaks.*


**Detected Issues**:
- 🎨 **Over Blur**: Overall painterly smoothing reduces fine texture and edge sharpness, giving a soft appearance.
- 🎨 **Texture Inconsistency**: Inconsistent material detail levels across surfaces (e.g., upholstery vs. walls) suggest varying reconstruction fidelity.


### View 5 (120°)

![View 5](captured_views/ktv75/view_004_120deg.png)


**VLM Analysis**:

**Score**: 6/10


> *The rendering shows a plausible room layout with reasonable perspective and object placement, but several geometric and texture inconsistencies reduce realism. Warped/wavy wall regions, slight edge misalignment, and depth inconsistencies detract from structural fidelity. Texture artifacts include painterly blur, high-frequency scribbles, and inconsistent surface textures. Overall realism is moderate; it resembles a real scene but with noticeable reconstruction artifacts that prevent near-photorealistic quality.*


**Detected Issues**:
- ⚠️ **Curved Or Warped Walls**: Subtle warping along left wall and wall panels; some curved contours appear unnaturally bending away from perspective.
- ⚠️ **Misaligned Edges**: Ceiling/edge lines show slight misalignment where wall panels meet ceiling; edges do not perfectly align.
- ⚠️ **Depth Or Perspective Errors**: Depth cues are somewhat inconsistent: foreground table and chairs have exaggerated proximity relative to mid/background objects.
- 🎨 **Floating Artifacts**: High-frequency scribble-like artifacts around surfaces, notably on darker wall area and along edges.
- 🎨 **Over Blur**: Overall softening and painterly blur reduce sharpness of fine textures on furniture and wall details.
- 🎨 **Texture Inconsistency**: Inconsistent texture resolution across surfaces (floor vs walls vs paintings) leading to non-uniform appearance.


### View 6 (150°)

![View 6](captured_views/ktv75/view_005_150deg.png)


**VLM Analysis**:

**Score**: 6/10


> *The rendering presents a recognizable interior layout with plausible geometry and furniture arrangement. However, depth/perspective cues are slightly inconsistent, and texture continuity is variable with noticeable blur and surface inconsistency. Overall realism is moderate, with clear room for improvement in sharpness and geometric alignment.*


**Detected Issues**:
- ⚠️ **Depth Or Perspective Errors**: Subtle perspective and scale inconsistencies around the back wall and chairs, causing a mild sense of depth mismatch.
- 🎨 **Over Blur**: Overall soft focus and motion-like blur reduce sharpness of surfaces (table edges, chair contours).
- 🎨 **Texture Inconsistency**: Inconsistent texture detail across surfaces (wall paneling vs artwork area) leading to non-uniform material appearance.


### View 7 (180°)

![View 7](captured_views/ktv75/view_006_180deg.png)


**VLM Analysis**:

**Score**: 3/10


> *The rendering exhibits strong geometric distortions (curved/wavy walls, misaligned edges, and inconsistent depth) and pervasive texture inconsistencies with excessive blur. These factors collectively yield a scene that is not visually consistent with a real-world room and would be considered a poor reconstruction in terms of geometric fidelity and texture stability.*


**Detected Issues**:
- ⚠️ **Curved Or Warped Walls**: Wavy and distorted wall planes, especially near the central panel and doorway area.
- ⚠️ **Misaligned Edges**: Edges do not align cleanly at wall junctions; noticeable misregistration along the cabinet/door frame and seating area.
- ⚠️ **Depth Or Perspective Errors**: Depth cues are inconsistent; perspective appears warped and objects do not recede or scale realistically.
- 🎨 **Over Blur**: Overall blur and smeared textures reduce detail; surfaces lack sharpness.
- 🎨 **Texture Inconsistency**: Texture quality varies abruptly between surfaces; some areas look washed out or smeared.


### View 8 (210°)

![View 8](captured_views/ktv75/view_007_210deg.png)


**VLM Analysis**:

**Score**: 4/10


> *The rendering exhibits noticeable geometric and texture inconsistencies that undermine realism. Structural cues such as walls and edges are warped or misaligned, depth perception is unreliable, and textures show ghosting and blur. Overall, the scene resembles a distorted reconstruction rather than a faithful real-world capture.*


**Detected Issues**:
- ⚠️ **Curved Or Warped Walls**: Large portions of wall surfaces appear heavily warped and twisted with scribble-like lines across surfaces.
- ⚠️ **Misaligned Edges**: Edges between wall panels and floor/ceiling are inconsistent; boundary lines do not align cleanly.
- ⚠️ **Depth Or Perspective Errors**: Depth cues are unreliable; perspective seems flattened or distorted, causing misinterpretation of room geometry.
- 🎨 **Ghosting**: Repeated or smeared textures across large areas, especially on walls and furniture.
- 🎨 **Over Blur**: Overall surface details are blurry, reducing fidelity of textures (fabric, wood, etc.).
- 🎨 **Texture Inconsistency**: Inconsistent texture density and grain between adjacent surfaces.


### View 9 (240°)

![View 9](captured_views/ktv75/view_008_240deg.png)


**VLM Analysis**:

**Score**: 5/10


> *The rendering shows noticeable geometric and texture inconsistencies: warped/wrinkled surfaces, misaligned edges, and depth-perspective errors. Texture quality is degraded by ghosting and blur, leading to an overall reconstruction that is only partially convincing as a real scene. Improvements needed in surface planarization, depth accuracy, and texture coherence.*


**Detected Issues**:
- ⚠️ **Curved Or Warped Walls**: Multiple curved/wrinkled surfaces on the main cardboard-like plane, suggesting non-planar geometry.
- ⚠️ **Misaligned Edges**: Edges around the vertical white panel and box boundaries appear slightly misaligned or jagged.
- ⚠️ **Depth Or Perspective Errors**: Unnatural perspective foreshortening and inconsistent depth cues across the scene.
- 🎨 **Ghosting**: Numerous fine line artifacts overlaying surfaces, resembling ghost textures.
- 🎨 **Over Blur**: General softening of details, reducing sharpness of edges and textures.
- 🎨 **Texture Inconsistency**: Inconsistent surface textures across adjacent regions (cardboard vs wall) with patchy shading.


### View 10 (270°)

![View 10](captured_views/ktv75/view_009_270deg.png)


**VLM Analysis**:

**Score**: 5/10


> *The rendering shows noticeable geometric inconsistencies and significant texture/artifact issues. Warped walls, misaligned edges, and unreliable depth cues indicate reconstruction problems. Ghosting, floating artifacts, and over-blurred textures reduce realism and spatial coherence, resulting in a reconstruction that is only partially plausible as a real scene.*


**Detected Issues**:
- ⚠️ **Curved Or Warped Walls**: Large-scale warping and bending of wall and corridor surfaces, especially on the right-side box area and doorway regions.
- ⚠️ **Misaligned Edges**: Edges between walls, floor, and ceiling are misaligned with noticeable gaps and irregular junctions.
- ⚠️ **Depth Or Perspective Errors**: Depth cues are inconsistent; perspective foreshortening is unreliable, leading to ambiguous scale and depth.
- 🎨 **Ghosting**: Faint translucent duplicates and ghost-like traces near edges and surfaces.
- 🎨 **Floating Artifacts**: Stray strands or haze-like artifacts float in the scene, not tied to geometry.
- 🎨 **Over Blur**: Extended blur across surfaces reduces fine texture detail.
- 🎨 **Texture Inconsistency**: Inconsistent texture quality between surfaces (varying sharpness and noise) across the scene.


### View 11 (300°)

![View 11](captured_views/ktv75/view_010_300deg.png)


**VLM Analysis**:

**Score**: 4/10


> *The rendering shows pronounced geometric distortion and texture artifacts that degrade structural realism. Curved/warped walls, misaligned edges, depth inconsistencies, and heavy blur indicate a low-to-moderate reconstruction quality with limited spatial fidelity. Not suitable as a faithful real-world scene reconstruction without correction or refinement.*


**Detected Issues**:
- ⚠️ **Curved Or Warped Walls**: Extensive warping and curved distortions across large wall surfaces, including doorway edges.
- ⚠️ **Misaligned Edges**: Edges of door frames and walls do not align cleanly, giving a skewed perspective.
- ⚠️ **Depth Or Perspective Errors**: Inconsistent depth cues and perspective, likely due to global distortion and blur.
- 🎨 **Ghosting**: Subtle ghost outlines and multiple faint echoes around edges.
- 🎨 **Floating Artifacts**: Isolated stray shapes and rings appear detached from surfaces.
- 🎨 **Over Blur**: Significant motion-like blur reduces surface definition.
- 🎨 **Texture Inconsistency**: Textures appear smeared and nonuniform across surfaces.


### View 12 (330°)

![View 12](captured_views/ktv75/view_011_330deg.png)


**VLM Analysis**:

**Score**: 5/10


> *The rendering shows recognizable architectural layout but suffers from notable geometric and texture inconsistencies typical of 3D Gaussian Splatting reconstructions. Structural elements exhibit warped walls and misaligned edges, with depth cues not fully coherent. Texture fidelity is compromised by ghosting, floating artifacts, and over-blur, reducing realism. Overall, the scene is partially plausible but not a faithful reconstruction of a real-world interior.*


**Detected Issues**:
- ⚠️ **Curved Or Warped Walls**: Vertical and horizontal wall planes appear irregular and slightly curved due to heavy stitching/warping, notably along doorway frames.
- ⚠️ **Misaligned Edges**: Door frames and edges do not align perfectly; joints feel offset in several regions.
- ⚠️ **Depth Or Perspective Errors**: Depth cues appear inconsistent; scale and perspective shift between foreground and background surfaces, reducing realism.
- 🎨 **Ghosting**: Subtle ghost-like traces around edges and high-contrast transitions.
- 🎨 **Floating Artifacts**: Sparse stray scribbles/lines that float over surfaces, not tied to geometry.
- 🎨 **Over Blur**: Overall softening blur reduces sharpness of textures and edges.
- 🎨 **Texture Inconsistency**: Inconsistent texture density; some walls look smoother while others show different grain/noise levels.
