# Review loop

Motion is verified from frames and measurements, never from reading the code and never from one screenshot of the resting state. The loop: capture, measure, grade, fix, recapture, then hand the rest to the owner.

Grading order follows the owner's scoring: identity first (I1 to I4), then motion (R and E rules). A build that passes every motion rule and fails I2 is a fail, so do the identity checks on a resting screenshot BEFORE spending time on slow-motion capture.

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
| Identity: masked rest frame (logo, game name, named currencies and characters covered with a plain box) | 1 per panel changed |
| Identity: the rest frames of the game's other main panels, side by side with the changed one | 1 sheet |
| Show-off: rest frame with each idle or decorative effect switched off | 1 per effect |
| Benchmark (only if the profile names one): the build beside the benchmark's same kind of screen | 1 pair, for the reviewer only; never commit the benchmark's screenshot |

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

The hide-the-logo test needs a SECOND reviewer who has not read the game's profile (it states the identity, which would give the answer away). Give that reviewer only the masked rest frames and the question in I2. If no second reviewer is available, mark the item "cannot tell" and hand it to the owner; the grader must not answer it from memory of the profile.

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

IDENTITY (first)    verdict   proof / note
Identity statement (from the profile): "<...>"     Benchmark: <game or none>
I1 statement names a world (not adjectives, not just the genre)
I1 every element has its "how it expresses the identity" line (blanks: <n>)
I1 same surfaces, type, accent, borders across panels (side-by-side sheet)
I2 hide-the-logo: blind reviewer's answer: "<...>"   matches the identity? names >= 2 elements?
I2 generic tells present: <n> of <list size> (list them; >= 3 = fail; each kept tell has a reason)
I2 identity carriers: <list> (fewer than 3 = fail)
I3 every beat has a job for the player (blanks: <n>)
I3 effect types on the resting screen: <n> (limit: profile idle budget)
I3 removal test per idle or decorative effect: kept because <job> | cut
I4 benchmark: principles listed in words; build not mistakable for it (pair frame); no copied art, logo, icons, layout or trade dress

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
9 logo hidden: fits most games of the genre
10 three or more genre tells without a reason
11 a panel or icon set from another world
12 motion with no job / several effect types at rest
13 mistakable for the benchmark game

RESULT: pass | fail (n items)
FIXES REQUIRED: <rule id: change>
CANNOT TELL: <item: capture needed>
OWED TO THE OWNER'S EYES: <list>
```

How to judge the items that are not numbers:
- **I1:** read the statement, then look at the side-by-side sheet. Name any panel, tab or icon set that would look at home in a different game; that is the fail. Check the per-element lines against the frame: a line that claims a material or motif the frame does not show is a blank.
- **I2:** the blind reviewer's answer passes only if it describes the world of the identity statement and points at concrete elements (a shape, a material, a motif). "A simulator shop", "an RPG menu", "a clean dark UI" are genre or adjective answers: fail. Then tick the profile's "Generic tells" one by one on the unmasked rest frame, and list the identity carriers. The three results must agree; if the blind answer passes but 3 or more tells are present, it is still a fail.
- **I3:** for each effect read its job in the beat table, then compare the frame with the effect off. "It looks cool", "adds polish" and "makes it unique" are not jobs. Something moving on a screen where the player is reading or choosing needs the strongest reason.
- **I4:** compare the pair. Same placement of the same elements, the same frame shapes, look-alike icons or ornaments, or the same palette as a whole: fail. The same principle carried out with the game's own shapes and content (a still rail, a cross-fading detail pane, large numerals): pass.
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
- **Identity as a player reads it**: the checks prove the UI is not generic by the list; only the owner (and players) can say whether the identity is the right one and whether it "pops up immediately". Ask it as one question, with the masked frame: "what world is this?"
- **A benchmark comparison that is close to the line** (I4): show the pair and ask before shipping.
- **Taste calls**: whether the hero is the right hero, whether an ornament is charming or too much. The owner's standard: subtle, not noisy; "too much is less".
- **Any override** of a core rule or a profile number. Record the owner's words and reason in the game's project profile.
- **Anything the capture tool could not draw**, and real devices (phone, low-end PC, a very large screen).
- **The real Reduced Motion setting**, if the review only faked it.
- **A draft profile**: when the genre profile's status is draft, every number was a guess, so the owner's reaction is the only evidence. Offer to record it as evidence.

How to ask: show the frame strip, state the measured numbers, ask one precise question per doubt. Fix exactly what the owner notes, recapture, and log the ruling in the game's decision log.

## 6. What to report

The identity statement and the per-element lines, the blind reviewer's hide-the-logo answer, the tells ticked, the beat table as built (with each beat's job), planned against measured totals, the grading form, the list of fixes made between rounds, and the "owed to the owner's eyes" list. Never write "verified" for an item that was only read from code.
