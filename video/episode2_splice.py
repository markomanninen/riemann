"""Join a passage from one NotebookLM narration into another one.

Usage:
  python3 video/episode2_splice.py SPEC.json OUT.m4a

SPEC.json names a base narration and a donor narration, each with its Whisper transcript and an
optional edit list, the phrase of the base before which the passage goes, and the first and last
phrases of the passage in the donor:

  {"base":  {"audio": "...", "words": "...", "drop": "..."},
   "donor": {"audio": "...", "words": "...", "drop": "..."},
   "before": "first words of the base sentence that follows the passage",
   "from": "first words of the passage in the donor",
   "to": "last words of the passage in the donor"}

The result is a plain narration without inserts. The phrases of both edit lists are cut out on the
way. Transcribe the result again before placing inserts into it with episode2_assemble.py.
"""
import json
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from episode2_assemble import duration, find_span, load_drops, load_words, run  # noqa: E402
from paths import ROOT, need  # noqa: E402


def keep_ranges(a, b, drops):
    """The stretches of [a, b] that remain after the dropped spans are taken out."""
    out, pos = [], a
    for d0, d1 in drops:
        if d1 <= a or d0 >= b:
            continue
        if d0 - pos > 0.05:
            out.append((pos, d0))
        pos = max(pos, d1)
    if b - pos > 0.05:
        out.append((pos, b))
    return out


def load(side):
    audio = Path(need(ROOT / side["audio"]))
    words = load_words(need(ROOT / side["words"]))
    drops = load_drops(need(ROOT / side["drop"]), words) if side.get("drop") else []
    return audio, words, drops


def main():
    if len(sys.argv) != 3:
        raise SystemExit(__doc__)
    spec, out = json.loads(Path(need(sys.argv[1])).read_text(encoding="utf-8")), Path(sys.argv[2])
    base, bwords, bdrops = load(spec["base"])
    donor, dwords, ddrops = load(spec["donor"])
    at, _, s0 = find_span(bwords, spec["before"], [])
    start, _, s1 = find_span(dwords, spec["from"], [])
    _, end, s2 = find_span([w for w in dwords if start is not None and w[1] >= start], spec["to"], [])
    if None in (at, start, end) or min(s0, s1, s2) < 0.85:
        raise SystemExit(f"A phrase of the spec was not found (matches {s0:.2f}, {s1:.2f}, {s2:.2f}).")
    print(f"base is split at {at / 60:.2f} min, donor passage runs from {start / 60:.2f} to {end / 60:.2f} min")
    pieces = ([(base, a, b) for a, b in keep_ranges(0.0, at, bdrops)]
              + [(donor, a, b) for a, b in keep_ranges(start, end, ddrops)]
              + [(base, a, b) for a, b in keep_ranges(at, duration(base), bdrops)])
    out.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory() as tmp:
        parts = []
        for i, (src, a, b) in enumerate(pieces):
            part, d = Path(tmp) / f"p{i:03d}.wav", b - a
            af = f"aresample=48000,afade=t=in:st=0:d=0.02,afade=t=out:st={max(0.0, d - 0.03):.3f}:d=0.03"
            run(["ffmpeg", "-y", "-loglevel", "error", "-ss", f"{a:.3f}", "-t", f"{d:.3f}", "-i", str(src),
                 "-af", af, "-ac", "2", str(part)])
            parts.append(part)
        lst = Path(tmp) / "list.txt"
        lst.write_text("".join(f"file '{p}'\n" for p in parts), encoding="utf-8")
        run(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", str(lst),
             "-ar", "48000", "-c:a", "aac", "-b:a", "192k", str(out)])
    print(f"wrote {out} ({duration(out) / 60:.1f} min) from {len(pieces)} pieces")


if __name__ == "__main__":
    main()
