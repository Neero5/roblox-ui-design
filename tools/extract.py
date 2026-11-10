"""Turn a reference video into evidence a model can read.

Usage:  python -I tools/extract.py <video.mp4> <out_dir> [--every 0.5] [--width 288]

Writes into <out_dir>:
  sheet_<n>.png   contact sheets: one frame every --every seconds, labelled with the time
  motion.png      how much the picture changes per frame (spikes = something animates)
  bursts.json     the motion bursts found: start/peak/end frame and time, at the video's own fps
  burst_<k>.png   every frame of each burst (up to 48), labelled f<frame> and ms from the burst start
  info.json       fps, size, duration, frame count

The video itself never goes into git: keep it outside the repo (owner's OneDrive / uploads).
"""
import argparse
import json
import os
import shutil
import subprocess
import sys
import tempfile

import numpy as np
from PIL import Image, ImageDraw, ImageFont


def font(size):
    for path in ("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
                 "C:/Windows/Fonts/arialbd.ttf"):
        if os.path.exists(path):
            return ImageFont.truetype(path, size)
    return ImageFont.load_default()


def probe(video):
    out = subprocess.check_output([
        "ffprobe", "-v", "error", "-select_streams", "v:0",
        "-show_entries", "stream=width,height,r_frame_rate:format=duration",
        "-of", "json", video])
    j = json.loads(out)
    s = j["streams"][0]
    num, den = s["r_frame_rate"].split("/")
    return {"width": s["width"], "height": s["height"],
            "fps": float(num) / float(den), "duration": float(j["format"]["duration"])}


def label(img, text):
    d = ImageDraw.Draw(img)
    f = font(max(12, img.width // 14))
    box = d.textbbox((0, 0), text, font=f)
    d.rectangle((0, 0, box[2] + 8, box[3] + 6), fill=(0, 0, 0))
    d.text((4, 2), text, fill=(255, 230, 80), font=f)
    return img


def grid(frames, cols, path):
    w, h = frames[0].size
    rows = (len(frames) + cols - 1) // cols
    sheet = Image.new("RGB", (cols * w + (cols - 1) * 4, rows * h + (rows - 1) * 4), (40, 40, 40))
    for i, f in enumerate(frames):
        sheet.paste(f, ((i % cols) * (w + 4), (i // cols) * (h + 4)))
    sheet.save(path)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("video")
    ap.add_argument("out")
    ap.add_argument("--every", type=float, default=0.5, help="seconds between contact-sheet frames")
    ap.add_argument("--width", type=int, default=288, help="frame width in the sheets")
    ap.add_argument("--threshold", type=float, default=2.0, help="motion level that counts as a burst")
    ap.add_argument("--crop", help="x,y,w,h in source pixels: keep only the game area (drops captions/watermarks)")
    ap.add_argument("--start", type=float, help="first second to keep")
    ap.add_argument("--end", type=float, help="last second to keep")
    a = ap.parse_args()

    info = probe(a.video)
    fps = info["fps"]
    os.makedirs(a.out, exist_ok=True)
    tmp = tempfile.mkdtemp(prefix="refx_")
    try:
        # every frame, small, at the video's own rate
        vf = f"scale={a.width}:-2"
        if a.crop:
            x, y, w, h = a.crop.split(",")
            vf = f"crop={w}:{h}:{x}:{y}," + vf
        cmd = ["ffmpeg", "-v", "error"]
        if a.start is not None:
            cmd += ["-ss", str(a.start)]
        cmd += ["-i", a.video]
        if a.end is not None:
            cmd += ["-t", str(a.end - (a.start or 0))]
        subprocess.check_call(cmd + ["-vf", vf, "-vsync", "0", os.path.join(tmp, "f%05d.png")])
        offset = a.start or 0.0  # labels show the time in the original video
        names = sorted(os.listdir(tmp))
        frames = [Image.open(os.path.join(tmp, n)).convert("RGB") for n in names]
        info["frames"] = len(frames)

        # motion: mean absolute difference to the previous frame (0-255 scale)
        arr = [np.asarray(f.convert("L"), dtype=np.int16) for f in frames]
        motion = [0.0] + [float(np.abs(arr[i] - arr[i - 1]).mean()) for i in range(1, len(arr))]

        # contact sheets, 24 frames each
        step = max(1, round(a.every * fps))
        picks = list(range(0, len(frames), step))
        for n, start in enumerate(range(0, len(picks), 24)):
            chunk = [label(frames[i].copy(), f"{offset + i / fps:.1f}s") for i in picks[start:start + 24]]
            grid(chunk, 6, os.path.join(a.out, f"sheet_{n + 1}.png"))

        # motion graph
        gw, gh = 1200, 240
        g = Image.new("RGB", (gw, gh + 30), (20, 20, 20))
        d = ImageDraw.Draw(g)
        top = max(motion) or 1
        for i, m in enumerate(motion):
            x = int(i / max(1, len(motion) - 1) * (gw - 1))
            d.line((x, gh, x, gh - int(m / top * (gh - 10))), fill=(90, 200, 255))
        ty = gh - int(a.threshold / top * (gh - 10))
        d.line((0, ty, gw, ty), fill=(255, 80, 80))
        for s in range(0, int(info["duration"]) + 1, 2):
            x = int(s * fps / max(1, len(motion) - 1) * (gw - 1))
            d.text((x + 2, gh + 8), f"{s}s", fill=(220, 220, 220), font=font(12))
        g.save(os.path.join(a.out, "motion.png"))

        # bursts: runs above the threshold, joined across gaps of <= 3 frames
        bursts, cur, gap = [], None, 0
        for i, m in enumerate(motion):
            if m >= a.threshold:
                if cur is None:
                    cur = [i, i]
                cur[1], gap = i, 0
            elif cur is not None:
                gap += 1
                if gap > 3:
                    bursts.append(cur)
                    cur, gap = None, 0
        if cur:
            bursts.append(cur)
        out = []
        for k, (s, e) in enumerate(bursts):
            s0, e0 = max(0, s - 2), min(len(frames) - 1, e + 2)
            peak = max(range(s, e + 1), key=lambda i: motion[i])
            out.append({"burst": k + 1, "start_f": s, "peak_f": peak, "end_f": e,
                        "start_s": round(offset + s / fps, 3), "length_ms": round((e - s + 1) / fps * 1000),
                        "peak_ms_from_start": round((peak - s) / fps * 1000),
                        "peak_motion": round(motion[peak], 2)})
            idx = list(range(s0, e0 + 1))
            if len(idx) > 48:  # long bursts: keep the start and the peak region
                idx = sorted(set(idx[:24] + list(range(max(s0, peak - 12), min(e0, peak + 12) + 1))))[:48]
            chunk = [label(frames[i].copy(), f"f{i} +{round((i - s) / fps * 1000)}ms") for i in idx]
            grid(chunk, 8, os.path.join(a.out, f"burst_{k + 1}.png"))

        with open(os.path.join(a.out, "bursts.json"), "w") as fh:
            json.dump(out, fh, indent=1)
        with open(os.path.join(a.out, "info.json"), "w") as fh:
            json.dump(info, fh, indent=1)
        print(json.dumps({"info": info, "bursts": len(out), "sheets": (len(picks) + 23) // 24}))
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


if __name__ == "__main__":
    sys.exit(main())
