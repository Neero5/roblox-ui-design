---
type: inbox
category: ui
status: adopted
created: 2026-11-10
tags: [motion, ui-pilot]
---
# UI motion rules: draft for the owner's ruling (pilot, 6 clips)

Distilled from the six pilot teardowns ([[UI motion 01 Simulator shop filmed]] .. [[UI motion 06 Mines panel filmed]]). Each line needs the owner's verdict: **adopt**, **change** (with the note), or **refuse**. Adopted lines become one note each in `06 Rules` (template [[T Rule]]) and a line in the [[Decision log]].

Pilot finding first: our DURATIONS already sit inside the measured range (`UIKit.MOTION`: popIn 0.18 s Back, popOut 0.10 s, enter 0.22 s, fade 0.15 s; the clips measure 130-300 ms per beat). What the good clips have and we mostly don't is CHOREOGRAPHY: order, stagger, a still anchor, and life placed only in the hero.

| # | Proposed rule | Evidence | Verdict |
|---|---|---|---|
| R1 | A panel arrives in beats: frame, then header, then content, then the hero item last, 50-80 ms apart. | 02, 03, 05 | adopt, depends on game type (owner 2026-11-10) |
| R2 | Entry length follows how often it is seen: under 350 ms in total for panels opened often (Bag, Store, Settings); up to about 800 ms for rare moments (a win, a rare drop, the first open of the day). | 05 (1.5 s, too long), 02, 03 | adopt (owner 2026-11-10) |
| R3 | Exit is about half the entry and runs it in reverse: content leaves first, its container last. | 02, 03 | adopt (owner 2026-11-10) |
| R4 | Swapping panels: the old one finishes leaving before the new one starts; never two panels visibly overlapping. | 03 (good), 04 at 10.0 s (the slip) | adopt (owner 2026-11-10) |
| R5 | A value that changes in place (carousel, tab name, counter, day hero) cross-fades in place in about 200 ms; it does not slide the whole panel. | 04 | adopt (owner 2026-11-10) |
| R6 | Keep one still anchor during every transition (the frame, the avatar, the world), so the eye has somewhere to rest. | 03, 04 | adopt (owner 2026-11-10) |
| R7 | Ambient motion lives only in the hero (the featured item), on a slow cycle of 3 s or more, and the chrome stays still. Off under Reduced Motion. | 05 (jet fly-by) | adopt, depends on the game, generally yes (owner 2026-11-10) |
| R8 | One hero per screen: only one element gets full saturation, glow or idle motion; the rest step down. | 05 (counter-example), 04 | adopt (owner 2026-11-10) |
| R9 | Type does the hierarchy before colour or boxes: three voices at most (small label, large value, muted line). | 02, 04 | adopt (owner 2026-11-10) |
| R10 | Effects come from the game's own world: for us chisel, marble dust, polish sheen, paint, confetti. No glitch, no scramble-decoding text, no sci-fi smears. | 02, 05 (both off-theme for us) | adopt (owner 2026-11-10) |
| R11 | Pops overshoot no more than about 5% and settle within 200 ms. | 06 (92 -> 102 -> 100%) | adopt (owner 2026-11-10) |
| R12 | Never ship placeholder or debug text ("Insert description here", raw ids, "TODO"). A reviewer checks every visible string. | 05 | adopt (owner 2026-11-10) |
| R13 | Every text stays readable on what is behind it: contrast first, elegance second. | 02, 04 (both too faint) | adopt (owner 2026-11-10) |

## Anti-slop list (the reviewer's quick check)
- Everything appears at once, or everything fades at the same speed.
- Every element bounces.
- Every card is saturated, glows or moves at idle.
- Linear motion on anything that is not a loop.
- An entry longer than the action it leads to.
- Placeholder text, lorem ipsum, raw ids.
- An effect borrowed from another genre (glitch, decoding text, neon on marble).
- Text that loses against the background.

## Notes on the evidence
- 01 and 06 were filmed off a monitor: layout only, no timing, no colour. Screen recordings are worth far more.
- TikTok clips are 576 px wide: timing reads well, small text does not. For look studies a full-resolution source (the creator's own video or a screenshot) is better.
- All six are clips captioned as AI-made. Fine as references for what a model CAN do, but some carry the slop tells above: that is useful contrast.

## Owner's answers (2026-11-10)
1. No longer first-open entry for the Store: "No need".
2. Idle motion only in the hero: "Depends on the game, but generally yes".
3. Clip 04 rated 5: "04's pretty solid".

Scope: the rules are for Roblox games in general (a reusable skill); genre-dependent values move into per-genre profiles.

## Open questions for the owner (answered above)
1. Does R2's 350 ms budget feel right for the Store, or do you want the Store's first open of a session to get a longer "showroom" entry?
2. R7: should the kiosk and the Store Featured block be the only places with idle motion?
3. Which clip, if any, would you rate 5? (Claude proposed 04.)

## Second ruling (2026-11-10): the skill's additions
- E1 to E5 (Reduced Motion, interruptible, input never held hostage, one motion table, start states before the first frame): owner "Adopt E1 to E5".
- Refinements (R3 exit 40 to 65% of the entry; R5 160 to 240 ms; R4 allows a cross-dissolve of content inside the same frame for 160 ms or less): owner "refinements stand too".
- New clip 07 (@santonixs): owner "I like this one quite a lot too" read as a 5; see `INDEX.md` for which number is which video.

## Third ruling (2026-11-10): the owner's ratings of clips 01 to 07
| # | Rating | Owner's words |
|---|---|---|
| 01 | 2.5 | "It's not bad because it's consistent and matches today's incremental game style. However, it's too generic, it matches 90% of typical simulation games." |
| 02 | 4 | "It's very solid, the whole thing is unique and all its tabs and elements match its red, ninja identity. It's consistent too, but what stands out the most from it are the animations (closing/opening, switching tabs etc)" |
| 03 | 4 | "It gives off \"Elden Ring\" vibes, in other words, the UI gives off somewhat of a AAA feel with its looks and matching identities. The consistent color palette and animations also make it worth mentioning." |
| 04 | 4.5 | "Very impressive aswell, in the same way 03 stands out, its RPG identity pops up immedately and catches the eye with its dynamic animations and fluidity." (was 5 earlier the same day) |
| 05 | 3 | "Similar reasons as 01, but the 0.5 comes from the way it catches the eye, but it gets point deductions due to is maximalistic looks, as if trying too hard to be unique and a \"showoff\" of its UI elements, with jets going everywhere and everything with movements, almost sloppy." |
| 06 | 2.5 | "It's okay, the UIs are somewhat unique but its essence stills fall under the generic category" |
| 07 | 5 | "No words, it's beautifully done, specially because it mimics the successful game Genshin impact, which already proved its successful execution. Your reasons about why it stands out are valids and correct aswell" |

What the ratings say (Claude's reading, proposed as rules I1 to I4 for the owner's ruling): the score follows IDENTITY first (a UI that belongs to one nameable world), consistency is necessary but not enough (01), generic loses points even when tidy (01, 06), showing off loses points (05), and a proven benchmark game executed well wins (07, 03).

