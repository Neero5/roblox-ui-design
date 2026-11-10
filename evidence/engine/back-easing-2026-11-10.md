# Back Out overshoot, measured in Studio (owner, 2026-11-10)

Owner's local session, Studio MCP, Edit and Play.

| Item | Value |
|---|---|
| `TweenService:GetValue(alpha, Back, Out)` peak | 1.100004 |
| alpha of the peak | 0.580 |
| UIScale 0.92 -> 1 peak | 1.0080 (+0.8% of the final size) |
| UIScale 0.85 -> 1 peak | 1.0150 (+1.5%) |
| UIScale 0.5 -> 1 peak | 1.0500 (+5.0%) |
| Play: UIScale 0.92 -> 1 over 0.18 s, read every RenderStepped | peak 1.00785 at 0.098 s (predicted 0.58 x 0.18 = 0.104 s); ended exactly at 1.0 after 30 frames |

Conclusion: Back Out overshoots 10% of the distance TRAVELLED, not 10% of the final size. A pop from 0.92 overshoots 0.8% of the final size, too small to see; a visible peak needs a large start (0.5 -> 1 gives 5%, the R11 limit). Peak value = 1 + 0.1 x (1 - start).
