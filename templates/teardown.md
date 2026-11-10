---
type: reference
category: ui            # ui | vfx | animation
source:                 # creator handle + what it is; the video stays OUT of git
captured:
capture: screen         # screen (screen recording) | filmed (phone at a monitor: no timing, no colour)
rating: 3               # owner's 1-5; Claude proposes, the owner sets it
verdict:                # good | fine | bad (the owner's call)
keep: []
avoid: []
tags: [motion]
---
# <title>

**Source:**  ·  **Clip length:**  ·  **fps:**  ·  **Evidence:** `tools/reference/extract.py` sheets in `media/ui-motion/`

## Intent
What the moment must make the player feel or understand, in one line.

## Timeline (ms from the trigger, measured in frames at the clip's fps)
| t (ms) | element | what happens | easing / shape |
|---|---|---|---|
| 0 | | | |

Total: … ms. Exit vs entry: …

## Choreography
Order of arrival, stagger between elements, what leads and what follows, what is still while the rest moves.

## Look at rest
Type (case, tracking, weights), colour roles, density, framing, how it sits on the world behind.

## The one detail that makes it work

## What is weak or sloppy
(Name it even in a good clip: placeholder text, jank, too long, noise.)

## Roblox recipe
Which tools build it here: `TweenService` (style/direction), `UIGradient` offset, `CanvasGroup.GroupTransparency`, `UIScale`, `ClipsDescendants` masks, `ParticleEmitter` in a `ViewportFrame`, text effects, etc. Name the `UIKit.MOTION` entry it maps to, or the new one it needs.

## Fit for Sculpt Me!
Keep / adapt / refuse, against [[Pillars]] and the owner's "subtle, not noisy" rule.
