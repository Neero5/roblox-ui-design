# Core rules

Universal rules for Roblox UI motion. They hold in every genre. Numbers that change with the game live in `profiles/<genre>.md`; where a rule says "profile", read the number there.

Status: R1 to R13 and the anti-slop list were adopted by the owner on 2026-11-10 (`evidence/ui/pilot-rules-verdicts-2026-11-10.md`). The wording here is generalised from that ruling: game-specific examples were replaced by "the game's profile". Section E (engineering requirements) and the numeric refinements of R3 (40 to 65% of the entry), R5 (160 to 240 ms) and the R4 tab cross-dissolve exception were adopted by the owner on 2026-11-10: "Adopt E1 to E5, refinements stand too". Section I (identity rules I1 to I4) was adopted by the owner on 2026-11-10: "Adopt all, they sounds reasonable".

Evidence ids are the teardown notes in `evidence/ui/`, with the owner's rating out of 5 (third ruling, 2026-11-10): 01 simulator shop, filmed (2.5); 02 dark commands panel (4); 03 sword RPG menu (4); 04 Aftertwelve menus (4.5); 05 sky shop (3); 06 mines panel, filmed (2.5); 07 anime action RPG character hub (5). Seven clips is thin evidence. 01 and 06 were filmed off a monitor: layout only, timing within about one frame at best, no colour.

**How the owner scores (read this before anything else).** Identity comes first: a UI that belongs to one nameable world, every element matching it (02, 03, 04, 07). Consistency is necessary but not enough: 01 is consistent and gets 2.5 for being generic. Showing off loses points (05). Animation quality is the second axis (02: "what stands out the most from it are the animations"; 04: "dynamic animations and fluidity"). So the R rules below make motion good, and the I rules decide whether the UI is worth animating at all. A build that passes every R rule and fails I2 is a fail.

**Weight of the evidence.** Clips rated 4 or more (07, 04, 02, 03) are models: numbers lean on them. Clips rated 3 or less (05, 01, 06) are mainly counter-examples; a number taken from one of them says so.

Terms:
- **Entry total**: from the trigger (the click or key) to the last element at rest.
- **Beat**: one element or group starting to move. **Stagger**: the gap between the starts of two beats.
- **Frequent panel**: one a player opens many times a session (inventory, shop, settings). **Rare moment**: at most a few times a session (a win, a rare drop, the first open of the day, a place change).
- **Chrome**: frames, headers, tabs, close buttons, labels. **Hero**: the one featured element of the screen.

## Identity (adopted by the owner 2026-11-10; checked first)

### I1. One identity, and every element belongs to it
**Rule.** The game's profile states the UI's identity in a few words a player could say (a world, not a list of adjectives: "red ninja clan", "dark fantasy in the manner of a AAA action RPG", "starlit anime character hub"). Every panel, tab, icon, colour, type face, shape, sound and motion is checked against that statement. Before building, write one line per element: how it expresses the identity (which material, shape, motif or way of moving). The identity is expressed through R10's theme vocabulary; I1 asks for the whole, R10 for each effect.
**Forbidden.** Building without an identity statement. An identity made only of adjectives any game could claim ("clean", "modern", "polished"). A panel, tab or icon set that belongs to a different world than the rest (a flat settings page in a carved-stone game). An element whose "how it expresses the identity" line is blank.
**Why.** It is what every clip rated 4 or more has, and what the owner names first in each of those ratings.
**Check.** (a) The profile has an identity statement of 2 to 8 words (owner 2026-11-10) that names a world. (b) The beat table or build notes carry the per-element line; no blanks. (c) Put resting screenshots of every panel of the game side by side: each must show the same surfaces, type faces, accent and corner or border treatment. A panel that could be swapped into another game without anyone noticing fails here and in I2.
**Evidence.** 02 (4), 03 (4), 04 (4.5), 07 (5).
**Owner.** 02: "the whole thing is unique and all its tabs and elements match its red, ninja identity". 03: "gives off somewhat of a AAA feel with its looks and matching identities". 04: "its RPG identity pops up immedately".

### I2. Generic fails
**Rule.** Consistent but interchangeable is a fail. The UI must be recognisable as this game's with the logo and the game's name hidden.
**Forbidden.** The genre's default look taken as the design. Meeting I1 with a statement that only names the genre ("a simulator", "an RPG").
**Why.** 01 is tidy and consistent and still scores 2.5; 06 has some touches of its own and still scores 2.5.
**Check.** Three steps on the resting screenshots, all repeatable:
1. **Hide-the-logo test.** Mask the logo, the game's name and any named currency or character. Give the masked screenshots to a reviewer who has NOT read the game's profile and ask: "In a few words, what world is this, and what in the picture tells you?" Pass if the answer matches the identity statement in substance and points at 2 or more concrete elements. An answer that only names the genre ("some simulator shop") is a fail.
2. **Tick the genre's default tells.** Each profile lists them under "Generic tells". Count the tells present. 3 or more is a fail; each tell that stays must have a written reason from the identity (threshold owner 2026-11-10). Tells seen in any genre: the engine's default fonts and plain rounded dark-grey frames; emoji or a stock icon pack used as the icons; icons of mixed styles; one saturated colour per card with no system behind it (these four are guesses, not from a clip).
3. **Name the identity carriers.** List the elements only this game would have (a shape, a material, a motif, a way of moving). Fewer than 3 on the main panels is a fail (owner 2026-11-10).
Example of step 2 for simulators (from 01, 05, 06): the default blue header bar, a red X close button, saturated gradient cards each in a different colour, "BEST DEAL" and "LIMITED" tags, an icon rail of round buttons. Full list in `profiles/simulator.md`.
**Evidence.** 01 (2.5), 06 (2.5), 05 (3, "similar reasons as 01").
**Owner.** 01: "It's not bad because it's consistent and matches today's incremental game style. However, it's too generic, it matches 90% of typical simulation games." 06: "the UIs are somewhat unique but its essence stills fall under the generic category".

### I3. Serve, don't show off
**Rule.** Every motion and effect has a job for the player: it shows where something came from, what changed, what to look at, or that an input was received. Write that job in the beat table row. If the job cannot be written in a few words, cut the motion. Being unique (I1, I2) comes from the identity, never from the amount of motion.
**Forbidden.** Motion or effects whose only job is to display the UI kit. Several effect types performing on one resting screen. Fixing a generic UI by adding more effects.
**Why.** When every element performs, the screen reads as trying too hard, and the owner takes points off for it even though it catches the eye.
**Check.** (a) Every beat table row has its job written; blanks fail. (b) Removal test: for each idle or decorative effect, capture the screen with it switched off. If the player loses no information and the identity still reads, the effect stays only if it is the single hero motion R7 allows. (c) Count the distinct effect types visible on the resting screen (particles, sweeps, loops, flying objects, text effects): more than the profile's idle budget is a fail.
**Evidence.** 05 (3, the counter-example); 07 and 04 (the opposite: the chrome is calm and the world or the character carries the life).
**Owner.** 05: "it gets point deductions due to is maximalistic looks, as if trying too hard to be unique and a "showoff" of its UI elements, with jets going everywhere and everything with movements, almost sloppy."
**Note.** R7 and R8 count the moving things; I3 asks why each one moves. The teardown of 05 found one idle loop over still chrome and praised it; the owner's verdict on the whole clip is the one that counts.

### I4. A proven benchmark (optional)
**Rule.** A game's profile may name ONE successful game as its benchmark. Match the benchmark's execution principles: what stays still (anchors), how much is left out (restraint), how type sets the hierarchy, how long things take, what answers a selection. Write the borrowed principles as a list in the profile, in words. Everything a player sees is made new, from the game's own identity.
**Hard line: never copy** the benchmark's art, logos, wordmarks, icon sets, fonts that are its property, characters, names, sounds, exact layouts (the same elements in the same places), or its trade dress (the overall combination of colours, shapes and ornaments that makes a screen look like that game's). A screenshot of the build must never be mistaken for a screenshot of the benchmark.
**Forbidden.** More than one benchmark (two benchmarks give two identities; fails I1). A benchmark used in place of an identity statement. Tracing or rebuilding a benchmark screen element for element. Using extracted or re-drawn benchmark assets.
**Why.** A successful game has already proved that its way of executing works; the owner's top rating went to a clip that executes such a way well.
**Check.** (a) The profile names zero or one benchmark and lists the borrowed principles as principles (no asset, no screen). (b) Place the build's screenshot beside one of the benchmark's same kind of screen: the frame shapes, the icon drawings, the ornaments, the palette as a whole and the positions of the elements must differ; if a player could take one for the other, it fails. (c) The I2 hide-the-logo answer must name this game's world, not the benchmark's title.
**Evidence.** 07 (5; in the manner of Genshin Impact), 03 (4; "Elden Ring" feel). Both show the manner of a benchmark with their own content.
**Owner.** 07: "it's beautifully done, specially because it mimics the successful game Genshin impact, which already proved its successful execution." 03: "It gives off "Elden Ring" vibes".
**Note.** The owner's word is "mimics". The adopted I4 text limits that to execution principles; where a build and this hard line seem to disagree, the hard line wins and the question goes to the owner.

## Layout (adopted by the owner 2026-11-10)

From still references (`evidence/layout/`), owner: "Adopt L1 to L7"; L8 to L10 and the L4 extension: "Adopt them all" (from L02 to L04, the layouts of clips 03, 04 and 07). Evidence L01 (Genshin UI template sheet, rated 4.5: "purely because it cannot fit on most *roblox* game type, but doesn't stop being great and unique") and clips 07, 04, 03. These are principles: they hold in any genre and any identity. The AAA look they came from is NOT a default style (owner: it does not fit most Roblox game types), and no benchmark is set by them.

- **L1 Two surfaces at most.** The whole UI uses at most two surface treatments (for example a menu surface and a card surface), both from the game's identity. Check: list every distinct panel or card fill, frame and material across the game's screens; more than two is a fail unless the profile gives a reason.
- **L2 Rarity colour is a system.** Rarity or tier colours form one fixed set and appear only where they carry information (a badge, a band, stars, the best result). The rest of the UI stays neutral. Check: every rarity-coloured pixel answers "which tier is this?"; a rarity colour used as decoration is a fail.
- **L3 The hero owns the centre.** The hero (character, item, reward, sculpture) takes the middle; text sits in side columns or under it; the space between stays empty. Check: on the resting capture, nothing but the hero overlaps the centre third.
- **L4 Fixed parts stay put.** Top bar, tab list, the primary button and the back or close control keep the same position on every tab of a screen, and the back or close control keeps one spot across the whole game; a tab changes only its content (and at most the backdrop's hue). Each page may earn ONE striking device of its own (an arc of slots, an orbit, giant numerals) inside the fixed frame. Check: overlay two tabs' captures; the anchors must match to the pixel. (Extended 2026-11-10 from L03, L04.)
- **L5 One primary action, one place.** Each screen has one primary action, visibly the strongest button, in the same position on every screen of the game (the profile names the position). Secondary actions are quieter.
- **L6 One ornament family.** A few motifs and one line weight, quiet everywhere, from the game's theme vocabulary. Check: list the ornaments; any outside the family is cut.
- **L7 Emptiness follows importance.** The more important the screen or moment, the more calm empty space around its content; dense grids belong to browsing screens only.
- **L8 A signature motif from the premise.** The game has one motif drawn from its name or premise (a clock for "Aftertwelve", blade-shaped diamonds for a sword game), reused in several places: ornaments, numbering and at least one major screen built around it. A pattern pasted on top does not count. The game's profile names the motif. Check: name the motif and list three places it appears. (L03, L02, L04)
- **L9 Browse = selection beside a big detail.** Browsing screens (shops, inventories, slot pickers) put the list or grid on one side and a large detail of the selected item on the other; selecting changes the detail, nothing pops up per item. (L02 Store, L03 slots and Satchel, L04 inventory, L01)
- **L10 Quiet but unmistakable selected state.** The chosen item is marked by a filled marker, a lit edge, a thin accent frame or an underline, never by a large block of colour. Check: on a capture, the selected item is found in under a second and is not the loudest thing on screen. (L02, L03, L04)

## Choreography

### R1. A panel arrives in beats
**Rule.** Order every entry: container (frame, backdrop), then header, then content, then the hero item last. Content with columns or rows arrives in reading order (left to right, top to bottom). The number of beats and the stagger come from the profile. A profile may allow a single beat for small or very frequent panels; then the whole panel moves as one and R11 applies.
**Forbidden.** All elements starting on the same frame when the profile asks for 2 or more beats. Random or centre-out order. More than 6 beats in any entry.
**Why.** The panel reads itself to the player in the order they would read it (02). Order is the main thing the good clips have and default builds lack (pilot finding).
**Check.** In the frame sequence, list the first frame on which each element is visible. The order must match the beat table, and each stagger must be inside the profile's range.
**Evidence.** 02 (title, then columns left to right, 60 to 70 ms apart), 03 (frame before content), 05 (six clear beats, order good, total too long), 06 (one beat for the whole panel: fine for that genre), 07 (grid cells light up row by row, about 100 ms a row: the same rule at cell level).
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
**Never instant (owner 2026-11-14).** No element disappears or appears instantly with no tell: every exit and entry has some transition (a fade, a shrink, a dissolve, a wipe, anything that reads); the owner: "it looks ugly for any element to disappear away instantly with no tell". Under Reduced Motion a short fade still counts. Exempt: a hit flash or impact frame in VFX (1 to 4 frames), which is itself the tell (owner 2026-11-14).

### R4. Swapping panels: one leaves, then the other arrives
**Rule.** The old panel finishes its exit before the new panel's first beat. Order: old content out, old frame out, an optional empty beat of 30 ms or less, new frame in, new content in. The profile sets the swap budget.
**Exception.** A cross-dissolve of content inside the SAME frame (a tab switch where the frame stays) is an R5 change, not a swap, and may overlap old and new content in the same place for 160 ms or less.
**Forbidden.** Two different panels or two full pages both readable on one frame.
**Why.** Two clean events read better than a smear.
**Check.** Step through the swap frames: no frame shows readable text from both pages at different positions.
**Evidence.** 03 (the good case, with a single empty frame between pages), 04 at 10.0 s (the slip: two pages overlap for one frame), 07 (the opposite slip: a fade through near black leaves about 100 ms of nothing between two pages; keep the empty beat at 30 ms or less).

### R5. A value that changes in place cross-fades in place
**Rule.** A carousel value, tab name, counter, day or featured name changes where it stands: old value dims or fades over about 100 ms (ease In), new value arrives over about 100 ms (ease Out), about 200 ms in total (range 160 to 240 ms). Everything that depends on the choice (name, sub-line, description, pager dot) changes in the same beat.
**Forbidden.** Sliding or re-popping the whole panel for a value change. Dependent texts updating on different frames.
**Why.** The panel is the anchor; only the information changed.
**Check.** In the frames the panel frame's position and size are identical before, during and after. All dependent elements change on the same frame.
**Evidence.** 04 (values cross-fade in about 200 ms, no slide anywhere), 07 (the detail pane dims in about 70 ms and the new detail fades in over about 100 ms, about 170 ms in total, on every selection).
**Note.** A stage that slides one hero item in the direction of an arrow is allowed if the profile lists it; the surrounding text still follows R5.

### R6. Keep one still anchor
**Rule.** In every transition at least one large thing does not move, scale or fade: the panel frame, the menu column, the avatar or the world behind. Name the anchor in the beat table.
**Forbidden.** Camera moves, background blur ramps and panel motion all at once with nothing at rest. Moving the avatar or 3D preview during a page change that does not concern it.
**Why.** The eye needs a place to rest; a still anchor makes the screen feel loaded, not loading.
**Check.** Pick the anchor's pixels in the first and last frame and two frames between: identical position and size.
**Evidence.** 03 (menu column and the sword never move), 04 (the character never moves between pages), 02 (the frame stays while rows filter), 07 (two anchors, the icon rail and the 3D character, hold through every page change; the hub never seems to reload).

## Emphasis

### R7. Idle motion lives only in the hero
**Rule.** At rest, only the hero may move, on a cycle of 3 s or longer, with the active part of the cycle short (profile value). The chrome is still. Idle motion pauses while the panel is hidden and is off under Reduced Motion. The profile sets the budget and may set it to zero.
**Forbidden.** Breathing buttons, shimmering every card, bobbing icons across a grid, looping glows on chrome.
**Why.** One moving thing draws the eye; many moving things are noise.
**Check.** Capture two frames of the resting screen 500 ms apart, several times across 6 s. Only pixels inside the hero may differ. Count idle animations: at most the profile's budget.
**Evidence.** 05 (rated 3: the jet crosses the featured card about every 3 s, about 700 ms long, while the chrome stays still; the cycle and length are measured there, but the clip as a whole was marked down for too much movement, see I3), 07 and 04 (rated 5 and 4.5: no idle motion in the UI at all; life comes from the world and the character).
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
**Why.** The two highest rated clips (07, 04) get their look from size, spacing and one letter or numeral used large, not from boxes.
**Check.** List every distinct text style on the screen (family, size, weight, colour). More than three styles for content text is a fail (button labels and numeric badges may share one extra style).
**Evidence.** 04 (tracked label, large value, muted line, one accent), 07 (tiny caps labels, large serif numerals, a rank letter as a big faint glyph), 02 (serif title, tracked caps subtitle, light rows).

### R13. Every text stays readable
**Rule.** Every text is readable on the worst background it can meet (bright sky, snow, a busy world). Text over the world sits on a scrim, a panel or carries a stroke or shadow. Contrast first, elegance second. Use the profile's minimum text size and contrast target.
**Forbidden.** Thin pale text straight on a bright scene. Body text below the profile's minimum size. Text that is mid-fade (partly transparent) at rest.
**Why.** Three of the four best clips are weak only here.
**Check.** Screenshot the text over the brightest and the busiest background the game has. Read every string at the real window size, then at a small window.
**Evidence.** 02 (tiny low-contrast text), 04 (thin pale text lost on snow), 07 (small grey italic descriptions and very small pill buttons).

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

Added with the identity rules (owner 2026-11-10):

9. With the logo hidden, the screen could belong to most games of its genre. (I2)
10. Three or more of the genre's default tells, with no reason from the identity. (I2)
11. A panel, tab or icon set from a different world than the rest. (I1)
12. Motion or effects with no job for the player; several effect types performing on one resting screen. (I3)
13. A screen that could be mistaken for the benchmark game's. (I4)

## E. Engineering requirements (adopted by the owner 2026-11-10)

These are not taste rules. They keep the adopted rules true in a real game.

- **E1. Reduced Motion.** When `GuiService.ReducedMotionEnabled` is true: no scale, slide, overshoot, stagger, idle loop or particle. State changes still happen and are still visible, instantly or with an opacity fade of 150 ms or less (the profile says which). Check: capture the same transitions with the setting on. Basis: R7's "off under Reduced Motion"; the owner plays with Reduced Motion on.
- **E2. Interruptible.** Opening during a running exit, or closing during a running entry, cancels the running sequence and starts the new one from the current state. No panel may end half transparent, at the wrong scale or invisible while logically open. Check: trigger open, close, open inside 150 ms and capture the rest state.
- **E3. Input is never held hostage.** Buttons work from the first frame they are visible; a click during the entry is honoured. Press feedback starts on the same frame as the input (within about 50 ms). Check: click the primary button during the entry.
- **E4. One motion table.** Every duration and easing is a named token in one module. Panel code uses token names. Check: search the UI code for `TweenInfo.new(` outside the motion module.
- **E5. Start states are set before the first frame.** An element whose beat starts later must already be in its hidden start state when the container appears. Check: the first captured frame shows no element at rest that has not had its beat.
