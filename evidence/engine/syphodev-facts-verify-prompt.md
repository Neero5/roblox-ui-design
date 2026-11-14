# Studio check: six engine facts reported by SyphoDev (paste into a local session with Studio open)

```
Read-only engine check for my roblox-ui-design plugin. Use the Roblox Studio MCP (list_roblox_studios
first). Build test objects under a new Folder "FactCheck" in Workspace; delete it at the end; change
nothing else; stop Play when done.

1. Particle size: a ParticleEmitter (Size 4 constant, Rate 0, Lifetime 5, Speed 0, LockedToPart) on a
   part beside a 1x8x1 reference part; Emit(1); capture from the side. Is the particle about 4 or about
   8 studs wide?
2. Emitter Shape under an Attachment: the same emitter with Shape = Box on a 10x1x10 Part, then moved
   under an Attachment on that Part; Emit(30) each; capture. Does the Attachment one spawn from one point?
3. CFrame tween direction: tween a part's CFrame by 260 degrees about Y in 1 s; sample its Y angle every
   0.1 s. Does it turn +260 or -100?
4. SurfaceAppearance on a plain Part: parent one to a Part (not a MeshPart). Error, or accepted?
5. Dark additive aura: two emitters with black colour, LightEmission 0 and LightEmission 1, side by side
   on a mid-grey background; capture. Does the LightEmission 1 one turn reddish or invisible?
6. Mesh orientation through OBJ to FBX: not testable without an upload; reply "not tested" unless an
   asymmetric mesh uploaded that way is at hand.

Reply with a table: fact, result, evidence, "confirmed" / "wrong" / "not tested". Then delete FactCheck
and stop Play.
```
