# Liftoff sunset: two-pass 8K enhancement

Export: **8192 × 4608**, lossless RGB PNG. Source: the **1672 × 941** native sunset illustration. Both that source and the earlier simple 8K export are preserved byte for byte. The existing wallpaper’s 16:9 framing is retained; the native source has approximate 16:9 dimensions.

This uses two passes of contextual AI crop enhancement rather than only resizing a single image. Painted detail is reconstructed; it is plausible artwork, not recovered photographic information. Native crops are retained at their actual generated dimensions, listed below. Maximum practical native resolution was requested; the built-in editor has no exposed resolution parameter.

Pass 1: nine 3 × 3 core crops, padded by 20% of each core dimension on every side and clipped to the source. Every edit received the unmodified full sunset illustration first and its target crop second. The registered, blended assembly retains the median practical native crop scale, then resizes to 8192 × 4608.

Pass 2: seven padded salient crops from M1: rocket nose, rocket body, tower and exhaust, left smoke volume, right smoke volume, foreground channels, and flame base with vapor. Low-information sky and saturated highlights were excluded as dedicated focal targets. Every edit again received the original complete sunset artwork as context.

Prompts retain violet/indigo shadows, magenta/pink/coral midtones and orange/gold highlights. The original painterly softness and selective crisp edges are preserved; no conversion to photographic texture is requested.

Assembly: bounded global similarity registration using low-frequency correlation. No local deformation of rigid geometry or repeated tower members. Broad exposure/color correction transfers no old fine texture. Normalized overlap blending feathers 20% of interior borders to zero, retains prior pixels at unreliable correspondences, and uses stricter confidence around the rocket and tower. Native generated crops are preserved.

Validation: full image and 100% focal/overlap review before each next pass, full PNG chunk verification and decode, RGB dimensions, source SHA-256 and archive CRC.

## Native edits and source-coordinate boxes

| Edit | Pass | Region | Native dimensions | Source box (x0, y0, x1, y1) | Result |
|---|---:|---|---|---|---|
| p1-01 | 1 | grid-1-1 | 1670 × 942 | [0.0, 0.0, 668.0, 377.0] | accepted |
| p1-02 | 1 | grid-1-2 | 1806 × 871 | [445.0, 0.0, 1227.0, 377.0] | accepted |
| p1-03 | 1 | grid-1-3 | 1670 × 942 | [1004.0, 0.0, 1672.0, 377.0] | accepted |
| p1-04 | 1 | grid-2-1 | 1548 × 1016 | [0.0, 251.0, 668.0, 690.0] | accepted |
| p1-05 | 1 | grid-2-2 | 1674 × 939 | [445.0, 251.0, 1227.0, 690.0] | rejected |
| p1-06 | 1 | grid-2-3 | 1546 × 1017 | [1004.0, 251.0, 1672.0, 690.0] | accepted |
| p1-07 | 1 | grid-3-1 | 1669 × 942 | [0.0, 564.0, 668.0, 941.0] | accepted |
| p1-08 | 1 | grid-3-2 | 1806 × 871 | [445.0, 564.0, 1227.0, 941.0] | accepted |
| p1-09 | 1 | grid-3-3 | 1669 × 942 | [1004.0, 564.0, 1672.0, 941.0] | accepted |
| p2-01 | 2 | rocket-nose | 1026 × 1532 | [758.033, 190.732, 877.024, 368.395] | accepted |
| p2-02 | 2 | rocket-body | 948 × 1659 | [757.217, 278.543, 874.779, 484.386] | rejected |
| p2-03 | 2 | tower-and-exhaust | 1024 × 1536 | [718.233, 409.237, 926.825, 722.699] | accepted |
| p2-04 | 2 | left-smoke-volume | 1336 × 1177 | [51.025, 317.955, 463.923, 682.062] | accepted |
| p2-05 | 2 | right-smoke-volume | 1387 × 1134 | [1098.883, 251.995, 1596.074, 657.965] | accepted |
| p2-06 | 2 | foreground-channels | 1915 × 821 | [493.109, 716.165, 995.812, 931.811] | accepted |
| p2-07 | 2 | flame-base-and-vapor | 1465 × 1073 | [717.417, 584.041, 965.604, 765.992] | accepted |

## Fallbacks and retries

- p1-05: Central crop disagreed with the source rocket geometry and horizon after registration. The initial local box fallback produced a horizon transition at its edge.; After one targeted retry, reject this first-pass crop for remaining rigid-geometry drift. Retain prior source content and reliable overlapping crops; refine rocket/tower in the focal second pass.; targeted retries: 1; retry status: rejected; prior content retained.
- p2-01: The focal nose edit introduced horizontal panel/joint lines not visible in the original sunset artwork.; The targeted retry removed the prominent panel division. Retain prior pixels locally across the remaining faint mid-cylinder joint line, preserving the continuous source surface.; targeted retries: 1; retry status: resolved with targeted retry and local prior-pixel fallback; final 100% review passed.
- p2-05: The editor could not process this PNG target (input decode failed: image file is truncated).; Rebuilt the truncated lossless target from the exact M1 crop box, then retried using a quality-100, subsampling-0 JPEG compatibility copy (1536 × 1254). Full lossless crop retained. Retry generated successfully.; targeted retries: 1; retry status: resolved input; final smoke/overlap review passed.
- p2-02: The first body edit made the painted frost texture too regular and faceted.; The targeted retry reduced the regularity but final 100% review still found faceted painted coating. Reject the body crop and retain prior M1 content with reliable neighboring overlaps.; targeted retries: 1; retry status: rejected after one targeted retry; prior content retained.

## Exact prompts

### p1-01 — grid-1-1

```text
1=original: composition, geometry, painted style, color and light authority. 2=target: return exact crop/framing/geometry. Reconstruct plausible high-resolution painted detail while preserving the original soft digital-painting aesthetic, contours, atmospheric falloff, selective crisp edges and quiet intervals. Retain exactly the violet/indigo shadows, magenta/pink/coral midtones and luminous orange/gold highlights. Repair inherited upscaling artifacts with natural painted transitions and spatially varied detail. Avoid invented structures/marks, relighting, halos, ringing, embossed/crosshatched/repeated texture, synthetic grain, blanket sharpening, photographic conversion or style drift.
Keep the exact painted cloud placements and silhouettes, smooth color gradients and original atmospheric softness. Preserve the sweeping magenta and coral brush-like clouds against violet sky and the golden horizon. No new wisps, stars, streaks or noisy fine grain; smooth low-information sky stays smooth.
Return only image 2, the target crop. Match its entire framing and aspect ratio (668:377), without cropping, borders or returning the full scene. Image 1 is the original complete sunset illustration, supplied as context in every edit. Use maximum practical supported native output resolution, aiming for 3840 pixels on the longest edge if supported. Enhancement of the existing painting only.
```

### p1-02 — grid-1-2

```text
1=original: composition, geometry, painted style, color and light authority. 2=target: return exact crop/framing/geometry. Reconstruct plausible high-resolution painted detail while preserving the original soft digital-painting aesthetic, contours, atmospheric falloff, selective crisp edges and quiet intervals. Retain exactly the violet/indigo shadows, magenta/pink/coral midtones and luminous orange/gold highlights. Repair inherited upscaling artifacts with natural painted transitions and spatially varied detail. Avoid invented structures/marks, relighting, halos, ringing, embossed/crosshatched/repeated texture, synthetic grain, blanket sharpening, photographic conversion or style drift.
Keep the exact painted cloud placements and silhouettes, smooth color gradients and original atmospheric softness. Preserve the sweeping magenta and coral brush-like clouds against violet sky and the golden horizon. No new wisps, stars, streaks or noisy fine grain; smooth low-information sky stays smooth. Keep the exact single slender rocket silhouette, nose and existing small fins, cylinder proportions, flight position and tower lattice. Preserve the existing painted dark and warm-lit surfaces. Do not invent or redesign any fin, ring, panel seam, rivet, marking, hardware, lattice member or launch structure. Geometry and repeated tower members must stay consistent with image 1.
Return only image 2, the target crop. Match its entire framing and aspect ratio (782:377), without cropping, borders or returning the full scene. Image 1 is the original complete sunset illustration, supplied as context in every edit. Use maximum practical supported native output resolution, aiming for 3840 pixels on the longest edge if supported. Enhancement of the existing painting only.
```

### p1-03 — grid-1-3

```text
1=original: composition, geometry, painted style, color and light authority. 2=target: return exact crop/framing/geometry. Reconstruct plausible high-resolution painted detail while preserving the original soft digital-painting aesthetic, contours, atmospheric falloff, selective crisp edges and quiet intervals. Retain exactly the violet/indigo shadows, magenta/pink/coral midtones and luminous orange/gold highlights. Repair inherited upscaling artifacts with natural painted transitions and spatially varied detail. Avoid invented structures/marks, relighting, halos, ringing, embossed/crosshatched/repeated texture, synthetic grain, blanket sharpening, photographic conversion or style drift.
Keep the exact painted cloud placements and silhouettes, smooth color gradients and original atmospheric softness. Preserve the sweeping magenta and coral brush-like clouds against violet sky and the golden horizon. No new wisps, stars, streaks or noisy fine grain; smooth low-information sky stays smooth. Preserve exact irregular smoke-bank contours and lobes, lavender/purple shadows, coral/orange illumination and soft translucent fringes. Add only restrained irregular painted volume consistent with the source; no new lobes, repeated cauliflower/foam texture, crystalline facets or uniformly sharp cloud surfaces.
Return only image 2, the target crop. Match its entire framing and aspect ratio (668:377), without cropping, borders or returning the full scene. Image 1 is the original complete sunset illustration, supplied as context in every edit. Use maximum practical supported native output resolution, aiming for 3840 pixels on the longest edge if supported. Enhancement of the existing painting only.
```

### p1-04 — grid-2-1

```text
1=original: composition, geometry, painted style, color and light authority. 2=target: return exact crop/framing/geometry. Reconstruct plausible high-resolution painted detail while preserving the original soft digital-painting aesthetic, contours, atmospheric falloff, selective crisp edges and quiet intervals. Retain exactly the violet/indigo shadows, magenta/pink/coral midtones and luminous orange/gold highlights. Repair inherited upscaling artifacts with natural painted transitions and spatially varied detail. Avoid invented structures/marks, relighting, halos, ringing, embossed/crosshatched/repeated texture, synthetic grain, blanket sharpening, photographic conversion or style drift.
Preserve exact irregular smoke-bank contours and lobes, lavender/purple shadows, coral/orange illumination and soft translucent fringes. Add only restrained irregular painted volume consistent with the source; no new lobes, repeated cauliflower/foam texture, crystalline facets or uniformly sharp cloud surfaces.
Return only image 2, the target crop. Match its entire framing and aspect ratio (668:439), without cropping, borders or returning the full scene. Image 1 is the original complete sunset illustration, supplied as context in every edit. Use maximum practical supported native output resolution, aiming for 3840 pixels on the longest edge if supported. Enhancement of the existing painting only.
```

### p1-05 — grid-2-2

```text
1=original: composition, geometry, painted style, color and light authority. 2=target: return exact crop/framing/geometry. Reconstruct plausible high-resolution painted detail while preserving the original soft digital-painting aesthetic, contours, atmospheric falloff, selective crisp edges and quiet intervals. Retain exactly the violet/indigo shadows, magenta/pink/coral midtones and luminous orange/gold highlights. Repair inherited upscaling artifacts with natural painted transitions and spatially varied detail. Avoid invented structures/marks, relighting, halos, ringing, embossed/crosshatched/repeated texture, synthetic grain, blanket sharpening, photographic conversion or style drift.
Keep the exact single slender rocket silhouette, nose and existing small fins, cylinder proportions, flight position and tower lattice. Preserve the existing painted dark and warm-lit surfaces. Do not invent or redesign any fin, ring, panel seam, rivet, marking, hardware, lattice member or launch structure. Geometry and repeated tower members must stay consistent with image 1. Keep the original bright creamy-gold/white flame outline, orange spill light, luminous softness and original painted plume boundaries. Smooth saturated highlights stay smooth. No invented sparks, shock diamonds, extra flame tongues or crisp lines inside clipped glare. Keep the exact painted cloud placements and silhouettes, smooth color gradients and original atmospheric softness. Preserve the sweeping magenta and coral brush-like clouds against violet sky and the golden horizon. No new wisps, stars, streaks or noisy fine grain; smooth low-information sky stays smooth.
Return only image 2, the target crop. Match its entire framing and aspect ratio (782:439), without cropping, borders or returning the full scene. Image 1 is the original complete sunset illustration, supplied as context in every edit. Use maximum practical supported native output resolution, aiming for 3840 pixels on the longest edge if supported. Enhancement of the existing painting only.
Targeted geometry correction: copy the exact layout of image 2. Keep the rocket at the exact same horizontal coordinate and width, and the level ocean horizon at the exact same vertical height across the entire crop. The rocket head is cropped off the top in this target; do not move or fit the whole rocket into view. Do not zoom, change perspective, bend the horizon or shift any tower member. Preserve all existing painted cloud and ground boundaries. Reconstruct only detail within those locked shapes.
```

First attempt, before the targeted correction:

```text
1=original: composition, geometry, painted style, color and light authority. 2=target: return exact crop/framing/geometry. Reconstruct plausible high-resolution painted detail while preserving the original soft digital-painting aesthetic, contours, atmospheric falloff, selective crisp edges and quiet intervals. Retain exactly the violet/indigo shadows, magenta/pink/coral midtones and luminous orange/gold highlights. Repair inherited upscaling artifacts with natural painted transitions and spatially varied detail. Avoid invented structures/marks, relighting, halos, ringing, embossed/crosshatched/repeated texture, synthetic grain, blanket sharpening, photographic conversion or style drift.
Keep the exact single slender rocket silhouette, nose and existing small fins, cylinder proportions, flight position and tower lattice. Preserve the existing painted dark and warm-lit surfaces. Do not invent or redesign any fin, ring, panel seam, rivet, marking, hardware, lattice member or launch structure. Geometry and repeated tower members must stay consistent with image 1. Keep the original bright creamy-gold/white flame outline, orange spill light, luminous softness and original painted plume boundaries. Smooth saturated highlights stay smooth. No invented sparks, shock diamonds, extra flame tongues or crisp lines inside clipped glare. Keep the exact painted cloud placements and silhouettes, smooth color gradients and original atmospheric softness. Preserve the sweeping magenta and coral brush-like clouds against violet sky and the golden horizon. No new wisps, stars, streaks or noisy fine grain; smooth low-information sky stays smooth.
Return only image 2, the target crop. Match its entire framing and aspect ratio (782:439), without cropping, borders or returning the full scene. Image 1 is the original complete sunset illustration, supplied as context in every edit. Use maximum practical supported native output resolution, aiming for 3840 pixels on the longest edge if supported. Enhancement of the existing painting only.
```

### p1-06 — grid-2-3

```text
1=original: composition, geometry, painted style, color and light authority. 2=target: return exact crop/framing/geometry. Reconstruct plausible high-resolution painted detail while preserving the original soft digital-painting aesthetic, contours, atmospheric falloff, selective crisp edges and quiet intervals. Retain exactly the violet/indigo shadows, magenta/pink/coral midtones and luminous orange/gold highlights. Repair inherited upscaling artifacts with natural painted transitions and spatially varied detail. Avoid invented structures/marks, relighting, halos, ringing, embossed/crosshatched/repeated texture, synthetic grain, blanket sharpening, photographic conversion or style drift.
Preserve exact irregular smoke-bank contours and lobes, lavender/purple shadows, coral/orange illumination and soft translucent fringes. Add only restrained irregular painted volume consistent with the source; no new lobes, repeated cauliflower/foam texture, crystalline facets or uniformly sharp cloud surfaces.
Return only image 2, the target crop. Match its entire framing and aspect ratio (668:439), without cropping, borders or returning the full scene. Image 1 is the original complete sunset illustration, supplied as context in every edit. Use maximum practical supported native output resolution, aiming for 3840 pixels on the longest edge if supported. Enhancement of the existing painting only.
```

### p1-07 — grid-3-1

```text
1=original: composition, geometry, painted style, color and light authority. 2=target: return exact crop/framing/geometry. Reconstruct plausible high-resolution painted detail while preserving the original soft digital-painting aesthetic, contours, atmospheric falloff, selective crisp edges and quiet intervals. Retain exactly the violet/indigo shadows, magenta/pink/coral midtones and luminous orange/gold highlights. Repair inherited upscaling artifacts with natural painted transitions and spatially varied detail. Avoid invented structures/marks, relighting, halos, ringing, embossed/crosshatched/repeated texture, synthetic grain, blanket sharpening, photographic conversion or style drift.
Keep the exact original winding wetland channels, vegetation islands, muddy track outlines, perspective and pink-orange water reflections. Use restrained irregular painterly material detail, without new roads, tracks, tire patterns, vegetation rows, repeated brush marks or a photographic microtexture. Preserve exact irregular smoke-bank contours and lobes, lavender/purple shadows, coral/orange illumination and soft translucent fringes. Add only restrained irregular painted volume consistent with the source; no new lobes, repeated cauliflower/foam texture, crystalline facets or uniformly sharp cloud surfaces.
Return only image 2, the target crop. Match its entire framing and aspect ratio (668:377), without cropping, borders or returning the full scene. Image 1 is the original complete sunset illustration, supplied as context in every edit. Use maximum practical supported native output resolution, aiming for 3840 pixels on the longest edge if supported. Enhancement of the existing painting only.
```

### p1-08 — grid-3-2

```text
1=original: composition, geometry, painted style, color and light authority. 2=target: return exact crop/framing/geometry. Reconstruct plausible high-resolution painted detail while preserving the original soft digital-painting aesthetic, contours, atmospheric falloff, selective crisp edges and quiet intervals. Retain exactly the violet/indigo shadows, magenta/pink/coral midtones and luminous orange/gold highlights. Repair inherited upscaling artifacts with natural painted transitions and spatially varied detail. Avoid invented structures/marks, relighting, halos, ringing, embossed/crosshatched/repeated texture, synthetic grain, blanket sharpening, photographic conversion or style drift.
Keep the exact original winding wetland channels, vegetation islands, muddy track outlines, perspective and pink-orange water reflections. Use restrained irregular painterly material detail, without new roads, tracks, tire patterns, vegetation rows, repeated brush marks or a photographic microtexture. Keep the original bright creamy-gold/white flame outline, orange spill light, luminous softness and original painted plume boundaries. Smooth saturated highlights stay smooth. No invented sparks, shock diamonds, extra flame tongues or crisp lines inside clipped glare.
Return only image 2, the target crop. Match its entire framing and aspect ratio (782:377), without cropping, borders or returning the full scene. Image 1 is the original complete sunset illustration, supplied as context in every edit. Use maximum practical supported native output resolution, aiming for 3840 pixels on the longest edge if supported. Enhancement of the existing painting only.
```

### p1-09 — grid-3-3

```text
1=original: composition, geometry, painted style, color and light authority. 2=target: return exact crop/framing/geometry. Reconstruct plausible high-resolution painted detail while preserving the original soft digital-painting aesthetic, contours, atmospheric falloff, selective crisp edges and quiet intervals. Retain exactly the violet/indigo shadows, magenta/pink/coral midtones and luminous orange/gold highlights. Repair inherited upscaling artifacts with natural painted transitions and spatially varied detail. Avoid invented structures/marks, relighting, halos, ringing, embossed/crosshatched/repeated texture, synthetic grain, blanket sharpening, photographic conversion or style drift.
Keep the exact original winding wetland channels, vegetation islands, muddy track outlines, perspective and pink-orange water reflections. Use restrained irregular painterly material detail, without new roads, tracks, tire patterns, vegetation rows, repeated brush marks or a photographic microtexture. Preserve exact irregular smoke-bank contours and lobes, lavender/purple shadows, coral/orange illumination and soft translucent fringes. Add only restrained irregular painted volume consistent with the source; no new lobes, repeated cauliflower/foam texture, crystalline facets or uniformly sharp cloud surfaces.
Return only image 2, the target crop. Match its entire framing and aspect ratio (668:377), without cropping, borders or returning the full scene. Image 1 is the original complete sunset illustration, supplied as context in every edit. Use maximum practical supported native output resolution, aiming for 3840 pixels on the longest edge if supported. Enhancement of the existing painting only.
```

### p2-01 — rocket-nose

```text
1=original: composition, geometry, painted style, color and light authority. 2=target: return exact crop/framing/geometry. Reconstruct plausible high-resolution painted detail while preserving the original soft digital-painting aesthetic, contours, atmospheric falloff, selective crisp edges and quiet intervals. Retain exactly the violet/indigo shadows, magenta/pink/coral midtones and luminous orange/gold highlights. Repair inherited upscaling artifacts with natural painted transitions and spatially varied detail. Avoid invented structures/marks, relighting, halos, ringing, embossed/crosshatched/repeated texture, synthetic grain, blanket sharpening, photographic conversion or style drift.
Keep the exact single slender rocket silhouette, nose and existing small fins, cylinder proportions, flight position and tower lattice. Preserve the existing painted dark and warm-lit surfaces. Do not invent or redesign any fin, ring, panel seam, rivet, marking, hardware, lattice member or launch structure. Geometry and repeated tower members must stay consistent with image 1. Keep the exact painted cloud placements and silhouettes, smooth color gradients and original atmospheric softness. Preserve the sweeping magenta and coral brush-like clouds against violet sky and the golden horizon. No new wisps, stars, streaks or noisy fine grain; smooth low-information sky stays smooth.
Return only image 2, the target crop. Match its entire framing and aspect ratio (583:870), without cropping, borders or returning the full scene. Image 1 is the original complete sunset illustration, supplied as context in every edit. Use maximum practical supported native output resolution, aiming for 3840 pixels on the longest edge if supported. Enhancement of the existing painting only.
Targeted correction: the long dark upper rocket cylinder in image 2 is a continuous smooth painted surface. Keep it continuous and remove any invented horizontal panel seam, circumferential joint line, groove, band or extra section division anywhere within that dark surface. Preserve only the original neck transition at its bottom and the existing small crossbars below it. Do not introduce a new boundary under the pointed nose. Retain the original painted finish and subtle reflected sunset light, without an outlined polished-metal redesign. Keep the exact silhouette and fin geometry of image 2.
```

First attempt, before the targeted correction:

```text
1=original: composition, geometry, painted style, color and light authority. 2=target: return exact crop/framing/geometry. Reconstruct plausible high-resolution painted detail while preserving the original soft digital-painting aesthetic, contours, atmospheric falloff, selective crisp edges and quiet intervals. Retain exactly the violet/indigo shadows, magenta/pink/coral midtones and luminous orange/gold highlights. Repair inherited upscaling artifacts with natural painted transitions and spatially varied detail. Avoid invented structures/marks, relighting, halos, ringing, embossed/crosshatched/repeated texture, synthetic grain, blanket sharpening, photographic conversion or style drift.
Keep the exact single slender rocket silhouette, nose and existing small fins, cylinder proportions, flight position and tower lattice. Preserve the existing painted dark and warm-lit surfaces. Do not invent or redesign any fin, ring, panel seam, rivet, marking, hardware, lattice member or launch structure. Geometry and repeated tower members must stay consistent with image 1. Keep the exact painted cloud placements and silhouettes, smooth color gradients and original atmospheric softness. Preserve the sweeping magenta and coral brush-like clouds against violet sky and the golden horizon. No new wisps, stars, streaks or noisy fine grain; smooth low-information sky stays smooth.
Return only image 2, the target crop. Match its entire framing and aspect ratio (583:870), without cropping, borders or returning the full scene. Image 1 is the original complete sunset illustration, supplied as context in every edit. Use maximum practical supported native output resolution, aiming for 3840 pixels on the longest edge if supported. Enhancement of the existing painting only.
```

### p2-02 — rocket-body

```text
1=original: composition, geometry, painted style, color and light authority. 2=target: return exact crop/framing/geometry. Reconstruct plausible high-resolution painted detail while preserving the original soft digital-painting aesthetic, contours, atmospheric falloff, selective crisp edges and quiet intervals. Retain exactly the violet/indigo shadows, magenta/pink/coral midtones and luminous orange/gold highlights. Repair inherited upscaling artifacts with natural painted transitions and spatially varied detail. Avoid invented structures/marks, relighting, halos, ringing, embossed/crosshatched/repeated texture, synthetic grain, blanket sharpening, photographic conversion or style drift.
Keep the exact single slender rocket silhouette, nose and existing small fins, cylinder proportions, flight position and tower lattice. Preserve the existing painted dark and warm-lit surfaces. Do not invent or redesign any fin, ring, panel seam, rivet, marking, hardware, lattice member or launch structure. Geometry and repeated tower members must stay consistent with image 1.
Return only image 2, the target crop. Match its entire framing and aspect ratio (576:1008), without cropping, borders or returning the full scene. Image 1 is the original complete sunset illustration, supplied as context in every edit. Use maximum practical supported native output resolution, aiming for 3840 pixels on the longest edge if supported. Enhancement of the existing painting only.
Targeted material correction: the pale coating on the rocket body is irregular soft painted frost, with uneven patches and quiet intervals. Preserve its exact original outer contour and coverage. Do not render it as scales, diamonds, lozenges, hexagons, facets, crystalline tessellation, embossing or repeated diagonal brush stamps. Resolve only subtle nonrepeating painted transitions. Keep the dark upper cylinder smooth and continuous, with no new horizontal panel lines or extra section joints. The unchanged target geometry remains authoritative.
```

First attempt, before the targeted correction:

```text
1=original: composition, geometry, painted style, color and light authority. 2=target: return exact crop/framing/geometry. Reconstruct plausible high-resolution painted detail while preserving the original soft digital-painting aesthetic, contours, atmospheric falloff, selective crisp edges and quiet intervals. Retain exactly the violet/indigo shadows, magenta/pink/coral midtones and luminous orange/gold highlights. Repair inherited upscaling artifacts with natural painted transitions and spatially varied detail. Avoid invented structures/marks, relighting, halos, ringing, embossed/crosshatched/repeated texture, synthetic grain, blanket sharpening, photographic conversion or style drift.
Keep the exact single slender rocket silhouette, nose and existing small fins, cylinder proportions, flight position and tower lattice. Preserve the existing painted dark and warm-lit surfaces. Do not invent or redesign any fin, ring, panel seam, rivet, marking, hardware, lattice member or launch structure. Geometry and repeated tower members must stay consistent with image 1.
Return only image 2, the target crop. Match its entire framing and aspect ratio (576:1008), without cropping, borders or returning the full scene. Image 1 is the original complete sunset illustration, supplied as context in every edit. Use maximum practical supported native output resolution, aiming for 3840 pixels on the longest edge if supported. Enhancement of the existing painting only.
```

### p2-03 — tower-and-exhaust

```text
1=original: composition, geometry, painted style, color and light authority. 2=target: return exact crop/framing/geometry. Reconstruct plausible high-resolution painted detail while preserving the original soft digital-painting aesthetic, contours, atmospheric falloff, selective crisp edges and quiet intervals. Retain exactly the violet/indigo shadows, magenta/pink/coral midtones and luminous orange/gold highlights. Repair inherited upscaling artifacts with natural painted transitions and spatially varied detail. Avoid invented structures/marks, relighting, halos, ringing, embossed/crosshatched/repeated texture, synthetic grain, blanket sharpening, photographic conversion or style drift.
Keep the exact single slender rocket silhouette, nose and existing small fins, cylinder proportions, flight position and tower lattice. Preserve the existing painted dark and warm-lit surfaces. Do not invent or redesign any fin, ring, panel seam, rivet, marking, hardware, lattice member or launch structure. Geometry and repeated tower members must stay consistent with image 1. Keep the original bright creamy-gold/white flame outline, orange spill light, luminous softness and original painted plume boundaries. Smooth saturated highlights stay smooth. No invented sparks, shock diamonds, extra flame tongues or crisp lines inside clipped glare.
Return only image 2, the target crop. Match its entire framing and aspect ratio (1022:1535), without cropping, borders or returning the full scene. Image 1 is the original complete sunset illustration, supplied as context in every edit. Use maximum practical supported native output resolution, aiming for 3840 pixels on the longest edge if supported. Enhancement of the existing painting only.
```

### p2-04 — left-smoke-volume

```text
1=original: composition, geometry, painted style, color and light authority. 2=target: return exact crop/framing/geometry. Reconstruct plausible high-resolution painted detail while preserving the original soft digital-painting aesthetic, contours, atmospheric falloff, selective crisp edges and quiet intervals. Retain exactly the violet/indigo shadows, magenta/pink/coral midtones and luminous orange/gold highlights. Repair inherited upscaling artifacts with natural painted transitions and spatially varied detail. Avoid invented structures/marks, relighting, halos, ringing, embossed/crosshatched/repeated texture, synthetic grain, blanket sharpening, photographic conversion or style drift.
Preserve exact irregular smoke-bank contours and lobes, lavender/purple shadows, coral/orange illumination and soft translucent fringes. Add only restrained irregular painted volume consistent with the source; no new lobes, repeated cauliflower/foam texture, crystalline facets or uniformly sharp cloud surfaces.
Return only image 2, the target crop. Match its entire framing and aspect ratio (2023:1783), without cropping, borders or returning the full scene. Image 1 is the original complete sunset illustration, supplied as context in every edit. Use maximum practical supported native output resolution, aiming for 3840 pixels on the longest edge if supported. Enhancement of the existing painting only.
```

### p2-05 — right-smoke-volume

```text
1=original: composition, geometry, painted style, color and light authority. 2=target: return exact crop/framing/geometry. Reconstruct plausible high-resolution painted detail while preserving the original soft digital-painting aesthetic, contours, atmospheric falloff, selective crisp edges and quiet intervals. Retain exactly the violet/indigo shadows, magenta/pink/coral midtones and luminous orange/gold highlights. Repair inherited upscaling artifacts with natural painted transitions and spatially varied detail. Avoid invented structures/marks, relighting, halos, ringing, embossed/crosshatched/repeated texture, synthetic grain, blanket sharpening, photographic conversion or style drift.
Preserve exact irregular smoke-bank contours and lobes, lavender/purple shadows, coral/orange illumination and soft translucent fringes. Add only restrained irregular painted volume consistent with the source; no new lobes, repeated cauliflower/foam texture, crystalline facets or uniformly sharp cloud surfaces.
Return only image 2, the target crop. Match its entire framing and aspect ratio (2436:1988), without cropping, borders or returning the full scene. Image 1 is the original complete sunset illustration, supplied as context in every edit. Use maximum practical supported native output resolution, aiming for 3840 pixels on the longest edge if supported. Enhancement of the existing painting only.
Image 2 is a high-quality JPEG compatibility copy of the exact same recorded target framing. Preserve its full crop and all source geometry, palette and painted texture. Return only that target at maximum practical native resolution.
```

First attempt, before the targeted correction:

```text
1=original: composition, geometry, painted style, color and light authority. 2=target: return exact crop/framing/geometry. Reconstruct plausible high-resolution painted detail while preserving the original soft digital-painting aesthetic, contours, atmospheric falloff, selective crisp edges and quiet intervals. Retain exactly the violet/indigo shadows, magenta/pink/coral midtones and luminous orange/gold highlights. Repair inherited upscaling artifacts with natural painted transitions and spatially varied detail. Avoid invented structures/marks, relighting, halos, ringing, embossed/crosshatched/repeated texture, synthetic grain, blanket sharpening, photographic conversion or style drift.
Preserve exact irregular smoke-bank contours and lobes, lavender/purple shadows, coral/orange illumination and soft translucent fringes. Add only restrained irregular painted volume consistent with the source; no new lobes, repeated cauliflower/foam texture, crystalline facets or uniformly sharp cloud surfaces.
Return only image 2, the target crop. Match its entire framing and aspect ratio (2436:1988), without cropping, borders or returning the full scene. Image 1 is the original complete sunset illustration, supplied as context in every edit. Use maximum practical supported native output resolution, aiming for 3840 pixels on the longest edge if supported. Enhancement of the existing painting only.
```

### p2-06 — foreground-channels

```text
1=original: composition, geometry, painted style, color and light authority. 2=target: return exact crop/framing/geometry. Reconstruct plausible high-resolution painted detail while preserving the original soft digital-painting aesthetic, contours, atmospheric falloff, selective crisp edges and quiet intervals. Retain exactly the violet/indigo shadows, magenta/pink/coral midtones and luminous orange/gold highlights. Repair inherited upscaling artifacts with natural painted transitions and spatially varied detail. Avoid invented structures/marks, relighting, halos, ringing, embossed/crosshatched/repeated texture, synthetic grain, blanket sharpening, photographic conversion or style drift.
Keep the exact original winding wetland channels, vegetation islands, muddy track outlines, perspective and pink-orange water reflections. Use restrained irregular painterly material detail, without new roads, tracks, tire patterns, vegetation rows, repeated brush marks or a photographic microtexture.
Return only image 2, the target crop. Match its entire framing and aspect ratio (2463:1056), without cropping, borders or returning the full scene. Image 1 is the original complete sunset illustration, supplied as context in every edit. Use maximum practical supported native output resolution, aiming for 3840 pixels on the longest edge if supported. Enhancement of the existing painting only.
```

### p2-07 — flame-base-and-vapor

```text
1=original: composition, geometry, painted style, color and light authority. 2=target: return exact crop/framing/geometry. Reconstruct plausible high-resolution painted detail while preserving the original soft digital-painting aesthetic, contours, atmospheric falloff, selective crisp edges and quiet intervals. Retain exactly the violet/indigo shadows, magenta/pink/coral midtones and luminous orange/gold highlights. Repair inherited upscaling artifacts with natural painted transitions and spatially varied detail. Avoid invented structures/marks, relighting, halos, ringing, embossed/crosshatched/repeated texture, synthetic grain, blanket sharpening, photographic conversion or style drift.
Keep the original bright creamy-gold/white flame outline, orange spill light, luminous softness and original painted plume boundaries. Smooth saturated highlights stay smooth. No invented sparks, shock diamonds, extra flame tongues or crisp lines inside clipped glare. Preserve exact irregular smoke-bank contours and lobes, lavender/purple shadows, coral/orange illumination and soft translucent fringes. Add only restrained irregular painted volume consistent with the source; no new lobes, repeated cauliflower/foam texture, crystalline facets or uniformly sharp cloud surfaces.
Return only image 2, the target crop. Match its entire framing and aspect ratio (1216:891), without cropping, borders or returning the full scene. Image 1 is the original complete sunset illustration, supplied as context in every edit. Use maximum practical supported native output resolution, aiming for 3840 pixels on the longest edge if supported. Enhancement of the existing painting only.
```
