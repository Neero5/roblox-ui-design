# Studio check for the roblox-vfx recipes (paste into a local session with Studio open)

```
Read-only engine check for my roloblox-ui-design plugin's VFX recipes. Use the Roblox Studio MCP
(list_roblox_studios first). Build every test object under a new Folder "VfxCheck" in Workspace and
delete the folder at the end; change nothing else in the place; stop Play when done.

In Play (client execute_luau unless noted), test and report each:
1. Emit timing: clone a ParticleEmitter (Rate 0, Lifetime 2) into a new Part and call :Emit(20) in the
   SAME statement after parenting. Read emitter:GetParticleCount() (or count visually in a capture)
   next frame. Repeat with task.defer before :Emit. Do both emit?
2. math.noise range: sample math.noise(seed, t) for 100000 random inputs; report min and max.
3. Highlight limit: add 40 Highlights to 40 small Parts in view; capture the screen. How many are
   drawn? Is 31 the limit?
4. Attachment under Terrain: create an Attachment parented to workspace.Terrain, set .Position to
   (0, 50, 0); is .WorldPosition (0, 50, 0)? Put a ParticleEmitter on it; do particles appear there?
5. Flipbook sheet size: is there a documented or enforced limit (1024 x 1024)? Check the API docs or
   the emitter's behaviour with a 2048 texture if one is at hand; say "not tested" if none.
6. Inversion with ColorCorrectionEffect: on the client, add one to Lighting with Contrast = -2 and
   capture; then remove it. Does it read as a colour inversion, or only a washed or crushed image?
   (Remove it right away; do not leave it.)
7. Neon glow vs quality: capture a Neon part at the current quality, then set
   settings().Rendering.QualityLevel to Level01 (Studio only), capture again, restore it.
   Does the glow change?
8. Particle thinning at low quality: same two quality levels, an emitter at Rate 200; compare
   GetParticleCount() if available, or the captures. Restore the quality level.

Reply with a table: fact, result, evidence (value or capture), and "confirmed", "wrong" or "not testable".
Then delete the VfxCheck folder and any effect you added to Lighting, and stop Play.
```
