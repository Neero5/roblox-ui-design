---
name: roblox-vfx
description: Use when designing, building, changing, polishing or reviewing Roblox visual effects in the 3D world (ParticleEmitter, Beam, Trail, Attachment rigs, PointLight and SpotLight pulses, mesh shards and shockwave rings; ability, hit, projectile, explosion, aura, pickup, level-up, hatch, reveal and cutscene effects; screen shake, impact frames, screen flashes), or when asked to make Roblox VFX look professional, on-identity or less like AI slop. Do not use for 2D UI (ScreenGui panels, menus, HUD motion: that is roblox-ui-design), for character animation, or for Luau work with nothing visible.
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

## Mode A: design an effect (from a description or a reference)

1. **Classify first (X1).** FREQUENT (cast or seen often: basic abilities, hits, pickups) or RARE / CINEMATIC (ultimates, late-game attacks, cutscenes, rare reveals). The profile's lists decide; if the effect is on neither list, ask. An always-on effect (an aura, an ambient loop) has no adopted numbers: see `references/tiers.md`.
2. **References, if any.** Take the timing, layering and shape language, never the art (I4). A video: run `tools/extract.py` from the plugin root on it first.
3. **Write a short brief before building** (10 lines at most):
   - the concept name (a thing, in the game's world: "frost lance", not "blue explosion") and how colour, shape, motion and detail each express it (X5);
   - the one hue family plus the white core; any second hue and what it means;
   - the phase table with ms: anticipation, flash, burst, debris, fade (starting numbers in `references/tiers.md`);
   - the layers (4 to 6 for a frequent effect), each with its job, and the one crafted element (X4);
   - size against the character, and what stays visible (the caster, the target, other players);
   - what Reduced Motion does, and what each lower quality level drops.
4. **One direction by default.** A second only when the owner asks. If the game reviews looks first, stop after the brief or a first capture for the owner's notes.

## Mode B: build or change (a known design)

Follow the brief or the owner's note exactly. Put numbers in the game's effect table, not scattered through code. Effects play on clients; the server sends the event. Every part, emitter and connection the effect makes is cleaned up or returned to the pool. Engine patterns: `references/roblox-vfx-recipes.md`.

## Mode C: audit existing VFX

Do not edit. Return a short ranked list: the finding, the rule it breaks (id), the frozen ruling it touches (if any), the suggested fix, its size (small/medium). The owner picks; then switch to Mode B for the picked items only.

## Rules (full text, checks and evidence in `references/vfx-rules.md`)

- **X1 Budget by frequency.** Frequent effects are compact and short: about 1 s from impact to clean, close to the caster or target, never covering other players or the screen. Big, long and screen-level is for rare moments only.
- **X2 Repeatable.** A frequent effect still pleases on the twentieth cast: no long holds, no full-screen flash, the same readable shape each time with small variation.
- **X3 The impact shape.** Anticipation, a 1 to 2 frame flash, a burst or ring, debris, a soft fade. Every element fades or shrinks in and out; nothing pops on or cuts off.
- **X4 Detail over quantity.** A few well-made elements beat many generic particles. Maximalism loses even when it impresses.
- **X5 Identity at a glance.** One named concept per effect, expressed by colour, shape, motion and detail; one hue family plus a white core unless a hue carries meaning (rarity, element).
- **X6 Screen-level effects only at the peak of rare moments.** Screen shake, impact frames, a darkened world, an inversion: brief, at the hit, never on frequent effects, off or reduced under Reduced Motion, no fast repeated full-screen flashes.
- The identity rules of the UI skill apply unchanged: **I1** every element belongs to the game's one identity, **I2** generic fails (could this effect be in any game?), **I3** every effect has a job for the player, **I4** a benchmark lends principles only. **E1** Reduced Motion: the effect still tells the player what happened. Text: `../roblox-ui-design/references/core-rules.md` (sections Identity and Engineering).

## Check (light by default; more only on request)

Every time: capture the **peak frame** and **one frame mid-fade** from a normal play camera. For a frequent effect, cast it several times in a row (five or more) and watch the last cast. Then tick in a few lines: the concept reads from the peak frame alone; one hue family plus white; the character and the target stay visible; no element pops on or cuts off in the mid-fade frame; clean within the tier's time; nothing left in the workspace after it ends; no screen-level effect on a frequent tier; Reduced Motion and the lowest quality level still show that it happened; nothing frozen changed. Fix what fails. Say what still needs the owner's eyes (captures miss motion feel, and some tools do not draw every layer).
A fuller review (frame strips with `tools/extract.py`, many casts, several players, a real map background) only when the owner asks, or for a rare moment after asking.

## Report

Two to six lines: what changed, the brief (Mode A), what the check found, anything frozen you proposed but did not change, what the owner should look at.

## Reference files (load only when needed)

| File | Load it when |
|---|---|
| `references/tiers.md` | Mode A, or any timing, size or count choice. |
| `references/vfx-rules.md` | A rule's exact wording or check is needed, or an audit. |
| `references/roblox-vfx-recipes.md` | Writing or changing effect code or emitter properties. |
| `../roblox-ui-design/references/core-rules.md` | I1 to I4 or E1 in full. |
