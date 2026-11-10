# Review loop

Motion is verified from frames and measurements, never from reading the code and never from one screenshot of the resting state. The loop: capture, measure, grade, fix, recapture, then hand the rest to the owner.

## 1. Set up the capture

A UI beat lasts 100 to 200 ms. A screenshot tool driven by an agent takes one picture every few hundred milliseconds at best, with uneven delay. So slow the motion down and stamp every frame with its own time.

**a. Time scale.** The motion table has a debug constant (see `roblox-recipes.md`, `Motion.TIME_SCALE`) that multiplies every duration and every beat start. Set it for the capture session only (in the running client, or in the Studio copy), never in committed code. Choose it so that the transition lasts at least 8 capture intervals: with one capture per second and a 300 ms entry, use 30 (the entry then lasts 9 s). Sounds are not slowed; ignore them here.

If the game's motion code has no single table, that is finding number one (E4): add the table first.

**b. Elapsed label.** Add a temporary debug label in a screen corner that shows the game-time milliseconds since the trigger, already divided by the time scale, so each captured frame states its own time at real speed:

```lua
-- Debug only. Remove after the review.
local label = Instance.new("TextLabel")
label.Size = UDim2.fromOffset(120, 28)
label.Position = UDim2.fromOffset(8, 8)
label.BackgroundColor3 = Color3.new(0, 0, 0)
label.TextColor3 = Color3.new(1, 1, 0)
label.TextSize = 18
label.ZIndex = 1000
label.Parent = debugScreenGui

local t0 = os.clock()
local conn = game:GetService("RunService").RenderStepped:Connect(function()
	label.Text = string.format("%d ms", (os.clock() - t0) * 1000 / Motion.TIME_SCALE)
end)
-- call t0 = os.clock() on the same line that triggers the open or close
```

**c. Trigger through the real path.** Open the panel the way a player does (the real button or key), not by calling an internal function, so that the real start state, sound and input handling are in the capture.

**d. Capture set.** For each panel changed:

| Capture | Frames |
|---|---|
| Entry | at least 8 across the transition, plus 1 at rest |
| Exit | at least 6, plus 1 after (panel gone) |
| One swap or tab change (if the panel has one) | at least 8 |
| One in-place value change (if any) | at least 5 |
| Rest state over time | 6 frames, 1 s apart at time scale 1 (idle motion check, R7) |
| Interrupt: open, close, open within 150 ms (time scale 1) | 1 frame at rest |
| Reduced Motion on: entry and exit | 2 frames each, plus rest |
| Worst background for text (brightest, busiest scene) | 1 frame at rest |
| Small window and large window | 1 frame each at rest |

Use whatever screenshot tool the session has (for example a Studio MCP screen capture). Check first that the tool draws the layer under test: some capture tools skip BillboardGuis or lose the 3D layer. If a layer cannot be captured, say so and list it for the owner's eyes.

Reduced Motion: turn the setting on in the client's Roblox settings. If the session cannot do that, temporarily make the game's `reduced()` helper return true in the running client and say in the report that the real setting was not exercised.

**e. Numeric trace (the timing truth).** Frames show the look; a trace gives exact times. During the same run, record the animated properties every frame:

```lua
-- Debug only. watch = { {name = "panel.scale", get = function() return panelScale.Scale end}, ... }
local rows = {}
local t0 = os.clock()
local conn
conn = game:GetService("RunService").RenderStepped:Connect(function()
	local row = { math.floor((os.clock() - t0) * 1000 / Motion.TIME_SCALE) }
	for _, w in watch do
		table.insert(row, w.get())
	end
	table.insert(rows, row)
end)
-- after the transition: conn:Disconnect(); print rows as CSV
```

Watch each beat's driving property (`Scale`, `GroupTransparency`, `Position`). The trace can be taken at time scale 1 as well, which also proves the real-speed timing.

## 2. Measure

From the trace (or, failing that, from the frame labels):

| Quantity | How | Compare with |
|---|---|---|
| Start of each beat | first row where its property leaves the start value | the beat table |
| Stagger | difference between consecutive beat starts | profile range |
| Beat duration | start to the first row at the rest value | the beat table |
| Entry total | trigger to the last property at rest | R2 and the profile |
| Exit total, and exit / entry | same way | R3 (0.40 to 0.65) |
| Peak overshoot | largest scale (or position past rest, as a percent of the element's size) | R11 and the profile |
| Settle time | pop start to the first row that stays at rest | R11 (200 ms) |
| Swap gap | end of the old panel's last beat to the start of the new one's first | R4 (0 to 30 ms, never negative) |
| Value change | first change to rest | R5 (160 to 240 ms) |

Precision: a trace at 60 fps is good to about 17 ms at time scale 1. Frame labels are good to one capture interval divided by the time scale. A measured value that differs from the plan by more than that precision is a defect in the build or in the plan; fix whichever is wrong and say which.

If only frames are available: duration = (label of the first frame at rest) minus (label of the last frame at the start state); state the uncertainty.

## 3. Grade

The grader is not the builder. Use a fresh subagent (the strongest model available for subtle calls) and give it only: the frames, the trace or the measured table, the beat table, the game's project profile, the genre profile and `core-rules.md`. Do not give it the code or the builder's opinion. If no second agent is available, grade in a separate pass after re-reading the rules, and say so in the report.

Rules for the grader:
- Every verdict cites a frame (by its ms label) or a trace row. No frame, no pass.
- "Looks fine" is not a verdict. Use pass, fail, or cannot tell (and then name what capture would settle it).
- A fail states the rule id, what was seen, and the smallest change that would pass.
- Do not soften: one fail means the build is not done.

### Grading form

```
Panel: <name>            Frequency: frequent | rare
Game profile: <path>     Genre profile: <name> (status: evidenced | draft)
Hero: <element>          Anchor: <element>
Time scale used: <n>     Capture interval: <ms>   Precision: +/- <ms>

MEASURED            planned   measured   limit            verdict   proof (frame ms / trace)
entry total         ...       ...        <= 350 / 800     ...
exit total          ...       ...        40-65% of entry  ...
beats (count)       ...       ...        profile          ...
stagger (min-max)   ...       ...        profile          ...
peak overshoot %    ...       ...        <= 105, profile  ...
settle ms           ...       ...        <= 200           ...
swap gap ms         ...       ...        0-30, no overlap ...
value change ms     ...       ...        160-240          ...
idle elements       ...       ...        profile budget   ...
idle cycle s        ...       ...        >= 3, profile    ...

CORE RULES          verdict   proof / note
R1 beats in order
R2 budget
R3 exit half, reversed
R4 no overlap on swap
R5 in-place change
R6 still anchor
R7 idle only in hero
R8 one hero
R9 type hierarchy (<= 3 voices)
R10 on theme (each effect -> vocabulary word)
R11 small overshoot
R12 no placeholder text (string dump attached)
R13 legible on worst background
E1 Reduced Motion (nothing moves, end state identical)
E2 interruptible (open-close-open rests correctly)
E3 input live during entry
E4 tokens only
E5 start states set before first frame

PROFILE NUMBERS     (one line per row of the genre profile that this panel uses, and per override in the game's profile)

ANTI-SLOP           seen? (yes = fail)   proof
1 all at once / same speed
2 everything bounces
3 everything saturated, glowing or idling
4 linear motion outside loops
5 entry longer than the action
6 placeholder text / raw ids
7 effect from another genre
8 text loses against background

RESULT: pass | fail (n items)
FIXES REQUIRED: <rule id: change>
CANNOT TELL: <item: capture needed>
OWED TO THE OWNER'S EYES: <list>
```

How to judge the items that are not numbers:
- **R1, E5:** in the first frame after the trigger, nothing that belongs to a later beat is visible at rest.
- **R4:** no frame of the swap shows readable text of both pages.
- **R6:** the anchor's edges are at the same pixels in the first, middle and last frame.
- **R7:** compare the six rest frames; differences only inside the hero.
- **R8:** on the rest frame, name what the eye lands on first; then count glows, full-saturation elements and idle elements.
- **R9:** list the distinct text styles.
- **R10:** each effect mapped to a word of the theme vocabulary; none on the refused list.
- **R12:** read the dump of every visible string, not just the frame.
- **R13:** read every string in the worst-background frame and the small-window frame.

## 4. Fix and recapture

Fix every fail. Recapture the transitions that changed and re-measure; re-grade the changed items and re-run the whole anti-slop list (fixes cause new slips). Two rounds are normal. If the same item fails three times, or the builder believes the rule is wrong for this game, stop and take it to the owner with the frames.

Afterwards: set the time scale back to 1, remove the debug label and the trace, and confirm at real speed that the panel still opens and closes (one frame at rest is enough).

## 5. Escalate to the owner's eyes

Frames at slow speed cannot judge everything. Always hand these to the owner, stated plainly as not yet verified:

- **Feel at real speed**: whether the motion feels quick, calm, heavy or cheap. Slow-motion frames prove order and size, not feel.
- **Sound**: timing against the motion, loudness, whether cues suit the theme.
- **Taste calls**: whether the hero is the right hero, whether an ornament is charming or too much. The owner's standard: subtle, not noisy; "too much is less".
- **Any override** of a core rule or a profile number. Record the owner's words and reason in the game's project profile.
- **Anything the capture tool could not draw**, and real devices (phone, low-end PC, a very large screen).
- **The real Reduced Motion setting**, if the review only faked it.
- **A draft profile**: when the genre profile's status is draft, every number was a guess, so the owner's reaction is the only evidence. Offer to record it as evidence.

How to ask: show the frame strip, state the measured numbers, ask one precise question per doubt. Fix exactly what the owner notes, recapture, and log the ruling in the game's decision log.

## 6. What to report

The beat table as built, planned against measured totals, the grading form, the list of fixes made between rounds, and the "owed to the owner's eyes" list. Never write "verified" for an item that was only read from code.
