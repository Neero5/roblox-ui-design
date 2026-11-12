# VFX verdicts

## First ruling (2026-11-12): the owner's ratings of V01 to V10
| # | Rating | Owner's words |
|---|---|---|
| V01 | 4.5 | "It's very decent, specially for cutscenes and rare/late game attacks for RPGs or Roguelikes. I also put it because it seems like they somehow managed to get claude to use the roblox plugin called VFX studio" |
| V02 | 3.5 | "I suppose it's nice as opening animations, like the cutscene and vfxs, but it's a bit maximalistic, which isn't exactly my taste." |
| V03 | 4.5 | "Same as V01. But it also does well by adding those impact frames and the flame looks well done" |
| V04 | 5 | "Basically the model for all kind of abilities, it's small, reasonable vfx attack duration and doesn't get tiring to look at even after firing the ability multiple times. All ability like attacks that are used very often should follow this pattern. Not only that, the vfx it self looks very great, such as the details on the icicles, the fade in and fade out of the icicles, the particle burst that happens every cast, etc" |
| V05 | 4.5 | "I rather like the vfx themself, such as the professionalism, in other words, it's polished and immediately communicates its entire identity via colors, shapes, movements, details, etc" |
| V06 | 5 | "Very similar reason to V04. It's the kind of ability vfx that sticks. It's addicting to cast and looks impressive." |
| V07 | 4 | "But falls under the same critism as V02. But i like that spark effect as it disappears." |
| V08 | 4.5 | "Similar to V05. Now, as for the model, I'd say Opus' is slightly superior. Opus conveys each aura's identity slightly better. And for almost double the cost, just for a slight difference, Opus takes the upper hand" |
| V09 | 5 | "It's wonderful, the screenshakes add a lot to the impact, the details on the chains, crystal, room... all look very professional and the VFX of each moment really sells the feeling of power" |
| V10 | 4.5 | "Same as V05." |

**Model choice for VFX (V08):** Opus 5.5 over Fable 5.2: "Opus conveys each aura's identity slightly better. And for almost double the cost, just for a slight difference, Opus takes the upper hand".

## Proposed VFX rules (Claude, 2026-11-12, from the ratings; for the owner's ruling)
| # | Proposed rule | Evidence |
|---|---|---|
| X1 | **Budget by frequency.** An effect players trigger often (a basic ability, a hit) stays compact and short: about 1 s from impact to clean, close to the caster or target, never covering other players or the screen. Big, long and screen-level effects are for rare moments: an ultimate, a late-game attack, a cutscene, a rare reveal. | V04, V06 (5: "doesn't get tiring ... used very often should follow this pattern") vs V01, V03, V09 (rare and cinematic) |
| X2 | **Repeatable.** A frequent effect must still please on the twentieth cast: no long holds, no full-screen flash, the same readable shape each time with small variation (size, angle, spark count). | V04, V06 ("addicting to cast") |
| X3 | **The impact shape.** Anticipation, a 1 to 2 frame flash, a burst or ring, debris, then a soft fade. Every element fades or shrinks in and out; nothing pops on or cuts off. | V04 (charge 300 to 500 ms, flash 1 to 2 frames, gone in about 1 s; "the fade in and fade out of the icicles"), V06, V07 ("that spark effect as it disappears") |
| X4 | **Detail over quantity.** A few well-made elements (shaped shards, drawn flame, chains with real detail) beat many generic particles. Maximalism loses even when it looks impressive. | V04 icicles, V03 flame, V09 chains and crystal vs V02 (3.5) and V07 (4) "maximalistic" |
| X5 | **Identity at a glance.** Each effect is one named concept that its colour, shape, motion and details all express; one hue family plus a white core unless a hue carries meaning (rarity, element). | V05, V10, V08 ("immediately communicates its entire identity via colors, shapes, movements, details") |
| X6 | **Screen-level effects sell power, only at the peak.** Screen shake, impact frames, a darkened world or a colour inversion are allowed on rare or cinematic moments, briefly, at the hit. Never on frequent effects; off or reduced under Reduced Motion; no fast repeated full-screen flashes. | V09 ("the screenshakes add a lot to the impact"), V03 ("impact frames") |

Model note (from V08): give VFX work to Opus rather than Fable (owner: similar quality, Opus conveys identity slightly better, at about half the cost).
Tool note (from V01): the owner believes the creator had Claude drive a Roblox Studio VFX plugin; not verified here.
