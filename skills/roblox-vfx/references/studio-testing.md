# Studio testing: traps and fixes

Read before any playtest, capture or texture upload in Roblox Studio (VFX or UI). Every trap below cost real time in the owner's first ability effect (Ink Lance, 2026-11-24); the fix is what worked. Game-specific values (rig coordinates, asset ids, cooldowns) live in the game's own notes: look for them in the profile's "References folder" or style guide before testing.

## Quick checklist
1. Textures: white on transparent, hard-edged, before upload (section Textures).
2. Code reaches Studio only if the sync tool (Rojo) is alive, or after: stop play, push, verify, start play (section Getting code into Studio).
3. Pin the camera every frame with a RenderStep binding; a one-off `CameraType = Scriptable` gets overwritten.
4. Record with `video_capture` and build contact sheets locally; never loop `screen_capture` (section Recording).
5. Slow the effect with a client time-scale attribute so 1 to 2 frame beats can be seen.
6. Particles with `VelocityParallel`: a **negative** `Squash` stretches along the motion.
7. Check every view: behind, side, front (camera outside the effect's range), 45°, near and far, bright and dark ground.
8. Cast 10 times at normal speed and compare the effect folder's instance count.

## Getting code into Studio
| Problem | Cause | Fix |
|---|---|---|
| Studio keeps running old code; changes "do nothing", with no error. | `rojo serve` crashed (`NotFound` in the change processor) when files were replaced whole while it was serving (a full-file write, or a formatter such as `stylua` rewriting files). The Studio plugin shows nothing. | After big edits or a format run, check the serve task is still alive; restart it and reconnect the plugin. Prefer small in-place edits while serving. |
| Pushing code by hand also "does nothing". | Setting `Script.Source` with `execute_luau` on the Edit datamodel while a playtest runs is silently not applied, and a running playtest never picks up Edit changes (it copied the scripts when play started). | Stop play, push, verify the Edit copy holds the new text (`string.find(script.Source, "<new value>")`), start play, then read the live value back from the Client datamodel (`require(<module>).<field>`). Never trust a push without both checks. |
| `execute_luau` fails: "datamodel_type is required". | The Studio MCP needs it on every call. | Pass `Edit`, `Client` or `Server`. Server: world and server state. Client: camera, casting, effect and UI checks. |
| Pushed code is not saved. | A push edits the open place only. | Say so in the report; a resync from the repo makes it moot. |

Push recipe (one ModuleScript): `local s = <path>; s.Source = [=====[<file text>]=====]; return #s.Source`. Check that the file text never contains the closing delimiter.

## Casting and the camera in a playtest
- **Cast without a keypress:** fire the game's cast remote from the Client datamodel with the same arguments the input code sends. The server treats it as a real cast.
- **Cooldown:** wait at least the ability's cooldown between test casts, or the cast is refused and the recording shows nothing.
- **Camera:** the game's camera scripts reset `CameraType`. Bind once per playtest: `RunService:BindToRenderStep("DevContactCam", Enum.RenderPriority.Last.Value + 10, fn)`, where `fn` sets `Scriptable` and `CFrame.lookAt(workspace:GetAttribute("DevCamPos"), workspace:GetAttribute("DevCamLook"))` every frame. Move the camera by setting the two attributes. Restarting play drops the binding; remove it before reporting (rule E).
- **Front view:** put the camera outside the effect's range, or the effect sweeps through the lens.

## Recording and contact sheets
| Problem | Fix |
|---|---|
| `screen_capture` puts every image into the conversation; many views and frames flood the context and burn usage. | Use `video_capture` (start, cast, wait, stop): it returns file paths only. Build contact sheets on the owner's machine and look only at the sheet. For a light check, one or two `screen_capture` frames are still fine. |
| No ffmpeg, Homebrew or PIL on the owner's Mac. | Use the game's own capture tools if its notes list them (an AVFoundation Swift script for frames and tiling, standard-library Python for stacking); `sips -s format png` converts JPEG. Do not install packages without asking. |
| Beats last 1 to 2 frames and fall between captures. | Slow motion: the effect code reads a client attribute such as `workspace:GetAttribute("FxTimeScale")` (0.05: 1 effect frame = about 0.66 s real). Only effects slow down; server hits keep real time; effect-side timers last 1/scale longer. Set it back to 1 for count tests. If the game has no such attribute, propose adding it to the effect player. |
| Matching effect time to video time. | Note the clock when recording starts and when the cast fires: video time = (cast − record start) + effect time / scale. |

Sampling: 8 frames across the effect are enough to judge (for a 1 s effect: through the charge, release, hit, hold and fade); keep 16-frame sheets for a report.

## Textures
| Problem | Fix |
|---|---|
| ServerStorage effect libraries can't be read by clients. | Reference textures by asset id from a client config; never clone from ServerStorage at run time. |
| A drawn texture with clean alpha but dark paint renders near-black: Roblox multiplies texture by tint. | Check the brightness histogram first; keep the alpha and make the colour white, then tint in Roblox. Crop atlas cells, threshold away faint frame lines and haze, pack cells into a flipbook if needed. |
| Uploading. | `upload_image` (Studio MCP) needs an http URL: serve the folder on 127.0.0.1 in the background, upload, stop the server. Uploading publishes to the owner's account: ask first. |
| Right after upload: "Asset content representation is being generated". | Retry `ContentProvider:PreloadAsync` on the ids until each reports `Success` (about 30 s) before recording. |
| A texture with a grey edge (for example `rbxassetid://244221535`, a 4-point star) tinted white or pale reads grey. | Tint it with the rim or mid tone only. |

## Engine behaviour checked in Studio
- **Particles, `Orientation = VelocityParallel`:** the texture's X axis runs along the velocity. A **negative** `Squash` stretches along the motion, a positive one across it. A texture that points "up" needs `Rotation = 90` to lead along the motion. When unsure, emit three particles side by side (Squash −1.5, 0, 1.5) and take one screenshot.
- **Beams:** with `TextureMode = Stretch`, the texture's left edge sits at `Attachment0`. A `FaceCamera` beam seen along its length shrinks to almost nothing: from behind the caster, add camera-facing billboards (rings, a blot at the head) as the cue.
- **Highlight:** a white fill at transparency 0 turns the target into a flat white shape. Use about 0.3 for a single white hit frame. A very pale tint (around 0.55 transparency) still reads white on light-coloured characters.
- **Post effects:** DepthOfField can blur thin lines; test with it on and off. Bloom with threshold 2 leaves flat colours alone.

## Design traps found by review (general lessons)
| First build | Why it read wrong | What fixed it |
|---|---|---|
| A fast head with a short trail | Arrives in 3 to 6 frames: reads as an arrow or dart | Make the concept the real thing (X8): a stroke painted from source to head that holds. Keep gameplay speed; it is a balance number, not a VFX one. |
| A hairline left along the path | Reads as a laser or wire | Let the shape erode (X13): thin in steps, break up from the source end, drip. |
| Target flat white for 2 frames plus white star puffs | Harsh, hides the target | One semi-transparent white frame, then a tint, then an outline. |
| Tiny burst specks | Impact reads as a white flash | Layers: a ring around the target, a splat thrown through behind it, spray, shards, drops, a ground mark. |
| Small charge, hidden by the caster's body | Invisible from behind | A bigger charge with parts outside the body silhouette. |
| A per-ability behaviour (turn to aim) applied to every slot | Decided design for abilities not made yet | Make such behaviour opt-in per ability in the combat data. |

## Budget and cleanup check
Count the effect folder's descendants, enabled beams, billboards and highlights before and after each of 10 casts at time scale 1. The count must stay flat (pooled marks reused and hidden, never piling up).

## Harmless console noise
- "Assistant plugin version changed ... restart Roblox Studio": Studio's own plugin; the MCP still works.
- DataStore or ProfileStore "no API access" lines: Studio without API access; save data runs in mock mode.
