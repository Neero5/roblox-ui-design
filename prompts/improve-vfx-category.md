# Prompt: improve every effect in one category

Paste into a session in the game's repo (Studio open if the work needs it). Fill in the brackets; delete lines you do not need. For UI motion or UI pop-ups use `/roblox-ui-design:roblox-ui-design` instead (same shape).

```
/roblox-ui-design:roblox-vfx

Improve the [CATEGORY, e.g. win effects] of this game.

Where they are: [paths, e.g. ReplicatedStorage.Sculpt.VfxTable rows win*, Sculpt.VfxTemplates]. If you are not sure which effects belong to the category, list what you found and ask before going on.
What I want: [the goal in one line, e.g. "more impact at the moment of winning, less clutter"].
What bothers me now: [optional: specific effects and what is wrong with them].
References: [optional: clip numbers from the skill's library, or attached videos/images].
Keep as they are: [optional: anything you like now; everything I ruled on in the decision log stays frozen anyway].

Step 1, audit only (Mode C): for each effect in the category, give one line: its tier (frequent or rare),
the rule it breaks (X1 to X7, I1 to I4), the reference you would aim at, and the fix with its size (small
or medium). Rank them, biggest gain first. Then stop and wait for my pick.

Step 2, after I pick: build only the picked fixes (Mode B), with the light check from the default play
camera (peak frame, mid-fade, beside its reference; frequent effects cast five times), at the lowest
quality level once, and with Reduced Motion considered. Leave the scene as found. Report in 2 to 6 lines
per effect.
```

## Why it is shaped this way
- The slash command loads the skill for certain (a plain "use the skill" was missed once).
- Audit first, then build only what the owner picks: the first field test spent tokens on small changes nobody asked for.
- "Frozen" is restated because a category pass touches many values the owner has ruled on.
