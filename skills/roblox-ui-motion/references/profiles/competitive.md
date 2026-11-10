---
profile: competitive
status: draft
evidence: []
---
# Profile: competitive (UNVERIFIED DRAFT)

**Status: draft. No clip evidence. No owner ruling. Every number below is a starting guess.** Use it only when the game's project profile names this genre, tell the owner it is a draft, and prefer the owner's answers over any row here. Replace it by following `_how-to-add-a-profile.md`.

Speed and clarity: shooters, fighters, arena and ranked games. The player wants the UI out of the way; information must be readable in a glance during play. Closest evidenced profile: `premium.md` (no overshoot), with shorter times.

The core rules still apply in full (order, budgets, exit ratio, no overlap, one hero, legibility, on theme).

| Parameter | Starting guess |
|---|---|
| Beats, frequent panel | 1 (guess) |
| Beats, rare moment (match result, rank up) | 3 to 5 (guess) |
| Stagger | 40 to 60 ms (guess; below core R1's 50 ms needs the owner's agreement) |
| Entry total, frequent | 100 to 200 ms (guess) |
| Entry total, rare | 400 to 800 ms (guess) |
| Exit total | 60 to 120 ms (guess) |
| Overshoot | 0% in menus; up to 3% on a hit marker or kill feed entry (guess) |
| Easing | Quad or Quart Out for entries, Quad In for exits (guess) |
| In-place value change (score, ammo, timer) | 100 to 160 ms, or instant with a brief colour flash (guess; shorter than core R5's range, so confirm with the owner) |
| Idle budget | 0 during play; 1 in the lobby hero (guess) |
| HUD during play | no decorative motion at all; motion only signals a state change (guess) |
| Accent hues | 2: team or state colours carry meaning and must not be used as decoration (guess) |
| Type | 3 voices, numeric values large, tabular digits if the font has them (guess) |
| Sound and feedback | immediate (within one frame), sharp, short (guess) |
| Reduced Motion | instant state changes; colour flashes stay if they carry information (guess) |

## Open questions for the owner or new evidence
- Scoreboard and kill feed timing have no evidence at all.
- Whether result screens may use the rare budget every match (they are seen every few minutes).
