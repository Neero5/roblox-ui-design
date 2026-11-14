---
name: roblox-vfx
description: Roblox VFX: design, build or audit 3D effects (ParticleEmitter, Beam, Trail, meshes, lights; abilities, hits, auras, reveals, cutscenes, screen shake, impact frames). Not for UI or character animation.
---
# Roblox VFX

Goal: effects that look made by a careful studio. Each one is a single named concept the player reads at a glance, sized and timed for how often it plays, built from a few well-made elements, and gone cleanly. The owner's top scores went to compact, repeatable ability effects and to rare cinematic moments with real detail; "maximalistic" effects lost points even when they impressed.

## Cost rules (always)

- **Light by default.** No subagents unless the owner asks for them. One pass, one or two captures, one self-check.
- **Ask before spending.** If the work needs more than the request implies (new textures or meshes, a whole ability set, several directions, a full review), say so in one line and ask first.
- **Small requests get small answers.** A tweak is a tweak: change the named value, do not re-author the effect around it.

## Step 0: read the game (once per session)

1. The game's profile (`docs/ui-profile.md` or a file with `type: ui-profile`): the IDENTITY, the signature motif, the theme vocabulary, refused effects, Reduced Motion policy, and the VFX block (quality levels and what each drops, the frequent and rare effect lists, hue per element or rarity). If the profile or its VFX block is missing, draft it from `../../templates/project-profile.md` and what the repo shows, and ask the owner in ONE short round. Never design on unconfirmed guesses.
2. **The owner's rulings win.** Read the game's decision log and style rules (the profile lists their paths). Any colour, size, duration, count or effect the owner has ruled on is FROZEN: never change it on your own. If a rule here disagrees with a ruling, propose the change in one line; the ruling stands until the owner says otherwise.
3. The game's existing VFX code: its effect table or module, templates folder, pooling, quality levels, the remote that triggers effects. Build with them; never paste a second VFX system beside the first. Tables the owner tunes by hand are the owner's: add or change a row only as asked.
4. **Production tools (optional).** If SyphoDev's roblox-ai-skills tools are on this machine (the profile's "External VFX tools" path), use them as helpers only: its browser simulator for frame strips and timing checks (cheaper than Studio captures), its texture library and generator, its Blender mesh scripts (weapons, rocks, craters, creatures), its hit-reaction module. Our rules, the owner's rulings and the cost rules still decide: no subagents unless asked, so its blind review runs only on request. Credit: SyphoDev (free licence).
5. **Assets.** Find the game's own VFX assets (a texture and mesh pack, template effects, flipbook sheets). Use them: the look is capped by the textures and meshes, not by the rules. If the game has none and the effect needs custom textures or meshes (slash, crack, flare sheets; shard meshes), say so and propose making them (Blender, drawn sheets) before building; built-in textures alone give a generic look (A/B test 1).

## Mode A: design an effect (from a description or a reference)

1. **Classify first (X1).** FREQUENT (cast or seen often: basic abilities, hits, pickups) or RARE / CINEMATIC (ultimates, heavy unspammable attacks, late-game attacks, cutscenes, rare reveals). Also note melee or ranged (X1). The profile's lists decide; if the effect is on neither list, ask. Always-on effects (auras, transformations): size and visibility come from the game type in the profile (`references/tiers.md`).
2. **References (every time).** First the game's own references folder (the profile's "References folder"), then pick one to three rated frames from `references/reference-library.md` that match the tier, effect type and element; open them and note what to take. Add the owner's own references if given (a video: run `tools/extract.py` from the plugin root on it first). Take timing, layering, shape and value, never the art (I4).
3. **Write a short brief before building** (10 lines at most):
   - the concept name (a thing, in the game's world: "frost lance", not "blue explosion") and how colour, shape, motion and detail each express it (X5);
   - the one hue family plus the white core; any second hue and what it means;
   - the phase table with ms: anticipation, flash, burst, debris, fade (starting numbers in `references/tiers.md`);
   - the layers (4 to 6 for a frequent effect), each with its job, and the one crafted element (X4);
   - size against the character, and what stays visible (the caster, the target, other players);
   - what Reduced Motion does, and what each lower quality level drops;
   - the references: one line each, what to take and what to avoid.
4. **One direction by default.** A second only when the owner asks. If the game reviews looks first, stop after the brief or a first capture for the owner's notes.

## Mode B: build or change (a known design)

Follow the brief or the owner's note exactly. Put numbers in the game's effect table, not scattered through code. Effects play on clients; the server sends the event. Every part, emitter and connection the effect makes is cleaned up or returned to the pool. Engine patterns: `references/roblox-vfx-recipes.md`.

## Mode C: audit existing VFX

Do not edit. Return a short ranked list: the finding, the rule it breaks (id), the frozen ruling it touches (if any), the suggested fix, its size (small/medium). The owner picks; then switch to Mode B for the picked items only.

## Rules (full text, checks and evidence in `references/vfx-rules.md`)

- **X1 Budget by frequency.** Frequent effects are compact and short: about 1 s from the hit to clean (a ranged attack's travel time is extra, never cut short), close to the caster or target, yet at least about as tall on screen as the target character from the default play camera, and visible for about 0.6 to 1 s after the hit (never a blink), never covering other players or the screen. Big, long and screen-level is for rare moments and strong unspammable attacks only.
- **X2 Repeatable.** A frequent effect still pleases on the twentieth cast: no long holds, no full-screen flash, the same readable shape each time with small variation.
- **X3 The impact shape.** Anticipation, a 1 to 2 frame flash, a burst or ring, debris, a soft fade. Every element fades or shrinks in and out; nothing pops on or cuts off.
- **X4 Detail over quantity.** A few well-made elements beat many generic particles. Maximalism loses even when it impresses.
- **X5 Identity at a glance.** One named concept per effect, expressed by colour, shape, motion and detail; one hue family plus a white core unless a hue carries meaning (rarity, element).
- **X6 Screen-level effects only at the peak of rare moments.** Screen shake, impact frames, a darkened world, an inversion: brief, at the hit, never on spammable effects; strong unspammable attacks (ultimates, heavy impacts) ALWAYS get shake; seen by every player in the attack's effective range; length set per attack, kept short; off or reduced under Reduced Motion; no fast repeated full-screen flashes.
- **X7 One bright hero shape at the peak.** One shape is clearly the brightest and crispest at the peak and carries the concept; everything else is dimmer.
- **X8 to X15** (`references/vfx-rules.md`): the real thing, never a stand-in; white-hot core, colour at the rims; a dark copy under bright strokes; long charge, tiny release; nothing perfectly regular; erode, don't fade; layers die at different times; greyscale check. The hit flash and impact frames may cut hard (they are the tell); every other element keeps a transition.
- **E Leave the scene as found.** No changes to lighting, map, spawn or camera unless asked (propose instead); remove debug and capture hooks before reporting, or list them.
- The identity rules of the UI skill apply unchanged: **I1** every element belongs to the game's one identity, **I2** generic fails (could this effect be in any game?), **I3** every effect has a job for the player, **I4** a benchmark lends principles only. **E1** Reduced Motion: the effect still tells the player what happened. Text: `../roblox-ui-design/references/core-rules.md` (sections Identity and Engineering).

## Check (light by default; more only on request)

Every time: capture the **peak frame** and **one frame mid-fade** from a normal play camera. For a frequent effect, cast it several times in a row (five or more) and watch the last cast. **Stand-in audit (X8)** and **greyscale check (X15)** on the peak frame. **Compare with the reference:** the peak capture beside the chosen reference frame; name the three biggest gaps (core brightness and contrast, shape, layering, detail, size, colour) and fix the largest one or two. Then tick in a few lines: from the DEFAULT play camera at a normal fighting distance, the peak is at least about as tall as the target character; one shape is clearly the brightest (X7); the concept reads from the peak frame alone; one hue family plus white; the character and the target stay visible; no element pops on or cuts off in the mid-fade frame; clean within the tier's time; nothing left in the workspace after it ends; no screen-level effect on a frequent tier; Reduced Motion and the lowest quality level still show that it happened; nothing frozen changed; the scene is as found and no debug hooks are left (or they are listed). Fix what fails. Say what still needs the owner's eyes (captures miss motion feel, and some tools do not draw every layer).
A fuller review (frame strips with `tools/extract.py`, many casts, several players, a real map background) only when the owner asks, or for a rare moment after asking.

## Report

Two to six lines: what changed, the brief (Mode A), what the check found, anything frozen you proposed but did not change, what the owner should look at.

## Reference files (load only when needed)

| File | Load it when |
|---|---|
| `references/reference-library.md` | Mode A, every time: pick 1 to 3 rated frames; again at the check. |
| `references/tiers.md` | Mode A, or any timing, size or count choice. |
| `references/vfx-rules.md` | A rule's exact wording or check is needed, or an audit. |
| `references/roblox-vfx-recipes.md` | Writing or changing effect code or emitter properties. |
| `../roblox-ui-design/references/core-rules.md` | I1 to I4 or E1 in full. |
