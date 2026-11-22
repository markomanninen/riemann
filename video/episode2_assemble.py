"""Place the reaction inserts into a NotebookLM narration at its spoken cue lines.

Usage:
  python3 video/episode2_assemble.py audio NARRATION.m4a WORDS.json OUT.m4a [DROP.txt]
  python3 video/episode2_assemble.py video NARRATION.mp4 WORDS.json OUT.mp4 [DROP.txt]

WORDS.json is a Whisper transcript of the narration with word timestamps. The script finds each cue
line in the transcript, cuts the narration right after the cue, and puts the matching insert from
build/episode2/ there. A cue that is missing from the narration is reported and skipped.

DROP.txt is an optional edit list with one spoken phrase per line, written as the transcript has it.
Each phrase is found in the transcript and cut out of the narration, from its first word to its last.
A line of the form  FIRST WORDS ||| LAST WORDS  cuts a longer passage, from the start of the first
phrase to the end of the last one. Lines that start with # are notes. A phrase that the transcript
lacks is reported and skipped.
"""
import difflib
import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from paths import build_dir, need  # noqa: E402

INS = build_dir("episode2")
W, H, FPS = 1280, 720, 30

CUES = {
    "audio": [
        ("here is how the news sounded", "A"),
        ("here is brian greene in his own words", "B"),
        ("here are the voices of caution", "C"),
        ("brian greene summed up the mood in three words", "D"),
    ],
    "video": [
        ("here is how the news sounded", "A"),
        ("here are the voices of caution", "C"),
    ],
}


def norm(text):
    text = text.lower().replace("here's", "here is").replace("’", "'")
    return re.sub(r"[^a-z0-9 ]+", "", text).split()


def load_words(path):
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    words = []
    for seg in data["segments"]:
        for w in seg.get("words", []):
            for token in norm(w["word"]):
                words.append((token, float(w["start"]), float(w["end"])))
    return words


def find_cue(words, cue, after=0.0):
    """Return (cut_time, score) for the best match of the cue that starts after the given time."""
    target = norm(cue)
    n = len(target)
    best = (None, 0.0)
    tokens = [w[0] for w in words]
    for i in range(len(words) - n + 1):
        if words[i][1] < after:
            continue
        for m in (n - 1, n, n + 1):
            window = tokens[i:i + m]
            if len(window) < m or m <= 0:
                continue
            score = difflib.SequenceMatcher(None, " ".join(window), " ".join(target)).ratio()
            if score > best[1]:
                end = words[i + m - 1][2]
                nxt = words[i + m][1] if i + m < len(words) else end + 1.0
                cut = end + min(0.25, max(0.03, (nxt - end) / 2))
                best = (cut, score)
    return best


def find_span(words, phrase, used):
    """Return (start_time, end_time, score) of the best match of the phrase outside the used spans."""
    target = norm(phrase)
    n = len(target)
    tokens = [w[0] for w in words]
    best = (None, None, 0.0)
    goal = " ".join(target)
    for i in range(len(words) - n + 1):
        if any(a <= words[i][1] < b for a, b in used):
            continue
        for m in (n - 1, n, n + 1):
            if m <= 0 or i + m > len(words):
                continue
            score = difflib.SequenceMatcher(None, " ".join(tokens[i:i + m]), goal).ratio()
            if score > best[2]:
                prev_end = words[i - 1][2] if i > 0 else 0.0
                nxt = words[i + m][1] if i + m < len(words) else words[i + m - 1][2] + 0.5
                start = words[i][1] - min(0.08, max(0.0, (words[i][1] - prev_end) / 2))
                end = words[i + m - 1][2] + min(0.10, max(0.0, (nxt - words[i + m - 1][2]) / 2))
                best = (start, end, score)
    return best


def load_drops(path, words):
    """Read the edit list and return the time spans to cut, in time order."""
    spans = []
    for line in Path(path).read_text(encoding="utf-8").splitlines():
        phrase = line.strip()
        if not phrase or phrase.startswith("#"):
            continue
        if "|||" in phrase:
            first, last = (part.strip() for part in phrase.split("|||", 1))
            a, _, s1 = find_span(words, first, spans)
            later = [w for w in words if a is not None and w[1] >= a]
            _, b, s2 = find_span(later, last, spans) if later else (None, None, 0.0)
            score = min(s1, s2)
        else:
            a, b, score = find_span(words, phrase, spans)
        if a is None or b is None or score < 0.85:
            print(f"drop phrase missing or unclear ({score:.2f}): {phrase[:70]!r}")
            continue
        print(f"drop {int(a // 60):02d}:{a % 60:05.2f} to {int(b // 60):02d}:{b % 60:05.2f} "
              f"({b - a:.1f} s, match {score:.2f}): {phrase[:60]!r}")
        spans.append((a, b))
    return sorted(spans)


def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        raise SystemExit("ffmpeg failed:\n" + " ".join(map(str, cmd)) + "\n" + r.stderr[-1500:])


def duration(path):
    r = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(path)],
                       capture_output=True, text=True)
    return float(r.stdout.strip())


def plan(kind, words, total, drops=()):
    """Return the pieces in order, each ('narration', start, end, pause) or ('insert', name).

    The pause is the silence added after a narration piece. It is used before an insert and is zero
    where a dropped phrase was cut out, so the speech closes up there.
    """
    events, after = [], 0.0
    for cue, name in CUES[kind]:
        cut, score = find_cue(words, cue, after=after)
        if cut is None or score < 0.8:
            print(f"cue missing or unclear ({score:.2f}): {cue!r}")
            continue
        print(f"cue {name} at {int(cut // 60):02d}:{cut % 60:05.2f} (match {score:.2f}): {cue!r}")
        events.append((cut, "insert", name))
        after = cut
    events += [(a, "drop", b) for a, b in drops]
    pieces, pos = [], 0.0
    for t, kind_, value in sorted(events, key=lambda e: e[0]):
        if t < pos:
            continue
        if kind_ == "insert":
            pieces += [("narration", pos, t, 0.35), ("insert", value)]
            pos = t
        else:
            if t - pos > 0.05:
                pieces.append(("narration", pos, t, 0.0))
            pos = value
    pieces.append(("narration", pos, total, 0.0))
    return pieces


def assemble_audio(src, pieces, out):
    with tempfile.TemporaryDirectory() as tmp:
        parts = []
        for i, piece in enumerate(pieces):
            part = Path(tmp) / f"p{i:02d}.wav"
            if piece[0] == "narration":
                _, a, b, pause = piece
                d = b - a
                af = f"aresample=48000,afade=t=in:st=0:d=0.02,afade=t=out:st={max(0.0, d - 0.03):.3f}:d=0.03"
                if pause:
                    af += f",apad=pad_dur={pause}"
                run(["ffmpeg", "-y", "-loglevel", "error", "-ss", f"{a:.3f}", "-t", f"{d:.3f}", "-i", str(src),
                     "-af", af, "-ac", "2", str(part)])
            else:
                run(["ffmpeg", "-y", "-loglevel", "error", "-i", need(INS / f"insert_{piece[1]}.wav"),
                     "-af", "aresample=48000,apad=pad_dur=0.45", "-ac", "2", str(part)])
            parts.append(part)
        lst = Path(tmp) / "list.txt"
        lst.write_text("".join(f"file '{p}'\n" for p in parts), encoding="utf-8")
        run(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", str(lst),
             "-af", "loudnorm=I=-16:TP=-1.5:LRA=11", "-ar", "48000", "-c:a", "aac", "-b:a", "192k", str(out)])


def assemble_video(src, pieces, out):
    with tempfile.TemporaryDirectory() as tmp:
        parts = []
        vf = (f"scale={W}:{H}:force_original_aspect_ratio=decrease,pad={W}:{H}:(ow-iw)/2:(oh-ih)/2:color=black,"
              f"setsar=1,fps={FPS}")
        for i, piece in enumerate(pieces):
            part = Path(tmp) / f"p{i:02d}.mp4"
            if piece[0] == "narration":
                _, a, b, _pause = piece
                d = b - a
                af = (f"aresample=48000,afade=t=in:st=0:d=0.02,afade=t=out:st={max(0.0, d - 0.03):.3f}:d=0.03,"
                      "volume=1.0")
                run(["ffmpeg", "-y", "-loglevel", "error", "-ss", f"{a:.3f}", "-t", f"{d:.3f}", "-i", str(src),
                     "-vf", vf, "-af", af, "-ac", "2",
                     "-c:v", "libx264", "-preset", "veryfast", "-crf", "19", "-pix_fmt", "yuv420p",
                     "-c:a", "aac", "-b:a", "192k", "-ar", "48000", str(part)])
            else:
                part = Path(need(INS / f"insert_{piece[1]}.mp4"))
            parts.append(part)
        lst = Path(tmp) / "list.txt"
        lst.write_text("".join(f"file '{p}'\n" for p in parts), encoding="utf-8")
        run(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", str(lst),
             "-af", "loudnorm=I=-16:TP=-1.5:LRA=11",
             "-c:v", "libx264", "-preset", "veryfast", "-crf", "19", "-pix_fmt", "yuv420p", "-r", str(FPS),
             "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-ac", "2", "-movflags", "+faststart", str(out)])


def main():
    if len(sys.argv) not in (5, 6) or sys.argv[1] not in CUES:
        raise SystemExit(__doc__)
    kind, src, words_path, out = sys.argv[1], Path(need(sys.argv[2])), need(sys.argv[3]), Path(sys.argv[4])
    out.parent.mkdir(parents=True, exist_ok=True)
    words = load_words(words_path)
    drops = load_drops(need(sys.argv[5]), words) if len(sys.argv) == 6 else []
    pieces = plan(kind, words, duration(src), drops)
    (assemble_audio if kind == "audio" else assemble_video)(src, pieces, out)
    print(f"wrote {out} ({duration(out) / 60:.1f} min)")


if __name__ == "__main__":
    main()
