---
profile: simulator
status: evidenced (weak: no clip rated above 3)
evidence: [05, 01, 06]
---
# Profile: simulator

Lively and friendly: pet, clicker, tycoon, mining, incremental and collecting games with a young audience and panels opened very often.

**Owner ratings:** 05 sky shop: 3. 01 simulator shop (filmed): 2.5. 06 mines panel (filmed): 2.5. (Owner, 2026-11-10, `evidence/ui/pilot-rules-verdicts-2026-11-10.md`.)

**How strong is this profile? Weak, and say so when using it.** No simulator clip is rated above 3, so this profile has no model, only counter-examples. The owner's reasons: 01 "too generic, it matches 90% of typical simulation games"; 06 "its essence stills fall under the generic category"; 05 "maximalistic looks, as if trying too hard to be unique and a "showoff" of its UI elements, with jets going everywhere and everything with movements, almost sloppy". 05 is the only screen recording; 01 gives layout only and 06 timing within about one frame.

What that means for the numbers:
- A number sourced to 05, 01 or 06 is a measurement of a UI the owner did not rate highly. It tells what such a UI does, not what a good one should do. Those rows are marked "low-rated clip".
- The rows the owner has actually ruled on are the core rules (R1 to R13, I1 to I4, E1 to E5). They bind here in full.
- Order, in-place change and still anchors are proved on the clips rated 4 or more (07, 04, 02, 03) and carry over through the core rules. Their calm (no overshoot, no idle) is noted below as the safe direction when in doubt.
- This profile needs a simulator clip the owner rates 4 or more. Until then, show the owner frames early and record the verdicts as evidence.

Source column: an evidence id with "low-rated clip" where it applies, "core Rn" or "core In" (the adopted rule sets the bound), "worked example" (one game's shipped values, not a simulator), or "guess".

## Identity first (core I1, I2)

A simulator can have its own identity. The genre is not the identity: "a pet simulator" names 90% of the genre; "a candy factory run by robots" or "a cloud harbour of paper planes" names one game. The usual simulator look is not a style to match: it is the list of I2 tells below.

| Parameter | Value | Source |
|---|---|---|
| Identity statement | names the game's own world (its place, its material, its mascot or its main object), never just "simulator" plus a noun | core I1, I2; 01, 06 (counter-examples) |
| Where identity lives | in the things the genre usually leaves at default: the frame's shape and material, the header, the close button, the card surface, the icon drawing style, the currency pill, the button shape, the title face | guess, from the tells below |
| Ornaments | from the theme vocabulary, on the frame, arriving as one beat. An ornament alone does not make an identity | 05, low-rated clip (cloud puffs on a default blue shop: on theme, still "similar reasons as 01") |
| Liveliness | bright and bouncy is allowed, inside the identity. Unique comes from the world, never from more motion | core I3; 05 (counter-example) |
| Benchmark | optional, one successful game, principles only | core I4; no simulator benchmark has been studied: guess |

### Generic tells (tick for core I2: 3 or more present is a fail; each one kept needs a reason from the identity)

- [ ] A flat blue or teal header bar with a bold white outlined title. (01, 05, 06)
- [ ] A square X close button in a clashing colour (most often red) on the header's right corner. (01, 06 red; 05 purple)
- [ ] A shop or bag icon hanging off the header's left corner. (01, 05)
- [ ] Saturated gradient cards, each row or card a different colour. (01, 05)
- [ ] "BEST DEAL", "LIMITED TIME ONLY" tags and struck-through prices as decoration. (05)
- [ ] White text with a dark stroke on everything. (01, 05)
- [ ] A rail or column of the standard buttons (Featured, Eggs, Passes, Codes, Rebirth) in the standard style. (01)
- [ ] Green or yellow glossy price buttons. (01, 05)
- [ ] A sunburst, speed lines or sparkles behind items with no source in the game's world. (05; guess for sunbursts)
- [ ] A patterned tile wallpaper inside the header or panel. (05)

A tell is a default, not a ban: a red close button is fine in a game whose world has it. The fail is taking the whole set as the design.

## Entry and exit

| Parameter | Value | Source |
|---|---|---|
| Beats, frequent panel | 1 to 3. Default 2: panel pop, then content. | core R1; 06, low-rated clip (1 beat); "2" is a guess |
| Beats, rare moment | 4 at most as a start | owner 2026-11-10; 05, low-rated clip, used 6 and read as showing off (core I3) |
| Beat order | container, ornaments, section label, content, hero last | core R1; 05, low-rated clip (the order was the good part) |
| Stagger | 50 to 80 ms | core R1; 02 and 07 (60 to 100 ms, other genre); 05, low-rated clip, measured 100 to 200 ms: too slow |
| Duration of one beat | 150 to 200 ms | 06 and 05, low-rated clips; matches 07 (200 ms) |
| Entry total, frequent | 250 to 350 ms | core R2 |
| Entry total, rare | 500 to 800 ms | core R2; 05, low-rated clip (1500 ms on a shop: far too long) |
| Exit total | 100 to 180 ms, one or two beats | core R3; no simulator exit was measured: guess |
| Panel swap total | 400 ms or less | guess |
| In-place value change | 160 to 240 ms cross-fade; a number that goes up may also pop (below) | core R5; 07 and 04 (170 to 200 ms, other genre) |
| Still anchor | the world and the HUD stay still while a panel opens | core R6; 07, 04, 03 (other genre) |

## Pops and easing

| Parameter | Value | Source |
|---|---|---|
| Panel pop start scale | 0.92 | 06, low-rated clip |
| Panel pop peak | 102% (allowed 100% to 104%) | 06, low-rated clip; range is a guess inside core R11 |
| Settle | at rest by 200 ms | core R11; 06 |
| Entry easing | Back Out for the panel only; Quad or Quint Out for content, slides and ornaments | core R11; 05 and 06, low-rated clips; narrowed to the panel after the verdict on 05, owner 2026-11-10 |
| Exit easing | Quad In, no overshoot | core R3; guess |
| Elements that may overshoot in one entry | 1 (the panel), or 2 with the hero | owner 2026-11-10; core I3; anti-slop "every element bounces" |
| No overshoot at all | always acceptable; every clip rated 4 or more has none | 07, 04, 02, 03 (other genre) |
| Value-change pop | 8% up, back within 300 ms | worked example |
| Forbidden easing | Bounce, Elastic, Linear (except loops) | core R11, anti-slop |

## Idle motion

| Parameter | Value | Source |
|---|---|---|
| Idle budget | 1 looping element per screen at most: the hero. Start a new build with 0 and add the hero loop only if it has a job for the player | core R7, core I3; owner 2026-11-10 |
| The loop stays inside the hero | it never crosses other cards, the header or the panel edge | 05, low-rated clip (counter-example: the jet, its trail and smoke rings cross the whole panel; the owner: "jets going everywhere") |
| Effect types in the loop | 1 (for example a sheen or a small bob), not a moving object plus a trail plus rings | core I3; 05 (counter-example); guess |
| Cycle | 3 to 5 s | core R7; 05, low-rated clip (about 3 s) |
| Active part of the cycle | 700 ms or less | 05, low-rated clip |
| Chrome at rest | still | core R7 |
| Second idle element (for example a "claim" badge that needs attention) | only by an override in the game's profile | owner: "depends on the game" |

## Colour and hero policy

| Parameter | Value | Source |
|---|---|---|
| Palette | taken from the game's identity, not from the genre's blue, red, green and yellow | core I1, I2; 01, 05, 06 (counter-examples) |
| Hero | 1 per screen, placed first (top or left), larger than grid cards | core R8; 06, low-rated clip (a hero card on top) |
| Full-strength accent hues on one screen | 3 at most, plus the hero | guess; 01 (eight at equal weight) and 05 (four saturated cards) are the counter-examples |
| Non-hero cards | one shared card surface from the identity, clearly lower in saturation than the hero (start at 70% of the hero's saturation); no glow | guess; 05, 06 counter-examples |
| Urgency tags ("LIMITED", "BEST DEAL") | 1 per screen, and only when true | guess; 05 counter-example |
| Upgrade or rebirth explanation | a NOW > AFTER pair with an arrow | 01, low-rated clip (its one clear idea) |
| A change of place | may get its own short title card | 06, low-rated clip (its one clear idea); core R2 for the length |

## Type and legibility

| Parameter | Value | Source |
|---|---|---|
| Voices | 3 at most | core R9 |
| Title face | chosen for the identity. The bold rounded face with a dark stroke is the genre default and a tell | core I2; 01, 05 |
| Minimum text size | 14 px at the design resolution | guess (worked example) |
| Text on saturated cards | dark on a light plate, or white with a shadow or stroke where the background needs it; not a stroke on every text by habit | guess; core R13, core I2 |

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

- The genre's default look taken as the design (the tells above). (01, 06; core I2)
- Making a default look "unique" by adding motion and effects to it. (05; core I3)
- A long choreographed entry on the shop or inventory. (05)
- An idle object that leaves the hero card. (05)
- Scramble or decode text unless the game's theme vocabulary includes it. (05)
- More than one saturated gradient card style per row. (05)

## Default beat table: frequent panel (starting point built from the core rules, not from a rated model; hero card Quad Out from 0.96 confirmed by the owner 2026-11-10)

| # | element | start ms | duration ms | easing | property | job for the player |
|---|---|---|---|---|---|---|
| 1 | dim behind the panel | 0 | 150 | Quad Out | BackgroundTransparency 1 -> rest | the world steps back |
| 1 | panel (frame + header) | 0 | 180 | Back Out | UIScale 0.92 -> 1 | where the panel came from |
| 2 | content group | 70 | 180 | Quad Out | GroupTransparency 1 -> 0 | read the header first |
| 3 | hero card (if any) | 140 | 180 | Quad Out | UIScale 0.96 -> 1 and transparency 1 -> 0 | look here last |

Entry total 320 ms. Exit: content fade 0 to 80 ms (Quad In), panel UIScale 1 -> 0.92 and fade 60 to 160 ms (Quad In). Exit total 160 ms.

Note on the 102% peak (measured in Studio 2026-11-10, `evidence/engine/back-easing-2026-11-10.md`): Back Out overshoots 10% of the distance travelled, so 0.92 -> 1 peaks at 100.8%, which is too small to see. To get 06's visible 102%, start the Back pop at 0.8 (peak 1 + 0.1 x 0.2 = 1.02), or keep 0.92 and use the two-step pop in `roblox-recipes.md`. A plain Back Out from 0.92 is inside R11 but reads as a plain ease-out.

## Open questions for the owner or new evidence

- No simulator clip rated 4 or more exists. One good reference would replace most guesses here.
- How lively may a good simulator be? The ratings punish showing off (05) but no clip shows the upper limit of "lively and still good".
- (answered) The tell threshold of 3 or more: owner 2026-11-10.
