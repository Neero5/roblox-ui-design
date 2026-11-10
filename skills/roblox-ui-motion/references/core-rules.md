# Core rules

Universal rules for Roblox UI motion. They hold in every genre. Numbers that change with the game live in `profiles/<genre>.md`; where a rule says "profile", read the number there.

Status: R1 to R13 and the anti-slop list were adopted by the owner on 2026-11-10 (`evidence/ui/pilot-rules-verdicts-2026-11-10.md`). The wording here is generalised from that ruling: game-specific examples were replaced by "the game's profile". Section E at the end is engineering practice proposed by the skill, not yet ruled on.

Evidence ids are the teardown notes in `evidence/ui/`: 01 simulator shop (filmed), 02 dark commands panel, 03 sword RPG menu, 04 Aftertwelve menus (rated 5 by the owner), 05 sky shop, 06 mines panel (filmed). Six clips is thin evidence. 01 and 06 were filmed off a monitor: layout only, timing within about one frame at best, no colour.

Terms:
- **Entry total**: from the trigger (the click or key) to the last element at rest.
- **Beat**: one element or group starting to move. **Stagger**: the gap between the starts of two beats.
- **Frequent panel**: one a player opens many times a session (inventory, shop, settings). **Rare moment**: at most a few times a session (a win, a rare drop, the first open of the day, a place change).
- **Chrome**: frames, headers, tabs, close buttons, labels. **Hero**: the one featured element of the screen.

## Choreography

### R1. A panel arrives in beats
**Rule.** Order every entry: container (frame, backdrop), then header, then content, then the hero item last. Content with columns or rows arrives in reading order (left to right, top to bottom). The number of beats and the stagger come from the profile. A profile may allow a single beat for small or very frequent panels; then the whole panel moves as one and R11 applies.
**Forbidden.** All elements starting on the same frame when the profile asks for 2 or more beats. Random or centre-out order. More than 6 beats in any entry.
**Why.** The panel reads itself to the player in the order they would read it (02). Order is the main thing the good clips have and default builds lack (pilot finding).
**Check.** In the frame sequence, list the first frame on which each element is visible. The order must match the beat table, and each stagger must be inside the profile's range.
**Evidence.** 02 (title, then columns left to right, 60 to 70 ms apart), 03 (frame before content), 05 (six clear beats, order good, total too long), 06 (one beat for the whole panel: fine for that genre).
**Owner.** "Adopt, but depends on game type." So the order is universal; the beat count and stagger are profile values.

### R2. Entry length follows how often it is seen
**Rule.** Frequent panel: entry total 350 ms or less. Rare moment: entry total 800 ms or less. No longer "first open" entry for a frequent panel (owner: "No need"). The profile may set tighter numbers, never looser.
**Forbidden.** An entry longer than the action it leads to (anti-slop). A 1.5 s entry on a shop (05).
**Why.** A player who opens a panel fifty times pays the entry fifty times.
**Check.** Measure the entry total from the frames or the trace. Classify the panel as frequent or rare in the beat table before measuring.
**Evidence.** 02 (about 300 ms, feels right), 03 (entry about 230 ms), 05 (about 1500 ms, three to four times too long for a shop).

### R3. Exit is about half the entry, in reverse
**Rule.** Exit total is 40% to 65% of the entry total. Content leaves first, its container last. The exit may merge beats (two beats is enough) but keeps the order. Exits ease In; entries ease Out.
**Forbidden.** An exit slower than the entry. A container that vanishes while its content is still visible. An exit with overshoot.
**Why.** The player has already decided to leave; the UI must get out of the way.
**Check.** Exit total divided by entry total. In the frames, the last visible thing must be the container.
**Evidence.** 02 (entry about 300 ms, exit 130 to 200 ms, right column leaves first), 03 (content fades before the frame shrinks away).

### R4. Swapping panels: one leaves, then the other arrives
**Rule.** The old panel finishes its exit before the new panel's first beat. Order: old content out, old frame out, an optional empty beat of 30 ms or less, new frame in, new content in. The profile sets the swap budget.
**Exception.** A cross-dissolve of content inside the SAME frame (a tab switch where the frame stays) is an R5 change, not a swap, and may overlap old and new content in the same place for 160 ms or less.
**Forbidden.** Two different panels or two full pages both readable on one frame.
**Why.** Two clean events read better than a smear.
**Check.** Step through the swap frames: no frame shows readable text from both pages at different positions.
**Evidence.** 03 (the good case, with a single empty frame between pages), 04 at 10.0 s (the slip: two pages overlap for one frame).

### R5. A value that changes in place cross-fades in place
**Rule.** A carousel value, tab name, counter, day or featured name changes where it stands: old value dims or fades over about 100 ms (ease In), new value arrives over about 100 ms (ease Out), about 200 ms in total (range 160 to 240 ms). Everything that depends on the choice (name, sub-line, description, pager dot) changes in the same beat.
**Forbidden.** Sliding or re-popping the whole panel for a value change. Dependent texts updating on different frames.
**Why.** The panel is the anchor; only the information changed.
**Check.** In the frames the panel frame's position and size are identical before, during and after. All dependent elements change on the same frame.
**Evidence.** 04 (values cross-fade in about 200 ms, no slide anywhere).
**Note.** A stage that slides one hero item in the direction of an arrow is allowed if the profile lists it; the surrounding text still follows R5.

### R6. Keep one still anchor
**Rule.** In every transition at least one large thing does not move, scale or fade: the panel frame, the menu column, the avatar or the world behind. Name the anchor in the beat table.
**Forbidden.** Camera moves, background blur ramps and panel motion all at once with nothing at rest. Moving the avatar or 3D preview during a page change that does not concern it.
**Why.** The eye needs a place to rest; a still anchor makes the screen feel loaded, not loading.
**Check.** Pick the anchor's pixels in the first and last frame and two frames between: identical position and size.
**Evidence.** 03 (menu column and the sword never move), 04 (the character never moves between pages), 02 (the frame stays while rows filter).

## Emphasis

### R7. Idle motion lives only in the hero
**Rule.** At rest, only the hero may move, on a cycle of 3 s or longer, with the active part of the cycle short (profile value). The chrome is still. Idle motion pauses while the panel is hidden and is off under Reduced Motion. The profile sets the budget and may set it to zero.
**Forbidden.** Breathing buttons, shimmering every card, bobbing icons across a grid, looping glows on chrome.
**Why.** One moving thing draws the eye; many moving things are noise.
**Check.** Capture two frames of the resting screen 500 ms apart, several times across 6 s. Only pixels inside the hero may differ. Count idle animations: at most the profile's budget.
**Evidence.** 05 (the jet crosses the featured card about every 3 s, about 700 ms long, while the chrome stays still).
**Owner.** "Depends on the game, but generally yes." So a game's profile may raise the budget with a reason.

### R8. One hero per screen
**Rule.** Exactly one element per screen gets the full treatment: full saturation, glow, or idle motion. All other elements step down by the profile's hero policy (lower saturation, no glow, no idle).
**Forbidden.** Every card at full saturation. Several "BEST DEAL" style tags of equal weight. More accent hues at full strength than the profile allows.
**Why.** If everything shouts, nothing is heard.
**Check.** Squint test on a resting screenshot: name the one element the eye lands on first; it must be the hero named in the beat table. Count elements with glow, with idle motion, with full saturation: each count is 1 or 0.
**Evidence.** 05 and 01 (counter-examples: all cards saturated, eight colours at equal weight), 06 (a hero card on top, but the grid under it has equal weight), 04 (one accent, clear focus).

### R9. Type does the hierarchy
**Rule.** Build hierarchy with type before colour or boxes. Three voices at most per panel: a small label (often tracked caps), a large value, a muted line. One font family, two at most.
**Forbidden.** A fourth text style added to make something stand out. A coloured box around text whose only job is hierarchy.
**Why.** The highest rated clip gets its premium look from size and spacing alone.
**Check.** List every distinct text style on the screen (family, size, weight, colour). More than three styles for content text is a fail (button labels and numeric badges may share one extra style).
**Evidence.** 04 (tracked label, large value, muted line, one accent), 02 (serif title, tracked caps subtitle, light rows).

### R13. Every text stays readable
**Rule.** Every text is readable on the worst background it can meet (bright sky, snow, a busy world). Text over the world sits on a scrim, a panel or carries a stroke or shadow. Contrast first, elegance second. Use the profile's minimum text size and contrast target.
**Forbidden.** Thin pale text straight on a bright scene. Body text below the profile's minimum size. Text that is mid-fade (partly transparent) at rest.
**Why.** Two of the best clips lose points only here.
**Check.** Screenshot the text over the brightest and the busiest background the game has. Read every string at the real window size, then at a small window.
**Evidence.** 02 (tiny low-contrast text), 04 (thin pale text lost on snow).

## Feel

### R10. Effects come from the game's own world
**Rule.** Every ornament, particle and transition style is drawn from the theme vocabulary in the game's profile (its materials, objects, motifs). If the profile lists no vocabulary, ask the owner before inventing effects.
**Forbidden.** Anything on the profile's refused list. Effects borrowed from another genre: glitch smears, scramble-decoding text, scan lines, neon in a game whose theme is none of those.
**Why.** An effect from the wrong world is the fastest way to look like a template.
**Check.** For each effect in the beat table, write which vocabulary word it comes from. A blank is a fail.
**Evidence.** 05 (cloud puffs in a sky shop: on theme; scramble text in the same shop: off theme), 02 (a glitch smear exit: on theme only for a sci-fi game).

### R11. Pops are small and settle fast
**Rule.** A pop peaks at 105% of rest size or less and is at rest within 200 ms of its start. The profile sets the exact overshoot (it may be 0). At most one overshoot per element per entry.
**Forbidden.** Bounce or Elastic easing on panels and cards. Every element bouncing (anti-slop). A slide with Back easing over a long distance (the overshoot is about 10% of the distance travelled: see `roblox-recipes.md`).
**Why.** A small overshoot reads as alive; a large one reads as a toy and delays reading.
**Check.** Measure the element's largest size in the frames against its rest size. Count frames from pop start to rest.
**Evidence.** 06 (about 92% to 102% to 100% within about 200 ms; filmed, so within one frame).

### R12. Never ship placeholder or debug text
**Rule.** Every visible string is final copy. Before every review, list every visible string of the screen.
**Forbidden.** "Insert description here", lorem ipsum, "TODO", "Label", "TextLabel", raw asset ids, internal keys such as `item_sword_01`, untruncated numbers such as `1234567.8901`.
**Why.** The loudest slop tell in the evidence set.
**Check.** Dump the `Text` of every visible TextLabel, TextButton and TextBox under the screen (a short script) and read the list.
**Evidence.** 05 ("Insert description here..." on shipped cards).

## Anti-slop checklist (the reviewer's quick pass)

Each line is a fail if seen in the frames.

1. Everything appears at once, or everything fades at the same speed. (R1)
2. Every element bounces. (R11)
3. Every card is saturated, glows or moves at idle. (R7, R8)
4. Linear motion on anything that is not a loop. (easing: entries Out, exits In)
5. An entry longer than the action it leads to. (R2)
6. Placeholder text, lorem ipsum, raw ids. (R12)
7. An effect borrowed from another genre (glitch, decoding text, neon in a game with no neon). (R10)
8. Text that loses against the background. (R13)

## E. Engineering requirements (proposed by the skill, NOT yet ruled on by the owner)

These are not taste rules. They keep the adopted rules true in a real game. Treat them as required until the owner rules otherwise.

- **E1. Reduced Motion.** When `GuiService.ReducedMotionEnabled` is true: no scale, slide, overshoot, stagger, idle loop or particle. State changes still happen and are still visible, instantly or with an opacity fade of 150 ms or less (the profile says which). Check: capture the same transitions with the setting on. Basis: R7's "off under Reduced Motion"; the owner plays with Reduced Motion on.
- **E2. Interruptible.** Opening during a running exit, or closing during a running entry, cancels the running sequence and starts the new one from the current state. No panel may end half transparent, at the wrong scale or invisible while logically open. Check: trigger open, close, open inside 150 ms and capture the rest state.
- **E3. Input is never held hostage.** Buttons work from the first frame they are visible; a click during the entry is honoured. Press feedback starts on the same frame as the input (within about 50 ms). Check: click the primary button during the entry.
- **E4. One motion table.** Every duration and easing is a named token in one module. Panel code uses token names. Check: search the UI code for `TweenInfo.new(` outside the motion module.
- **E5. Start states are set before the first frame.** An element whose beat starts later must already be in its hidden start state when the container appears. Check: the first captured frame shows no element at rest that has not had its beat.
