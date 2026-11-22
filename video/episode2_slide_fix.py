"""Replace a wrong slide of a NotebookLM video with a corrected checklist slide.

Usage:
  python3 video/episode2_slide_fix.py IN.mp4 OUT.mp4 SLIDES.json

SLIDES.json is a list of slides. Each slide gives the time span in seconds during which the wrong
slide is on screen, a title, the lines that are ticked and the lines that are still open:

  [{"start": 218.3, "end": 264.7, "title": "...", "done": ["..."], "running": ["..."]}]

The corrected slide is drawn over the picture for that span and fades in and out. The sound and the
bottom strip of the picture, which holds the NotebookLM mark, stay as they are.
"""
import json
import subprocess
import sys
import tempfile
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

sys.path.insert(0, str(Path(__file__).resolve().parent))
from paths import FONTS, need  # noqa: E402

W, H, STRIP = 1280, 720, 36
INK, GREEN, GREY = (20, 24, 32), (26, 127, 78), (120, 126, 138)


def probe(path, entry):
    r = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries", entry,
                        "-of", "csv=p=0", str(path)], capture_output=True, text=True)
    return r.stdout.strip()


def background(src, t):
    """Take the paper colour from the wrong slide itself, so the corrected slide matches it."""
    with tempfile.TemporaryDirectory() as tmp:
        frame = Path(tmp) / "frame.png"
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-ss", f"{t:.2f}", "-i", str(src),
                        "-frames:v", "1", str(frame)], check=True)
        return Image.open(frame).convert("RGB").getpixel((12, 12))


def draw_slide(spec, colour, out):
    img = Image.new("RGB", (W, H - STRIP), colour)
    d = ImageDraw.Draw(img)
    title = ImageFont.truetype(str(FONTS / "Inter-SemiBold.ttf"), 34)
    line = ImageFont.truetype(str(FONTS / "Inter-Regular.ttf"), 30)
    small = ImageFont.truetype(str(FONTS / "Inter-Medium.ttf"), 22)
    x, y = 96, 64
    d.text((x, y), spec["title"], font=title, fill=INK)
    y += 78
    for text in spec.get("done", []):
        d.line([(x, y + 18), (x + 10, y + 30), (x + 30, y + 4)], fill=GREEN, width=6, joint="curve")
        d.text((x + 54, y), text, font=line, fill=INK)
        y += 52
    if spec.get("running"):
        y += 14
        d.text((x, y), "Still running that evening", font=small, fill=GREY)
        y += 42
    for text in spec.get("running", []):
        d.rectangle([(x + 2, y + 6), (x + 28, y + 32)], outline=GREY, width=3)
        d.text((x + 54, y), text, font=line, fill=INK)
        y += 52
    if y > H - STRIP - 10:
        raise SystemExit("The slide has too many lines to fit.")
    img.save(out)


def main():
    if len(sys.argv) != 4:
        raise SystemExit(__doc__)
    src, out, specs = Path(need(sys.argv[1])), Path(sys.argv[2]), json.loads(Path(need(sys.argv[3])).read_text())
    w, h = (int(v) for v in probe(src, "stream=width,height").split(","))
    if (w, h) != (W, H):
        raise SystemExit(f"Expected a {W}x{H} video and got {w}x{h}.")
    total = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0",
                                  str(src)], capture_output=True, text=True).stdout)
    out.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory() as tmp:
        inputs, chains, last = ["-i", str(src)], [], "0:v"
        for i, spec in enumerate(specs):
            a, b = float(spec["start"]), float(spec["end"])
            png = Path(tmp) / f"slide{i}.png"
            draw_slide(spec, background(src, (a + b) / 2), png)
            inputs += ["-loop", "1", "-t", f"{total:.3f}", "-i", str(png)]
            chains.append(f"[{i + 1}:v]format=rgba,fade=t=in:st={a:.2f}:d=0.3:alpha=1,"
                          f"fade=t=out:st={b - 0.3:.2f}:d=0.3:alpha=1[s{i}]")
            chains.append(f"[{last}][s{i}]overlay=0:0:enable='between(t,{a:.2f},{b:.2f})'[v{i}]")
            last = f"v{i}"
            print(f"slide {i + 1}: {a:.1f} s to {b:.1f} s, {spec['title']}")
        r = subprocess.run(["ffmpeg", "-y", "-loglevel", "error", *inputs, "-filter_complex", ";".join(chains),
                            "-map", f"[{last}]", "-map", "0:a", "-c:v", "libx264", "-preset", "veryfast", "-crf", "18",
                            "-pix_fmt", "yuv420p", "-c:a", "copy", "-t", f"{total:.3f}", str(out)],
                           capture_output=True, text=True)
        if r.returncode != 0:
            raise SystemExit("ffmpeg failed:\n" + r.stderr[-1500:])
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
