# roblox-ui-design

A Claude Code plugin that turns a simple Roblox UI mockup (plus a prompt, and references when useful) into a **professional, on-identity UI: layout, look and motion**, for any Roblox game, instead of generic "AI slop", and builds **professional Roblox VFX** (abilities, hits, auras, reveals, cutscenes) sized and timed for how often they play. Animation later.

It is built from real reference clips: each clip is turned into frames and measurements (`tools/extract.py`), torn down into a note (`evidence/`), and the rules distilled from them are ruled on by the owner before they enter a skill.

## Install (once per computer)
In Claude Code:
```
/plugin marketplace add Neero5/roblox-ui-design
/plugin install roblox-ui-design@roblox-ui-design
```
Update later with `/plugin marketplace update roblox-ui-design`.

## Use in a game
Copy `templates/project-profile.md` into the game's repo (for example `docs/ui-profile.md`), pick a genre profile and fill in the theme vocabulary. The skill reads it first.

## Layout
- `skills/roblox-ui-design/` the skill: `SKILL.md` (mockup to UI, build, audit) + `references/` (layout craft, core rules, genre profiles, Roblox recipes, the opt-in full review loop)
- `skills/roblox-vfx/` the VFX skill: `SKILL.md` (design, build, audit an effect) + `references/` (rules X1 to X6, frequent and rare tiers, Roblox VFX recipes)
- `evidence/<area>/` teardown notes per clip, key frame sheets in `media/`, the owner's verdicts
- `tools/extract.py` clip -> contact sheets, motion graph, frame strips, bursts (needs ffmpeg, Python, Pillow, numpy)
- `templates/` teardown and project-profile templates
