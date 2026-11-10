# Field test 1 (owner, 2026-11-10): the skill on Sculpt Me!

The owner ran the skill (then `roblox-ui-motion`) on Sculpt Me! in a local session.

Owner's words: "all it did was very small changes that somehow took very long (probably due to the use of subagents) and consumed a lot of tokens. Which to be honest isn't cost efficient as there were only minor improvements, such as addition of pop-up animation instead of a fade in, it also sped up the flying speed of received items (possibly under some rulings) but I honestly didn't like it and just overall, there wasn't really much change nor improvement".

What the owner wants the skill to be: "a tool where I can transform a simple layout mockup and the AI can come up with a professional and stunning UI layout with proper prompting and when necessary, with references".

Changes made the same day (owner: "Yes, apply the change"):
- Renamed `roblox-ui-motion` -> `roblox-ui-design`; the main use is now Mode A, mockup to UI (read the sketch's intent, keep the owner's arrangement, a short brief, one direction by default, show it before wiring it), with `references/layout-craft.md`.
- Cost rules: light by default, no subagents unless the owner asks, ask before spending more than the request implies.
- The owner's rulings win: the game's decision log is read in step 0 and every ruled value is frozen (proposed, never changed silently). Likely cause of the disliked flying-speed change.
- Mode C, audit: a ranked list of findings, no edits until the owner picks.
- The full review loop is opt-in; everyday work uses a light check (one capture, a few ticks).
