---
name: roblox-ui-design
description: Use when turning a Roblox UI mockup, sketch, wireframe, screenshot or written idea into a professional, finished UI (layout, look and motion), when building or changing Roblox UI that players see (ScreenGui, SurfaceGui, BillboardGui menus, HUDs, panels, shops, inventories, popups, toasts, tabs, reward and purchase screens, transitions, tweens, hover and press feedback), or when asked to make Roblox UI look polished, premium or less like AI slop, or to audit existing UI. Do not use for Luau work with no visible UI, for 3D world VFX, or for character animation.
---
# Roblox UI design

Goal: take the owner's simple mockup (plus a prompt, and references when given) and return a UI that looks made by a careful studio: it belongs to one nameable world, has one clear hero, reads at a glance and moves with restraint. The owner scores **identity first, animation quality second**; generic loses even when tidy, showing off loses even when eye-catching.

## Cost rules (always)

- **Light by default.** No subagents unless the owner asks for them. One pass, one capture, one self-check.
- **Ask before spending.** If the work needs more than the request implies (a redesign of a whole screen, several directions, a full review loop), say so in one line and ask first.
- **Small requests get small answers.** A tweak is a tweak: do not re-plan the screen around it.

## Step 0: read the game (once per session)

1. The game's profile: `docs/ui-profile.md` (or a file with `type: ui-profile`). It states the IDENTITY, an optional benchmark, the genre profile, theme vocabulary, refused effects, Reduced Motion policy, motion tokens and overrides. If it is missing, draft one from `../../templates/project-profile.md` (plugin root `templates/`) and what the repo shows, and ask the owner to confirm the identity and the genre before designing.
2. **The owner's rulings win.** Read the game's decision log and style rules (the profile lists their paths). Any value, layout or effect the owner has ruled on is FROZEN: never change it on your own. If a skill rule disagrees with a ruling, you may propose the change in one line; the ruling stands until the owner says otherwise.
3. The genre profile `references/profiles/<genre>.md` and the game's existing UI kit (its panel, button and motion modules). Build with the kit; never paste a second kit beside it.

## Mode A: mockup to UI (the main use)

1. **Read the mockup's intent.** For every box in the sketch: what it is, its job for the player, and which one is the hero. Keep the owner's arrangement (what sits where); your job is to elevate its treatment, not to move things around. If something must move (overlap, an edge, a rule), say what and why.
2. **Read the references, if any.** Take principles (hierarchy, anchors, spacing, timing, material), never art, logos, icon sets or exact layouts (I4). A video reference: run `tools/extract.py` from the plugin root on it first.
3. **Write a short design brief before any code** (10 lines at most): identity statement; how the frame, header, buttons, type, colour and icons express it (I1); the hero and how it stands out (R8); the three type voices (R9); the genre tells present and why they stay or go (I2); the entry and exit in one line each with their budgets (R1 to R3); what Reduced Motion does.
4. **Lay it out with craft** (`references/layout-craft.md`): a spacing scale, an alignment grid, depth layers, every state (hover, pressed, selected, disabled, empty, locked), real content lengths, two window sizes.
5. **One direction by default.** Make it the best you can. Offer a second direction only when the owner asks, or when the brief shows two genuinely different readings of the mockup (then ask which first).
6. **Show it before wiring it.** If the game's workflow reviews looks first (a mockup or a Studio screenshot), stop there for the owner's notes. Then build the behaviour and motion.

## Mode B: build or change UI (a known design)

Follow the brief or the owner's note exactly. Motion: plan the beats in a small table (element, start ms, duration, easing, property, job for the player) only when there are three or more moving parts; otherwise one line. Use the game's motion tokens; never scatter raw `TweenInfo.new` literals.

## Mode C: audit existing UI

Do not edit. Return a short ranked list: the finding, the rule it breaks (id), the frozen ruling it touches (if any), the suggested fix, its size (small/medium). The owner picks; then switch to Mode B for the picked items only.

## Rules (details and checks in `references/core-rules.md`)

Identity, checked first: **I1** every element belongs to the one identity; **I2** consistent but interchangeable is a fail (hide the logo: could this be any game of the genre?); **I3** every motion has a job for the player, nothing performs to show off the kit; **I4** a benchmark lends principles only.
Layout and look: **L1** two surfaces at most; **L2** rarity colour is a system, only where it informs; **L3** the hero owns the centre, text in side columns; **L4** top bar, tabs and primary button stay put on every tab; **L5** one primary action, in the same place on every screen; **L6** one ornament family; **L7** more important screen, more empty space; **R8** one hero per screen; **R9** hierarchy from type first, three voices at most; **R10** effects from the game's theme vocabulary only; **R12** no placeholder text; **R13** legible on the worst background.
Motion: **R1** entries in beats, hero last; **R2** frequent panels 350 ms or less, rare moments 800 ms or less; **R3** exits 40 to 65% of the entry, reverse order; **R4** no two panels visibly overlapping; **R5** in-place changes cross-fade 160 to 240 ms; **R6** something stays still; **R7** idle motion only in the hero; **R11** overshoot 5% or less, at rest within 200 ms.
Engineering: **E1** Reduced Motion: no scale, slide, stagger or loop, changes still visible; **E2** interruptible; **E3** input live from the first visible frame; **E4** one motion table; **E5** start states set before the first frame.

## Check (light by default; full loop only on request)

Light check, every time: one capture of the result at rest (and one mid-transition if motion changed), then tick in a few lines: identity carriers visible, two surfaces at most, the hero in the centre, anchors and the primary button in their places, one hero, three type voices or fewer, legible, no placeholder text, nothing frozen changed, Reduced Motion handled. Fix what fails. Report what still needs the owner's eyes.
Full review loop (`references/review-loop.md`): only when the owner asks, or for a new full screen or a rare moment, and only after asking.

## Report

Two to six lines: what changed, the brief (Mode A), what the light check found, anything frozen you proposed but did not change, what the owner should look at.

## Reference files (load only when needed)

| File | Load it when |
|---|---|
| `references/layout-craft.md` | Mode A, or any new layout. |
| `references/core-rules.md` | A rule's exact wording or check is needed, or an audit. |
| `references/profiles/<genre>.md` | Step 0. |
| `references/roblox-recipes.md` | Writing tween or layout code. |
| `references/review-loop.md` | Only for the full review loop. |
