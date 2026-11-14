---
type: reference
category: vfx
captured: 2026-11-11
status: first pass; owner ratings 2026-11-12 (verdicts.md)
---
# VFX V01 to V10: first-pass teardowns

One pass per clip, zoomed only on the main effect (frames in `media/`). Timings are measured at the clip's fps from the zoom sheets. Ratings and verdicts are the owner's to give; nothing here is a rule yet.

## V01 Gold summoning circle (@espada.four3), built in Roblox Studio
- **Owner's rating: 4.5.** "It's very decent, specially for cutscenes and rare/late game attacks for RPGs or Roguelikes. I also put it because it seems like they somehow managed to get claude to use the roblox plugin called VFX studio"
- **Moment:** a summoning or ascension: a ritual circle charges and fires a pillar of light.
- **Layers:** floor rune circle (decal rings at several radii); thin rising rings and vertical gold beams; a cloud vortex disc overhead; final: a white-gold pillar with a bright core, a multi-ring floor circle, orbiting shards and sparks. ![[V01-overview.jpg]] ![[V01-finale.jpg]]
- **Colour:** ONE hue (gold) plus a white core, on black.
- **Works:** one hue with value contrast; rings at different radii and speeds give depth; the floor circle anchors it.
- **Weak:** a very long build (tens of seconds, a showcase); tested only on a black void, so readability on a real map is unknown.

## V02 Caged egg hatch (@jarvislabsreal)
- **Owner's rating: 3.5.** "I suppose it's nice as opening animations, like the cutscene and vfxs, but it's a bit maximalistic, which isn't exactly my taste."
- **Moment:** unlock and hatch, then the reveal of a rare pet. ![[V02-overview.jpg]] ![[V02-unlock.jpg]] ![[V02-hatch.jpg]]
- **Timeline:** cyan lock arrows pulse (0 to 3.0 s, the "interaction"); **3.1 s unlock flash** (white core, a ring, radial sparks, about 300 ms); 3.4 to 3.6 s the cage bars fan open; 4.4 to 4.9 s a **charge** (rays, the egg's cracks brighten); **5.1 s one white flash frame**; 5.2 to 5.4 s a spark shell and a floor shockwave ring; 5.5 to 6.3 s sparks rise and fade (about 800 ms); 7.1 s cut to the reveal; 11 to 12 s the pet's own purple burst.
- **Shape:** two escalating stages (unlock, then hatch), each anticipation, flash, shockwave, debris, linger.
- **Colour:** warm gold for the build; the reveal switches to the pet's rarity hue (purple). Cyan only on the lock (interaction).
- **Works:** escalation in two steps; the flash is one frame; the linger is long and soft; the palette switch tells "this is rare".
- **Weak:** the cyan lock arrows look like UI pasted in the scene; the cut back to a closed cage (7.0 s) is a loop seam.

## V03 Anime ultimate (itsjustfx3)
- **Owner's rating: 4.5.** "Same as V01. But it also does well by adding those impact frames and the flame looks well done"
- **Moment:** a cinematic ultimate move. ![[V03-overview.jpg]] ![[V03-impact-frames-1.jpg]] ![[V03-impact-frames-2.jpg]]
- **Timeline:** 2.4 to 2.7 s small charge; **2.8 s a black dome** closes over the area (the world darkens); 2.9 s impact flash and a lava splash; 3.0 to 3.8 s stylised fire everywhere; **3.9 to 4.1 s full-screen impact frames** (speed-line slashes, white-yellow on black); 4.2 s one full red frame; 4.3 to 4.8 s full-screen orange; 4.9 to 6.1 s a giant stylised slash swirl (orange, magenta); **6.2 to 6.4 s inverted frames** (white stars on black, then black stars on white, about 3 frames); 6.5 to 7.1 s aftermath: a red pillar inside the dome.
- **Colour:** red, orange, magenta, black; hand-drawn (cel-shaded) shapes.
- **Works:** anime language done with conviction: darken the world first, impact frames, colour inversion, hand-drawn fire.
- **Weak / risk:** about 3 s of full-screen takeover: in play it hides everything; flashing and inversion are a photosensitivity risk; screen-level effects should be limited to cutscene moments.

## V04 Ice and lightning skills (itsjustfx3)
- **Owner's rating: 5.** "Basically the model for all kind of abilities, it's small, reasonable vfx attack duration and doesn't get tiring to look at even after firing the ability multiple times. All ability like attacks that are used very often should follow this pattern. Not only that, the vfx it self looks very great, such as the details on the icicles, the fade in and fade out of the icicles, the particle burst that happens every cast, etc"
- **Moment:** combat skills; one sample measured. ![[V04-overview.jpg]] ![[V04-ice-burst.jpg]]
- **Timeline:** 4.4 to 4.8 s a charge orb glows and pulls in; **4.9 s white bloom flash** (1 to 2 frames); 5.0 to 5.2 s radial ice shards and a ground ring burst; 5.3 to 5.6 s a crescent sweeps along the ground; 5.6 to 5.9 s shards linger and shrink. Impact to clean: about 1 s.
- **Colour:** one hue family (icy blue) plus white.
- **Works:** short, readable phases; the effect hugs the ground so the character stays visible; one hue.
- **Weak:** several skills look alike (radial shard burst each time).

## V05 Auras, RNG Battlegrounds part 1 (@mojangopa)
- **Owner's rating: 4.5.** "I rather like the vfx themself, such as the professionalism, in other words, it's polished and immediately communicates its entire identity via colors, shapes, movements, details, etc"
- **Moment:** equipped auras (idle loops) on a character. ![[V05-overview.jpg]]
- **Each aura is ONE named concept:** Celestial (gold wings, halo, rune floor), Midnight Lotus (a pink lotus, falling light streaks), Eclipse (a black sun with a corona over a fire ring), Unbound (white chains and a rune circle), Chronos V2 (crystal spikes), Unwritten (black ink pages).
- **Works:** the name and the shape agree; one or two hues each; a floor circle anchors most.
- **Weak:** some (Midnight Lotus, Eclipse) are bigger than the character and fill the frame: in a crowded server they would cover other players.

## V06 Dark-energy shot (itsjustfx3)
- **Owner's rating: 5.** "Very similar reason to V04. It's the kind of ability vfx that sticks. It's addicting to cast and looks impressive."
- **Moment:** a projectile hit. ![[V06-overview.jpg]] ![[V06-orb.jpg]]
- **Timeline:** 0.8 to 1.1 s a thin red projectile with a trail; 1.1 to 1.6 s a black-red sphere grows with smoke; 1.7 to 1.8 s red X slashes; **1.9 s red flash pillar**; 2.0 to 2.1 s rings collapse inward; 2.3 s a cracked black core remains. Later a dark vortex and a large pink burst.
- **Colour:** black and red, white only at the peak.
- **Works:** dark core with a bright rim reads as "dark energy"; the collapse inward before the core is a good beat.
- **Weak:** many stages in a short time; the pink burst at the end changes hue for no clear reason.

## V07 Black hole (@cordhub_)
- **Owner's rating: 4.** "But falls under the same critism as V02. But i like that spark effect as it disappears."
- **Moment:** a black hole opens, rages and collapses. ![[V07-overview.jpg]] ![[V07-black-hole.jpg]]
- **Timeline:** 1.0 s a thin beam rises; 1.4 s a ring pulse flash; 2.0 s the disk forms; 2.4 to 6 s lightning, rocks lifted; 7.0 s collapse; **8.0 s a white star flash**; 9.0 s gone.
- **Colour:** rainbow (pink, cyan, yellow, white) on deep blue.
- **Works:** a clear arc (form, rage, collapse, flash, gone); the lifted rocks tie it to the world.
- **Weak:** the rainbow palette has no reason (a black hole is not a rainbow); lightning is generic decoration.

## V08 Fable 5.2 vs Opus 5.5, same three prompts (@jarvislabsreal)
- **Owner's rating: 4.5.** "Similar to V05. Now, as for the model, I'd say Opus' is slightly superior. Opus conveys each aura's identity slightly better. And for almost double the cost, just for a slight difference, Opus takes the upper hand"
- **Moment:** three auras by two models. ![[V08-overview.jpg]] ![[V08-overview-2.jpg]]
- **Black Hole:** Opus: a clean gold ring disk with floor rings. Fable: a tilted ring with gold debris flying around it.
- **Nebula Wings:** Opus: soft pink wings from particles. Fable: layered wing shapes with a nebula texture inside, a spiral galaxy on the floor.
- **Supernova Crown:** Opus: a cyan star with floor rings. Fable: a large crystalline white star with ring layers.
- **Use:** the owner's preference between the two shows which qualities matter (detail and texture, or cleanness).

## V09 Purple cutscene (@bbstudios4)
- **Owner's rating: 5.** "It's wonderful, the screenshakes add a lot to the impact, the details on the chains, crystal, room... all look very professional and the VFX of each moment really sells the feeling of power"
- **Moment:** a cinematic reveal. ![[V09-overview.jpg]]
- **Beats:** camera through vault rings; chains; a seal; a purple energy burst; a crystal with a halo. 24 fps.
- **Works:** camera moves do half the work; one hue (purple) plus white.
- **Weak:** dark and murky in places; hard to read what breaks.
- **Screen shakes measured 2026-11-12** (phase correlation between frames, 24 fps; `media/V09-shakes.jpg`): 0.21 to 0.46 s vertical, frame-to-frame jumps up to 27 px of a 240 px view; 0.79 to 1.08 s vertical, up to 46 px; 4.79 to 5.29 s horizontal, 30 to 56 px of 576. Each changes direction every frame and decays. About 5 to 10% of the view: large, cutscene-sized.

## V10 Auras, RNG Battlegrounds part 2 (@mojangopa)
- **Owner's rating: 4.5.** "Same as V05."
- **Moment:** equipped auras. ![[V10-overview.jpg]]
- **Each ONE concept:** Axiom Zero (blue gyroscope rings), Rimeheart (ice crystals), Razorbloom (teal flower blades), Saum ("liminal" text rings, black and white), Gilded Hourglass (a gold hourglass over a clock floor).
- **Works:** the strongest concept-to-shape match in the set (Gilded Hourglass); floor circles anchor them.
- **Weak:** like V05, several are much bigger than the character.

## Patterns seen across the set (not rules yet; waiting for the owner's ratings)
- Anticipation, a 1 to 2 frame flash, a shockwave or ring, debris, a soft linger (V02, V04, V06, V07).
- One hue family plus a white core (V01, V04, V09); multi-hue only with a reason (V02's rarity switch) versus without one (V07's rainbow).
- A floor circle anchors auras and charges (V01, V05, V10).
- Auras as one named concept each (V05, V10).
- Screen-level effects (darkened world, impact frames, inversion) reserved for cinematic moments (V03).
- Size against the character: ground-hugging effects keep the player readable (V04); oversized auras cover the scene (V05, V10).

## V11 Clean VFX showcase (idle loops)
- Three small elemental loops (fire, electric, frost), each a few dozen particles in one hue plus white, sized like a held item. ![[V11-overview.jpg]]
- Works: one hue each, tight shapes, the brightest point in the core (X7). Use: hand or weapon idle effects, pickups.
- **Owner's rating: 4.5.** "They could serve as example to as what's a good fire/electricity/ice vfx"

## V12 Bloom Cannon (@kxntiqe)
- The clip loops (it opens on the previous beam). In order: a four-point spark slowly sparks up and pulses (about 1.0 to 3.8 s), four clover-like wings unfold outwards (4.0 to 4.4 s), a one-frame black-and-white impact frame (4.6 s), and the beam fires, leaving an aftermath trail. ![[V12-bloom-cannon.jpg]]
- Works: one warm hue family plus white, a crisp four-point star as the hero shape (X7), an impact frame at the peak (X6); reads well on a bright, saturated map.
- Watch: the long charge suits an ultimate, not a basic attack.
- **Owner's rating: 5.** "I like how the beam actually leaves an aftermath trail, the appearing animation of it is also very cleanly done: first the four point spark slowly sparks up, then the 4 clovers like wings unfold outwards, and only after all that anticipation does the beam actually fire, a devastating attack. Not only that, the map it is on is also very very solid, that belongs to models I guess but worth mentioning, because I really like how it looks."

## V13 Water bending (@freilfrako)
- Several abilities: a water lance thrown from the hand (about 0.4 s), a whip, a rising column with spinning rings, a vortex wrapped round the body. ![[V13-water-bending.jpg]] ![[V13-overview.jpg]]
- Works: the effect flows from the caster's hand (it belongs to the body), one hue family (blue plus white), shapes that read as water (streams, droplets, curls). Close to V04 in scale.
- **Owner's rating: 4.5.** "Could serve as a general reference for melee attacks that have elemental effects like water, fire, electricity etc. Could also serve as animation reference too to be honest"

## V14 Star beam (@corektvfx)
- A violet slash streak with sparkle stars (0.9 to 1.9 s), small star hits, a brief cut to black, a burst of stars (3.1 to 3.3 s), then a wide white-pink beam from the sky (3.5 to 4.9 s), gone with a fading star. ![[V14-star-beam.jpg]]
- Works: one concept (stars) in every part; the sky beam as the finisher.
- The black frame before the burst is an impact frame on the hit that sends the dummy flying (not a cut).
- **Owner's rating: 4.5.** "Great ability effect, note the use of flash and impact frame as it sends the dummy out flying, that's the touch that makes it impactful"

## V15 Arcane Atelier (@arcane_atelier): impact frames, measured
![[V15-impact-frames.jpg]] ![[V15-overview.jpg]]
- **Two-tone impact frames on strong hits**, found at 8.17, 9.10, 11.43, 23.63 and 34.37 s (frame-by-frame brightness at 29.97 fps). Each is the same sequence of about 5 frames (about 170 ms): a white frame with black silhouettes, a black frame with the attacker and target as white silhouettes, white again (1 or 2 frames), a high-contrast black-and-white frame of the scene, then straight back to colour. The HUD stays visible through it.
- **On the target:** a brief white hit ring and spark at the contact point (37.20 to 37.34 s) plus a short red pulse on the target (2 frames, about 70 ms).
- **Owner's rating: 5.** "the animations are very fluid and the combat system is nice too. I also like the map design. The HUDs match the game well too."
- **Damage tint (found after the owner's note):** "very very brief, it happens every time the bottom health bar drops ... a quite transparent red overlay". Measured at 9 moments (29.4 to 61.5 s): the whole screen's red shifts up by about 13 to 20 (of 255) in ONE frame, on the same frame the health bar starts to drop, then fades back over about 200 to 300 ms. Very transparent: roughly 10 to 15% red. ![[V15-damage-tint.jpg]]
- No low-health alert was seen.
- **A leaf wipe** at 60.0 s: green leaves sweep across the whole screen in about 70 ms, hold about 300 ms, then clear (a transition or an ability).
- Bright, saturated cartoon map; an ornate HUD in one theme (RPG1).

