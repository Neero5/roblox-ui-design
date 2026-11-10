# roloblox-ui-design

A Claude Code plugin that teaches Claude to build **polished Roblox UI motion** (later VFX and animation) for any Roblox game, instead of generic "AI slop".

It is built from real reference clips: each clip is turned into frames and measurements (`tools/extract.py`), torn down into a note (`evidence/`), and the rules distilled from them are ruled on by the owner before they enter a skill.

## Install (once per computer)
In Claude Code:
```
/plugin marketplace add Neero5/roloblox-ui-design
/plugin install roblox-ui-design@roblox-ui-design
```
Update later with `/plugin marketplace update roblox-ui-design`.

## Use in a game
Copy `templates/project-profile.md` into the game's repo (for example `docs/ui-profile.md`), pick a genre profile and fill in the theme vocabulary. The skill reads it first.

## Layout
- `skills/roblox-ui-motion/` the skill: `SKILL.md` + `references/` (core rules, genre profiles, Roblox recipes, review loop)
- `evidence/<area>/` teardown notes per clip, key frame sheets in `media/`, the owner's verdicts
- `tools/extract.py` clip -> contact sheets, motion graph, frame strips, bursts (needs ffmpeg, Python, Pillow, numpy)
- `templates/` teardown and project-profile templates
