# Layout craft: turning a mockup into a finished screen

Working method. The owner-adopted rules are in `core-rules.md`, including the layout rules L1 to L7; where this file names one, it cites it. Numbers here are starting points: the game's UI kit and the owner's rulings win.

## 1. Read the sketch as intent, not as pixels

- List every box: its name, its job for the player, what it shows when empty or locked.
- Find the hero: the one thing the screen exists for (the item to buy, the reward to claim, the choice to make). If the sketch has two equal heroes, ask which one.
- Keep the arrangement. The owner drew where things go; elevate the treatment (material, hierarchy, spacing, depth). Moving a box is a change to report, not a silent improvement.
- Note what the sketch does not show and the screen still needs: a close control, a title, empty and loading states, a disabled reason ("Need 20 more coins"), the currency the player spends.

## 2. Structure

- **One spacing scale.** Pick a base (the game's kit if it has one; else 4 px) and use only its multiples (4, 8, 12, 16, 24, 32, 48). Equal gaps between siblings; larger gaps between groups than inside them.
- **One alignment grid.** Left edges line up; columns share widths; a centred block is centred on its visual mass, not its box.
- **Margins.** The same inner padding on all four sides of a panel unless the design calls for an asymmetry on purpose (a title board, a tab strip). Keep a clear margin to the screen edges.
- **Density follows the job.** A shop grid can be dense; a reward moment needs air around the hero.
- **Surfaces (L1):** two treatments at most for the whole game. **Hero in the centre (L3)**, text in side columns. **Anchors and the primary button fixed (L4, L5).**
- **Depth in layers, back to front:** backdrop or dim; panel (frame and surface); content; the hero (raised: larger, a glow or a stage, R8); overlays (tooltips, toasts). Each layer has one treatment, used everywhere.

## 3. Hierarchy (R8, R9)

- One hero per screen. Everything else steps down in size, saturation and contrast.
- Three type voices at most: a small label, a large value, a muted line. Build hierarchy with size and weight before reaching for a box or a colour.
- Buttons: one primary action per screen, visibly the strongest button; secondary actions quieter; destructive actions distinct and never next to the primary without space.

## 4. Identity (I1 to I4)

- Give every surface the game's material (its wood, metal, paper, glass, stone): frame, header, buttons, tabs, pills, tooltips. A default rounded grey or blue box is a generic tell (I2).
- Draw icons in one hand and one weight. Mixed icon styles are a tell.
- Use the game's theme vocabulary for every ornament and effect (R10). If an ornament has no source in the game's world, remove it.
- With a benchmark (I4): borrow its anchors, restraint, type scale, timing and hierarchy; never its art, layout or icons.

## 5. Every state, every size

- States per control: rest, hover, pressed, selected, disabled (with the reason), locked, empty, loading, error. A screen is not finished while a state is undrawn.
- Real content: the longest item name, the biggest number, a long player name, an empty list. No placeholder text (R12).
- Two window sizes: the design size and a smaller one (and a forced UI scale if the game has one). Nothing overlaps, nothing is cut, text stays readable (R13).

## 6. Motion last

Design the screen at rest first; then add only the motion that has a job (I3): how the panel arrives and leaves (R1 to R3), how a change is answered (R5), what stays still (R6), and whether the hero earns an idle loop (R7). Plain is better than busy.

## 7. Before showing it

Look at the resting capture at real size and ask: can a player tell which game this is (I2)? Where does the eye land first, and is that the hero (R8)? Is anything there only to look busy (I3)? Cut what fails.
