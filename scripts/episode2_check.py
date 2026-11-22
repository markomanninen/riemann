"""Check a Whisper transcript of an episode 2 narration against the brief.

Usage:
  python3 scripts/episode2_check.py audio WORDS.json [OUT.txt]
  python3 scripts/episode2_check.py video WORDS.json [OUT.txt]

WORDS.json is a Whisper transcript with segments. The script prints the length, the cue lines it finds,
the facts of the script that it finds or misses, how often the three status phrases occur, and every
sentence that states the result as settled. With OUT.txt it also writes a timestamped transcript.
A passing check here means the wording was found. Reading the transcript is still needed for errors.
"""
import json
import re
import sys
from pathlib import Path

CUES = {
    "audio": ["here is how the news sounded", "here is brian greene in his own words",
              "here are the voices of caution", "brian greene summed up the mood in three words"],
    "video": ["here is how the news sounded", "here are the voices of caution"],
}

# label -> regular expression that should match somewhere in the transcript
FACTS = {
    "date 20 November 2026": r"(20th|twentieth) of november|november (20|twentieth)",
    "Alpöge named": r"alp\w+",
    "Anthropic": r"anthropic",
    "note titled remark": r"\bremark\b",
    "key sentence": r"working with claude,? discovered a proof",
    "flew, danced, sparkled": r"flew,? and danced|danced,? and sparkled|flew and danced",
    "175,187 files": r"175[, ]?187",
    "17.4 million lines": r"17\.4 million",
    "818,755 theorems": r"818[, ]?755",
    "main file 12 lines": r"(12|twelve) lines",
    "250,000 pages": r"250[, ]?000|quarter of a million",
    "Mathlib": r"math ?lib",
    "Dirichlet L-functions": r"l[- ]functions?",
    "kernel": r"kernels?",
    "three standard axioms": r"three standard axioms",
    "nanoda": r"nano ?da|nanota|nanoda",
    "about 28 minutes": r"28 minutes",
    "con-leche": r"con[- ]?leche|conleche|con leche",
    "lean4lean": r"lean ?(4|four|for) ?lean",
    "Comparator": r"comparator",
    "Sutherland": r"sutherland",
    "mirror symmetry": r"mirror",
    "ceiling": r"ceiling",
    "12.2 million and 11": r"12\.2 million",
    "lattices": r"lattices?",
    "slope inequality": r"slope inequality",
    "Stepanov": r"stepanov|stepanoff|stepan",
    "theta lifts": r"theta lifts?",
    "Tao": r"\btao\b|terence",
    "Vakil and Masullo": r"vakil|masullo|vaquil|masulo",
    "all human, with no AI": r"all human",
    "Clay prize rules": r"clay",
    "scoreboard 1896": r"1896",
    "archive of 239 megabytes": r"239 megabytes",
    "141,928 files in Development": r"141[, ]?928",
    "folder Misc Lemmas Q": r"mis[ck]\w* lemmas",
    "file with 17,981 lines": r"17[, ]?981",
    "statement Every Character": r"every character",
    "the word sorry": r"sorry",
    "one divided by two is zero": r"(one|1) divided by (two|2)",
    "48 cores and 503 gigabytes": r"\b503\b",
    "closing thought": r"hard part (may|might)( just)? be reading",
}
AUDIO_ONLY = {"57,554 requests for more time": r"57[, ]?554", "about a terabyte": r"terabyte", "sealed container": r"sealed", "kernel bug proved a false statement": r"false statement", "declined, not rejected": r"declined", "only present Lean": r"only present lean", "timing is horrible": r"timing is horrible", "guided us": r"guided us to the right situation", "660,000 views": r"660[, ]?000", "Chebyshev 1850": r"1850", "versions 4.33.1 and 4.36.0": r"4\.36", "this episode": r"this episode", "Landau": r"landau", "61.6 gigabytes": r"61\.6", "1,468,418": r"1[, ]?468[, ]?418", "67 files": r"\b67 files",
              "Chowla and Selberg": r"chowla|selberg", "Pasten": r"pasten|pastin|pastén",
              "Conrad": r"conrad", "two years": r"two years",
              "final words": r"back when the reading is done"}
STATUS = ["claimed proof", "machine-checked", "still being digested", "deep dive", "according to the map", "according to the code", "according to the author"]
SETTLED = [r"\b(has|have) (now )?(been )?(proved|proven|solved)\b", r"\bis (now )?(proved|proven|solved)\b",
           r"\b(proved|solved|cracked) the riemann hypothesis\b", r"\bfinally (proved|solved)\b",
           r"\bconfirmed\b", r"\bwon the (prize|million)\b"]


def main():
    if len(sys.argv) < 3 or sys.argv[1] not in CUES:
        raise SystemExit(__doc__)
    kind = sys.argv[1]
    data = json.loads(Path(sys.argv[2]).read_text(encoding="utf-8"))
    segs = data["segments"]
    text = " ".join(s["text"].strip() for s in segs)
    low = re.sub(r"\s+", " ", text.lower().replace("-", " ").replace("’", "'"))
    low_plain = low.replace("here's", "here is").replace("brian green ", "brian greene ")
    total = segs[-1]["end"] if segs else 0
    print(f"length {total / 60:.1f} min, {len(text.split())} words")
    print(f"first words: {text[:110]!r}")
    print(f"last words:  {text[-140:]!r}")

    print("\ncue lines")
    for cue in CUES[kind]:
        pat = re.sub(r"[^a-z ]", "", cue)
        hit = pat in re.sub(r"[^a-z ]", "", low_plain)
        when = ""
        if hit:
            key = cue.split()[-2] + " " + cue.split()[-1]
            for s in segs:
                if key in re.sub(r"[^a-z ]", "", s["text"].lower()):
                    when = f" at {int(s['start'] // 60):02d}:{int(s['start'] % 60):02d}"
                    break
        print(f"  {'found  ' if hit else 'MISSING'} {cue}{when}")

    facts = dict(FACTS)
    if kind == "audio":
        facts.update(AUDIO_ONLY)
    missing = [k for k, pat in facts.items() if not re.search(pat, low)]
    print(f"\nfacts found {len(facts) - len(missing)} of {len(facts)}")
    for k in missing:
        print(f"  MISSING {k}")

    print("\nstatus phrases")
    for p in STATUS:
        print(f"  {low.count(p.replace('-', ' ')):3d} x {p}")

    print("\nsentences that state the result as settled")
    count = 0
    for s in segs:
        t = s["text"].strip()
        if any(re.search(p, t.lower()) for p in SETTLED):
            count += 1
            print(f"  [{int(s['start'] // 60):02d}:{int(s['start'] % 60):02d}] {t}")
    if not count:
        print("  none found")

    if len(sys.argv) > 3:
        out = Path(sys.argv[3])
        out.parent.mkdir(parents=True, exist_ok=True)
        with open(out, "w", encoding="utf-8") as f:
            buf, start = [], None
            for s in segs:
                if start is None:
                    start = s["start"]
                buf.append(s["text"].strip())
                if s["end"] - start >= 20:
                    f.write(f"[{int(start // 60):02d}:{int(start % 60):02d}] {' '.join(buf)}\n")
                    buf, start = [], None
            if buf:
                f.write(f"[{int(start // 60):02d}:{int(start % 60):02d}] {' '.join(buf)}\n")
        print(f"\ntranscript written to {out}")


if __name__ == "__main__":
    main()
