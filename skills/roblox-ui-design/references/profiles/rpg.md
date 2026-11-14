---
profile: rpg
status: evidenced
evidence: [L05, L01, L02, L03, L04, 03, 04, 07]
---
# Profile: RPG (action RPG, dark fantasy, anime RPG)

**Owner ratings:** V15 Arcane Atelier 5 (damage tint, impact frames, HUD matching the game); 09 @lastqual combat HUD 5; 10 @skaterstudios.com combat HUD 5; L05 @mystyismee RPG UI kit 4.5; 07 santonixs hub 5; 04 / L03 Aftertwelve 4.5; L01 Genshin sheet 4.5; 03 / L02 Bladebound 4.
**Adopted 2026-11-14** (owner: "Keep them RPG-only ... As for the principles, adopt them"). These rules apply only when the game's profile names this genre.

## Motion
Use the numbers in `premium.md`: its model clips (03, 04, 07) are RPG menus. This profile adds the HUD and theme rules below.

## Identity in this genre
- The identity lives in an **ornament family drawn from the game's world** (skulls and chains, vines, kitsune masks, a sun disc with crossed swords, silver filigree): one family per game (L05).
- The world and the character carry the life; menus stay still around them (07, 04).
- **Generic tells (core I2), tick each:** plain flat bars with no frame; a different frame style on bars, slots and panels; a stock icon pack; ornaments with no source in the game's world; every bar the same width (guess, from L05's contrast).

## HUD and theme rules (adopted, evidence L05)
| # | Rule | Check |
|---|---|---|
| RPG1 | **A theme is a full set.** Bars, hotbar slots, frames and the danger or alert banner share one ornament family and one palette; changing the theme redraws all of them together. | List the HUD parts; every one uses the same frame and ornament family. |
| RPG2 | **Ornament on the ends and corners, never across the fill.** Caps, masks, discs and studs sit on bar ends and frame corners; the fill and the value stay clean and readable. | On a capture at the lowest bar value, the fill still reads; nothing crosses it. |
| RPG3 | **Bar size sets the hierarchy.** The main bar (health) is the widest and centred; secondary bars (stamina, mana, XP) are thinner and shorter, stacked above or below it in the same frame. | Measure: the main bar is the widest; each secondary bar is visibly thinner. |
| RPG4 | **Menu items fade by distance from the selected one.** The chosen item is full strength; the others step down the further they are (Ashen Overture's menu). | On a capture, the selected item is the brightest; the others dim in order. |
| RPG5 | **The HUD hugs the bottom and the edges; the centre stays clear for play.** | Nothing but alerts and the crosshair sits in the centre third during play. |

## Type and legibility
- A serif or engraved face suits the genre (L05, L01, L03) but must pass R13: no grey-on-grey, no thin italic body text at Roblox sizes (L05 weak points, owner agreed 2026-11-14).

## Forbidden in this profile
- Typos or broken words in the art ("YOU LIFE IS AT RISK", "Dispand", "DANGERED" in L05): proofread every word baked into an image (R12).
- Grey-on-grey type and thin italic body text (R13).
- Heavy decoration (skulls plus chains plus stars) on a bar that is on screen all match; save it for titles and banners (I3).

## HUD motion (measured 2026-11-14; clips 09 and 10 rated 5; phases confirmed by the owner)
| Item | Start at | Source |
|---|---|---|
| Health fill drops to the new value | 100 to 130 ms, eased | 09 (9 hits measured) |
| "Recent damage" segment | a lighter segment stays where the lost health was | 09 |
| Segment hold | 230 to 300 ms | 09 |
| Segment shrink | 300 to 400 ms, eased | 09 |
| One hit, start to clean | about 0.7 s | 09 |
| Hits in quick succession | they stack into one segment that shrinks once after the last hit | 09 (18.07 to 19.60 s) |
| Damage numbers | float above the target at the hit | 10 |
| Damage tint when the player is hit | a full-screen transparent red overlay (about 10 to 15%), on in ONE frame as the health bar starts to drop, fading out over about 200 to 300 ms; the HUD stays readable | V15 (rated 5; 9 hits measured) |
| Low-health alert (owner's design 2026-11-14, no clip) | Below a threshold the game sets, a DEEPER red tint than the damage tint comes onto the screen with a transition (a fade or any clear, good-looking entry). It STAYS while health is below the threshold, either beating (pulsing) or still: the game decides. It leaves, again with a transition, ONLY when health rises back above the threshold. It never hides the HUD: at most a transparent overlay over it, best kept off the HUD. | owner 2026-11-14 |
| Reduced Motion | the fill and the segment jump; the segment still shows for its hold; the damage tint stays (it is a colour change, not motion) but softer | guess (E1) |

## Open
- Low-health alert: specified by the owner (above); no clip yet, so its tint strength and beat rate are to be set per game.
