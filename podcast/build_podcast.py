"""Build the audio podcast and its static-image video.

Takes the NotebookLM podcast audio, cuts it at the points in data/podcast_timeline.json,
inserts the audio of the interview clips built by video/clips_c.py at the podcast's own
speech level, and normalises the result to -16 LUFS. No music or effects.

Inputs:  SOURCES/podcast/AI_Proves_Historic_Riemann_Hypothesis_Bound.m4a, BUILD/clips/clip01..10.mp4
Outputs: BUILD/podcast/Predicting_Primes_podcast.m4a and .mp4 (cover image as the picture)
"""
import json, re, subprocess, sys
from pathlib import Path
import numpy as np, soundfile as sf
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "video"))
from paths import ROOT, SOURCES, BUILD, build_dir, need
from scenes_b import *
from scenes_b import _art

SR = 44100
OUT = build_dir("podcast")
SRC = need(SOURCES / "podcast" / "AI_Proves_Historic_Riemann_Hypothesis_Bound.m4a")
TITLE = "Predicting Primes"

def run(a): subprocess.run(a, check=True)
def lufs(p):
    o = subprocess.run(["ffmpeg", "-hide_banner", "-i", str(p), "-af", "ebur128", "-f", "null", "-"], capture_output=True, text=True).stderr
    return float(re.findall(r"I:\s+(-?[0-9.]+) LUFS", o)[-1])

pod = OUT / "pod44.wav"
run(["ffmpeg", "-v", "error", "-y", "-i", SRC, "-ac", "2", "-ar", str(SR), str(pod)])
level = lufs(pod); frames = sf.info(pod).frames
fade = int(0.25 * SR); gap = np.zeros((int(0.35 * SR), 2), np.float32)
marks = []; pos = 0
# Written piece by piece: an hour of stereo audio does not fit comfortably in memory
with sf.SoundFile(OUT / "speech.wav", "w", SR, 2, "PCM_16") as out:
    def put(x):
        global pos
        out.write(x); pos += len(x)
    for entry in json.load(open(ROOT / "data" / "podcast_timeline.json")):
        if entry[0] == "pod":
            a = int(entry[1] * SR); b = frames if entry[2] is None else int(entry[2] * SR)
            x, _ = sf.read(pod, start=a, stop=b, dtype="float32", always_2d=True)
            x[:fade] *= np.linspace(0, 1, fade)[:, None]; x[-fade:] *= np.linspace(1, 0, fade)[:, None]; put(x)
        else:
            wav = OUT / f"c{entry[1]:02d}.wav"
            run(["ffmpeg", "-v", "error", "-y", "-i", need(BUILD / "clips" / f"clip{entry[1]:02d}.mp4"), "-vn", "-ac", "2", "-ar", str(SR), str(wav)])
            x, _ = sf.read(wav, dtype="float32", always_2d=True); x = x * 10 ** ((level - lufs(wav)) / 20)
            put(gap); marks.append((entry[1], pos / SR, (pos + len(x)) / SR)); put(x); put(gap)
end = pos / SR
json.dump({"clips": marks, "end": end}, open(OUT / "marks.json", "w"))

audio = OUT / "Predicting_Primes_podcast.m4a"; tmp = OUT / "tmp.m4a"
run(["ffmpeg", "-v", "error", "-y", "-i", str(OUT / "speech.wav"), "-af", "loudnorm=I=-16:TP=-1.5:LRA=11", "-ar", str(SR), "-c:a", "aac", "-b:a", "128k",
     "-metadata", f"title={TITLE}", "-metadata", "artist=Marko T. Manninen", "-metadata", "date=2026", str(tmp)])
tmp.replace(audio)

# Cover image in the style of the video's title card
fig = plt.figure(figsize=(W, H), dpi=DPI); ax = canvas(fig, 0); _art(ax, "title")
txt(ax, 0.8, 7.75, spaced("Podcast"), 12, ORANGE, "semibold")
ax.text(0.8, 6.65, TITLE, fontsize=80, color=INK, family=HEAD, va="center")
txt(ax, 0.8, 5.55, "A conversation on the Riemann Hypothesis and the AI result of autumn 2026", 18, MUTED)
panel(ax, 0.8, 3.6, ORANGE, "With interview excerpts", "Brian Greene and Alex Kontorovich\nWorld Science Festival, 2026", 15, 12.5)
txt(ax, 0.8, 1.0, "AI-generated voices  ·  © 2026 Marko T. Manninen", 11, MUTED)
cover = OUT / "cover.png"; fig.savefig(cover, dpi=DPI); plt.close(fig)

video = OUT / "Predicting_Primes_podcast.mp4"; tmpv = OUT / "tmp.mp4"
run(["ffmpeg", "-v", "error", "-y", "-loop", "1", "-framerate", "2", "-i", str(cover), "-i", str(audio), "-c:v", "libx264", "-preset", "medium", "-tune", "stillimage",
     "-crf", "22", "-pix_fmt", "yuv420p", "-g", "120", "-c:a", "copy", "-shortest", "-movflags", "+faststart", str(tmpv)])
tmpv.replace(video)
print("Done:", audio, video, "| clips at", [(k, round(a)) for k, a, _ in marks])
