# A/B test: the roblox-vfx skill (before and after)

Two brand-new Roblox places, two Claude Code sessions, the same prompt. The only difference is the first line.

- **Session A (before):** the plugin disabled (`/plugin` > disable roblox-ui-design), or a machine without it. First line: `Do not use any skill or plugin for this task.`
- **Session B (after):** the plugin enabled. First line: `Use the roblox-vfx skill for this task.`

Everything below the first line is identical. Paste it as is.

```
<FIRST LINE HERE>

Brand-new Roblox place, open in Studio (Studio MCP: call list_roblox_studios first). Build two
ability effects for a test game. Work only in this place; put scripts and assets in
ReplicatedStorage.Abilities, a LocalScript in StarterPlayerScripts and a Script in
ServerScriptService. No external assets: use only built-in textures, meshes and parts.

Game profile (treat this as the game's docs/ui-profile.md):
- Game: "Frostfall", a PvP arena duel game on a frozen lake. Players are frost witches.
- Identity: a frost witch's duel on a frozen lake: ice, snow, pale blue and white, a little silver.
- Signature motif: the snowflake (six-pointed shapes, hexagonal patterns).
- Theme vocabulary: ice shards, frost crystals, snow powder, cold mist, cracking ice, silver light.
- Refused effects: fire, lightning, rainbow colours, neon pink or purple.
- Auras: none in this test.
- VFX quality: the game has none yet; Reduced Motion must be respected.
- No decision log yet (nothing is frozen).

The two effects:
1. "Frost Lance": the basic attack, cast every 1.5 s. A ranged shot: the witch throws an ice lance
   that flies about 40 studs and hits whatever is in front (a dummy is fine).
2. "Glacier Slam": the ultimate, once every 60 s. The witch slams the ground; ice erupts in a
   circle of 18 studs around her. Players in range should feel it.

Bind Frost Lance to the left mouse button and Glacier Slam to R. Add a target dummy 25 studs in
front of the spawn. The server decides hits; effects play on clients.

When done, in Play:
- capture Frost Lance at its peak and mid-fade, then cast it 6 times in a row and capture the
  last cast;
- capture Glacier Slam at its peak and mid-fade;
- set settings().Rendering.QualityLevel to Level01, capture each effect once, then restore it.
Report: what you built (2 to 6 lines), the captures, and the time it took. Then stop Play.
```

## How to judge (the owner)
Watch both in Play yourself, then rate each effect 1 to 5 like the clips. Useful checks:
1. Does Frost Lance still please after many casts (V04 test)? Is it about 1 s from the hit to clean, plus its flight?
2. Is Glacier Slam clearly bigger, with a shake at the hit only, felt by everyone in range?
3. Is it obviously frost and snowflake (identity), or a generic blue burst?
4. A few crafted elements, or a cloud of particles (detail over quantity)?
5. Does it still read at the lowest quality (shape from meshes, not glow)?
6. Time and tokens each session spent.

Send me both captures (or the places' scripts) and your ratings; I will compare them against the rules.
