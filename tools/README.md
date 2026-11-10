# extract.py

```
python -I tools/extract.py <clip.mp4> <out_dir> [--every 1.0] [--width 432] [--crop x,y,w,h] [--start s] [--end s] [--threshold 2.0]
```
Writes `sheet_*.png` (labelled contact sheets), `motion.png` (picture change per frame), `bursts.json` (start/peak/length in ms of each motion burst), `burst_*.png` (every frame of each burst) and `info.json`.

1. Whole clip, `--every 1.0`: what is in it.
2. `--crop` the game area (source pixels) to drop captions and watermarks.
3. Zoom: `--start/--end` around one moment with `--every 0.0334` (each frame at 30 fps). Labels show the time in the original clip.

Outputs go to a scratch folder, not the repo.
