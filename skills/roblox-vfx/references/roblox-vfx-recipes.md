# Roblox VFX recipes

Engine building blocks for effects. Facts marked **(verify)** are believed true but should be confirmed in Studio before relying on them; everything else is stated with confidence. Use the game's own VFX module, effect table, templates and pool where they exist; these are patterns, not a second system to paste beside the first. Numbers in the snippets are placeholders: take real ones from the brief and `tiers.md`.

## 1. Where effects run

- **Play effects on clients.** The server decides that something happened and sends one event (what, where, who); each client builds and plays the effect locally. Instances a server script creates replicate to everyone, cost bandwidth, and arrive late and stuttering.
- Send data, not instances: the effect key, a position or CFrame, a seed for the variation, the caster's UserId. Under StreamingEnabled a part the server points at may not exist on a far client; handle nil.
- `RemoteEvent:FireAllClients` works. `UnreliableRemoteEvent` suits purely cosmetic, high-frequency effects (a dropped event loses only a visual); keep payloads small.
- The caster's own client can play the effect at once on input (before the server answers) and skip the echo of its own event; other clients play it when the event arrives.
- Screen-level layers (shake, flash, impact frames) are always client-side, and play for every player within the attack's effective range (owner 2026-11-12); the server sends the hit with its position and radius, each client checks its own distance.

## 2. ParticleEmitter

Parent an emitter to an **Attachment** (emits from that point, along the attachment's axes) or to a **BasePart** (emits from the part's volume or faces, see `Shape`). The carrier part is usually `Anchored`, `CanCollide = false`, `CanQuery = false`, `CanTouch = false`, `Transparency = 1`.

**Burst or stream**
- `emitter:Emit(n)` fires n particles at once and ignores `Enabled` and `Rate`. This is the tool for impacts: `Enabled = false`, then `Emit`.
- `Rate` (particles per second) runs while `Enabled = true`: charge-ups, trails of smoke, auras. To stop softly set `Enabled = false` and let live particles finish; `emitter:Clear()` removes them at once (a visible cut: avoid, X3).
- An emitter cloned or parented in the same frame may not emit when `Emit` is called immediately; if a burst is silently missing, `task.defer` or wait one frame before `Emit` **(verify)**.
- At low client graphics quality the engine itself draws fewer particles **(verify the exact scaling)**: never let a single particle carry gameplay meaning.

**Life and motion**
- `Lifetime` (NumberRange, seconds), `Speed` (NumberRange, studs per second), `SpreadAngle` (Vector2, degrees around the emission direction; 180, 180 is every direction), `EmissionDirection` (which face of the parent).
- `Acceleration` (Vector3, world space): gravity for debris (negative Y), lift for embers (positive Y).
- `Drag`: speed decays exponentially over the particle's life. High speed plus drag gives the "burst out, then hang" look of a good impact.
- `VelocityInheritance` (0 to 1): how much of the parent's velocity new particles keep.
- `LockedToPart = true`: particles move with the emitter (auras, a charge glow on a hand). False: they stay in the world (trails, debris).
- `Rotation` and `RotSpeed` (NumberRange, degrees and degrees per second): random start angle and spin; a random `Rotation` hides texture repetition.
- `TimeScale` (0 to 1): slows the emitter's whole simulation; useful for a slow-motion beat. It cannot run faster than 1.
- `Shape` (Box, Sphere, Cylinder, Disc), `ShapeStyle` (Volume or Surface), `ShapeInOut`, `ShapePartial`: where on a part particles are born and whether they move outward or inward (inward = a gather or charge).

**Look**
- `Texture`: a white or greyscale image with alpha, tinted by `Color` (ColorSequence over the particle's life). Drawn, shaped textures are where X4's detail comes from.
- `Size` (NumberSequence, studs) and `Transparency` (NumberSequence, 0 opaque to 1 invisible) run over each particle's life. A NumberSequence holds at most 20 keypoints; each keypoint may carry an envelope for random spread.
- **Fade in and out (X3):** never start or end a particle visible at full size.
```lua
-- in over the first 15%, hold, out over the last 40%
emitter.Transparency = NumberSequence.new({
	NumberSequenceKeypoint.new(0, 1),
	NumberSequenceKeypoint.new(0.15, 0),
	NumberSequenceKeypoint.new(0.6, 0.1),
	NumberSequenceKeypoint.new(1, 1),
})
-- grow fast, then shrink away
emitter.Size = NumberSequence.new({
	NumberSequenceKeypoint.new(0, 0.2),
	NumberSequenceKeypoint.new(0.2, 1.6),
	NumberSequenceKeypoint.new(1, 0),
})
```
- `LightEmission` (0 to 1): 0 is normal blending, 1 is additive (colours add to what is behind, so overlapping particles burn toward white). Additive is the easy white core; it also vanishes against a bright sky and cannot draw anything dark (black smoke or a dark core needs 0).
- `LightInfluence` (0 to 1): how much the world's lighting tints the particles. 0 = always full colour (energy, magic, glows); 1 = lit like the scene (dust, smoke, debris).
- `Brightness`: scales the light the particles give off; values above 1 push a core toward bloom.
- `Squash` (NumberSequence): non-uniform scale over life; positive stretches the particle tall and thin, negative short and wide. Streaks, stretch-and-settle sparks.
- `Orientation`: `FacingCamera` (default billboard), `FacingCameraWorldUp` (upright billboard: flames, pillars), `VelocityParallel` (stretched along travel: sparks, streaks, speed lines), `VelocityPerpendicular` (flat, facing along travel: ground rings, see section 6).
- `ZOffset` (studs): draws the particle nearer to or farther from the camera without changing its size. Positive pulls a core in front of its own glow or of the mesh it sits on; it also settles sorting fights between layers.
- **Flipbooks** (animated textures): `FlipbookLayout` (None, Grid2x2, Grid4x4, Grid8x8), `FlipbookMode` (Loop, OneShot, PingPong, Random), `FlipbookFramerate`, `FlipbookStartRandom`. The sheet must be square. OneShot plays the frames once across the particle's lifetime, so Lifetime sets the speed. Drawn flame, slash and smoke animations (the V03 look) are flipbooks. Sheet size limit 1024 x 1024 **(verify)**.

## 3. Beam

A textured ribbon between two Attachments (`Attachment0`, `Attachment1`); it follows them every frame.
- `Width0`, `Width1` (studs at each end); `Segments` (straight pieces; raise it for curves); `CurveSize0`, `CurveSize1` bend it as a cubic Bezier whose control points lie along each attachment's X axis, so rotating an attachment steers the curve.
- `Color` and `Transparency` are sequences **along the beam's length**, not over time. Fade the ends: transparency 1 at both tips.
- `Texture`, `TextureMode`, `TextureLength`, `TextureSpeed` (scrolls the texture: energy flow), `FaceCamera`, `LightEmission`, `LightInfluence`, `Brightness`, `ZOffset`.
- Over time: `Width0` and `Width1` are plain numbers and tween with TweenService. A NumberSequence does not tween: drive a fade from a loop or a tweened NumberValue that rebuilds the sequence.
```lua
local function beamAlpha(beam: Beam, a: number) -- a: 0 visible .. 1 gone, tips always soft
	beam.Transparency = NumberSequence.new({
		NumberSequenceKeypoint.new(0, 1),
		NumberSequenceKeypoint.new(0.15, a),
		NumberSequenceKeypoint.new(0.85, a),
		NumberSequenceKeypoint.new(1, 1),
	})
end
```
- Uses: lasers, lightning (several short beams between jittered attachments), tethers, flat ground cones, light shafts. A pillar that shrinks its width to 0 while fading reads better than one that only fades (X3).

## 4. Trail

A ribbon drawn behind two moving Attachments on the same part (`Attachment0`, `Attachment1`: the two edges of the ribbon).
- `Lifetime` (seconds each segment lasts: the trail's length in time), `MinLength`, `MaxLength`, `WidthScale` (NumberSequence along the trail: taper to 0 at the tail), `Color` and `Transparency` (along the trail: fade the tail to 1), `Texture`, `TextureMode`, `TextureLength`, `FaceCamera`, `LightEmission`, `LightInfluence`.
- A trail only draws while its attachments move. Teleporting the part draws a streak across the map: set `Enabled = false` before a teleport or a pool return, call `trail:Clear()`, move, then enable again.
- To end softly: set `Enabled = false` and wait `Lifetime` before destroying the part.
- Uses: projectiles, weapon swings (attachments at blade base and tip), dashes.

## 5. Attachments and effect rigs

- An Attachment is a point with an orientation inside a part; emitters, beams, trails and lights hang from it. One invisible carrier part with several attachments is a whole effect rig.
- Save authored effects as templates (a Part, Model or Attachment holding emitters, beams and lights) in the game's templates folder; clone, place, play, clean up. Store per-emitter burst data on the template as attributes (for example an emit count, a delay, a duration: a common convention of VFX plugins, name them as the game already does) so artists retune without code.
- Play a template: for each ParticleEmitter descendant wait its delay, then `Emit(count)` or enable it for its duration; scale counts by the quality level.
- To follow a character, parent the attachment to a body part (or weld the carrier). Under `Terrain` an attachment's position is a world position, handy for one-shot points with no carrier part **(verify)**.

## 6. Lights

- `PointLight` (`Brightness`, `Range` up to 60 studs, `Color`), `SpotLight` (adds `Angle` and `Face`). Keep `Shadows = false` on effect lights.
- A pulse: create at brightness 0, tween up in about 50 ms, down over 150 to 300 ms, then destroy. A light that pops on and off breaks X3 like any other element.
```lua
local light = Instance.new("PointLight")
light.Color, light.Range, light.Brightness, light.Shadows = color, 14, 0, false
light.Parent = attachment
TweenService:Create(light, TweenInfo.new(0.05), { Brightness = 3 }):Play()
task.delay(0.05, function()
	local out = TweenService:Create(light, TweenInfo.new(0.25, Enum.EasingStyle.Quad, Enum.EasingDirection.Out), { Brightness = 0 })
	out.Completed:Once(function() light:Destroy() end)
	out:Play()
end)
```
- Lights are among the most expensive parts of an effect: one per effect on the frequent tier, none at the lowest quality level.

## 7. Meshes: shards, rings, domes, slashes

Shaped meshes are the cheapest way to real detail (X4): V04's icicles are meshes, not particles.
- Use MeshParts (or Parts) with `Anchored = true`, `CanCollide = false`, `CanQuery = false`, `CanTouch = false`, `CastShadow = false`, `Massless = true`.
- **In and out (X3):** tween `Size` up from a small fraction (not from zero) with a fast ease-out, hold, then tween `Size` down and `Transparency` to 1 together. Stagger siblings by 10 to 30 ms and vary yaw, tilt and scale a little (X2).
- Shards that rise from the ground: start the part sunk below the surface and tween its CFrame up as it scales.
- **Shockwave ring, mesh:** a flat ring or disc mesh on the ground, `Size` X and Z tweened outward with ease-out while `Transparency` goes to 1; thin it as it grows.
- **Shockwave ring, particle:** one particle with a ring texture, `Orientation = VelocityPerpendicular`, the emitter aimed straight up with a tiny `Speed` (about 0.01) so the particle lies flat, `Size` growing and `Transparency` fading over its life, `Emit(1)`.
- **Dome or sphere:** a ball with `Material = ForceField` or Neon, or an inverted-normal mesh for a dome seen from inside; scale it in, fade it out.
- Neon's glow depends on the client's graphics quality (bloom) **(verify)**: do not rely on glow alone to make a shape read.
- A `Highlight` flash on a hit character is a cheap impact accent; the engine shows only a limited number of Highlights at once (31 **(verify)**), so keep them brief and few.

## 8. Cleanup and pooling

- Everything an effect creates has an owner and an end. One-shots: `Debris:AddItem(instance, seconds)` or `task.delay(seconds, function() instance:Destroy() end)`, with `seconds` = the last emit time + the longest `Lifetime.Max` + a small margin. Destroying an emitter's parent earlier cuts its live particles (X3).
- Stop order for a held effect: `Enabled = false` on emitters and trails, wait the longest lifetime, then destroy or pool.
- **Pool frequent effects.** Keep carrier parts and cloned templates in a folder; on return disable emitters, clear trails and reset EVERY property the effect tweened (Size, Transparency, CFrame, Brightness, Width). A pooled part that keeps the last cast's size is a classic bug.
- Guard delayed callbacks: give each use a token and have the callback check it, so a late timer from the previous use cannot switch off the next one.
- Limit frequent bursts per effect: a minimum interval between two plays and a cap on how many are alive; refuse the extra ones silently.
- Disconnect RenderStepped and Heartbeat connections and unbind render steps when the effect ends, including when the character or the target is destroyed mid-effect.

## 9. Reduced Motion and the player's settings

```lua
local GuiService = game:GetService("GuiService")
local function reducedMotion(): boolean
	local ok, on = pcall(function()
		return GuiService.ReducedMotionEnabled
	end)
	return ok and on == true
end
```
Read it when the effect plays, on the client. Under Reduced Motion: no camera shake, no inversion, flashes softened or dropped, loops stopped or slowed; the effect still shows what happened (E1). The game's profile states the exact policy.

## 10. Camera shake (client, RARE tier only: X6)

Decaying noise added after the camera script has written the frame's CFrame. The default camera rewrites `CFrame` every frame, so the offset does not pile up; with a Scriptable camera the game's own camera code must add the offset instead.
```lua
local RunService = game:GetService("RunService")

local function shake(amplitude: number, duration: number) -- studs, seconds
	if reducedMotion() or amplitude <= 0 then
		return
	end
	local camera = workspace.CurrentCamera
	local seed = math.random() * 1000
	local name = "VfxShake_" .. tostring(seed)
	local t0 = os.clock()
	RunService:BindToRenderStep(name, Enum.RenderPriority.Camera.Value + 1, function()
		local t = os.clock() - t0
		if t >= duration then
			RunService:UnbindFromRenderStep(name)
			return
		end
		local k = amplitude * (1 - t / duration) ^ 2 -- strongest at the hit, eases to zero
		local x = math.noise(seed, t * 25) * 2 * k -- math.noise stays roughly within -0.5..0.5 (verify)
		local y = math.noise(seed + 57, t * 25) * 2 * k
		camera.CFrame *= CFrame.new(x, y, 0)
	end)
end
```
- Keep it small (start values in `tiers.md`), start it on the impact frame, never loop it. Scale it down with distance from the hit and skip it past a cut-off range.
- Offer a strength setting if the game has a settings screen; shake is a common cause of motion sickness.
- A lighter alternative is `Humanoid.CameraOffset` driven the same way; it moves the camera subject offset rather than the camera.

## 11. Impact frames and screen flashes (client, RARE tier only: X6)

- **Impact frame, drawn:** a ScreenGui (`IgnoreGuiInset = true`, a high `DisplayOrder`, `ResetOnSpawn = false`) with one full-screen ImageLabel showing a high-contrast drawn frame (speed lines, a two-tone silhouette) for about 3 frames, then removed. Preload the image with `ContentProvider:PreloadAsync` beforehand or the first play shows nothing. This is the one place a hard cut is the style; keep it to the peak.
- **Impact frame, colour pulse:** a `ColorCorrectionEffect` parented to `workspace.CurrentCamera` (post effects work there as well as under Lighting, and stay local to this client and out of the game's Lighting setup): push `Contrast` up and `Saturation` to -1 for 2 or 3 frames, optionally with a `TintColor`, then tween back over 100 to 200 ms. Never leave it behind: restore or destroy it in every exit path.
- **Colour inversion:** no built-in invert effect. A strongly negative `Contrast` is sometimes used for it **(verify the range and the look in Studio)**; a drawn inverted frame (white on black, then black on white) is the reliable way.
- **Darkened world:** a dark dome mesh around the area (seen from inside), or a ColorCorrectionEffect `Brightness` dip on the camera. Do not script the game's Lighting properties unless its rules allow it; many games keep Lighting hand-tuned.
- **White flash:** prefer a local one (an additive particle or a light pulse at the hit). A full-screen flash is a frame with `BackgroundColor3` white, `BackgroundTransparency` tweened from about 0.3 to 1 in 100 to 200 ms; do not start fully opaque outside a cutscene (guess).
- **Photosensitivity:** no more than three full-screen flashes in any one second (WCAG 2.3.1); avoid large saturated red flashes; under Reduced Motion drop inversion and soften or drop flashes. Never chain impact frames back to back for longer than the tier allows.

## 12. Performance budgets and quality levels

- Costs, roughly in order: overdraw (many large, transparent, overlapping particles: a few big soft sprites near the camera cost more than hundreds of small sparks), lights (worse with shadows), particle count, part count and tweens, texture memory. Budgets per tier are in `tiers.md` (guesses until measured).
- Prefer one emitter with `Emit(12)` over twelve parts; prefer a mesh over a particle cloud when the shape matters.
- Skip effects the player cannot see: past a distance cut-off, or play a reduced version (core and ring only).
- Check the cost with the MicroProfiler and the fps readout while spamming the effect with several players' worth of casts.
- **Quality levels:** if the game has them (the profile's VFX block), obey them; if not, propose them rather than add them silently. A labelled example of a common three-level scheme, not a rule: Full = everything; Low = particle counts scaled down, lights and secondary layers dropped, the core shape kept; Off = no cosmetic particles, but anything that carries gameplay information (a hit, a telegraph) still shows in a minimal form. Reduced Motion can map onto the lower level.
- The engine's own graphics quality also thins particles and removes bloom at low settings; test the effect at the lowest setting once.
