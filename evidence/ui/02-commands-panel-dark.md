---
type: reference
category: ui
source: "TikTok @bbstudios4, "U rid ur Claude of slop ui": a dark admin Commands panel over a grey test baseplate"
captured: 2026-11-10
capture: screen
rating: 4
verdict: good
keep: ['entry by columns, left to right', 'exit faster than entry', 'three type voices: serif title, tracked caps subtitle, light mono rows']
avoid: ['text too small and too low in contrast', 'a glitch exit off-theme for us']
tags: [motion, ui-pilot]
---
# UI motion 02 Commands panel dark

**Source:** TikTok @bbstudios4, "U rid ur Claude of slop ui": a dark admin Commands panel over a grey test baseplate  ·  **Clip length:** 52.6 s  ·  **fps:** 30  ·  **Capture:** screen
**Rating and verdict:** 4, the owner's ruling 2026-11-10: "It's very solid, the whole thing is unique and all its tabs and elements match its red, ninja identity. It's consistent too, but what stands out the most from it are the animations (closing/opening, switching tabs etc)"

## Intent
An admin panel that feels crafted, not a default list: it arrives and leaves with intent.

## Timeline (ms from the trigger)
| t (ms) | element | what happens | easing / shape |
|---|---|---|---|
| 0 | panel | fades in from about 30% to 85% black | ease-out |
| 0-100 | title "COMMANDS" + subtitle | arrive first, full strength | |
| 70-200 | command column (`/UNMUTE`, `/BAN` ...) | appears | |
| 130-270 | argument column (PLAYER, REASON ...) | appears after the commands | |
| 200-300 | description column (right) | arrives last | |
| exit 0-70 | right column | clipped from the right, as if a mask closes | |
| exit 70-200 | the whole panel | dissolves with a horizontal smear | ease-in |

Entry about 300 ms, exit about 130-200 ms. Measured twice (2.9 s and 5.6-6.1 s), the same both times.

## Choreography
Strict reading order: title, then columns left to right; the exit runs the other way (right column first). Nothing bounces. While typing, rows that no longer match simply leave (18-23 s); the panel frame stays put as the anchor.

## Look at rest
Near-black panel at about 85% over the world, one red accent (the logo and the close arrow), a serif title, a widely tracked caps subtitle ("EXECUTE YOUR COMMAND"), slash commands in a light grey, help text right-aligned and dimmer.

## The one detail that makes it work
The column stagger: the panel reads itself to you in the order you would read it.

## What is weak or sloppy
Text is tiny and low-contrast (hard to read even before TikTok compression). The red arrow as a close button is unclear. The smear exit is a sci-fi/glitch flavour.

## Roblox recipe
Each column in its own `CanvasGroup`; tween `GroupTransparency` 1 -> 0 with `UIKit.MOTION.enter` (0.22 s Quad Out), started 60-70 ms apart. Exit: a `UIGradient` transparency mask whose offset sweeps right to left on the right column, then `fade` on the whole group.

## Fit for Sculpt Me!
Keep the column stagger and the reverse exit for list panels (quests, Settings, the code box). Refuse the dark palette and the glitch smear: our panels are marble and wood.

## Keep
- entry by columns, left to right
- exit faster than entry
- three type voices: serif title, tracked caps subtitle, light mono rows

## Avoid
- text too small and too low in contrast
- a glitch exit off-theme for us

## Media
![[ui02-open-close.jpg]] and ![[ui02-exit.jpg]]
