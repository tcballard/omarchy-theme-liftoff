# Starship ascent: original-colour 8K enhancement

Wallpaper: `backgrounds/04-starship-ascent.png`. Approved export: `starship-original-8k.png`, supplied by Tom Ballard on 10 October 2026. The wallpaper contains identical decoded pixels, with its lossless PNG encoding optimised for distribution.

Export: **8192 × 4667**, lossless, opaque, 8-bit RGB PNG with embedded sRGB profile. Source: **4044 × 2304** JPEG. Source aspect ratio is preserved to the nearest pixel; original daytime colours are retained. The original JPEG is preserved outside the theme release tree.

Two contextual AI crop-enhancement passes were completed. Fine detail is reconstructed and may differ from real hardware or terrain. The final dimensions describe the assembled export, not native 8K generation or recovery of hidden original information.

## Passes and settings

Pass 1: nine 3 × 3 grid cores, padded by 20% of each core dimension and clipped to the source. Every edit received the full original photograph and its target crop. All nine were accepted with local confidence fallbacks. Assembly retained the 4044 × 2304 source resolution before proportional resizing to 8K.

Pass 2: four focal targets from the first-pass 8K master: ship, booster, plume and coastline. Each edit again received the full original photograph as context. Three were accepted. The booster output was 724 × 2172, inconsistent with its 511 × 1701 target proportions; it was rejected in full and pass 1 pixels were retained. No generation retries were made.

The built-in image editor was used with `transparent_background: false` and two local image references per crop: full original context first, target second. Maximum practical native resolution was requested in each prompt; there is no exposed resolution setting. Actual generated dimensions are listed below.

Assembly used low-frequency correlation and bounded global similarity registration: scale 0.98–1.02, rotation within ±0.4°, translation within ±4% of the target dimensions. No local geometry deformation was applied. Low-frequency colour correction was capped at 22 sRGB code values per channel. Normalized blending used local confidence masks, strict high-contrast edge agreement, a prior-pixel fallback and 20% feathering at interior crop boundaries.

Full-image and actual 100% focal/overlap review was performed before final export. PNG signature, every chunk CRC, complete decode, exact dimensions, source hash and final hash passed verification. Areas using prior pixels remain softer at 100%. Live Omarchy display, portrait/ultrawide crops and lock controls were not tested in this environment.

The repository PNG uses adaptive scanline filtering and compression level 9. This lossless encoding reduces the file from 47,162,495 to 21,682,266 bytes. All decoded RGB bytes and the source sRGB ICC profile are preserved; the supplied export remains unchanged outside the repository.

| Image | SHA-256 |
| --- | --- |
| Original JPEG | e1150bcfda0580a91ff4e907c14fdfac56580dca37bd3ff16cd7822b28fa3271 |
| Approved export | f967d5ccdb03f18b345521c6ab981c5c0162062cbccb37f20be860604aac704f |
| Repository wallpaper | a764bfa96479b950499a2536087e8b70ba3326a7c6b10123767841461aa9459f |
| Decoded RGB pixels (both PNGs) | df95fd3802d1fae34f9cfbe5b725574f1a7c9d30ae386913bd89673379365d4c |

## Actual native edits

| Edit | Generated dimensions | Result |
| --- | --- | --- |
| p1-r1c2 | 1794 × 877 | accepted with local prior-pixel fallback |
| p1-r2c2 | 1661 × 947 | accepted with local prior-pixel fallback |
| p1-r1c1 | 1661 × 947 | accepted with local prior-pixel fallback |
| p1-r1c3 | 1661 × 947 | accepted with local prior-pixel fallback |
| p1-r2c1 | 1537 × 1023 | accepted with local prior-pixel fallback |
| p1-r2c3 | 1537 × 1023 | accepted with local prior-pixel fallback |
| p1-r3c1 | 1661 × 947 | accepted with local prior-pixel fallback |
| p1-r3c2 | 1794 × 876 | accepted with local prior-pixel fallback |
| p1-r3c3 | 1661 × 947 | accepted with local prior-pixel fallback |
| p2-ship | 890 × 1768 | accepted with local prior-pixel fallback |
| p2-booster | 724 × 2172 | rejected; pass 1 pixels retained |
| p2-plume | 753 × 2089 | accepted with local prior-pixel fallback |
| p2-coast | 1742 × 903 | accepted with local prior-pixel fallback |

## Exact prompts

### p1-r1c2

```text
1=original: composition, rigid geometry, color and light authority. 2=target: return exact crop/framing/geometry. Reconstruct plausible photographic detail with optical clarity, natural edge transitions and spatially varied texture, preserving the photographic character and focus falloff. Repair inherited JPEG artifacts. Avoid invented structures/marks, relighting, halos, ringing, embossed/crosshatched/repeated texture, synthetic grain or blanket sharpening. Rigid objects: preserve silhouette, proportions and existing hardware exactly; do not invent fins, rings, panel seams, rivets, lattice members, vents, lettering or markings. Clouds: preserve exact irregular contours/lobes and soft translucent fringes; no new cloud lobes, cauliflower texture or uniformly sharp edges. Frost: preserve the irregular white surface accumulation and underlying dark vertical streaks; no invented embossed pattern. Flame/glare: preserve outline, spill, luminous softness and plume boundaries; highlights stay smooth, no invented shock diamonds/sparks.
Return only image 2, the target crop, matching its entire framing and aspect ratio 1888:922, without borders, reframing or returning the full scene. Image 1 is the complete original supplied as context. Request maximum practical native resolution, 3072 pixels wide if supported. Enhance the existing image only; retain original colors/light. This region includes the rocket; all its rigid edges and hardware must remain aligned to image 2.
```

### p1-r2c2

```text
1=original: composition, rigid geometry, color and light authority. 2=target: return exact crop/framing/geometry. Reconstruct plausible photographic detail with optical clarity, natural edge transitions and spatially varied texture, preserving the photographic character and focus falloff. Repair inherited JPEG artifacts. Avoid invented structures/marks, relighting, halos, ringing, embossed/crosshatched/repeated texture, synthetic grain or blanket sharpening. Rigid objects: preserve silhouette, proportions and existing hardware exactly; do not invent fins, rings, panel seams, rivets, lattice members, vents, lettering or markings. Clouds: preserve exact irregular contours/lobes and soft translucent fringes; no new cloud lobes, cauliflower texture or uniformly sharp edges. Frost: preserve the irregular white surface accumulation and underlying dark vertical streaks; no invented embossed pattern. Flame/glare: preserve outline, spill, luminous softness and plume boundaries; highlights stay smooth, no invented shock diamonds/sparks.
Return only image 2, the target crop, matching its entire framing and aspect ratio 1888:1076, without borders, reframing or returning the full scene. Image 1 is the complete original supplied as context. Request maximum practical native resolution, 3072 pixels wide if supported. Enhance the existing image only; retain original colors/light. This region includes the rocket; all its rigid edges and hardware must remain aligned to image 2.
```

### p1-r1c1

```text
1=original: composition, rigid geometry, color and light authority. 2=target: return exact crop/framing/geometry. Reconstruct plausible photographic detail with optical clarity, natural edge transitions and spatially varied texture, preserving the photographic character and focus falloff. Repair inherited JPEG artifacts. Avoid invented structures/marks, relighting, halos, ringing, embossed/crosshatched/repeated texture, synthetic grain or blanket sharpening. Rigid objects: preserve silhouette, proportions and existing hardware exactly; do not invent fins, rings, panel seams, rivets, lattice members, vents, lettering or markings. Clouds: preserve exact irregular contours/lobes and soft translucent fringes; no new cloud lobes, cauliflower texture or uniformly sharp edges. Frost: preserve the irregular white surface accumulation and underlying dark vertical streaks; no invented embossed pattern. Flame/glare: preserve outline, spill, luminous softness and plume boundaries; highlights stay smooth, no invented shock diamonds/sparks.
Retain the quiet blue sky and exact wispy cloud/contrail patterns. Do not add cloud wisps or make calm sky busy.
Return only image 2, the target crop, matching its entire framing and aspect ratio 1618:922, without borders, reframing or returning the full scene. Image 1 is the complete original supplied as context. Use maximum practical supported native resolution (3072 pixels wide requested if supported). Enhance the existing image only, preserving original colors and daylight exposure.
```

### p1-r1c3

```text
1=original: composition, rigid geometry, color and light authority. 2=target: return exact crop/framing/geometry. Reconstruct plausible photographic detail with optical clarity, natural edge transitions and spatially varied texture, preserving the photographic character and focus falloff. Repair inherited JPEG artifacts. Avoid invented structures/marks, relighting, halos, ringing, embossed/crosshatched/repeated texture, synthetic grain or blanket sharpening. Rigid objects: preserve silhouette, proportions and existing hardware exactly; do not invent fins, rings, panel seams, rivets, lattice members, vents, lettering or markings. Clouds: preserve exact irregular contours/lobes and soft translucent fringes; no new cloud lobes, cauliflower texture or uniformly sharp edges. Frost: preserve the irregular white surface accumulation and underlying dark vertical streaks; no invented embossed pattern. Flame/glare: preserve outline, spill, luminous softness and plume boundaries; highlights stay smooth, no invented shock diamonds/sparks.
Retain the quiet blue sky and exact wispy cloud/contrail patterns. Do not add cloud wisps or make calm sky busy.
Return only image 2, the target crop, matching its entire framing and aspect ratio 1618:922, without borders, reframing or returning the full scene. Image 1 is the complete original supplied as context. Use maximum practical supported native resolution (3072 pixels wide requested if supported). Enhance the existing image only, preserving original colors and daylight exposure.
```

### p1-r2c1

```text
1=original: composition, rigid geometry, color and light authority. 2=target: return exact crop/framing/geometry. Reconstruct plausible photographic detail with optical clarity, natural edge transitions and spatially varied texture, preserving the photographic character and focus falloff. Repair inherited JPEG artifacts. Avoid invented structures/marks, relighting, halos, ringing, embossed/crosshatched/repeated texture, synthetic grain or blanket sharpening. Rigid objects: preserve silhouette, proportions and existing hardware exactly; do not invent fins, rings, panel seams, rivets, lattice members, vents, lettering or markings. Clouds: preserve exact irregular contours/lobes and soft translucent fringes; no new cloud lobes, cauliflower texture or uniformly sharp edges. Frost: preserve the irregular white surface accumulation and underlying dark vertical streaks; no invented embossed pattern. Flame/glare: preserve outline, spill, luminous softness and plume boundaries; highlights stay smooth, no invented shock diamonds/sparks.
Preserve the exact large cloud shapes, lighting, volume and softness; avoid over-sharpening or excessive tiny lobes.
Return only image 2, the target crop, matching its entire framing and aspect ratio 1618:1076, without borders, reframing or returning the full scene. Image 1 is the complete original supplied as context. Use maximum practical supported native resolution (3072 pixels wide requested if supported). Enhance the existing image only, preserving original colors and daylight exposure.
```

### p1-r2c3

```text
1=original: composition, rigid geometry, color and light authority. 2=target: return exact crop/framing/geometry. Reconstruct plausible photographic detail with optical clarity, natural edge transitions and spatially varied texture, preserving the photographic character and focus falloff. Repair inherited JPEG artifacts. Avoid invented structures/marks, relighting, halos, ringing, embossed/crosshatched/repeated texture, synthetic grain or blanket sharpening. Rigid objects: preserve silhouette, proportions and existing hardware exactly; do not invent fins, rings, panel seams, rivets, lattice members, vents, lettering or markings. Clouds: preserve exact irregular contours/lobes and soft translucent fringes; no new cloud lobes, cauliflower texture or uniformly sharp edges. Frost: preserve the irregular white surface accumulation and underlying dark vertical streaks; no invented embossed pattern. Flame/glare: preserve outline, spill, luminous softness and plume boundaries; highlights stay smooth, no invented shock diamonds/sparks.
Preserve the exact large cloud shapes, lighting, volume and softness; avoid over-sharpening or excessive tiny lobes.
Return only image 2, the target crop, matching its entire framing and aspect ratio 1618:1076, without borders, reframing or returning the full scene. Image 1 is the complete original supplied as context. Use maximum practical supported native resolution (3072 pixels wide requested if supported). Enhance the existing image only, preserving original colors and daylight exposure.
```

### p1-r3c1

```text
1=original: composition, rigid geometry, color and light authority. 2=target: return exact crop/framing/geometry. Reconstruct plausible photographic detail with optical clarity, natural edge transitions and spatially varied texture, preserving the photographic character and focus falloff. Repair inherited JPEG artifacts. Avoid invented structures/marks, relighting, halos, ringing, embossed/crosshatched/repeated texture, synthetic grain or blanket sharpening. Rigid objects: preserve silhouette, proportions and existing hardware exactly; do not invent fins, rings, panel seams, rivets, lattice members, vents, lettering or markings. Clouds: preserve exact irregular contours/lobes and soft translucent fringes; no new cloud lobes, cauliflower texture or uniformly sharp edges. Frost: preserve the irregular white surface accumulation and underlying dark vertical streaks; no invented embossed pattern. Flame/glare: preserve outline, spill, luminous softness and plume boundaries; highlights stay smooth, no invented shock diamonds/sparks.
Landscape/water: exact terrain, lagoon, channel, coastline, road outlines, perspective and reflections. Do not invent tracks, structures, vegetation rows, repeated marks, shore details or buildings. Flame stays luminous and soft with its exact outline; no new sparks or shock diamonds.
Return only image 2, the target crop, matching its entire framing and aspect ratio 1618:922, without borders, reframing or returning the full scene. Image 1 is the complete original supplied as context. Use maximum practical supported native resolution (3072 pixels wide requested if supported). Enhance the existing image only, preserving original colors and daylight exposure.
```

### p1-r3c2

```text
1=original: composition, rigid geometry, color and light authority. 2=target: return exact crop/framing/geometry. Reconstruct plausible photographic detail with optical clarity, natural edge transitions and spatially varied texture, preserving the photographic character and focus falloff. Repair inherited JPEG artifacts. Avoid invented structures/marks, relighting, halos, ringing, embossed/crosshatched/repeated texture, synthetic grain or blanket sharpening. Rigid objects: preserve silhouette, proportions and existing hardware exactly; do not invent fins, rings, panel seams, rivets, lattice members, vents, lettering or markings. Clouds: preserve exact irregular contours/lobes and soft translucent fringes; no new cloud lobes, cauliflower texture or uniformly sharp edges. Frost: preserve the irregular white surface accumulation and underlying dark vertical streaks; no invented embossed pattern. Flame/glare: preserve outline, spill, luminous softness and plume boundaries; highlights stay smooth, no invented shock diamonds/sparks.
Landscape/water: exact terrain, lagoon, channel, coastline, road outlines, perspective and reflections. Do not invent tracks, structures, vegetation rows, repeated marks, shore details or buildings. Flame stays luminous and soft with its exact outline; no new sparks or shock diamonds.
Return only image 2, the target crop, matching its entire framing and aspect ratio 1888:922, without borders, reframing or returning the full scene. Image 1 is the complete original supplied as context. Use maximum practical supported native resolution (3072 pixels wide requested if supported). Enhance the existing image only, preserving original colors and daylight exposure.
```

### p1-r3c3

```text
1=original: composition, rigid geometry, color and light authority. 2=target: return exact crop/framing/geometry. Reconstruct plausible photographic detail with optical clarity, natural edge transitions and spatially varied texture, preserving the photographic character and focus falloff. Repair inherited JPEG artifacts. Avoid invented structures/marks, relighting, halos, ringing, embossed/crosshatched/repeated texture, synthetic grain or blanket sharpening. Rigid objects: preserve silhouette, proportions and existing hardware exactly; do not invent fins, rings, panel seams, rivets, lattice members, vents, lettering or markings. Clouds: preserve exact irregular contours/lobes and soft translucent fringes; no new cloud lobes, cauliflower texture or uniformly sharp edges. Frost: preserve the irregular white surface accumulation and underlying dark vertical streaks; no invented embossed pattern. Flame/glare: preserve outline, spill, luminous softness and plume boundaries; highlights stay smooth, no invented shock diamonds/sparks.
Landscape/water: exact terrain, lagoon, channel, coastline, road outlines, perspective and reflections. Do not invent tracks, structures, vegetation rows, repeated marks, shore details or buildings. Flame stays luminous and soft with its exact outline; no new sparks or shock diamonds.
Return only image 2, the target crop, matching its entire framing and aspect ratio 1618:922, without borders, reframing or returning the full scene. Image 1 is the complete original supplied as context. Use maximum practical supported native resolution (3072 pixels wide requested if supported). Enhance the existing image only, preserving original colors and daylight exposure.
```

### p2-ship

```text
1=original: composition, rigid geometry, color and light authority. 2=target: return exact crop/framing/geometry. Reconstruct plausible photographic detail with optical clarity, natural edge transitions and spatially varied texture, preserving the photographic character and focus falloff. Repair inherited JPEG artifacts. Avoid invented structures/marks, relighting, halos, ringing, embossed/crosshatched/repeated texture, synthetic grain or blanket sharpening. Rigid objects: preserve silhouette, proportions and existing hardware exactly; do not invent fins, rings, panel seams, rivets, lattice members, vents, lettering or markings. Clouds: preserve exact irregular contours/lobes and soft translucent fringes; no new cloud lobes, cauliflower texture or uniformly sharp edges. Frost: preserve the irregular white surface accumulation and underlying dark vertical streaks; no invented embossed pattern. Flame/glare: preserve outline, spill, luminous softness and plume boundaries; highlights stay smooth, no invented shock diamonds/sparks.
Rigid ship: preserve its exact contour, original forward/aft flap shapes, existing interstage lattice and original visible markings only. Reconstruct subtle irregular charred metal tones, with quiet smooth intervals; do not create new seams, rivets, mesh, tile patterns or lettering. Correct inherited doubled/haloed rigid edges if present.
Image 1 is the complete original source, supplied as photographic/context, color and geometry authority. Image 2 is a visually selected focal crop from the first enhancement pass. Return only image 2, matching its entire framing and aspect ratio 750:1489, without borders, zooming, reframing or returning the full scene. Improve plausible local photographic detail and repair inherited artifacts while retaining all source features. Use maximum practical supported native resolution (3072 on longest edge requested if supported). Retain original color and light.
```

### p2-booster

```text
1=original: composition, rigid geometry, color and light authority. 2=target: return exact crop/framing/geometry. Reconstruct plausible photographic detail with optical clarity, natural edge transitions and spatially varied texture, preserving the photographic character and focus falloff. Repair inherited JPEG artifacts. Avoid invented structures/marks, relighting, halos, ringing, embossed/crosshatched/repeated texture, synthetic grain or blanket sharpening. Rigid objects: preserve silhouette, proportions and existing hardware exactly; do not invent fins, rings, panel seams, rivets, lattice members, vents, lettering or markings. Clouds: preserve exact irregular contours/lobes and soft translucent fringes; no new cloud lobes, cauliflower texture or uniformly sharp edges. Frost: preserve the irregular white surface accumulation and underlying dark vertical streaks; no invented embossed pattern. Flame/glare: preserve outline, spill, luminous softness and plume boundaries; highlights stay smooth, no invented shock diamonds/sparks.
Frosted booster: retain existing hardware, dimensions, silhouette and dark vertical exposed patches. Improve the irregular accumulated frost naturally, not into embossed faceted patterns. Keep its porous, soft, uneven texture and its original warm daylight. No new rivets, ribs, fins or metal rings.
Image 1 is the complete original source, supplied as photographic/context, color and geometry authority. Image 2 is a visually selected focal crop from the first enhancement pass. Return only image 2, matching its entire framing and aspect ratio 511:1701, without borders, zooming, reframing or returning the full scene. Improve plausible local photographic detail and repair inherited artifacts while retaining all source features. Use maximum practical supported native resolution (3072 on longest edge requested if supported). Retain original color and light.
```

### p2-plume

```text
1=original: composition, rigid geometry, color and light authority. 2=target: return exact crop/framing/geometry. Reconstruct plausible photographic detail with optical clarity, natural edge transitions and spatially varied texture, preserving the photographic character and focus falloff. Repair inherited JPEG artifacts. Avoid invented structures/marks, relighting, halos, ringing, embossed/crosshatched/repeated texture, synthetic grain or blanket sharpening. Rigid objects: preserve silhouette, proportions and existing hardware exactly; do not invent fins, rings, panel seams, rivets, lattice members, vents, lettering or markings. Clouds: preserve exact irregular contours/lobes and soft translucent fringes; no new cloud lobes, cauliflower texture or uniformly sharp edges. Frost: preserve the irregular white surface accumulation and underlying dark vertical streaks; no invented embossed pattern. Flame/glare: preserve outline, spill, luminous softness and plume boundaries; highlights stay smooth, no invented shock diamonds/sparks.
Flame: preserve the exact luminous soft pink-white exhaust emergence, broad original turbulent structures and outline. Do not invent sparks or hard shock diamonds. Do not sharpen clipped highlights. Preserve coast, roads and water shapes behind the flame.
Image 1 is the complete original source, supplied as photographic/context, color and geometry authority. Image 2 is a visually selected focal crop from the first enhancement pass. Return only image 2, matching its entire framing and aspect ratio 581:1614, without borders, zooming, reframing or returning the full scene. Improve plausible local photographic detail and repair inherited artifacts while retaining all source features. Use maximum practical supported native resolution (3072 on longest edge requested if supported). Retain original color and light.
```

### p2-coast

```text
1=original: composition, rigid geometry, color and light authority. 2=target: return exact crop/framing/geometry. Reconstruct plausible photographic detail with optical clarity, natural edge transitions and spatially varied texture, preserving the photographic character and focus falloff. Repair inherited JPEG artifacts. Avoid invented structures/marks, relighting, halos, ringing, embossed/crosshatched/repeated texture, synthetic grain or blanket sharpening. Rigid objects: preserve silhouette, proportions and existing hardware exactly; do not invent fins, rings, panel seams, rivets, lattice members, vents, lettering or markings. Clouds: preserve exact irregular contours/lobes and soft translucent fringes; no new cloud lobes, cauliflower texture or uniformly sharp edges. Frost: preserve the irregular white surface accumulation and underlying dark vertical streaks; no invented embossed pattern. Flame/glare: preserve outline, spill, luminous softness and plume boundaries; highlights stay smooth, no invented shock diamonds/sparks.
Landscape/water: preserve exact land-water boundaries, roads, tracks and existing distant buildings without inventing new structures. Keep photographic atmospheric distance; do not add arbitrary repeated ripples, vegetation rows, guessed lettering or synthetic texture.
Image 1 is the complete original source, supplied as photographic/context, color and geometry authority. Image 2 is a visually selected focal crop from the first enhancement pass. Return only image 2, matching its entire framing and aspect ratio 1645:852, without borders, zooming, reframing or returning the full scene. Improve plausible local photographic detail and repair inherited artifacts while retaining all source features. Use maximum practical supported native resolution (3072 on longest edge requested if supported). Retain original color and light.
```
