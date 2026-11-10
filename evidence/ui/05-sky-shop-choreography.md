---
type: reference
category: ui
source: "TikTok @6ix13, "Completely made by ai / Go and start printing": a simulator Shop with Exclusives, Passes, Boosts"
captured: 2026-11-10
capture: screen
rating: 3
verdict: fine
keep: ['an entry choreographed in beats', 'ornaments that come from the theme (cloud puffs in a sky shop)', 'ambient life only in the featured item (the jet fly-by)']
avoid: ['"Insert description here..." shipped', 'a 1.5 s entry for a shop opened often', 'every card fully saturated: no hero', 'scramble-decode text off-theme']
tags: [motion, ui-pilot]
---
# UI motion 05 Sky shop choreography

**Source:** TikTok @6ix13, "Completely made by ai / Go and start printing": a simulator Shop with Exclusives, Passes, Boosts  ·  **Clip length:** 60.4 s  ·  **fps:** 30  ·  **Capture:** screen
**Rating and verdict:** proposed by Claude (2026-11-10), the owner rules.

## Intent
Make the shop feel lively and premium: a reward to open.

## Timeline (ms from the trigger)
| t (ms) | element | what happens | easing / shape |
|---|---|---|---|
| 0 | header bar and empty body | already there | |
| 400 | basket icon | drops onto the header corner | Back Out |
| 400-800 | four cloud ornaments | puff in at the corners with small particle puffs | Back Out + particles |
| 500-1100 | section title "Exclusives" | scramble-decodes (random letters resolve), on a glowing bar | |
| 1000-1200 | featured card | slides in from the right | Quad/Quint Out, about 200 ms |
| 1300 | jet | flies in across the card with a trail | |
| 1500 | card text | scramble-decodes | |
| ambient, about every 3 s | jet | crosses the card with a contrail, a sonic-boom ring and a cloud puff (about 700 ms) | |

Entry total about 1.5 s in six beats about 100-200 ms apart.

## Choreography
Container, then decoration, then the label, then the card, then the hero, then the text. Clear and readable, just too long. Tabs scroll with the same cards; Passes and Boosts each get their own saturated card colour.

## Look at rest
Sky backdrop, a blue patterned header, cloud ornaments on the corners, cards with full-strength gradients (blue, orange, purple, green), strikethrough old prices, "LIMITED TIME ONLY!" and "BEST DEAL!" tags.

## The one detail that makes it work
The jet fly-by: the featured item performs itself, on a slow loop, while the chrome stays still.

## What is weak or sloppy
Placeholder text ("Insert description here...") is the loudest slop tell in the set. The entry is three to four times too long for a frequently opened panel. All cards shout equally. Decoding text is a sci-fi idea in a cloud shop.

## Roblox recipe
Beats as a timed list (`task.delay` per beat, or one sequence helper); ornaments `popIn` on a `UIScale` with a small `ParticleEmitter` puff inside a `ViewportFrame` or a sprite flipbook; ambient fly-by on a 3-5 s timer, paused under Reduced Motion and while the panel is hidden.

## Fit for Sculpt Me!
Keep the beat order and the hero-only ambient loop (our Store Featured block, the kiosk). Compress the entry to about 350 ms. Refuse the scramble text and the all-saturated cards.

## Keep
- an entry choreographed in beats
- ornaments that come from the theme (cloud puffs in a sky shop)
- ambient life only in the featured item (the jet fly-by)

## Avoid
- "Insert description here..." shipped
- a 1.5 s entry for a shop opened often
- every card fully saturated: no hero
- scramble-decode text off-theme

## Media
![[ui05-open.jpg]] and ![[ui05-ambient.jpg]]
