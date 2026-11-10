---
profile: premium
status: evidenced (thin)
evidence: [07, 04, 02, 03]
---
# Profile: premium

Restrained, calm, type-led: story, RPG, fantasy, anime action, adventure and showcase games, title menus, character hubs, character creation, inventories, admin and settings panels. Motion is cross-fades in place and short ordered fades. Nothing bounces. The game's project profile may call this `premium-fantasy`; it is the same profile.

**Owner ratings:** 07 anime action RPG character hub: 5. 04 Aftertwelve menus: 4.5. 02 dark commands panel: 4. 03 sword RPG menu: 4. (Owner, 2026-11-10, `evidence/ui/pilot-rules-verdicts-2026-11-10.md`.)

**How strong is this profile?** The best of the set, still thin. Four screen recordings, all rated 4 or more by the owner, so every clip here is a model and none is a counter-example. Where clips disagree, the higher rated one leads (07, then 04). 02's entry and exit were measured twice with the same result; 03, 04 and 07 were measured once each at 30 fps (one frame is 33 ms). Small text could not be read in any of them (576 px sources). No generic premium clip has been torn down, so the "Generic tells" list below is a guess.

Source column: an evidence id, "core Rn" or "core In", "worked example" (one game's shipped values), or "guess".

## Identity in this genre

What the owner praised in all four clips is identity before motion: 02 "all its tabs and elements match its red, ninja identity"; 03 "gives off somewhat of a AAA feel with its looks and matching identities"; 04 "its RPG identity pops up immedately"; 07 "beautifully done, specially because it mimics the successful game Genshin impact".

| Parameter | Value | Source |
|---|---|---|
| Where identity lives | in few, quiet carriers repeated on every panel: one accent, one title face, one border or corner mark, one surface, one way of moving | 02 (red accent, serif title), 03 (diamond on the top edge, dot on the selected item), 04 (corner caps, diamond arrows, pale teal), 07 (hairlines, serif numerals, rank letters, starfield) |
| Identity carriers per game | 3 or more, the same on every panel | core I2; the count is a guess |
| The world as carrier | the game's own 3D scene or character stays visible behind or beside the UI and is part of the identity | 03 (sword in grass), 04 (the character), 07 (the character and a starfield) |
| Motion as carrier | one manner of moving for the whole game (here: fade in place, a small rise); no panel moves in a different manner | 07, 04 |
| Benchmark | optional, one game; borrow anchors, restraint, type, timing, hierarchy; never its art, logos, icon sets, exact layouts or trade dress | core I4; 07 (5), 03 (4) |

### Generic tells (tick for core I2; all guesses, no generic premium clip yet)

- A near-black translucent rectangle with a thin serif title and nothing that names a world.
- Gold or teal as the accent only because "premium" games use it.
- Tracked caps labels as the only styling, on plain rectangles.
- A stock or mixed-style icon set on the rail or tabs.
- The benchmark game's frame shapes, rank badges or star rows taken as they are (this is also an I4 fail).
- Blur and vignette doing the work of a design.

## Entry and exit

| Parameter | Value | Source |
|---|---|---|
| Beats, frequent panel | 1 to 4, in reading order | 07 (1: a page's content fades and rises together), 03 (2: frame, content), 02 (4: title, then three columns) |
| Beats, rare moment | 4 to 6 | guess |
| Beat order | backdrop or frame, title and subtitle, content columns left to right (or rows top to bottom), hero last | 02, 03, 07 |
| Stagger, panel level | 60 to 70 ms (allowed 50 to 80 ms) | 02; core R1 |
| Duration of one beat | 100 to 200 ms; the backdrop fade may run the whole entry | 07 (200 ms), 02, 03 (100 to 150 ms) |
| Entry total, frequent | 200 to 300 ms | 07 (about 200 ms), 03 (about 230 ms), 02 (about 300 ms) |
| Entry total, rare (title screen, chapter card) | 500 to 800 ms | core R2; guess |
| Exit total | 130 to 200 ms | 02 |
| Exit order | last-arrived content first, container last | 02 (right column first), 03 |
| Fade-in drift | content may rise 6 to 8 px while it fades in; never more | 07 (seen; the pixel figure is an estimate) |

## Pages inside a hub (rail or tab navigation)

| Parameter | Value | Source |
|---|---|---|
| Still anchors | two: the navigation rail and the 3D character or subject. They sit outside the page content and never move, scale or fade on a page change | 07; 03 and 04 (one anchor each); core R6 |
| Page change | old page content out in 30 to 70 ms, new content fades in over about 200 ms with the small rise; about 230 to 270 ms in total | 07 (old content gone in about one frame, new in 0 to 200 ms); the 70 ms upper value is a guess |
| Panel swap total (two different panels) | 400 ms or less: exit 150 to 200, empty beat 0 to 30, entry 200 to 230 | 03 measured about 600 ms and was judged slow; 400 is a guess |
| Empty beat between pages | one frame, about 30 ms, or none | 03; core R4 |
| Fade through black between pages | avoid. 07 fades to near black, holds about 100 ms of nothing, then brings the next page in: the one slow spot of the top-rated clip | 07 (counter-example inside a model clip) |
| A page with its own entrance (a skill tree, a map) | may rise out of a glow, elements bottom-up, in about 200 ms, started straight after the old content leaves | 07 |

## In-place change and grids

| Parameter | Value | Source |
|---|---|---|
| Detail pane on selection | cross-fade in place: old detail dims over about 70 ms (ease In), new detail fades in over about 100 ms (ease Out), about 170 ms in total; starts on the frame of the click | 07 |
| Other in-place values (carousel, tab name) | 170 to 200 ms: old value dims to about 40% over 70 to 100 ms, new value in over 100 ms; all dependent texts in the same beat | 07 (170 ms), 04 (200 ms); core R5 allows 160 to 240 ms |
| What changes together | name, stars, rank letter, stats, description and the button label, in one beat | 07, 04 |
| Grid entry | rows light up top to bottom, about 100 ms a row | 07 |
| Grid cascade cap, frequent panel | the cascade ends by 300 ms and the whole entry by 350 ms. Up to 3 rows: 100 ms a row. More rows: 50 to 60 ms a row for the first 5, later rows arrive with the fifth | cap: core R2; 07's own cascade ran about 700 ms for 7 rows, longer than R2 allows (see the open question); the compression is a guess |
| Grid on reselect, scroll or filter | no cascade; cells are simply there | guess; core R2 |

## Pops and easing

| Parameter | Value | Source |
|---|---|---|
| Overshoot | 0%. No Back, no Bounce, no Elastic anywhere | 02, 03, 04, 07 (nothing bounces in any of them) |
| Entry easing | Quad Out or Sine Out; Quart Out for a slide of a hero stage | 02, 03, 04, 07 ("ease-out"); exact style is a guess |
| Exit easing | Quad In | 02, 03, 07 |
| Frame scale on entry and exit | 0.97 <-> 1, with the fade; or no scale at all | 03 ("shrinks a little"); 0.97 is a guess |
| Slides | none for panels and values; changes happen in place | 04, 07 |
| Backdrop | fades with the first beat to about 85% dark, or a soft vignette, or dark glass over the world | 02, 04, 07 |

## Idle motion

| Parameter | Value | Source |
|---|---|---|
| Idle budget in the UI | 0 | 07, 04, 03, 02 (no idle UI motion in any of them) |
| Life at rest | from the world behind the UI (a slowly drifting starfield, grass) and from the character, not from the chrome | 07, 03, 04 |
| Hero motion of a page | the character performs it: for example drawing the weapon over about 400 ms when the Weapon page opens. The panel itself only fades | 07 ("the world performs, not the panel") |
| If the game's profile grants a UI hero loop | cycle 5 s or longer, opacity or sheen only, no movement | guess; core R7 |

## Colour and hero policy

| Parameter | Value | Source |
|---|---|---|
| UI accent hues | 1 | 02 (red), 04 (pale teal), 07 (white hairlines on navy) |
| Rarity or rank colours | allowed as information, on the rank badge and its star row only; one rarity visible in the detail pane at a time; never as card backgrounds | 07 |
| Surfaces | dark or neutral translucent panels with a 1 px light border, dark glass over the world, or text on the world over a vignette or scrim | 03, 04, 07 |
| Hero | the 3D subject or one featured card; marked by size, placement and the accent, not by glow | 03, 04, 07 |
| Selected state | a small mark (dot, diamond, hairline frame) and the accent; not a filled saturated box | 03, 04, 07 |
| Empty space | keep a clear third of the screen empty | 04 (text left, character right, middle empty), 07 ("lots of empty space") |

## Type and legibility

| Parameter | Value | Source |
|---|---|---|
| Voices | exactly 3: small tracked caps label, large value, small muted line | 04, 07, 02 |
| The large voice as hierarchy | one large glyph may carry the rank or order: a rank letter (E, C, S, SS) as a big faint glyph behind the detail, or serif numerals 1, 2, 3 on slots. It replaces a box or a badge frame; one per pane | 07 |
| Families | 1, or 2 (a serif for titles or numerals) | 04 (one), 02 and 07 (a serif plus a plain face) |
| Minimum text size | 14 px at the design resolution; hairline weights and italics only at 20 px or more | guess; 02, 04 and 07 all lost points on size, weight or grey italics |
| Buttons | no smaller than 32 px high at the design resolution | guess; 07 (pill buttons too small) |
| Text on the world | always over a scrim, vignette or glass dark enough for the brightest scene; test on the brightest scene | 04 (lost on snow) |
| Muted line | muted by lower contrast, but still clearly readable; never the same grey as the label | 04 ("risk of everything being the same grey"), 07 (grey italic descriptions hard to read) |

## Sound and feedback

No clip was analysed for sound. All guesses.

| Parameter | Value | Source |
|---|---|---|
| Press and selection feedback | on the same frame as the input: the selection mark moves and the detail cross-fade starts | 07 (motion only; sound not analysed) |
| Press feedback on buttons | within 50 ms: a colour or brightness change and a 2% sink; no spring | guess |
| Hover | the hairline border or text brightens over 100 to 150 ms | guess |
| Sounds | soft, short, low in the mix; one cue per action; no cue on hover | guess |
| Confirm of a big choice (begin, purchase) | one slower beat, 400 to 800 ms, a title card; not a hold on black | core R2; guess (the title card idea is from 06, a clip rated 2.5 in another genre) |

## Reduced Motion

| Parameter | Value | Source |
|---|---|---|
| Entry and exit | one opacity fade of 150 ms or less for the whole panel, no stagger, no rise, no scale; or instant | guess; core E1 |
| Value and detail changes | instant swap or the same cross-fade (opacity only) | guess |
| Grid | all cells at once | guess; core E1 |
| Idle | none in the UI; the world's own ambient motion is the game's decision | core R7; guess |

## Forbidden in this profile (beyond the core)

- Any overshoot or squash.
- Sliding a panel in from a screen edge.
- A fade through black with a pause between pages (07).
- Moving, fading or re-posing the rail or the character on a page change that does not concern them (07 is the model).
- Glitch or smear exits unless the theme vocabulary is sci-fi or horror (02 used one; off theme for most games).
- Two pages readable on the same frame (04 at 10.0 s).
- Hairline text, grey italics or tiny buttons at small sizes (04, 07).
- Any element taken from the benchmark game (core I4).

## Default beat table: hub page with a grid and a detail pane (starting point, after 07)

Anchors (not in the table, never animated): the rail and the character.

| # | element | start ms | duration ms | easing | property | job for the player |
|---|---|---|---|---|---|---|
| 1 | old page content | 0 | 50 | Quad In | GroupTransparency 0 -> 1 | the old page is gone |
| 2 | page title and detail pane | 50 | 200 | Quad Out | GroupTransparency 1 -> 0, position 8 px low -> rest | what is selected now |
| 3 | grid row 1 | 50 | 100 | Quad Out | GroupTransparency 1 -> 0 | reading order, top first |
| 4 | grid row 2 | 150 | 100 | Quad Out | GroupTransparency 1 -> 0 | |
| 5 | grid row 3 and all later rows | 250 | 100 | Quad Out | GroupTransparency 1 -> 0 | |

Entry total 350 ms (at the R2 limit; drop the rows to 60 ms apart for more headroom). Selection: detail pane out 0 to 70 ms (Quad In), swap the texts, in 70 to 170 ms (Quad Out). Exit of the whole hub: content fades 0 to 80 ms, rail and backdrop 60 to 180 ms (Quad In). Exit total 180 ms.

## Default beat table: frequent list panel (starting point, after 02)

| # | element | start ms | duration ms | easing | property |
|---|---|---|---|---|---|
| 1 | backdrop / frame | 0 | 250 | Quad Out | transparency 1 -> rest |
| 1 | title + subtitle | 0 | 100 | Quad Out | GroupTransparency 1 -> 0 |
| 2 | column 1 | 70 | 130 | Quad Out | GroupTransparency 1 -> 0 |
| 3 | column 2 | 130 | 140 | Quad Out | GroupTransparency 1 -> 0 |
| 4 | column 3 | 200 | 100 | Quad Out | GroupTransparency 1 -> 0 |

Entry total 300 ms. Exit: column 3 out 0 to 70 ms, everything else fades 70 to 180 ms (Quad In). Exit total 180 ms.

## Open questions for the owner

- 07's inventory grid takes about 700 ms to light up (7 rows at about 100 ms). The owner rated the clip 5 and also adopted R2 (350 ms for frequent panels). This profile keeps R2 and caps the cascade at 300 ms. If the owner likes the full 700 ms cascade, it needs an R2 override for the first open of a grid.
- Rarity colours are treated as information, not as accents. Confirm.
