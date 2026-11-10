---
type: reference
category: ui
source: "TikTok (screen recording of a TikTok), "Making a Sword-Based RPG Game With Claude, Day #3": Bladebound main menu, News and Store panels"
captured: 2026-11-10
capture: screen
rating: 4
verdict: good
keep: ['panel swap: old content out, old frame out, new frame in, new content in', 'the world stays still behind the swap']
avoid: ['swap total near 600 ms is on the slow side']
tags: [motion, ui-pilot]
---
# UI motion 03 Sword RPG menu

**Source:** TikTok (screen recording of a TikTok), "Making a Sword-Based RPG Game With Claude, Day #3": Bladebound main menu, News and Store panels  ·  **Clip length:** 11.7 s  ·  **fps:** 30  ·  **Capture:** screen
**Rating and verdict:** 4, the owner's ruling 2026-11-10: "It gives off "Elden Ring" vibes, in other words, the UI gives off somewhat of a AAA feel with its looks and matching identities. The consistent color palette and animations also make it worth mentioning."

## Intent
Move between menu pages with weight and calm: a dark fantasy title menu.

## Timeline (ms from the trigger)
| t (ms) | element | what happens | easing / shape |
|---|---|---|---|
| 0 | News text | fades out | ease-in |
| 100 | News bullets | the last thing left, then gone | |
| 270 | News frame | shrinks a little and fades | ease-in, about 70 ms |
| 340 | (nothing) | a single empty beat, about 30 ms | |
| 370 | Store frame | arrives | ease-out |
| 470-570 | Store card art, then list rows | fill in | ease-out |

Swap total about 600 ms: exit about 340, entry about 230.

## Choreography
Exit is the entry in reverse: content leaves before its container; the new container comes before its content. The menu column on the left and the sword in the grass never move: they anchor the eye.

## Look at rest
Dark brown translucent panels with a 1 px light border and a small diamond on the top edge, a serif wordmark, small caps menu items with a dot on the selected one. Quiet and expensive-looking.

## The one detail that makes it work
The empty 30 ms beat between pages: it makes the swap read as two clean events instead of a smear.

## What is weak or sloppy
Double compression (a phone recording a TikTok), so the text is unreadable here. The whole swap is a touch slow for a menu used often.

## Roblox recipe
Two `CanvasGroup`s per panel (frame, content). Exit: content `fade` (0.1 s In), frame `popOut` (0.1 s Quad In) with a `UIScale` 1 -> 0.97. Entry: frame `popIn`, content `enter` 80 ms later.

## Fit for Sculpt Me!
Keep the swap order for the Store tabs and Bag categories (already uses `UIKit.dissolve`: compare). Shorten to under 400 ms for us.

## Keep
- panel swap: old content out, old frame out, new frame in, new content in
- the world stays still behind the swap

## Avoid
- swap total near 600 ms is on the slow side

## Media
![[ui03-panel-swap.jpg]]
