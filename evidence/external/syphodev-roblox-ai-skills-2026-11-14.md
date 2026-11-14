# External: SyphoDev "roblox-ai-skills" (reviewed 2026-11-14)

Source: https://github.com/SyphoDev-yt/roblox-ai-skills (free licence: use and modify for your own projects, commercial games included; no selling; credit the SyphoDev YouTube channel when sharing). Shown by the owner with the creator's video transcript. Read, not copied: nothing from it is in `skills/` unless the owner adopts it, and then as our own wording with this note as the source.

## What it is
Eleven skills installed into `~/.claude/skills` (unnamespaced): roblox-vfx, roblox-ui, roblox-animation, roblox-3d-model, roblox-map, roblox-sfx, roblox-texture-gen, roblox-code, create-roblox-game, a build orchestrator, a setup skill. The VFX skill is about 1,300 lines plus tools: a browser simulator of Roblox VFX (three.js, Roblox property names, deterministic frame strips, luma metrics), a maths texture generator (2,000+ white textures in cel, soft, glow and ink looks), Blender scripts for meshes (weapons, rocks, craters, a dragon, a phoenix), a numeric critic gate, a blind review against pro strips, a hit-reaction system, and a Studio kit exporter that uploads assets with an Open Cloud key.

## Where it agrees with ours (independent confirmation)
- Brief before building; layered effects; reference teardowns measured in frames.
- Impact frames on ultimates only (theirs: 4 of 4 ultimates, 0 of 9 moves; ours: X6).
- The look is capped by the assets: make the textures and meshes (ours: the asset step after A/B test 1).
- Peak early, residue outlives the hit, one dominant hue plus an accent (ours: X3, X5).

## New, worth proposing to the owner
1. **Real thing, not a stand-in** (their "rule zero"): if the effect IS a dragon, a sword, a crater, build that object (a mesh), never a beam with a blob or a decal of a crater. Sprites only as a layer on top.
2. **White-hot core, colour only at the rims** (12 of their 14 measured pro effects).
3. **A dark copy under every bright stroke**, so it reads on any background.
4. **Long charge, tiny release** (about 800 ms of charge to 70 ms of release). Matches the owner's V12 note.
5. **Nothing perfectly symmetric or evenly spaced**: regularity reads as "a preset, not a drawing".
6. **Erode, don't fade**: shapes break up over 6 to 8 frames rather than a flat transparency fade; no linear fades.
7. **Every layer dies at a different time** (everything fading together reads as one flat sticker).
8. **Greyscale check**: the effect must still read in black and white.

## In tension with ours (needs a ruling)
- **Flash hard off** (1 to 4 frames, then gone, not faded) and **slash shapes born at full size** (no grow-in) vs our X3 and the owner's "nothing appears or disappears instantly without a tell". Possible reading: the flash and impact frames ARE the tell of a hit; everything else keeps a transition.
- **"This overrides time and token budget"** vs the owner's cost rules (light by default, no subagents unless asked). Their blind review spawns a reviewer agent every time.

## Engine facts they report (to verify before adopting)
- ParticleEmitter Size draws twice its value (Size 4 = 8 studs wide).
- OBJ to FBX conversion turns meshes 180 degrees about Y (asymmetric test mesh to check).
- An emitter under an Attachment ignores its Shape (spawns from one point); shaped emitters go under the Part.
- A CFrame tween turns the short way round (a 260 degree spin turns -100).
- SurfaceAppearance only on a MeshPart; a fresh upload can show "being generated" for 30+ minutes.
- A dark aura must have LightEmission 0 (additive glow on black reads as red candy floss).

## Practical clash
Installing their skills as is puts an unnamespaced `roblox-vfx` and `roblox-ui` next to ours (`roblox-ui-design:roblox-vfx`, `roblox-ui-design:roblox-ui-design`): both would claim the same requests.
