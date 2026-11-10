---
type: reference
category: ui
source: "TikTok @weekndviolence, "Day 2 of making a game with ChatGPT and Claude": Aftertwelve start screen, slot select, origin/wield/home carousels, character creation, Satchel inventory"
captured: 2026-11-10
capture: screen
rating: 5
verdict: good
keep: ['value changes cross-fade in place, about 200 ms', 'the character stays still as the anchor', 'type carries the hierarchy: tracked label, large value, muted line']
avoid: ['faint text on bright snow', 'a frame where two screens overlap (10.0 s)']
tags: [motion, ui-pilot]
---
# UI motion 04 Aftertwelve menus

**Source:** TikTok @weekndviolence, "Day 2 of making a game with ChatGPT and Claude": Aftertwelve start screen, slot select, origin/wield/home carousels, character creation, Satchel inventory  ·  **Clip length:** 63.3 s  ·  **fps:** 30  ·  **Capture:** screen
**Rating and verdict:** 5, confirmed by the owner 2026-11-10 ("04's pretty solid").

## Intent
A calm, premium onboarding: choices feel considered, not busy.

## Timeline (ms from the trigger)
| t (ms) | element | what happens | easing / shape |
|---|---|---|---|
| carousel step 0 | value ("HEARTHVALE") | dims to about 40% | ease-in, about 100 ms |
| 100 | new value ("SALTCREST") + description + pager dot | arrive together in place | ease-out, about 100 ms |
| page step 0 | the whole text block | fades out | about 100 ms |
| 100-200 | the next page's block | fades in, same position | about 100 ms |

No slide anywhere: changes happen in place. Total per change about 200 ms.

## Choreography
Everything that depends on the choice (name, sub-line, description, dots) changes as one beat. The 3D character on the right never moves between pages, so the screen never feels like it is "loading".

## Look at rest
Text sits straight on the world, no panel, on a soft vignette. Left third text, right third the character, the middle empty. Three type voices: a tiny widely tracked caps label ("WIELD STYLE"), a large tracked value ("VANGUARD"), a small muted line. Hairline buttons with small corner caps, diamond arrows for the carousel, dot pager.

## The one detail that makes it work
Restraint: one font family, one accent (a pale teal), no boxes. Hierarchy comes from size and letter-spacing alone.

## What is weak or sloppy
Thin pale text loses against the bright snow (contrast). At 10.0 s the two pages overlap for a frame. Hairline buttons nearly vanish at small sizes. Risk of everything being the same grey.

## Roblox recipe
Value label + sub-line + description in one `CanvasGroup`; on step: `GroupTransparency` 0 -> 0.6 over 0.1 s In, swap the text, back to 0 over 0.1 s Out. Tracking: Roblox has no letter-spacing on `TextLabel`; use `RichText` with spaces or a font with wide caps, or per-letter labels for big titles only.

## Fit for Sculpt Me!
Keep the in-place cross-fade for Pick the Theme, the Daily Rewards day hero and the Store Featured name. Keep the anchor rule. Refuse the bare-text-on-world look: our panels stay marble and wood, and must stay legible.

## Keep
- value changes cross-fade in place, about 200 ms
- the character stays still as the anchor
- type carries the hierarchy: tracked label, large value, muted line

## Avoid
- faint text on bright snow
- a frame where two screens overlap (10.0 s)

## Media
![[ui04-carousel.jpg]] and ![[ui04-overview.jpg]]
