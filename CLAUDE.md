# roloblox-ui-design: working rules

This repo is a Claude Code plugin (skills for Roblox UI motion; VFX and animation later). It is for Roblox games in general: nothing game-specific goes in `skills/` except as a clearly labelled example.

- **The owner's taste decides.** Claude proposes rules, ratings and verdicts; the owner adopts, changes or refuses. Record every verdict in `evidence/<area>/` (the owner's words quoted, never an invented reason). A rule enters `skills/` only once adopted.
- **Videos never enter git** (`.gitignore`). Commit only the few frame sheets a teardown cites, as jpg, under `evidence/<area>/media/`.
- **Evidence first:** run `tools/extract.py` (first pass whole clip, `--crop` the game area, then a `--start/--end` zoom with `--every 0.0334` for frame timing). A clip filmed off a monitor gives layout only.
- **Universal vs genre:** a rule that holds in every game goes in `references/core-rules.md`; a number that changes with the game (beats, durations, overshoot, idle-motion budget, saturation) goes in a genre profile under `references/profiles/`. Each rule cites its evidence notes.
- **Model roles:** the strongest available model writes and revises the skill text and judges subtle clips and builds; everyday models do routine teardowns and follow the skill.
- **Keep SKILL.md short** (the workflow and the always-true rules); details load from `references/` only when needed.
