# Roblox recipes

Luau building blocks for UI motion. Engine facts marked **(verify)** are believed true but should be confirmed in Studio before relying on them; everything else is stated with confidence. Use the game's own UI kit and motion table where they exist; these are patterns, not a library to paste over a kit.

## 1. One motion table

All durations and easings are named tokens in one module. Panel code names a token, never a raw `TweenInfo.new`.

```lua
local TweenService = game:GetService("TweenService")
local GuiService = game:GetService("GuiService")

local Motion = {}

-- Debug only. 10 = ten times slower, for frame captures. Ship at 1.
Motion.TIME_SCALE = 1

-- Values come from the game's genre profile. { seconds, style, direction }
Motion.TOKENS = {
	press   = { 0.05, Enum.EasingStyle.Quad, Enum.EasingDirection.Out },
	enter   = { 0.18, Enum.EasingStyle.Quad, Enum.EasingDirection.Out },
	popIn   = { 0.18, Enum.EasingStyle.Back, Enum.EasingDirection.Out },
	exit    = { 0.10, Enum.EasingStyle.Quad, Enum.EasingDirection.In },
	swapOut = { 0.10, Enum.EasingStyle.Quad, Enum.EasingDirection.In },
	swapIn  = { 0.10, Enum.EasingStyle.Quad, Enum.EasingDirection.Out },
}

function Motion.reduced(): boolean
	local ok, on = pcall(function()
		return GuiService.ReducedMotionEnabled
	end)
	return ok and on == true
end

function Motion.info(token: string): TweenInfo
	local m = assert(Motion.TOKENS[token], "unknown motion token " .. tostring(token))
	return TweenInfo.new(m[1] * Motion.TIME_SCALE, m[2], m[3])
end
```

## 2. TweenService and easing facts

- `TweenInfo.new(time, easingStyle, easingDirection, repeatCount, reverses, delayTime)`. Defaults: 1 s, Quad, Out, 0, false, 0. `repeatCount = -1` loops for ever.
- Styles: Linear, Sine, Quad, Cubic, Quart, Quint, Exponential, Circular, Back, Bounce, Elastic. Directions: In (slow start), Out (slow end), InOut.
- Entries use Out. Exits use In. Loops may use Linear or Sine InOut. Nothing else uses Linear.
- Strength, mild to sharp: Sine, Quad, Cubic, Quart, Quint, Exponential. For UI beats of 100 to 250 ms, Quad and Quart cover nearly every case.
- **Back Out overshoots 10% of the distance TRAVELLED, not 10% of the final size**, peaking at 58% of the tween's time (measured in Studio 2026-11-10: `TweenService:GetValue` peak 1.100004 at alpha 0.580; a 0.18 s UIScale 0.92 -> 1 peaked at 1.00785 at 0.098 s; `evidence/engine/back-easing-2026-11-10.md`). For a scale pop: peak = 1 + 0.1 x (1 - start). Consequences:
  - UIScale 0.92 -> 1 peaks at 1.008 (0.8% over: too small to see, it reads as a plain ease-out). 0.85 -> 1 peaks at 1.015. 0.8 -> 1 peaks at 1.02. 0.5 -> 1 peaks at 1.05: the R11 limit. Never start a Back pop below 0.5.
  - A Back slide of 300 px overshoots by about 30 px. Check that against R11 (5% of the element's size) before using Back on Position. Prefer Quad or Quart Out for slides.
  - Back In dips backwards first: do not use it for exits.
- To get a visible peak (for example 102%), either start the Back pop from 0.8, or, if the start must stay close to 1, use two tweens: start -> 1.02 with Quad Out in about 70 ms, then 1.02 -> 1 with Quad InOut in about 130 ms.
- Bounce and Elastic overshoot or rebound several times: forbidden on panels and cards (R11).
- TweenService can tween numbers, booleans, Color3, UDim, UDim2, Vector2, Vector3, CFrame, Rect and a few more. It cannot tween `NumberSequence` or `ColorSequence`: animate a `UIGradient` through `Offset` or `Rotation`, not by tweening its sequences.
- **Playing a new tween on a property that another tween is animating cancels the older tween.** The older tween's `Completed` fires with `Enum.PlaybackState.Cancelled`. Always check the state in `Completed` before acting:

```lua
tween.Completed:Once(function(state)
	if state == Enum.PlaybackState.Completed then
		frame.Visible = false
	end
end)
```

- `tween:Cancel()` stops the tween and leaves the properties where they are. A new tween then starts from the current values, which is what an interrupted open or close needs.
- A tween keeps running on an invisible or unparented-from-screen object. Cancel loops when a panel hides.

## 3. Sequencing beats

One helper runs a beat table, sets start states before the first frame (E5), is cancellable (E2) and collapses under Reduced Motion (E1).

```lua
-- beats: { { at = ms, inst = Instance, token = "enter", from = {prop = value}?, to = {prop = value} }, ... }
local running = setmetatable({}, { __mode = "k" }) -- root -> run

function Motion.play(root: Instance, beats, onDone: (() -> ())?)
	local old = running[root]
	if old then
		old.cancelled = true
		for _, t in old.tweens do
			t:Cancel()
		end
	end
	local run = { tweens = {}, cancelled = false }
	running[root] = run

	if Motion.reduced() then
		for _, b in beats do
			for k, v in b.to do
				b.inst[k] = v
			end
		end
		running[root] = nil
		if onDone then onDone() end
		return run
	end

	-- Start states before anything is drawn. Skipped when interrupting a running
	-- sequence, so the new one continues from where the old one stopped.
	if not old then
		for _, b in beats do
			if b.from then
				for k, v in b.from do
					b.inst[k] = v
				end
			end
		end
	end

	local finish = 0
	for _, b in beats do
		local info = Motion.info(b.token)
		local startAt = b.at / 1000 * Motion.TIME_SCALE
		finish = math.max(finish, startAt + info.Time)
		local function go()
			if run.cancelled then return end
			local t = TweenService:Create(b.inst, info, b.to)
			table.insert(run.tweens, t)
			t:Play()
		end
		if startAt == 0 then go() else task.delay(startAt, go) end
	end
	task.delay(finish, function()
		if run.cancelled then return end
		running[root] = nil
		if onDone then onDone() end
	end)
	return run
end
```

Use: build the `open` beats and the `close` beats once per panel from the beat table. `open` sets `Visible = true` first, then plays. `close` plays and sets `Visible = false` in `onDone` (which never runs if a re-open cancelled it). Keep the beat table in the code as data, so the plan and the build can be compared line by line.

Notes:
- `task.delay` is accurate to about one frame (16 ms at 60 fps). Staggers of 50 ms and up are safe; do not plan staggers under 30 ms.
- `TweenInfo`'s own `delayTime` also staggers, but a delayed tween is harder to cancel cleanly as a group; the helper above is preferred.
- The elements of one beat that must change on the same frame (R5) belong in one `CanvasGroup` or are started in the same call, never in separate `task.delay` calls.

## 4. Fading a group: CanvasGroup

A `CanvasGroup` draws its descendants into one texture and exposes `GroupTransparency` (0 to 1) and `GroupColor3` (a tint). Tween `GroupTransparency` to fade a whole column, card or panel as one surface.

Why not tween each child: a panel has `BackgroundTransparency`, `TextTransparency`, `TextStrokeTransparency`, `ImageTransparency`, `UIStroke.Transparency` and `ScrollBarImageTransparency` on many objects; fading them one by one makes overlapping layers show through each other mid-fade, and each needs its own rest value restored.

Costs and limits:
- Descendants are clipped to the CanvasGroup's rectangle. Shadows, glows, badges or ornaments that hang outside it are cut off. Give the group padding, or keep the overhanging ornament outside the group as its own beat.
- Each group holds a texture about the size of its on-screen area: memory and a re-draw whenever anything inside changes. Use a few (one per beat group), not one per row of a long list. Do not wrap a whole-screen HUD that updates every frame.
- The group texture can render at reduced resolution on low-memory devices or low quality levels, so text inside may look softer than outside **(verify on the target devices)**.
- A `UICorner` on the CanvasGroup rounds the clip of its content **(verify)**. A plain Frame's `ClipsDescendants` never follows rounded corners.
- An object at `GroupTransparency = 1` still exists for input. A hidden panel must end with `Visible = false`, or its invisible buttons take clicks.
- For one or two simple elements (a label, an icon) tween their own transparency instead; no CanvasGroup needed.

In-place cross-fade (R5), all dependent texts in one group:

```lua
local function swapValue(group: CanvasGroup, apply: () -> ())
	if Motion.reduced() then apply() return end
	local out = TweenService:Create(group, Motion.info("swapOut"), { GroupTransparency = 0.6 })
	out.Completed:Once(function(state)
		if state ~= Enum.PlaybackState.Completed then return end
		apply() -- set the new name, sub-line, description, pager dot
		TweenService:Create(group, Motion.info("swapIn"), { GroupTransparency = 0 }):Play()
	end)
	out:Play()
end
```

If `apply` is also called on a rapid second press, make sure the latest value wins: keep a counter and apply only the newest request.

Tab change inside one frame without a blank frame: clone the current content into a temporary non-interactive CanvasGroup above it, rebuild the real content underneath, fade the clone out in about 160 ms (ease In), destroy it. Set `Interactable = false` on cloned buttons.

## 5. Pops: UIScale

- Put a `UIScale` (give it a fixed name, for example `Pop`) on the element and tween `Scale`. Layout around the element does not reflow the way it does when `Size` is tweened.
- The element scales about its `AnchorPoint`. For a pop from the centre set `AnchorPoint = Vector2.new(0.5, 0.5)` and position it by its centre.
- Only one `UIScale` per object takes effect. If the element already carries a fit-to-screen UIScale, put that one on a holder frame and the pop on the child.
- `AutomaticSize` on an object under a UIScale has been seen to count the scale twice (observed in one production game). If sizes look wrong under a UIScale, size the object from measured text bounds instead.
- Text sizes above 100 are not possible with `TextSize`; a UIScale on the label is the way to go bigger.
- Whether `UIStroke` thickness follows a UIScale depends on engine version and stroke settings **(verify)**: look at strokes in the captured frames of a pop.

Press feedback (starts on the input frame, never waits for the action):

```lua
button.MouseButton1Down:Connect(function()
	if Motion.reduced() then return end
	TweenService:Create(scale, Motion.info("press"), { Scale = 0.96 }):Play()
end)
local function release()
	TweenService:Create(scale, Motion.info("popIn"), { Scale = 1 }):Play()
end
button.MouseButton1Up:Connect(release)
button.MouseLeave:Connect(release)
button.Activated:Connect(doTheAction) -- the action itself; works for mouse, touch and gamepad
```

Hover state from `MouseEnter` / `MouseLeave` breaks if the object is destroyed and rebuilt under a resting pointer (the events do not fire). Build once and restyle, or test the pointer position against the object instead.

## 6. Sweeps and masks: UIGradient and ClipsDescendants

- A `UIGradient` has `Color`, `Transparency` (a NumberSequence), `Rotation` and `Offset` (a Vector2 in units of the parent's size). Tween `Offset` to move it.
- It affects only what its parent itself draws (background, image, text), not the parent's children. To mask a group, put the gradient on a CanvasGroup that holds the group **(verify that the gradient applies to the composed group in the current engine)**, or mask each element.
- Wipe reveal: `Transparency` = opaque up to 0.45, clear from 0.55; tween `Offset` from `Vector2.new(-1, 0)` to `Vector2.new(1, 0)`.
- Sheen: a white Frame over the element with a gradient that is clear, then about 60% opaque in a narrow band, then clear, rotated about 20 degrees; tween its `Offset` across once. Clip it with the element's bounds. One sheen is hero material (R7, R8), not something for every card.
- A UIGradient on a `TextButton` or `TextLabel` tints its text as well. Put the gradient on a child Frame behind the text.
- `ClipsDescendants` clips to an axis-aligned rectangle. It ignores `UICorner` rounding, and it stops clipping when the clipping object or an ancestor is rotated. Slide-in-from-behind-an-edge reveals: a clipping Frame with the moving child inside.

## 7. Reduced Motion

`GuiService.ReducedMotionEnabled` mirrors the player's Roblox setting (read it inside `pcall`, as above, in case of an older client).

- Read it at the moment of each transition, not once at start-up: the player can change it mid-session.
- Under it: no scale, slide, overshoot, squash, stagger, idle loop, shimmer or particle. A state change is instant or, if the profile allows, a single opacity fade of 150 ms or less.
- The end state must be identical with and without it. Bugs hide here: a start state (`Scale = 0.92`, `GroupTransparency = 1`) that the skipped tween never undoes. The helper in section 3 writes every `to` value directly for this reason.
- Idle loops: do not start them; if the setting turns on while one runs, stop it at the next cycle.
- Sound and colour feedback stay.

## 8. Text

- `TextLabel` has no letter-spacing (tracking) property **(true at the time of writing; verify)**. For tracked caps: a font with wide caps, thin spaces between letters for short labels, or one label per letter for a large title only.
- Measure text before sizing a container: `TextService:GetTextBoundsAsync(params)` with a `GetTextBoundsParams` (Text, Font, Size, Width). It yields and can fail: call it in `pcall`, off the hot path, and cache. `TextLabel.TextBounds` gives the bounds of an existing label after layout.
- `TextScaled` makes neighbouring labels end at different sizes, which breaks the three-voice hierarchy (R9). Use fixed `TextSize` values from the kit; if scaling is needed, a `UITextSizeConstraint` with the same max on sibling labels. A UIScale does not change a `UITextSizeConstraint`'s limits.
- `TextTransparency` and `TextStrokeTransparency` fade separately; forgetting the stroke leaves an outline ghost. A CanvasGroup avoids this.
- `MaxVisibleGraphemes` reveals text letter by letter (a typewriter). Use it only if the theme vocabulary calls for it, and never as scramble or decode text unless the profile lists that.
- Never tween the `Size` of a wrapped text container: the text re-wraps every frame.

## 9. Sparkle in UI: 2D pieces and flipbooks

- **A `ViewportFrame` does not render `ParticleEmitter`s** (nor, as far as known, Beams and Trails). Do not plan UI particles that way. (Some notes in `evidence/` suggest it; treat that as an error.)
- 2D burst: a small pool of `ImageLabel`s (8 to 12), each tweened once for position, rotation, size and transparency over 300 to 600 ms with Quad Out, then returned to the pool with every property reset. Seed the directions randomly so two bursts differ.
- Flipbook: one sprite sheet image, `ImageRectSize` = one cell, step `ImageRectOffset` at a fixed rate (12 to 24 per second) from a single `RunService.Heartbeat` connection that accumulates time; disconnect at the last cell. Keep sheets at 1024 x 1024 or under.
- Both are on-theme ornaments (R10) and count toward the idle budget if they loop (R7). Both are off under Reduced Motion.
- Preload images that appear inside a short entry (`ContentProvider:PreloadAsync`) or the first open shows them popping in late, which breaks the beat order.

## 10. Idle loops

```lua
-- One hero loop: active for a short part of a long cycle. Stops when hidden.
local function heroLoop(panel: GuiObject, playOnce: () -> (), cycle: number)
	task.spawn(function()
		while panel.Parent and panel.Visible do
			task.wait(cycle)
			if not (panel.Parent and panel.Visible) then break end
			if not Motion.reduced() then
				playOnce() -- 700 ms or less of motion
			end
		end
	end)
end
```

Start it when the panel opens; make sure only one runs per panel (keep a flag or a token). Prefer this to `repeatCount = -1` tweens when most of the cycle is rest.

## 11. Performance and robustness

- Prefer tweening `UIScale.Scale`, `GroupTransparency`, a single element's transparency, `UIGradient.Offset` and `Position`. Avoid tweening `Size` of objects inside a `UIListLayout` or `UIGridLayout` (every frame re-lays the list) and anything holding wrapped text.
- Build a panel's objects once; open and close only change properties. Rebuilding on every refresh kills hover states and running tweens and makes rows flicker.
- One `Heartbeat` or `RenderStepped` connection per panel at most, disconnected when the panel hides. No per-frame `TweenService:Create`.
- Keep CanvasGroups few and no larger than they need to be.
- Stagger long lists by row group, not by row: animate the first 6 to 8 visible rows as beats, show the rest with the last one. Rows scrolled out of view need no motion.
- Wrap optional flourishes (bursts, sheens, sounds) so a failure in one cannot leave the panel half open.
- Test at a small window and a large one. A layout that only looks right in Studio's viewport size is not done.
