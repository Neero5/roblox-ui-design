---
profile: simulator
status: evidenced (thin)
evidence: [01, 05, 06]
---
# Profile: simulator

Bright, lively, bouncy: pet, clicker, tycoon, mining and collecting games with a young audience and panels opened very often.

**How strong is this profile?** Weak. Three clips, none rated above 3 by proposal (the owner has not confirmed those ratings). 05 is the only screen recording; 01 and 06 were filmed off a monitor (01 gives layout only, 06 timing within about one frame). Much of this profile is the adopted core rules applied to the genre plus counter-examples (what 01 and 05 got wrong). Rows marked "guess" have no clip behind them.

Source column: an evidence id, "core Rn" (the adopted rule sets the bound), "worked example" (one game's shipped values, not a simulator), or "guess".

## Entry and exit

| Parameter | Value | Source |
|---|---|---|
| Beats, frequent panel | 1 to 3. Default 2: panel pop, then content. | 06 (1 beat), core R1; "2" is a guess |
| Beats, rare moment | 4 to 6 | 05 (6 beats, order good) |
| Beat order | container, ornaments, section label, content card, hero, hero text | 05 |
| Stagger | 50 to 80 ms frequent; 80 to 150 ms rare | core R1; 05 measured 100 to 200 ms |
| Duration of one beat | 150 to 200 ms | 06 (200 ms), 05 (card slide about 200 ms) |
| Entry total, frequent | 250 to 350 ms | core R2; 06 (about 200 ms for one beat) |
| Entry total, rare | 500 to 800 ms | core R2; 05 (1500 ms was too long) |
| Exit total | 100 to 180 ms, one or two beats | core R3; no simulator exit was measured: guess |
| Panel swap total | 400 ms or less | guess |
| In-place value change | 160 to 240 ms cross-fade; a number that goes up may also pop (below) | core R5; guess |

## Pops and easing

| Parameter | Value | Source |
|---|---|---|
| Panel pop start scale | 0.92 | 06 |
| Panel pop peak | 102% (allowed 101% to 104%) | 06; range is a guess inside core R11 |
| Settle | at rest by 200 ms | 06, core R11 |
| Entry easing | Back Out for the panel and ornaments; Quad or Quint Out for slides and content | 05, 06 |
| Exit easing | Quad In, no overshoot | core R3; guess |
| Elements that may overshoot in one entry | 2 at most (the panel, plus the hero or one ornament group) | guess; anti-slop "every element bounces" |
| Value-change pop | 8% up, back within 300 ms | worked example |
| Forbidden easing | Bounce, Elastic, Linear (except loops) | core R11, anti-slop |

## Idle motion

| Parameter | Value | Source |
|---|---|---|
| Idle budget | 1 looping element per screen: the hero | core R7, 05 |
| Cycle | 3 to 5 s | 05 (about 3 s); upper bound guess |
| Active part of the cycle | 700 ms or less | 05 |
| Chrome at rest | still | 05 |
| Second idle element (for example a "claim" badge that needs attention) | only by an override in the game's profile | owner: "depends on the game" |

## Colour and hero policy

| Parameter | Value | Source |
|---|---|---|
| Hero | 1 per screen, placed first (top or left), larger than grid cards | 06 (hero event card on top), core R8 |
| Full-strength accent hues on one screen | 3 at most, plus the hero | guess; 01 (eight at equal weight) and 05 (four saturated cards) are the counter-examples |
| Non-hero cards | one shared card colour or a clearly lower saturation than the hero (start at 70% of the hero's saturation); no glow | guess; 05, 06 counter-examples |
| Urgency tags ("LIMITED", "BEST DEAL") | 1 per screen | guess; 05 counter-example |
| Upgrade or rebirth explanation | a NOW > AFTER pair with an arrow | 01 |
| Ornaments | from the theme vocabulary, on the frame corners, arriving as one beat | 05 (cloud puffs) |

## Type and legibility

| Parameter | Value | Source |
|---|---|---|
| Voices | 3 at most; bold rounded display face is normal here | core R9; guess |
| Minimum text size | 14 px at the design resolution | guess (worked example) |
| Text on saturated cards | white with a dark stroke, or dark on a light plate | guess; core R13 |

## Sound and feedback

No clip was analysed for sound. All guesses, taken from one game's rulings as a starting point.

| Parameter | Value | Source |
|---|---|---|
| Press feedback | starts within 50 ms: squash 4% to 6%, spring back on release | worked example; guess for the upper value |
| Sounds | one cue per action; open and close cues; a rising cue for purchase or claim; hover near silent | worked example |
| Reward moment | pop on the changed element, optional short particle burst from the theme vocabulary, 800 ms or less | core R2; guess |

## Reduced Motion

| Parameter | Value | Source |
|---|---|---|
| Entry and exit | instant, or an opacity fade of 150 ms or less | guess (worked example uses instant); core E1 |
| Pops, squash, ornaments' puff, idle loop, particles | off; ornaments simply present | core R7; guess |
| Value changes | text swaps instantly | guess |

## Forbidden in this profile (beyond the core)

- A long choreographed entry on the shop or inventory (05).
- Scramble or decode text unless the game's theme vocabulary includes it (05).
- More than one saturated gradient card style per row (05).

## Default beat table: frequent panel (starting point)

| # | element | start ms | duration ms | easing | property |
|---|---|---|---|---|---|
| 1 | dim behind the panel | 0 | 150 | Quad Out | BackgroundTransparency 1 -> rest |
| 1 | panel (frame + header) | 0 | 180 | Back Out | UIScale 0.92 -> 1 |
| 2 | content group | 70 | 180 | Quad Out | GroupTransparency 1 -> 0 |
| 3 | hero card (if any) | 140 | 180 | Back Out | UIScale 0.94 -> 1 and transparency 1 -> 0 |

Entry total 320 ms. Exit: content fade 0 to 80 ms (Quad In), panel UIScale 1 -> 0.92 and fade 60 to 160 ms (Quad In). Exit total 160 ms.

Note on the 102% peak: Roblox's Back Out overshoots by about 10% of the distance travelled, so 0.92 -> 1 peaks near 100.8%, not 102% (see `roblox-recipes.md`). To match 06 exactly use a two-step pop. A plain Back Out from 0.92 is acceptable and is inside R11.
