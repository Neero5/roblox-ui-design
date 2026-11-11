---
type: reference
category: vfx
source:                 # creator + caption; the video stays OUT of git
captured:
capture: screen         # screen | filmed (layout only, no timing) | slow-motion
rating:                 # the owner's 1-5
verdict:                # good | fine | bad (the owner's call)
tags: [vfx]
---
# <number> <short name>

**Source:** · **Length:** · **fps:** · **Upload file:**

## The moment
What happens in the game (a hit, a level-up, a rare drop, a cast, an aura) and what the player must understand or feel.

## Timeline (ms from the trigger)
| t (ms) | layer | what happens | shape (burst, ramp, hold, fade) |
|---|---|---|---|
| 0 | | | |

Phases: anticipation ... ms, impact ... ms, hold ... ms, dissipation ... ms. Total ... ms.

## Layers
Core (the brightest, the shape that reads first), glow, secondary (sparks, debris, smoke), shockwave or ring, screen-level (flash, shake, light change). For each: shape, colour and value, size against the character, lifetime.

## Readability
Silhouette at a glance (one frame, small); does it read on a bright and a dark background; does it hide the character or the play.

## Colour and value
The palette (2-3 hues?), where the brightest value sits, how colour carries energy (hot core to cool edge?).

## Identity
Does it belong to its game's world (the motif, the materials), or is it a stock effect any game could use?

## The one detail that makes it work

## What is weak or overdone

## Roblox recipe
ParticleEmitter (rate vs Emit, Lifetime, Size/Transparency sequences, LightEmission, Drag, Acceleration, Squash, FlipbookLayout), Beam, Trail, Attachments, PointLight, mesh parts with tweens, ColorCorrection or Bloom pulses, camera shake.

## Fit
Which game types this suits; keep / adapt / refuse.
