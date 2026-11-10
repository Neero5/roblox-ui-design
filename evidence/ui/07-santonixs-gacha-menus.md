---
type: reference
category: ui
source: "TikTok @santonixs, \"HOW IS EVERYTHING SO CLEAN\": an anime action RPG's character menus (Overview, Weapon, Inventory, Skill Core, Items, Skill tree, Accessories)"
captured: 2026-11-10
capture: screen
rating: 5
verdict: good
keep: ["a left icon rail and the 3D character that never move across pages", "the detail pane cross-fades in place on every selection", "grid cells cascade in by row", "type and rank letters do the hierarchy on a dark glass ground"]
avoid: ["fade through near-black between some pages lasts about 200 ms: a dead beat", "small grey italic descriptions lose contrast"]
tags: [motion, ui-pilot]
---
# 07 santonixs gacha menus

**Source:** TikTok @santonixs, "HOW IS EVERYTHING SO CLEAN" · **Clip length:** 74.7 s (71 s of game) · **fps:** 30 · **Capture:** screen
**Upload file:** `36aeded9-92aed8a94ad59fdbd736523f5a888a24.mp4`
**Rating and verdict:** owner 2026-11-10: "I like this one quite a lot too" (after rating 04 a 5). Claude set 5 from those words; the owner may change it.

## Intent
A character and inventory hub that feels like a premium console gacha game: calm, ordered, every selection answered at once.

## Timeline (ms from the trigger, measured at 30 fps)
| t (ms) | element | what happens | easing / shape |
|---|---|---|---|
| page change Overview -> Weapon (2.0 s) | | | |
| 0 | Overview stats | gone in about 1 frame | cut / very short fade |
| 0-200 | Weapon name, stars, stats, description | fade in, a small upward drift | ease-out |
| 0-400 | the 3D character | draws the sword with an equip pose (the world performs, not the panel) | character animation |
| Inventory open (3.2 s) | | | |
| 0-700 | grid cells | rows light up from the top, about 100 ms a row | stagger by row |
| selection (4.4 s) | | | |
| 0-70 | old detail (name, stars, rank letter, text) | dims | ease-in |
| 70-170 | new detail | fades in where the old stood; the rank letter (E, C, S, SS) as a big faint glyph | ease-out |
| Items page (7.8 s) | | | |
| 0-200 | three slots with large serif numerals 1, 2, 3, the items, light wedges | fade and rise in together | ease-out |
| Items -> Skill tree (8.4 s) | | | |
| 0-100 | Items | fades to near black | |
| 100-200 | (near black) | a dead beat | |
| 200-400 | skill tree | rises out of a glow at the bottom, nodes bottom-up | ease-out |

## Choreography
Two anchors never move: the left icon rail and the character in the middle (on character pages). Every page change keeps them and swaps only the content beside them, so the hub never feels like it reloads. Selection answers on the same frame with an in-place cross-fade of the detail pane (R5). Grids cascade by row (R1 at the cell level). The page-level fade through black (Items -> Skill tree and back) is the one slow spot.

## Look at rest
Dark navy glass over a starfield that drifts slowly (life comes from the world, not the chrome). Thin white hairlines, tiny caps labels, large serif numerals, letter rank badges coloured by rarity, star rows, italic grey descriptions, small pill buttons ("Select", "Switch"). One accent per rarity; lots of empty space.

## The one detail that makes it work
The anchors: the rail and the character stay put while everything else changes, and the character's own animation (drawing the sword) is the "hero motion" of the page.

## What is weak or sloppy
The fade through near black between some pages leaves about 200 ms of nothing (R4 wants the swap, not a pause). Grey italic descriptions are hard to read at this size (R13). The pill buttons are very small.

## Roblox recipe
Rail and character outside the page content. Page content in one `CanvasGroup`: `GroupTransparency` 1 -> 0 with a 6 to 8 px upward offset over about 0.2 s, Quad Out. Detail pane: dim 0.07 s In, swap the text, back in 0.1 s Out. Grid: one beat per row, about 100 ms apart (cap the cascade to about 300 ms for grids opened often, R2). The skill tree rise: a `UIGradient` glow at the bottom plus nodes staggered bottom-up.

## Fit
Premium profile evidence (with 02, 03, 04): in-place detail cross-fade, row cascade, two still anchors, world-driven ambient life, letter-rank hierarchy.

## Media
![[ui07-overview.jpg]] ![[ui07-page-change.jpg]] ![[ui07-grid-select.jpg]] ![[ui07-items-fade-through.jpg]]
