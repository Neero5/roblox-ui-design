---
profile: premium
status: evidenced (thin)
evidence: [02, 03, 04]
---
# Profile: premium

Restrained, calm, type-led: story, RPG, fantasy, adventure and showcase games, title menus, character creation, admin and settings panels. Motion is cross-fades in place and short ordered fades. Nothing bounces. The game's project profile may call this `premium-fantasy`; it is the same profile.

**How strong is this profile?** The best of the set, still thin. Three screen recordings; 04 is the only clip the owner rated 5 ("04's pretty solid"); 02 and 03 are rated 4 by proposal, not yet confirmed. 02's entry and exit were measured twice with the same result. 03 and 04 were measured once each. Small text could not be read in any of them (576 px sources).

Source column: an evidence id, "core Rn", "worked example" (one game's shipped values), or "guess".

## Entry and exit

| Parameter | Value | Source |
|---|---|---|
| Beats, frequent panel | 2 to 4, in reading order | 02 (4: title, then three columns), 03 (2: frame, content) |
| Beats, rare moment | 4 to 6 | guess |
| Beat order | backdrop or frame, title and subtitle, content columns left to right (or rows top to bottom), hero last | 02, 03 |
| Stagger | 60 to 70 ms (allowed 50 to 80 ms) | 02; core R1 |
| Duration of one beat | 100 to 150 ms; the backdrop fade may run the whole entry | 02, 03 |
| Entry total, frequent | 230 to 300 ms | 02 (about 300 ms), 03 (about 230 ms) |
| Entry total, rare (title screen, chapter card) | 500 to 800 ms | core R2; guess |
| Exit total | 130 to 200 ms | 02 |
| Exit order | last-arrived content first, container last | 02 (right column first), 03 |
| Panel swap total | 400 ms or less: exit 150 to 200, empty beat 0 to 30, entry 200 to 230 | 03 measured about 600 ms and was judged slow; 400 is a guess |
| Empty beat between pages | one frame, about 30 ms | 03 |
| In-place value change | 200 ms: old value dims to about 40% over 100 ms (ease In), new value in over 100 ms (ease Out); all dependent texts in the same beat | 04 |

## Pops and easing

| Parameter | Value | Source |
|---|---|---|
| Overshoot | 0%. No Back, no Bounce, no Elastic anywhere | 02, 03, 04 (nothing bounces in any of them) |
| Entry easing | Quad Out or Sine Out; Quart Out for a slide of a hero stage | 02, 03, 04 ("ease-out"); exact style is a guess |
| Exit easing | Quad In | 02, 03 |
| Frame scale on entry and exit | 0.97 <-> 1, with the fade; or no scale at all | 03 ("shrinks a little"); 0.97 is a guess |
| Slides | none for panels and values; changes happen in place | 04 |
| Backdrop | fades with the first beat to about 85% dark, or a soft vignette | 02, 04 |

## Idle motion

| Parameter | Value | Source |
|---|---|---|
| Idle budget in the UI | 0 by default | 02, 03, 04 (no idle UI motion seen) |
| Life at rest | the 3D world or character behind the UI (slow, ambient), not the UI | 03, 04 |
| If the game's profile grants a hero loop | cycle 5 s or longer, opacity or sheen only, no movement | guess; core R7 |

## Colour and hero policy

| Parameter | Value | Source |
|---|---|---|
| Accent hues | 1 | 02 (red), 04 (pale teal) |
| Surfaces | dark or neutral translucent panels with a 1 px light border, or text on the world over a vignette or scrim | 03, 04 |
| Hero | the 3D subject or one featured card; marked by size, placement and the accent, not by glow | 03, 04 |
| Selected state | a small mark (dot, diamond, hairline) and the accent; not a filled saturated box | 03, 04 |
| Empty space | keep a clear third of the screen empty | 04 (text left, character right, middle empty) |

## Type and legibility

| Parameter | Value | Source |
|---|---|---|
| Voices | exactly 3: small tracked caps label, large value, small muted line | 04, 02 |
| Families | 1, or 2 (a serif for titles) | 04 (one), 02 (serif title plus rows) |
| Minimum text size | 14 px at the design resolution; hairline weights only at 20 px or more | guess; 02 and 04 both failed on size or weight |
| Text on the world | always over a scrim or vignette dark enough for the brightest scene; test on the brightest scene | 04 (lost on snow) |
| Muted line | muted by lower contrast, but still clearly readable; never the same grey as the label | 04 ("risk of everything being the same grey") |

## Sound and feedback

No clip was analysed for sound. All guesses.

| Parameter | Value | Source |
|---|---|---|
| Press feedback | within 50 ms: a colour or brightness change and a 2% sink; no spring | guess |
| Hover | the hairline border or text brightens over 100 to 150 ms | guess |
| Sounds | soft, short, low in the mix; one cue per action; no cue on hover | guess |
| Confirm of a big choice (begin, purchase) | one slower beat, 400 to 800 ms, fade through dark or a title card | 06 (title card idea, from another genre); core R2; guess |

## Reduced Motion

| Parameter | Value | Source |
|---|---|---|
| Entry and exit | one opacity fade of 150 ms or less for the whole panel, no stagger, no scale; or instant | guess; core E1 |
| Value changes | instant swap or the same 200 ms cross-fade (opacity only) | guess |
| Idle | none | core R7 |

## Forbidden in this profile (beyond the core)

- Any overshoot or squash.
- Sliding a panel in from a screen edge.
- Glitch or smear exits unless the theme vocabulary is sci-fi or horror (02 used one; off theme for most games).
- Two pages readable on the same frame (04 at 10.0 s).
- Hairline text or buttons at small sizes (04).

## Default beat table: frequent list panel (starting point, after 02)

| # | element | start ms | duration ms | easing | property |
|---|---|---|---|---|---|
| 1 | backdrop / frame | 0 | 250 | Quad Out | transparency 1 -> rest |
| 1 | title + subtitle | 0 | 100 | Quad Out | GroupTransparency 1 -> 0 |
| 2 | column 1 | 70 | 130 | Quad Out | GroupTransparency 1 -> 0 |
| 3 | column 2 | 130 | 140 | Quad Out | GroupTransparency 1 -> 0 |
| 4 | column 3 | 200 | 100 | Quad Out | GroupTransparency 1 -> 0 |

Entry total 300 ms. Exit: column 3 out 0 to 70 ms, everything else fades 70 to 180 ms (Quad In). Exit total 180 ms.
