# How to add or change a genre profile

A profile holds the numbers that change with the game type. It never restates or loosens a core rule's bound (R2's 350 / 800 ms, R11's 105% and 200 ms, R3's exit ratio). A game that needs to break a bound does it with an owner's override in its own project profile, not here.

## When to add one
- A game's genre fits none of the existing profiles, and
- there is at least one reference clip for it, or the owner asks for a draft.

Until then, use the closest profile and write the differences as overrides in the game's project profile.

## Steps
1. **Collect clips.** Screen recordings only for timing (a clip filmed off a monitor gives layout only). Aim for 3 or more, with at least one the owner rates 4 or 5 and one counter-example. A profile with no clip rated 4 or more has no model: it can list what to avoid, not what to aim for.
2. **Tear each down** with `tools/extract.py` and `templates/teardown.md` (repo root): a timeline in ms measured in frames, the choreography, the look at rest, the weak points. Notes go in `evidence/<area>/`, cited frame sheets in `evidence/<area>/media/`. Videos never enter git.
3. **Get the owner's verdicts** (rating, keep, avoid). Quote the owner's words; never invent a reason.
4. **Copy the table layout of `simulator.md` or `premium.md`** and fill every row below. Every row needs a Source: an evidence id, "core Rn", "worked example" or "guess". A row with no clip behind it is a guess and says so.
5. **Weight by the owner's ratings.** Numbers lean on the clips rated 4 or more; where clips disagree, the higher rated one leads. A clip rated 3 or less is mainly a counter-example: a number taken from one is marked "low-rated clip". Add an "Owner ratings" line under the title listing each clip with its rating.
6. **Set the status** in the front matter: `draft` (no clip evidence, every number a guess), `evidenced (weak: no clip rated above 3)` (clips exist but none is a model), `evidenced (thin)` (fewer than about 5 screen-recorded clips rated 4 or more), `evidenced`.
7. **Add a default beat table** for a frequent panel that satisfies the profile's own numbers and the core rules.
8. **Have the owner adopt it.** A profile is a set of rules; it enters `skills/` as anything but `draft` only once adopted.

## Required rows
Identity: how identity is expressed in this genre (where it lives, the world as carrier, motion as carrier), and a "Generic tells" list for core I2: the genre's default look as tick boxes, each with its evidence id or "guess". Take the tells from the low-rated clips' teardowns.
Entry and exit: beats (frequent, rare), beat order, stagger, beat duration, entry total (frequent, rare), exit total, swap total, in-place change.
Pops and easing: overshoot percent, start scale, settle time, entry easing family, exit easing family, how many elements may overshoot, forbidden easings.
Idle motion: budget (count), cycle length, active part, what the chrome does.
Colour and hero policy: accent hue count, non-hero treatment, hero marking, tags.
Type and legibility: voices, families, minimum size, text on the world.
Sound and feedback: press feedback (delay, amount), sounds, reward moment.
Reduced Motion: entry and exit, pops and idle, value changes.
Forbidden in this profile.

## Changing a number
Change a number only with new evidence or an owner's ruling. Write the source next to it. If a guess is confirmed by the owner in a real game, change its source to "owner <date>" and record the ruling in `evidence/`.
