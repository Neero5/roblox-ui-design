---
name: roblox-ui-motion
description: Use whenever building, changing or reviewing Roblox UI that a player sees move or respond. Covers ScreenGui / SurfaceGui / BillboardGui work in Luau such as menus, HUDs, panels, shops, inventories, popups, toasts, tabs, carousels, reward and purchase screens, open/close transitions, TweenService or TweenInfo tweens on GuiObjects, UIScale pops, CanvasGroup fades, hover/press feedback, idle UI animation and Reduced Motion handling. Also use when asked to make Roblox UI feel polished, premium, juicy or less like AI slop, or to review UI motion from screenshots. Do not use for Luau work with no visible UI (data stores, gameplay logic, networking), for 3D world VFX, or for character animation.
---
# Roblox UI motion

Goal: UI that belongs to one nameable world and moves like a careful studio made it. Identity first, then motion: subtle, ordered, legible, on theme. "Too much is less": when in doubt, remove motion.

The rules come from measured reference clips and an owner's ratings and rulings. The owner scores identity first (generic loses even when tidy, showing off loses even when eye-catching) and animation quality second. Evidence is thin (seven clips), so every number says where it comes from; numbers lean on the clips rated 4 or more. Follow the numbers anyway: they are what makes two builds look alike.

## Step 0: read the game's UI profile (always first)

1. Look in the game's repo for `docs/ui-profile.md`. If it is not there, search for a file with `type: ui-profile` in its front matter, or named `ui-profile*`.
2. If found: read it. It must state the game's IDENTITY in a few words a player could say (a world, for example "red ninja clan", not adjectives such as "clean, modern") and may name one benchmark game. If the identity is missing or only names the genre, stop and settle it with the owner before any build: propose two or three statements drawn from the game's world, the owner picks. The profile also names the genre profile, the theme vocabulary, the refused effects, the existing motion tokens and any overrides. An override in the game's profile beats the genre profile. Nothing beats a core rule except an owner's written override that cites the rule id.
3. If missing: do not guess silently. Read the template at `../../templates/project-profile.md` relative to this SKILL.md (the plugin root's `templates/` folder), fill in what the repo shows (style guide, existing tween code, palette), then ask the owner to pick the genre from `references/profiles/` and confirm the identity and the theme vocabulary. Save it as `docs/ui-profile.md` in the game's repo. If the template cannot be read, the fields are: identity, benchmark (optional, with the borrowed principles), genre profile, audience and pace, theme vocabulary, refused effects, Reduced Motion policy, existing motion tokens (path and values), overrides (rule id, new value, owner's reason), style guide and decision log paths.
4. Read the genre profile file it names: `references/profiles/<genre>.md`. If the genre has no profile, use the closest one, say so, and follow `references/profiles/_how-to-add-a-profile.md`.
5. Find the game's existing motion table (one module holding durations and easings). Use its tokens. If none exists, create one before animating anything. Never scatter raw `TweenInfo.new(0.3)` literals through panel code.

## Core rules (always true; details and checks in `references/core-rules.md`)

Identity (checked first; a build that passes every R rule and fails I2 is a fail):
- **I1 Identity.** Every panel, tab, icon, colour and motion belongs to the one identity stated in the game's profile.
- **I2 Generic fails.** Consistent but interchangeable is a fail: with the logo hidden, a player must still tell which game this is. Tick the genre's default tells listed in the profile.
- **I3 Serve, don't show off.** Every motion has a job for the player. When every element performs, the screen reads as trying too hard.
- **I4 Benchmark.** The profile may name one successful game: match its execution principles (anchors, restraint, type, timing, hierarchy), never its art, logos, icon sets, exact layouts or trade dress.

Motion:
- **R1 Beats.** An entry is ordered: container, header, content, hero last. Beat count and stagger come from the profile (a profile may allow one beat).
- **R2 Budget by frequency.** Panels opened often: whole entry 350 ms or less. Rare moments (win, rare drop, first open of the day): 800 ms or less.
- **R3 Exit.** About half the entry time, in reverse order: content leaves first, container last.
- **R4 No overlap.** On a swap the old panel finishes leaving before the new one starts. Never two panels visibly on top of each other.
- **R5 In-place change.** A value that changes (carousel, tab name, counter) cross-fades where it stands in about 200 ms. The panel does not slide.
- **R6 Still anchor.** Something stays perfectly still in every transition: the frame, the avatar or the world.
- **R7 Idle motion in the hero only.** Cycle 3 s or longer. The chrome never moves at rest. (The profile sets the budget; some genres allow none.)
- **R8 One hero.** Exactly one element per screen gets full saturation, glow or idle motion. Everything else steps down.
- **R9 Type first.** Hierarchy comes from type before colour or boxes: three voices at most (small label, large value, muted line).
- **R10 On theme.** Every effect comes from the game's theme vocabulary in its profile. Nothing from the profile's refused list. Nothing borrowed from another genre.
- **R11 Small overshoot.** A pop peaks at 105% or less and is at rest within 200 ms.
- **R12 No placeholder text.** No "Insert description here", lorem ipsum, raw ids, "TODO", "Label". Read every visible string.
- **R13 Legible first.** Every text is readable on the worst thing that can be behind it. Contrast beats elegance.

Forbidden everywhere: the genre's default look taken as the design; motion added to display the UI kit; everything appearing at once; everything fading at the same speed; every element bouncing; Linear easing on anything that is not a loop; Bounce or Elastic easing on panels; an entry longer than the action it leads to; motion that ignores Reduced Motion.

## Build workflow

1. **Name the identity.** Copy the identity statement (and the benchmark's borrowed principles, if any) from the profile. For each element of the screen (frame, header, tabs, icons, buttons, type, colour, motion) write one line: how it expresses the identity. Tick the genre profile's "Generic tells": each one present needs a reason from the identity or is redesigned now, before any motion work. A blank line is a stop.
2. **State the moment.** One line: what must the player understand or feel, how often they see it (frequent or rare), what the hero is, what the still anchor is.
3. **Write the beat table BEFORE any code.** One row per moving element, entry and exit both:

   | # | element | start ms | duration ms | easing (style, direction) | property (from -> to) | job for the player |
   |---|---|---|---|---|---|---|

   A row with no job is cut (I3).

   Add the totals: entry total (trigger to the last element at rest), exit total, largest overshoot in percent of the element's size, count of elements with idle motion.
4. **Check the table against the numbers** in the genre profile and the core rules. Fix the table, not the rules. If a number must break a rule, stop and ask the owner; record the answer as an override in the game's profile.
5. **Write the Reduced Motion column.** For each row: what happens when `GuiService.ReducedMotionEnabled` is true (see `references/roblox-recipes.md`). No row may be left blank.
6. **Build it** with the game's motion table and the patterns in `references/roblox-recipes.md`: set every start state before the first frame, run beats through one sequence helper, cancel the running sequence on re-open or early close, keep input alive during the entry.
7. **Review loop** (below). The work is not done until it passes.

## Review loop (required; details in `references/review-loop.md`)

One screenshot of the resting state proves nothing about motion.

1. **Capture a frame sequence** of the entry, the exit and one swap or value change: slow the motion with the debug time scale and take at least 8 frames per transition, each showing the elapsed-ms label. Also record the numeric trace for timing.
2. **Measure** the totals from the frames and the trace. Compare with the beat table. A difference of more than one captured frame is a defect.
3. **Grade** with a reviewer that did not write the code (a fresh subagent given only the frames, the beat table, the game's profile, the genre profile and `core-rules.md`). The reviewer fills the grading form: identity first (I1 to I4, with the generic check: a second reviewer who has not read the profile does the hide-the-logo test on masked rest screenshots, and the genre's tells are ticked), then pass or fail per core rule, per profile number and per anti-slop item, each with the frame that proves it.
4. **Fix every fail, then recapture.** Do not argue with a fail by description; show the frame.
5. **Capture once more with Reduced Motion on.** Everything must still work and nothing may move.
6. **Escalate to the owner** for anything the frames cannot settle: feel at real speed, sound, whether the identity reads to a player, a rule that seems wrong for this game. Report what was checked by frames and what is still owed to the owner's eyes. Never report motion as verified from code alone.

## Reference files (load only when needed)

| File | Load it when |
|---|---|
| `references/core-rules.md` | Writing a beat table for the first time in a session, grading a build, or a rule's exact wording or check is needed. Holds the identity rules with their checks and the anti-slop checklist. |
| `references/profiles/<genre>.md` | Always, once per session, for the game's genre (step 0). |
| `references/profiles/_how-to-add-a-profile.md` | The game's genre has no profile, or the owner wants to change profile numbers. |
| `references/roblox-recipes.md` | Before writing or changing tween code: easing facts, CanvasGroup fades, UIScale pops, gradient sweeps, the sequence helper, cancelling, Reduced Motion, text bounds, sparkle, performance. |
| `references/review-loop.md` | Before capturing or grading: capture set-up, measuring, the grading form, escalation. |

## Report format when the work is done

The identity statement with the per-element lines, the final beat table, the measured totals next to the planned ones, the grading form with frame references, what Reduced Motion does, any override requested, and the list of things still owed to the owner's eyes.
