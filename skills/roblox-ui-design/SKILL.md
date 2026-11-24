---
name: roblox-ui-design
description: Roblox UI design and build: turn a mockup, idea or Figma frame into a professional, on-identity ScreenGui (look mocked first, then ported layer by layer; layout, look, motion), change existing UI, or audit it. Use for menus, HUDs, panels, shops, popups and UI tweens. Not for 3D VFX or animation.
---
# Roblox UI design

Goal: take the owner's simple mockup (plus a prompt, and references when given) and return a UI that looks made by a careful studio: it belongs to one nameable world, has one clear hero, reads at a glance and moves with restraint. The owner scores **identity first, animation quality second**; generic loses even when tidy, showing off loses even when eye-catching.

## Cost rules (always)

- **Light by default.** No subagents unless the owner asks for them. One pass, one capture, one self-check.
- **Ask before spending.** If the work needs more than the request implies (a redesign of a whole screen, several directions, a full review loop), say so in one line and ask first.
- **Small requests get small answers.** A tweak is a tweak: do not re-plan the screen around it.

## Step 0: read the game (once per session)

1. The game's profile: `docs/ui-profile.md` (or a file with `type: ui-profile`). It states the IDENTITY, an optional benchmark, the genre profile, theme vocabulary, refused effects, Reduced Motion policy, motion tokens and overrides. If it is missing, create it with the owner before designing: draft it from `../../templates/project-profile.md` (plugin root `templates/`) and what the repo shows (style guide, existing UI, the game's name and premise), then ask in ONE short round: two or three identity statements to pick from, two signature motifs from the game's premise (L8), the genre profile, and where the primary action and back/close sit (L4, L5). Save the answers as `docs/ui-profile.md`; never design on unconfirmed guesses.
2. **The owner's rulings win.** Read the game's decision log and style rules (the profile lists their paths). Any value, layout or effect the owner has ruled on is FROZEN: never change it on your own. If a skill rule disagrees with a ruling, you may propose the change in one line; the ruling stands until the owner says otherwise.
3. The genre profile `references/profiles/<genre>.md` and the game's existing UI kit (its panel, button and motion modules). Build with the kit; never paste a second kit beside it.
4. **Other style skills.** If another UI style skill or component kit is installed (for example a cartoon menu kit), it pulls every build toward its own look. If its look is not the profile's identity, say so in one line, do not load its components or style rules for this work, and let the profile win.

## Mode A: mockup to UI (the main use)

1. **Read the mockup's intent.** For every box in the sketch: what it is, its job for the player, and which one is the hero. Keep the owner's arrangement (what sits where); your job is to elevate its treatment, not to move things around. If something must move (overlap, an edge, a rule), say what and why.
2. **References.** First the game's own references folder (the profile's "References folder", for example its Obsidian vault): pick the matching rated ones. Then, if needed, open one to three matching sheets from `references/reference-library.md` (plus the owner's own, if given; a video: run `tools/extract.py` first). Take principles (hierarchy, anchors, spacing, timing, material), never art, logos, icon sets or exact layouts (I4).
3. **Assets (C1).** If the identity or theme vocabulary names a material, list which elements need an image asset and find them (the game's textures first, then the owner's). If none exist, say so in one line and ask; until then plan the restrained version: no faked material, no containers that do not earn their place.
4. **Write a short design brief before any code** (10 lines at most): identity statement; how the frame, header, buttons, type, colour and icons express it (I1); the hero and how it stands out (R8); the three type voices and the font families (R9, C5); the assets used (C1); the genre tells present and why they stay or go (I2); the entry and exit in one line each with their budgets (R1 to R3); what Reduced Motion does.
5. **Lay it out with craft** (`references/layout-craft.md`): a spacing scale, an alignment grid, depth layers (C8: every surface in layers), every state (hover, pressed, selected, disabled, empty, locked), real content lengths, two window sizes.
6. **Mock the look first, outside Studio** (owner 2026-11-24: the first mockup made this way was the best UI of the whole project). Build the look as an HTML mockup, or as Figma frames when the Figma connector is available, never directly in Studio:
   - **On a real capture of the game**, with any old HUD painted out, so every contrast and opacity is chosen against the real world behind it. No capture: ask for one screenshot.
   - **Layers are cheap here, so use them** (C8): underlay or shadow, body with a gradient, edge or highlight, a detail at the ends.
   - **A states sheet**: every state of every element, on the brightest and the darkest background the game has (R13).
   - **Only what Roblox can draw**: gradients, thin tinted strokes, 9-slice shadows, masks, the game's textures, a font from `Enum.Font`. No blur and no blend modes in the mockup.
   - **One direction by default.** Offer a second only when the owner asks, or when the brief shows two genuinely different readings (then ask which first).
   Show it and iterate on the owner's notes until the look is approved. When a round fails, write the next brief against the named failures ("the bar has no track; the slot stopped reading as a button"), not against adjectives.
7. **Port it layer by layer.** In Studio, rebuild the approved mockup with its exact values: every layer, colour, opacity, size, font and offset, listed in a port table before code. Porting is translation: change nothing silently; if Roblox cannot draw a layer, say which and propose the nearest. Two known port traps (field test 4): scale the HUD with `math.clamp(viewportHeight / 900, 0.85, 1.3)`, updated on ViewportSize change and at least 1.0 on touch-only devices (never height / 1080 alone: Studio's play window and laptops shrink it to unreadable); and UIGradient is linear only, so a radial glow or scrim needs a radial-gradient image, not stacked gradients. Then build the behaviour and motion. The port may run on a cheaper model; the look should come from the strongest one available.

## Mode D: Figma frame to UI

When the owner designs the look in Figma (or approves Figma frames), read the frame with the Figma connector (design context, variables, a screenshot) and treat its values as frozen rulings: sizes, colours, fonts, effects, spacing. Then do Mode A step 7 (port table, then build), states, motion tokens and the light check. Do not restyle a Figma design; propose changes in one line instead.

## Mode B: build or change UI (a known design)

Follow the brief or the owner's note exactly. Motion: plan the beats in a small table (element, start ms, duration, easing, property, job for the player) only when there are three or more moving parts; otherwise one line. Use the game's motion tokens; never scatter raw `TweenInfo.new` literals.

## Mode C: audit existing UI

Do not edit. Return a short ranked list: the finding, the rule it breaks (id), the frozen ruling it touches (if any), the suggested fix, its size (small/medium). The owner picks; then switch to Mode B for the picked items only.

## Rules (details and checks in `references/core-rules.md`)

Identity, checked first: **I1** every element belongs to the one identity; **I2** consistent but interchangeable is a fail (hide the logo: could this be any game of the genre?); **I3** every motion has a job for the player, nothing performs to show off the kit; **I4** a benchmark lends principles only.
Layout and look: **L1** two surfaces at most; **L2** rarity colour is a system, only where it informs; **L3** the hero owns the centre, text in side columns; **L4** top bar, tabs, primary button and back/close stay put (one striking device per page allowed); **L5** one primary action, in the same place on every screen; **L6** one ornament family; **L7** more important screen, more empty space; **L8** one signature motif from the game's premise, used in several places; **L9** browse = list or grid beside a big detail, no popup per item; **L10** quiet but unmistakable selected state; **R8** one hero per screen; **R9** hierarchy from type first, three voices at most; **R10** effects from the game's theme vocabulary only; **R12** no placeholder text; **R13** legible on the worst background.
Motion: **R1** entries in beats, hero last; **R2** frequent panels 350 ms or less, rare moments 800 ms or less; **R3** exits 40 to 65% of the entry, reverse order; **R4** no two panels visibly overlapping; **R5** in-place changes cross-fade 160 to 240 ms; **R6** something stays still; **R7** idle motion only in the hero; **R11** overshoot 5% or less, at rest within 200 ms.
Craft (static look; a pass on I and R with a fail here is still a fail): **C1** a material identity uses real image assets, never faked with primitives; **C2** no black outlines by default; **C3** a container must earn its place, frame never louder than content; **C4** suggest, don't label: no word stamps or clip-art stickers; **C5** one type world, no default black text stroke; **C6** smooth fills, no stepped edges; **C7** the HUD is quieter than the game; **C8** every surface is built in layers; **C9** restraint is not absence: bars keep a track and a max, interactive elements keep a surface and their states.
Engineering: **E1** Reduced Motion: no scale, slide, stagger or loop, changes still visible; **E2** interruptible; **E3** input live from the first visible frame; **E4** one motion table; **E5** start states set before the first frame.

## Check (light by default; full loop only on request)

Before a playtest or capture in Studio, read the sections Getting code into Studio and Recording in `../roblox-vfx/references/studio-testing.md` (stale code after a push, the camera resetting, screenshots flooding the context).

Light check, every time: one capture of the result at rest (and one mid-transition if motion changed), then tick in a few lines: identity carriers visible, two surfaces at most, the hero in the centre, anchors and the primary button in their places, one hero, three type voices or fewer, legible, no placeholder text, nothing frozen changed, Reduced Motion handled. Then the craft ticks: no faked material (C1), no black outlines (C2), no box that does not earn its place (C3), no word or clip-art stickers (C4), two font families at most and no default text stroke (C5), no stepped edges (C6), squinting at the capture the play is seen before the UI (C7), each surface has at least an underlay, a body and an edge (C8), every bar shows its max and every button reads as pressable in each state (C9). If the build came from a mockup, put the capture beside the mockup too: any layer that went missing in the port is a fail. Put the capture beside the reference sheet chosen in Mode A step 2 and name the biggest craft gap; if the reference clearly wins, fix that gap before reporting. Fix what fails. Report what still needs the owner's eyes.
Full review loop (`references/review-loop.md`): only when the owner asks, or for a new full screen or a rare moment, and only after asking.

## Report

Two to six lines: what changed, the brief (Mode A), what the light check found, anything frozen you proposed but did not change, what the owner should look at.

## Reference files (load only when needed)

| File | Load it when |
|---|---|
| `references/layout-craft.md` | Mode A, or any new layout. |
| `references/reference-library.md` | Mode A: pick 1 to 3 rated frames; again at the check. |
| `references/core-rules.md` | A rule's exact wording or check is needed, or an audit. |
| `references/profiles/<genre>.md` | Step 0. |
| `references/roblox-recipes.md` | Writing tween or layout code. |
| `references/review-loop.md` | Only for the full review loop. |
| `../roblox-vfx/references/studio-testing.md` | Before a Studio playtest or capture (code sync and recording traps). |
