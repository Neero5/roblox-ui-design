# Tiers: starting numbers

Starting points, not rulings. Each number carries its source: a clip id means it was measured or read off that clip's frame sheet (`evidence/vfx/V01-V10-teardowns.md`); "estimate" means read by eye from a sheet; "guess" means no evidence yet. A value in the game's profile or decision log replaces any number here. Clip frame counts come from roughly 30 fps captures (V09: 24 fps); build by time, not by frames.

## Which tier
- **FREQUENT:** the player triggers or sees it many times a minute: basic abilities, hits, projectiles, pickups, footstep and tool feedback. Model clips: V04 (5), V06 (5).
- **RARE / CINEMATIC:** a few times a session or less: ultimates, late-game attacks, cutscenes, hatches, rare reveals. Model clips: V09 (5), V03 (4.5), V01 (4.5). CINEMATIC means the player is watching, not playing (camera or control taken).
- **Always-on (auras, ambient loops):** no adopted numbers. V05, V10 and V08 were rated 4.5 for identity (X5), with no ruling on size or density. See the last section.

## FREQUENT

| Item | Start at | Source |
|---|---|---|
| Anticipation (charge, gather, wind-up) | 300 to 500 ms; 0 to 150 ms for an instant hit | V04; the instant-hit range is a guess |
| Flash | 1 to 2 frames, about 30 to 70 ms; local to the effect, never full screen | V04 (frames); ms conversion is a guess |
| Burst or ring | 200 to 300 ms | V04 (5.0 to 5.2 s) |
| Secondary beat (ground crescent, rings collapsing inward) | 100 to 300 ms | V04 (5.3 to 5.6 s), V06 (2.0 to 2.1 s) |
| Debris linger and shrink | about 300 ms | V04 (5.6 to 5.9 s) |
| Impact to clean | about 1 s | V04, rule X1 |
| Whole effect with a projectile and stages | up to about 1.5 s | V06 (0.8 to 2.3 s) |
| Height at the peak | at or below about 1.5 character heights; hug the ground or the target | V04 estimate, guess |
| Footprint, area ability | radius about 2 to 3 character heights | V04 estimate |
| Footprint, single-target hit | about 1 character height across | guess |
| Layers | 4 to 6 (core flash, crafted shape, ring, sparks, ground mark, light) | V04 estimate, guess |
| Crafted shapes (shards, slashes) | 6 to 12 per cast | V04 estimate |
| Particles alive at the peak | 60 to 120 in total | guess |
| Emitters | 6 or fewer | guess |
| Variation per cast | yaw random; scale and spark count plus or minus 10 to 15% | guess (X2 names the properties, not the range) |
| Light | one PointLight pulse, 150 to 300 ms, no shadows | guess |
| Screen shake, impact frames, darkening, full-screen flash | none | X1, X2, X6 |
| Cooldown readability | clean before the next cast peaks; if the cooldown is under 1 s, shorten the fade to fit it | guess |

## RARE / CINEMATIC

| Item | Start at | Source |
|---|---|---|
| Anticipation | 500 ms to 3 s; longer only in a cutscene | V02 (charge 4.4 to 4.9 s; lock pulse 0 to 3.0 s) |
| Small pre-flash (unlock, seal) | about 300 ms | V02 (3.1 s) |
| Peak flash | 1 frame, about 30 to 40 ms | V02 (5.1 s) |
| Burst and shockwave ring | 200 to 300 ms | V02 (5.2 to 5.4 s) |
| Linger | about 800 ms | V02 (5.5 to 6.3 s) |
| Impact frames | about 3 frames, 100 to 200 ms, once or twice per moment | V03 (3.9 to 4.1 s; 6.2 to 6.4 s) |
| Colour inversion | about 3 frames, once | V03 (6.2 to 6.4 s) |
| Darkened world (dome, dimmed lighting) | starts 100 to 200 ms before the hit, lifts with the fade | V03 (2.8 s dome, 2.9 s impact); the lift is a guess |
| Full-screen takeover | up to about 3 s, CINEMATIC only; in live play 300 ms or less | V03 (about 3 s); the split and the live-play cap are guesses |
| Whole moment, live play (ultimate) | 2 to 5 s | V03 (2.4 to 7.1 s) |
| Whole moment, cutscene or world event | 8 to 20 s | V07 (8 s), V02 (18 s), V09 (19 s) |
| Stages | 2 to 3 escalating beats, each with its own small impact shape | V02 (unlock, then hatch), V06 |
| Screen shake amplitude | 0.15 to 0.4 studs of camera offset, or 0.5 to 1.5 degrees | guess (V09 has shakes; not measured) |
| Screen shake duration | 200 to 500 ms, decaying to zero, at the hit only | guess |
| Shakes per moment | one per beat, 3 at most | guess |
| Size | may exceed the character; anchor it with a floor circle or ring | V01, V05, V10 |
| Particles alive at the peak | 300 to 600 in total | guess |
| Full-screen flashes | 3 or fewer in any one second | WCAG 2.3.1, X6 |
| Reduced Motion | no shake, no inversion; flashes softened or dropped | X6, E1; the softening is a guess |

Notes for this tier:
- Big is allowed; busy is not. V02 (3.5) and V07 (4) are both rare-tier clips and both lost points for being "maximalistic" (X4). Spend the budget on a few detailed elements (V09's chains and crystal), not on more layers.
- V01's build takes tens of seconds: it is a Studio showcase, not a timing to copy.

## Always-on effects (auras, ambient loops): no adopted numbers
- Identity is the whole job (X5): one named concept, one or two hues, the name and the shape agree (V05, V10).
- A floor circle anchors most of the rated auras (V05, V10 teardowns).
- Size: several rated auras are much bigger than the character. The teardown calls that a weakness in a crowded server; the owner has not ruled on it. Ask the owner, or take the size from the game's profile.
- Loop density: keep the Rate low enough that the character's silhouette stays readable (guess).
- Reduced Motion: keep the still shape, stop or slow the loop (guess; E1 says changes stay visible).
