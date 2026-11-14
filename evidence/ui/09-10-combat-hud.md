---
type: reference
category: ui
captured: 2026-11-14
tags: [motion, hud, rpg]
---
# 09 and 10: combat HUD in motion

## 09 @lastqual, souls-like boss fight
**Owner, 2026-11-14: 5.** "I'm honestly speechless, it's really well done. I don't know what to comment on it. And I agree with your phases"

![[ui09-full.jpg]] ![[ui09-overview.jpg]] ![[ui09-health-drain.jpg]]

- **Layout:** the player's Health bar (with numbers "59 / 114") and a thin Posture bar under it, top centre; Mana, Tempo and Level as thin labelled bars bottom centre above the weapon slot; Hunger and Thirst as two small vertical bars bottom left; an "In combat" card with a countdown; a feed card; a floating hit counter and a riposte combo list beside the fight. Thin white bars on dark, small serif labels: a quiet HUD.
- **Health drain, measured** (pixel width of the fill, 30 fps, 9 hits across both recordings, all the same shape):

| Phase | Time | Shape |
|---|---|---|
| Fill drops to the new value | 100 to 130 ms | eased, fast |
| A lighter "recent damage" segment is left where the lost health was | appears with the drop | |
| The segment holds | 230 to 300 ms | still |
| The segment shrinks to the new value | 300 to 400 ms | eased |
| Whole hit, start to clean | about 0.7 s | |

  Example (`f345a638` at 2.20 s): fill 254 to 210 px over 2.20 to 2.33 s; the light segment holds to 2.60 s; it shrinks to nothing by 2.97 s. Repeated at 15.50 s and in `77994e1f` at 4.67, 9.00, 30.13, 43.43 s. A run of small hits (18.07 to 19.60 s) stacks into one segment that shrinks once.
- **Death:** the whole fill turns to the light segment colour in one frame, then the bar empties.

## 10 @skaterstudios.com, combat test
**Owner, 2026-11-14: 5.** "Comparable with 10" (read as: comparable with 09)

![[ui10-full.jpg]] ![[ui10-overview.jpg]]

- **Layout:** the target's name ("Dummy [Hard]") over an ornate green health bar with a thin bar above it (stamina or posture) and a blue bar below; floating damage numbers ("-10", "-3", "-1") above the target; the player's matching ornate bars and three round skill slots with key letters (Upper Cut, Smash, Barrage) at the bottom.
- **Works:** the target's bars and the player's bars share one ornate frame (RPG1); damage numbers at the hit.
- **Weak:** the bars are very wide and busy for a phone-height screen; the learning-project text overlays cover the play.
