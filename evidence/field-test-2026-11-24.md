# Field test 2 (owner, 2026-11-24): the skill on an invented HUD

The owner ran the skill (v0.3.1, Mode A, light check) from the CLI on the Azurath test place, for an invented game "Inkbound" (identity: "a scribe's ink-and-brush duel", genre profile rpg). Built: an ability slot with an ink-refill cooldown and a READY seal, and a target bar with a seal icon. The profile, written in the prompt, listed theme words as objects (seal stamp, rice paper, ink soaking).

Captures: `ui/media/ft2-inkbound-cooldown.png` (mid-cooldown, target bar up), `ui/media/ft2-inkbound-ready.png` (ready state).

Owner's words: "the UIs my claude build always end up looking like this cartoony, unprofessional type of thing. Like the typical thing that screams AI slop."

What read as slop (review the same day):
- 2 to 3 px black strokes on every panel, track and slot (Roblox default look).
- A large opaque cream box around one thin health line; the frame outshone the content and the fight.
- Theme words drawn as stickers: a square with a diamond as the seal, the word READY on a stamp spilling past the slot, grey dashes as paper grain.
- Two type worlds: a blackletter-style serif beside Roblox's chunky outlined numbers.
- A stepped, blocky ink-refill edge.
- Placeholder text "Dummy1" (R12).

Cause: built from primitives only (Frames, UIStroke, text), with no textures, and the rules judged identity and motion but not static craft, so the light check passed it. Part of the cause was the prompt: theme words given as a list of props.

Change made (owner: "Yes please"): Craft rules C1 to C7 in `skills/roblox-ui-design/references/core-rules.md`, anti-slop items 14 to 20, an Assets step in Mode A, craft ticks in the light check.
