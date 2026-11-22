"""Turn YouTube json3 subtitles into timestamped text lines, one line per caption window.

Usage:
  python3 scripts/subs_to_text.py SUBS_DIR OUT_DIR

Reads every <id>.en.json3 in SUBS_DIR (falling back to <id>.en-orig.json3) and writes OUT_DIR/<id>.txt
with lines of the form "[mm:ss] text". Consecutive windows are merged into lines of about ten seconds.
"""
import json
import sys
from pathlib import Path


def lines(path, span=10.0):
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    out, start, buf = [], None, []
    for ev in data.get("events", []):
        text = "".join(seg.get("utf8", "") for seg in ev.get("segs", []) or []).replace("\n", " ").strip()
        if not text:
            continue
        t = ev.get("tStartMs", 0) / 1000
        if start is None:
            start = t
        if t - start >= span and buf:
            out.append((start, " ".join(buf)))
            start, buf = t, []
        buf.append(text)
    if buf:
        out.append((start, " ".join(buf)))
    return out


def main():
    src, dst = Path(sys.argv[1]), Path(sys.argv[2])
    dst.mkdir(parents=True, exist_ok=True)
    ids = sorted({p.name.split(".")[0] for p in src.glob("*.json3")})
    for vid in ids:
        path = next((p for p in (src / f"{vid}.en.json3", src / f"{vid}.en-orig.json3") if p.exists()), None)
        if path is None:
            continue
        rows = lines(path)
        with open(dst / f"{vid}.txt", "w", encoding="utf-8") as f:
            for t, text in rows:
                m, s = divmod(int(t), 60)
                f.write(f"[{m:02d}:{s:02d}] {' '.join(text.split())}\n")
        print(vid, len(rows), "lines")


if __name__ == "__main__":
    main()
