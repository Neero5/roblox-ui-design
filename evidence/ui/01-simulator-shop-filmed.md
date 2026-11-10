---
type: reference
category: ui
source: "TikTok @93fuzzy, "Claude made ts in 2 prompts": a simulator HUD, Shop, Rebirth and Daily Rewards"
captured: 2026-11-10
capture: filmed
rating: 2
verdict: fine
keep: ['NOW > AFTER comparison card for an upgrade', 'icon tab rail beside the panel']
avoid: ['eight colours at equal weight', 'generic simulator template']
tags: [motion, ui-pilot]
---
# UI motion 01 Simulator shop filmed

**Source:** TikTok @93fuzzy, "Claude made ts in 2 prompts": a simulator HUD, Shop, Rebirth and Daily Rewards  ·  **Clip length:** 16.2 s (12 s of game)  ·  **fps:** 30  ·  **Capture:** filmed
**Rating and verdict:** proposed by Claude (2026-11-10), the owner rules.

## Intent
Show a whole simulator UI kit at a glance: HUD, Shop (Eggs, Passes), Rebirth, Daily Rewards.

## Timeline (ms from the trigger)
Not measurable: a phone filmed the laptop by hand, so the camera shake is larger than any UI motion (the motion graph is flat noise). Panel open/close is visible at 3.7 s, 6.5 s, 9.3 s and 11.8 s but its timing cannot be read.

## Choreography
Not readable.

## Look at rest
Bright blue headers, a red close X, a right-hand icon rail (Featured, Eggs, Passes, Speed, Wins, Codes), saturated cards. The Rebirth panel puts NOW and AFTER side by side with an arrow between (x3 Speed > x3.5 Speed): the clearest piece of UI in the clip.

## The one detail that makes it work
The NOW > AFTER card: a reward explained as a before/after pair needs no reading.

## What is weak or sloppy
Every element is loud at once: no hero. Dense. Reads as a template. Filmed, so colours are the laptop screen's, not the game's.

## Roblox recipe
Comparison card = two `UIKit.panel` tiles and an arrow icon, values in the body size, the gain in the accent colour.

## Fit for Sculpt Me!
Adapt only the comparison card idea (for example the Bag slot unlock, Lucky Blocks). Refuse the density and colour count.

## Keep
- NOW > AFTER comparison card for an upgrade
- icon tab rail beside the panel

## Avoid
- eight colours at equal weight
- generic simulator template

## Media
![[ui01-overview.jpg]]
