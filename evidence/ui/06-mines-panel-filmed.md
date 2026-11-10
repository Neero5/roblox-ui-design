---
type: reference
category: ui
source: "TikTok @ecrobloxgroup, "Did claude cook?": a mining sim Mines travel panel, a travel cut-scene, Pickaxe Skins"
captured: 2026-11-10
capture: filmed
rating: 3
verdict: fine
keep: ['panel pop with a small overshoot', 'a location title card as the travel transition ("VOID ABYSS / NOW ARRIVING")', 'skin panel: big preview left, grid right, Roll x1 / x10']
avoid: ['dense grid where every card has equal weight']
tags: [motion, ui-pilot]
---
# UI motion 06 Mines panel filmed

**Source:** TikTok @ecrobloxgroup, "Did claude cook?": a mining sim Mines travel panel, a travel cut-scene, Pickaxe Skins  ·  **Clip length:** 28.3 s  ·  **fps:** 29.97  ·  **Capture:** filmed
**Rating and verdict:** proposed by Claude (2026-11-10), the owner rules.

## Intent
Choosing where to go should feel like a trip, not a menu click.

## Timeline (ms from the trigger)
| t (ms) | element | what happens | easing / shape |
|---|---|---|---|
| 0 | Mines panel | appears at about 92% size, blurred | |
| 70 | | overshoots to about 102% | Back Out |
| 200 | | settles at 100% | |

Filmed off a curved monitor: timing within about 1 frame, colours unreliable.

## Choreography
One pop for the whole panel (no stagger). The scroll carries motion blur. Travel: the panel closes, a title card with particles announces the place, a cart ride, then the new place.

## Look at rest
Teal header, red X, a hero event card on top ("Haunted Hollow", "ENDS IN 10 DAYS", TRAVEL), then a grid of mine cards with art, name, a gem row and TRAVEL / "YOU'RE HERE".

## The one detail that makes it work
The location title card: a change of place gets its own moment.

## What is weak or sloppy
Filmed. Dense. The grid cards have identical weight under the hero.

## Roblox recipe
Pop = `UIScale` 0.92 -> 1 with `MOTION.popIn` (0.18 s Back Out); Roblox's Back overshoot is already about this size.

## Fit for Sculpt Me!
Keep the title-card idea for the Gallery/Reveal phase changes and the Hall of Fame wing entrance. The pop matches our `popIn` already.

## Keep
- panel pop with a small overshoot
- a location title card as the travel transition ("VOID ABYSS / NOW ARRIVING")
- skin panel: big preview left, grid right, Roll x1 / x10

## Avoid
- dense grid where every card has equal weight

## Media
![[ui06-open-scroll.jpg]]
