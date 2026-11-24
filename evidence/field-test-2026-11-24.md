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

## Field test 2b (same evening): textures, no boxes

Rerun with v0.4.0, the owner's ink textures as assets, ui09 as the reference, and a prompt (written by Claude) that said "no panels or boxes behind HUD elements". Capture: `ui/media/ft2b-inkbound-textured.png`.

Owner: "It did do exactly what was stated by using textures and all but, it looks so poor and not rich at all. It lacks professionalism."

What read wrong: the bar had no track or max (fill fades into the sky); the ability slot lost its surface and read as a floating smear, with no readable state; one stretched texture per element with nothing under or around it; thin light serif text straight on bright sky (R13). Cause: overcorrection from the prompt; C3 was read as "no containers at all".

## Field test 3 (same evening): look first, as a mockup

The same HUD built by Claude in chat as an HTML mockup on a cleaned capture of the test scene, with a states sheet on bright sky and dark ground, six to seven layers per element (underlay, gradient body, inner highlight, track, ticks, end caps, scrim), EB Garamond to match `Enum.Font.Garamond`, vermilion used once. Then rebuilt in Figma as variables, effect styles, text styles and variant components (file "Inkbound HUD" in the owner's Figma drafts).

Owner: "It looks wonderful. Genuinely it's one of the best UI I have so far seen from any mockups claude has produced for me throughout my entire Sculpt Me development session."

What made the difference (review the same evening): layer count; designing on the real game capture; a brief written against the two named failures; every state on the worst backgrounds; no other style skill in play (the owner's Sculpt Me sessions had a cartoon menu kit installed); the look made by the strongest model.

Changes made (owner: "add whatever I could apply ... to the skill"): Mode A steps 6 and 7 (mock the look first on a real capture, then port layer by layer with a port table), Mode D (Figma frame to UI), Step 0 item 4 (other style skills), Craft rules C8 (layers) and C9 (restraint is not absence), anti-slop items 21 and 22, mockup comparison in the light check.
