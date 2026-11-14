# VFX rules X1 to X6

Adopted by the owner on 2026-11-12 ("All rules approved"), from the ratings of clips V01 to V10 (`evidence/vfx/verdicts.md`, teardowns in `evidence/vfx/V01-V10-teardowns.md`, frame sheets in `evidence/vfx/media/`). The Rule lines are the adopted text. The Forbidden, Why and Check lines are Claude's working-out of that text: where one of them goes further than the owner's words it says "guess", and the owner's rulings in a game's decision log always win.

The identity rules I1 to I4 and the engineering rule E1 of the UI skill (`../../roblox-ui-design/references/core-rules.md`) apply to VFX unchanged; X5 is their VFX form.

## X1. Budget by frequency
**Rule.** An effect players trigger often (a basic ability, a hit) stays compact and short: about 1 s from impact to clean, close to the caster or target, never covering other players or the screen. Big, long and screen-level effects are for rare moments: an ultimate, a late-game attack, a cutscene, a rare reveal.
**Forbidden.** Designing before the effect is classed FREQUENT or RARE. A frequent effect that outlasts its tier time, hides the caster or the target, or reaches the screen (flash, shake, darkening). Giving every ability the ultimate's treatment.
**Why.** The two 5-rated ability clips are small and quick, and the owner names that as the pattern; the clips praised as big are praised for cutscenes and rare attacks.
**Check.** (a) The brief names the tier, and the game's profile lists the effect under it. (b) Time from the impact frame to the last visible particle: within the tier's number in `tiers.md`. (c) In the peak frame from a normal play camera, the caster, the target and a second player standing beside them are still visible (the second player is a guess at how to test "never covering other players").
**Evidence.** V04 (5), V06 (5) against V01 (4.5), V03 (4.5), V09 (5).
**Not a blink (adopted 2026-11-12, owner: "Adopt").** The impact stays visible for about 0.6 to 1 s after the hit: flash, burst, a short linger, fade. Shorter reads as nothing happened. Evidence: V04 (about 1 s), A/B test 2 recordings (about 1 s read fine; about 0.3 s too brief).
**Readable from the play camera (adopted 2026-11-12, owner: "Adopt them all").** Compact is not tiny: a frequent effect's peak shape is at least about as tall on screen as the target character, seen from the game's default camera at a normal fighting distance. Check it from that camera, not a close-up. Evidence: A/B test 2 (B's lance too small at 25 studs), V04 (shards about a character's height).
**Owner.** V04: "Basically the model for all kind of abilities, it's small, reasonable vfx attack duration and doesn't get tiring to look at even after firing the ability multiple times. All ability like attacks that are used very often should follow this pattern." V01: "It's very decent, specially for cutscenes and rare/late game attacks for RPGs or Roguelikes."

## X2. Repeatable
**Rule.** A frequent effect must still please on the twentieth cast: no long holds, no full-screen flash, the same readable shape each time with small variation (size, angle, spark count).
**Forbidden.** A hold or a slow build on a frequent effect. A full-screen flash on a frequent effect. Variation so large that the shape changes from cast to cast, or none at all (every cast a perfect copy).
**Why.** The owner's words for the top ability clips are about repetition: not tiring, addicting to cast.
**Check.** Cast it five or more times in a row at its real cooldown. (a) Each cast is clean before the next one peaks, or the overlap still reads as one shape. (b) The silhouette of the peak frame is the same each time. (c) Two casts side by side differ in a small way (yaw, scale, spark count; the ranges in `tiers.md` are a guess).
**Evidence.** V04 (5), V06 (5).
**Owner.** V06: "It's the kind of ability vfx that sticks. It's addicting to cast and looks impressive." V04: "the particle burst that happens every cast".

## X3. The impact shape
**Rule.** Anticipation, a 1 to 2 frame flash, a burst or ring, debris, then a soft fade. Every element fades or shrinks in and out; nothing pops on or cuts off.
**Forbidden.** An impact with no anticipation at all on an effect that has a wind-up in play. A flash that holds for many frames. Any element that appears at full size and full opacity in one frame (the flash itself is the one exception), or that is destroyed while still visible. Destroying an emitter's parent while its particles are alive.
**Why.** The phases make a hit readable in under a second; the soft in and out is what the owner singles out in two separate clips.
**Check.** (a) The brief's phase table has all five phases with ms (a phase may be 0 with a reason). (b) In a mid-fade capture, every remaining element is visibly smaller or more transparent than at the peak. (c) Step the last 200 ms frame by frame when in doubt: no element vanishes between two frames while larger than a spark.
**Evidence.** V04 (charge 300 to 500 ms, flash 1 to 2 frames, burst, crescent, shards linger and shrink, gone in about 1 s), V06 (growth, slashes, flash pillar, rings collapse inward, core), V02 (one white flash frame, sparks fade over about 800 ms), V07 (the sparks at the collapse).
**Owner.** V04: "the fade in and fade out of the icicles". V07: "i like that spark effect as it disappears." 2026-11-14: "it looks ugly for any element to disappear away instantly with no tell" (any transition that reads, not only a fade).

## X4. Detail over quantity
**Rule.** A few well-made elements (shaped shards, drawn flame, chains with real detail) beat many generic particles. Maximalism loses even when it looks impressive.
**Forbidden.** Raising particle counts, emitter counts or layer counts to make an effect "better". Stock sparkle and smoke textures as the main shape of an effect. Decoration with no link to the concept (V07's generic lightning). Fixing a weak effect by adding layers instead of improving one.
**Why.** The two clips marked down are the two with the most going on; the praise in the top clips is for named details.
**Check.** (a) The brief names ONE crafted element (a mesh, a drawn texture or flipbook, a shaped beam) that carries the effect. (b) Removal test: switch off each layer in turn; a layer whose absence nobody would notice goes. (c) Layer and particle counts within the tier's budget in `tiers.md` (guesses).
**Evidence.** V04 icicles, V03 flame, V09 chains and crystal, against V02 (3.5) and V07 (4).
**Owner.** V02: "it's a bit maximalistic, which isn't exactly my taste." V07: "falls under the same critism as V02." V04: "the details on the icicles". V03: "the flame looks well done". V09: "the details on the chains, crystal, room... all look very professional".
**Note.** "Detail" here means craft in a few elements, not density. In V08 the owner preferred the cleaner set of auras ("conveys each aura's identity slightly better") over the more layered and textured set.

## X5. Identity at a glance
**Rule.** Each effect is one named concept that its colour, shape, motion and details all express; one hue family plus a white core unless a hue carries meaning (rarity, element).
**Forbidden.** An effect with no concept name, or named by its colour ("blue burst"). A rainbow or a second hue with no meaning (V07's palette, the pink burst at the end of V06). A concept from outside the game's theme vocabulary or on its refused list (I1). An effect any game could use unchanged (I2).
**Why.** It is what the owner names in every aura clip, and it is the same test the UI rules put first.
**Check.** (a) The brief has the concept name and one line each for colour, shape, motion, detail. (b) Show the peak frame to someone who has not read the brief and ask "what is this?": the answer names the concept or its element. (c) Count hues in the peak frame: one family plus white or black; each extra hue has its meaning written in the brief or the profile.
**Evidence.** V05 (4.5), V10 (4.5), V08 (4.5); one hue plus white in V01, V04, V09.
**Owner.** V05: "it's polished and immediately communicates its entire identity via colors, shapes, movements, details, etc". V08: "Opus conveys each aura's identity slightly better."

## X6. Screen-level effects sell power, only at the peak
**Rule.** Screen shake, impact frames, a darkened world or a colour inversion are allowed on rare or cinematic moments, briefly, at the hit. Never on frequent effects; off or reduced under Reduced Motion; no fast repeated full-screen flashes.
**Forbidden.** Any screen-level effect on a FREQUENT effect. Shake that runs through the whole effect instead of at the hit. More than three full-screen flashes in one second, at any tier (the common photosensitivity limit, WCAG 2.3.1). A screen takeover that hides play from a player who still has control (guess: the owner praised V03's impact frames; the risk note on its 3 s takeover is the teardown's, not the owner's). Shake, flash or inversion for another player's effect unless the profile says so (guess).
**Why.** The owner credits the shake and the impact frames for the feeling of power in the rare clips, and the same things would break X1 and X2 on a frequent effect.
**Check.** (a) The tier is RARE or CINEMATIC. (b) Each screen-level layer sits within the peak window in the phase table and has a duration in ms. (c) With Reduced Motion on: no shake, no inversion, flashes softened or dropped; the effect still reads (E1). (d) Count full-screen flashes in the busiest second: three or fewer.
**Evidence.** V09 (5), V03 (4.5).
**Owner.** V09: "the screenshakes add a lot to the impact ... the VFX of each moment really sells the feeling of power". V03: "it also does well by adding those impact frames".

## X7. One bright hero shape at the peak (adopted 2026-11-12)
**Rule.** At the peak frame, one shape is clearly the brightest and crispest thing on screen (a glowing sigil, a flash core, a pillar) and carries the concept; every other layer is dimmer and supports it.
**Forbidden.** Many mid-value translucent pieces with no bright core, however many there are. Two shapes competing as the brightest.
**Why.** In both A/B tests the slam the owner preferred had one glowing white shape (a hexagon sigil); the version with many translucent crystals and no bright core lost.
**Check.** On the peak capture, name the brightest shape: it must be one shape, it must say the concept, and nothing else may match its brightness.
**Evidence.** A/B test 1 (A's slam preferred), A/B test 2 (B's slam, "I specially like the pop-up animation for Glaciar Slam session B did"), V04 (white bloom core), V06 (flash pillar), V01 (pillar core).
**Owner.** "Adopt them all" (2026-11-12).

## E. Leave the scene as found (adopted 2026-11-12)
Do not change lighting, the baseplate or map, the spawn or the camera unless asked: propose it instead. Remove capture and debug hooks (time-scale attributes, freeze switches, forced aim) before reporting, or list each one that stays and why. Evidence: A/B tests 1 and 2 (both sessions changed the scene and left hooks). Owner: "Adopt them all".

## Anti-slop checklist for VFX

Tick before calling an effect done. A "no" is a finding (in an audit) or a fix (in a build).

1. It has a concept name that is a thing in this game's world, and the peak frame alone says it (X5, I2).
2. It was classed FREQUENT or RARE before any number was chosen (X1).
3. One hue family plus a white core; every other hue has a written meaning (X5).
4. One crafted element carries it; stock sparkles and smoke are support only (X4).
5. No layer is there "for richness": each survives the removal test (X4, I3).
6. All five phases are in the brief with ms; the flash is 1 to 2 frames (X3).
7. Nothing pops on, nothing cuts off, nothing is destroyed while visible (X3).
8. Frequent: clean about 1 s after impact, hugs the ground or the target, the character stays visible, fine on the twentieth cast (X1, X2).
9. No screen shake, impact frame, flash or darkening unless the tier is RARE, and then only at the hit (X6).
10. Small variation per cast, same silhouette (X2).
11. Reduced Motion and the game's lowest quality level still show that it happened (E1).
12. Everything it created is gone or back in the pool afterwards; pooled parts have their tweened properties reset.
13. It reads on the game's real backgrounds, bright and dark, not only on a black test void (the V01 teardown's caveat; guess as a rule).
14. No frozen value changed; the numbers live in the game's effect table.
15. Typical slop tells (guesses, not from a rated clip): every colour of the rainbow, a default sparkle texture as the hero, one huge emitter with a high Rate, lightning added to everything, a glow sphere that pops off in one frame, the same radial burst reused for every ability (the V04 teardown's "several skills look alike").
