"""Cut the reaction clips for episode 2 and join them into news-style inserts.

Usage:
  python3 video/episode2_collage.py          # build every insert
  python3 video/episode2_collage.py A C      # build chosen inserts only

Reads   sources/episode2/video/<youtube id>.mp4    full source videos
        sources/episode2/heads/<youtube id>.mp4    opening sections of further videos
        docs/episode2/inserts.json                 the cuts of every insert
Writes  build/episode2/clips/<insert><n>.mp4       one captioned clip per cut
        build/episode2/insert_<insert>.mp4         the joined insert, 1280x720, 30 fps
        build/episode2/insert_<insert>.wav         its sound, 48 kHz stereo

Each insert is a list of cuts. A cut names the source video, one or more time ranges in seconds,
the speaker and a second caption line. Cut points come from Whisper word timestamps, see
docs/episode2/production_sheet.md.

Every change of clip is marked for the eye and for the ear. An insert with several clips opens with
a title card and a whoosh, a red band sweeps across the picture with a short whoosh between two
clips, and a bell closes the insert before the narration returns.

An insert marked "mosaic" fills the screen step by step. The first clip plays full screen, the next
ones join it in a grid of 2 by 2, then 3 by 3, then 4 by 4. The newest clip has a red frame and the
sound, and it enters with a short white flash. The earlier clips keep running a little darker, each
from its own source video. Every clip keeps its words whole, and a soft whoosh marks every change.

These fields of a mosaic insert shape it:
  overlap               seconds in which a clip drops to its tail level after its last word
  tail_takes, tail_db   a clip stays audible under this many later clips, starting at this level
  speed_from, speed_to  the clips speed up from the first speed to the second one
  speed_curve           1 gives equal steps of speed, a larger number lets the steps grow towards the end
  finale                the last clip grows from the centre to full screen and plays at normal speed
  calm                  seconds after the start of that last clip by which all earlier voices are silent
  hold                  seconds that the last picture stays after the last word
  whoosh_db             level of the whoosh at every change
"""
import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from paths import FONTS, ROOT, SOURCES, build_dir, need  # noqa: E402

SRC = SOURCES / "episode2" / "video"
HEADS = SOURCES / "episode2" / "heads"
MUSIC = SOURCES / "music"
SPEC = ROOT / "docs" / "episode2" / "inserts.json"
OUT = build_dir("episode2")
CLIPS = build_dir("episode2/clips")
W, H, FPS = 1280, 720, 30
BOLD = FONTS / "Inter-SemiBold.ttf"
REG = FONTS / "Inter-Regular.ttf"
NAVY, RED = "0x0E1422", "0xD7263D"
SPEECH_DB = -19.0  # mean level that every clip is brought to


def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        raise SystemExit("ffmpeg failed:\n" + " ".join(map(str, cmd)) + "\n" + r.stderr[-1500:])
    return r


def esc(path):
    return str(path).replace(":", r"\:")


def textfile(tmp, name, text):
    p = Path(tmp) / name
    p.write_text(text, encoding="utf-8")
    return esc(p)


def duration(path):
    r = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(path)],
                       capture_output=True, text=True)
    return float(r.stdout.strip())


def mean_level(path, a, d):
    """Mean level of a range in dB, used to bring every clip to the same loudness."""
    r = subprocess.run(["ffmpeg", "-hide_banner", "-ss", f"{a:.3f}", "-t", f"{d:.3f}", "-i", str(path),
                        "-vn", "-af", "volumedetect", "-f", "null", "-"], capture_output=True, text=True)
    m = re.search(r"mean_volume: (-?[0-9.]+) dB", r.stderr)
    return float(m.group(1)) if m else SPEECH_DB


def caption_filter(tmp, tag, cut, banner):
    """Lower third with the speaker and a second line, a banner at top left and a date at top right."""
    who = textfile(tmp, f"{tag}_who.txt", cut["who"])
    where = textfile(tmp, f"{tag}_where.txt", cut["where"])
    ban = textfile(tmp, f"{tag}_ban.txt", banner)
    label_text = ("RECORDED EARLIER, " + cut["earlier"].upper()) if cut.get("earlier") else cut.get("date", "20 NOVEMBER 2026")
    label = textfile(tmp, f"{tag}_label.txt", label_text)
    bold, reg = esc(BOLD), esc(REG)
    parts = [
        f"drawbox=x=0:y={H - 150}:w={W}:h=150:color=black@0.62:t=fill",
        f"drawbox=x=0:y={H - 150}:w=10:h=150:color={RED}@1:t=fill",
        f"drawtext=fontfile='{bold}':textfile='{who}':fontcolor=white:fontsize=40:x=44:y={H - 128}",
        f"drawtext=fontfile='{reg}':textfile='{where}':fontcolor=0xE6E6E6:fontsize=26:x=44:y={H - 72}",
        f"drawtext=fontfile='{bold}':textfile='{ban}':fontcolor=white:fontsize=24:x=44:y=38:box=1:boxcolor={RED}@1:boxborderw=12",
    ]
    if cut.get("label") is not False:
        parts.append(f"drawtext=fontfile='{reg}':textfile='{label}':fontcolor=white:fontsize=20:x=w-tw-44:y=40:"
                     f"box=1:boxcolor=black@0.55:boxborderw=10")
    return ",".join(parts)


def encode(args, out):
    run(["ffmpeg", "-y", "-loglevel", "error", *args, "-ac", "2", "-ar", "48000", "-r", str(FPS),
         "-c:v", "libx264", "-preset", "veryfast", "-crf", "18", "-pix_fmt", "yuv420p",
         "-c:a", "aac", "-b:a", "192k", str(out)])


def cut_clip(tmp, tag, cut, banner):
    """Render one cut, which may join several ranges of the same source, to a uniform captioned clip."""
    src = need((HEADS if cut.get("head") else SRC) / f"{cut['id']}.mp4")
    parts = []
    for i, (a, b) in enumerate(cut["ranges"]):
        part = Path(tmp) / f"{tag}_{i}.mp4"
        d = b - a
        gain = max(-12.0, min(18.0, SPEECH_DB - mean_level(src, a, d)))
        vf = (f"scale={W}:{H}:force_original_aspect_ratio=decrease,pad={W}:{H}:(ow-iw)/2:(oh-ih)/2:color=black,"
              f"setsar=1,fps={FPS}," + caption_filter(tmp, f"{tag}_{i}", cut, banner))
        for _ in range(3):
            af = (f"aresample=48000,volume={gain:.1f}dB,alimiter=limit=0.89,"
                  f"afade=t=in:st=0:d=0.03,afade=t=out:st={max(0.0, d - 0.05):.3f}:d=0.05")
            encode(["-ss", f"{a:.3f}", "-i", src, "-t", f"{d:.3f}", "-vf", vf, "-af", af], part)
            # The limiter lowers the level of speech with strong peaks, so measure again and add the rest.
            short = SPEECH_DB - mean_level(part, 0, d)
            if short < 1.0:
                break
            gain += short
        parts.append(part)
    out = CLIPS / f"{tag}.mp4"
    join(tmp, parts, out)
    return out


def effect(pattern, start, length, gain_db):
    """Input arguments and an audio filter for a stretch of a sound effect, or silence when it is missing."""
    found = sorted(MUSIC.glob(pattern))
    if not found:
        return ["-f", "lavfi", "-t", f"{length}", "-i", "anullsrc=r=48000:cl=stereo"], "aresample=48000"
    fade = min(0.12, length / 3)
    af = (f"aresample=48000,volume={gain_db}dB,afade=t=out:st={length - fade:.3f}:d={fade:.3f},"
          f"apad=whole_dur={length}")
    return ["-ss", f"{start}", "-t", f"{length}", "-i", str(found[0])], af


def bumper(tmp, tag, title, sub):
    """Title card with a whoosh that opens an insert."""
    out, d = Path(tmp) / f"{tag}_bumper.mp4", 1.3
    t1, t2 = textfile(tmp, f"{tag}_b1.txt", title), textfile(tmp, f"{tag}_b2.txt", sub)
    vf = ",".join([
        f"drawbox=x=0:y={H // 2 - 70}:w={W}:h=6:color={RED}@1:t=fill",
        f"drawtext=fontfile='{esc(BOLD)}':textfile='{t1}':fontcolor=white:fontsize=72:x=(w-tw)/2:y={H // 2 - 40}",
        f"drawtext=fontfile='{esc(REG)}':textfile='{t2}':fontcolor=0xD0D4DA:fontsize=30:x=(w-tw)/2:y={H // 2 + 56}",
        "fade=t=in:st=0:d=0.15",
    ])
    sound, af = effect("Low_soft_whoosh*", 0.0, d, -2)
    encode(["-f", "lavfi", "-t", f"{d}", "-i", f"color=c={NAVY}:s={W}x{H}:r={FPS}", *sound,
            "-vf", vf, "-af", af, "-t", f"{d}"], out)
    return out


def transition(tmp, tag, d):
    """A red band sweeps across a dark card while the loud part of the whoosh plays."""
    out, band = Path(tmp) / f"{tag}_transition.mp4", 380
    sound, af = effect("Low_soft_whoosh*", 0.08, d, -3)
    run(["ffmpeg", "-y", "-loglevel", "error",
         "-f", "lavfi", "-t", f"{d}", "-i", f"color=c={NAVY}:s={W}x{H}:r={FPS}",
         "-f", "lavfi", "-t", f"{d}", "-i", f"color=c={RED}:s={band}x{H}:r={FPS}", *sound,
         "-filter_complex", f"[0:v][1:v]overlay=x='-{band}+({W}+{band})*t/{d}':y=0[v];[2:a]{af}[a]",
         "-map", "[v]", "-map", "[a]", "-t", f"{d}", "-ac", "2", "-ar", "48000", "-r", str(FPS),
         "-c:v", "libx264", "-preset", "veryfast", "-crf", "18", "-pix_fmt", "yuv420p",
         "-c:a", "aac", "-b:a", "192k", str(out)])
    return out


def sting(tmp, tag):
    """A bell over a fading card that closes an insert and hands back to the narration."""
    out, d = Path(tmp) / f"{tag}_sting.mp4", 0.9
    sound, af = effect("Single_soft_glass*", 0.33, d, 14)
    vf = f"drawbox=x=0:y={H // 2 - 3}:w={W}:h=6:color={RED}@1:t=fill,fade=t=out:st=0.35:d=0.5"
    encode(["-f", "lavfi", "-t", f"{d}", "-i", f"color=c={NAVY}:s={W}x{H}:r={FPS}", *sound,
            "-vf", vf, "-af", af, "-t", f"{d}"], out)
    return out


GRID_STEPS = [(1, 1), (4, 2), (9, 3), (16, 4)]  # up to this many clips share an n by n grid
ZOOM = 0.45  # seconds in which a closing clip grows to full screen
TILE_STYLE = {1: dict(name=40, where=26, strip=150, pad=44, border=6),
              2: dict(name=24, where=16, strip=76, pad=18, border=5),
              3: dict(name=18, where=12, strip=56, pad=12, border=4),
              4: dict(name=14, where=0, strip=36, pad=9, border=3)}


def grid_for(k):
    for limit, n in GRID_STEPS:
        if k <= limit:
            return n
    raise SystemExit("A mosaic holds at most 16 clips.")


def take_speeds(n, first, last, curve=1.0):
    """Playback speed of every clip, with the last clip at speed 1.

    The speed rises from `first` to `last`. With a curve of 1 every step is equally large, and with a
    larger curve the steps grow towards the end, so the speeding up itself gets faster.
    """
    if n <= 2:
        return [first, 1.0][:n]
    return [first + (last - first) * (k / (n - 2)) ** curve for k in range(n - 1)] + [1.0]


def tile_filter(tmp, tag, cut, n, state, speed=1.0, flash=None):
    """Filter for one tile of an n by n grid. The state is 'active', 'past' or 'final'."""
    cw, ch = W // n, H // n
    tw, th = (W, H) if n == 1 else (cw - 4, ch - 4)
    st = TILE_STYLE[n]
    who = textfile(tmp, f"{tag}_who.txt", cut["who"])
    parts = [f"setpts=PTS/{speed:.4f}"] if abs(speed - 1.0) > 0.001 else []
    parts += [f"scale={tw}:{th}:force_original_aspect_ratio=decrease",
              f"pad={tw}:{th}:(ow-iw)/2:(oh-ih)/2:color=black", "setsar=1", f"fps={FPS}:start_time=0"]
    if state == "past":
        parts.append("eq=brightness=-0.14:saturation=0.6")
    if (state == "active" and n > 1) if flash is None else flash:
        parts.append("fade=t=in:st=0:d=0.16:color=white")
    if state == "active":
        parts.append(f"drawbox=x=0:y={th - st['strip']}:w={tw}:h={st['strip']}:color=black@0.62:t=fill")
        name_y = th - st["strip"] + max(4, (st["strip"] - st["name"] - (st["where"] + 8 if st["where"] else 0)) // 2)
        parts.append(f"drawtext=fontfile='{esc(BOLD)}':textfile='{who}':fontcolor=white:fontsize={st['name']}:"
                     f"x={st['pad']}:y={name_y}")
        if st["where"]:
            where = textfile(tmp, f"{tag}_where.txt", cut["where"])
            parts.append(f"drawtext=fontfile='{esc(REG)}':textfile='{where}':fontcolor=0xE6E6E6:"
                         f"fontsize={st['where']}:x={st['pad']}:y={name_y + st['name'] + 8}")
        parts.append(f"drawbox=x=0:y=0:w={tw}:h={th}:color={RED}@1:t={st['border']}")
    else:
        size = max(11, int(st["name"] * 0.8))
        parts.append(f"drawtext=fontfile='{esc(BOLD)}':textfile='{who}':fontcolor=white:fontsize={size}:"
                     f"x={st['pad']}:y={th - size - st['pad']}:box=1:boxcolor=black@0.55:boxborderw=5")
    return ",".join(parts)


def mosaic_segment(tmp, tag, cuts, tiles, shown, active, clock, seg_clock, seg_dur, speed, spec, closing=False):
    """Render one step of the mosaic, with the first `shown` clips on screen.

    `tiles` clips have a tile when the mosaic is full. `clock` gives the start of every clip on the
    clock of the source videos and `seg_clock` the start of this step on it, so every tile goes on
    from the place its source video had reached in the step before. `speed` is the playback speed of
    this step. With `closing`, the clip after the tiles grows from the centre of the mosaic to full screen.
    """
    n, final_n = grid_for(shown), grid_for(tiles)
    cw, ch = W // n, H // n
    inputs = ["-f", "lavfi", "-t", f"{seg_dur:.3f}", "-i", f"color=c={NAVY}:s={W}x{H}:r={FPS}"]
    chains, last = [], "0:v"
    used = max(0, tiles - n * (n - 1))  # tiles in the last row of the full mosaic
    if n == final_n and used < n:
        # the cells that stay free in the last row carry the title of the insert
        x0, y0, pw = used * cw, (n - 1) * ch, (n - used) * cw
        t1 = textfile(tmp, f"{tag}_p1.txt", spec["bumper"][0])
        t2 = textfile(tmp, f"{tag}_p2.txt", spec["bumper"][1])
        chains.append(f"[0:v]drawbox=x={x0 + 24}:y={y0 + 40}:w={pw - 48}:h=4:color={RED}@1:t=fill,"
                      f"drawtext=fontfile='{esc(BOLD)}':textfile='{t1}':fontcolor=white:fontsize=46:"
                      f"x={x0}+({pw}-tw)/2:y={y0 + 62},"
                      f"drawtext=fontfile='{esc(REG)}':textfile='{t2}':fontcolor=0xD0D4DA:fontsize=20:"
                      f"x={x0}+({pw}-tw)/2:y={y0 + 122}[panel]")
        last = "panel"
    for i in range(shown):
        cut = cuts[i]
        src = need((HEADS if cut.get("head") else SRC) / f"{cut['id']}.mp4")
        offset = cut["ranges"][0][0] + (seg_clock - clock[i])
        inputs += ["-ss", f"{offset:.3f}", "-t", f"{seg_dur * speed + 0.3:.3f}", "-i", src]
        state = "active" if i == active else ("past" if active is not None or closing else "final")
        chains.append(f"[{i + 1}:v]{tile_filter(tmp, f'{tag}_{i}', cut, n, state, speed)}[t{i}]")
        x, y = ((0, 0) if n == 1 else ((i % n) * cw + 2, (i // n) * ch + 2))
        chains.append(f"[{last}][t{i}]overlay={x}:{y}:eof_action=repeat[o{i}]")
        last = f"o{i}"
    if closing:
        cut = cuts[tiles]
        src = need((HEADS if cut.get("head") else SRC) / f"{cut['id']}.mp4")
        inputs += ["-ss", f"{cut['ranges'][0][0]:.3f}", "-t", f"{seg_dur + 0.3:.3f}", "-i", src]
        x0, y0 = (W - cw) // 2, (H - ch) // 2  # the closing clip starts at the size of a tile in the centre
        left = f"pow(1-min(t/{ZOOM:.2f},1),3)"  # share of the way that is still ahead, from 1 down to 0
        chains.append(f"[{shown + 1}:v]{tile_filter(tmp, f'{tag}_closing', cut, 1, 'active', flash=False)},"
                      f"scale=w='2*trunc(({W}-{W - cw}*{left})/2)':h='2*trunc(({H}-{H - ch}*{left})/2)':"
                      f"eval=frame[closing]")
        chains.append(f"[{last}][closing]overlay=x='{x0}*{left}':y='{y0}*{left}':eof_action=repeat[oc]")
        last = "oc"
    out = Path(tmp) / f"{tag}.mp4"
    run(["ffmpeg", "-y", "-loglevel", "error", *inputs, "-filter_complex", ";".join(chains), "-map", f"[{last}]",
         "-t", f"{seg_dur:.3f}", "-an", "-r", str(FPS), "-c:v", "libx264", "-preset", "veryfast", "-crf", "18",
         "-pix_fmt", "yuv420p", str(out)])
    return out


def mosaic_audio(tmp, tag, cuts, starts, speeds, total, spec):
    """The sound of the mosaic.

    Every clip plays its words at full level and at the speed of its step. After its last word the
    clip drops to the tail level within the overlap time and then fades out under the next clips.
    With a closing clip, all tails are silent shortly after it starts.
    """
    n = len(cuts)
    duck = spec.get("overlap", 0.25)
    tail_takes = spec.get("tail_takes", 0)
    level = 10 ** (spec.get("tail_db", -12.0) / 20)
    closing = bool(spec.get("finale"))
    inputs, chains, labels = [], [], []
    for i, cut in enumerate(cuts):
        src = need((HEADS if cut.get("head") else SRC) / f"{cut['id']}.mp4")
        a, b = cut["ranges"][0]
        d, v = b - a, speeds[i]
        played = d / v
        if i == n - 1:
            tail = max(0.12, total - (starts[i] + played)) if closing else 0.12
        else:
            later = i + 1 + tail_takes
            stop = starts[later] if later < n - 1 else starts[-1] + (spec.get("calm", 0.5) if closing else duck)
            tail = max(duck, stop - (starts[i] + played))
        if i == n - 1 or tail <= duck + 0.02:
            shape = f"afade=t=out:st={played:.3f}:d={tail:.3f}"
        else:
            shape = (f"asetnsamples=n=256,volume='if(lt(t,{played:.3f}),1,if(lt(t,{played + duck:.3f}),"
                     f"1-{1 - level:.4f}*(t-{played:.3f})/{duck:.3f},"
                     f"{level:.4f}*max(0,1-(t-{played + duck:.3f})/{tail - duck:.3f})))':eval=frame")
        tempo = f"atempo={v:.4f}," if abs(v - 1.0) > 0.001 else ""
        wav = Path(tmp) / f"{tag}_a{i}.wav"
        gain = max(-12.0, min(18.0, SPEECH_DB - mean_level(src, a, d)))
        for _ in range(3):
            run(["ffmpeg", "-y", "-loglevel", "error", "-ss", f"{a:.3f}", "-t", f"{d + tail * v + 0.1:.3f}", "-i", src,
                 "-vn", "-af", f"aresample=48000,volume={gain:.1f}dB,alimiter=limit=0.89:level=disabled,{tempo}"
                               f"afade=t=in:st=0:d=0.04,{shape}",
                 "-t", f"{played + tail:.3f}", "-ac", "2", str(wav)])
            short = SPEECH_DB - mean_level(wav, 0, played)
            if short < 1.0:
                break
            gain += short
        inputs += ["-i", str(wav)]
        ms = int(starts[i] * 1000)
        chains.append(f"[{len(labels)}:a]adelay={ms}|{ms}[s{i}]")
        labels.append(f"[s{i}]")
    whoosh = sorted(MUSIC.glob("Low_soft_whoosh*"))
    if whoosh:
        for i in range(1, n):
            inputs += ["-ss", "0.02", "-t", "0.5", "-i", str(whoosh[0])]
            ms = max(0, int((starts[i] - 0.25) * 1000))
            chains.append(f"[{len(labels)}:a]aresample=48000,volume={spec.get('whoosh_db', -5.0):.1f}dB,"
                          f"afade=t=out:st=0.35:d=0.15,adelay={ms}|{ms}[w{i}]")
            labels.append(f"[w{i}]")
    out = Path(tmp) / f"{tag}_audio.wav"
    chains.append(f"{''.join(labels)}amix=inputs={len(labels)}:normalize=0:dropout_transition=0,"
                  f"alimiter=limit=0.89:level=disabled,apad=whole_dur={total:.3f}[mix]")
    run(["ffmpeg", "-y", "-loglevel", "error", *inputs, "-filter_complex", ";".join(chains), "-map", "[mix]",
         "-t", f"{total:.3f}", "-ar", "48000", "-ac", "2", str(out)])
    return out


def mosaic_timeline(spec):
    """Start, length on screen and speed of every clip of a mosaic, and the length of the whole mosaic."""
    cuts = spec["cuts"]
    lengths = [c["ranges"][0][1] - c["ranges"][0][0] for c in cuts]
    closing = bool(spec.get("finale"))
    speeds = take_speeds(len(cuts), spec.get("speed_from", 1.0), spec.get("speed_to", 1.0),
                         spec.get("speed_curve", 1.0))
    if not closing:
        speeds[-1] = spec.get("speed_to", 1.0)
    played = [d / v for d, v in zip(lengths, speeds)]
    starts = [sum(played[:k]) for k in range(len(cuts))]
    clock = [sum(lengths[:k]) for k in range(len(cuts))]
    hold = spec.get("hold", 0.6 if closing else 1.6)
    return dict(lengths=lengths, speeds=speeds, played=played, starts=starts, clock=clock,
                end=starts[-1] + played[-1], total=starts[-1] + played[-1] + hold, hold=hold, closing=closing)


def build_mosaic(name, spec):
    cuts = spec["cuts"]
    if any(len(c["ranges"]) != 1 for c in cuts):
        raise SystemExit("Every clip of a mosaic has one time range.")
    tl = mosaic_timeline(spec)
    starts, clock, played, speeds, closing = tl["starts"], tl["clock"], tl["played"], tl["speeds"], tl["closing"]
    tiles = len(cuts) - 1 if closing else len(cuts)
    with tempfile.TemporaryDirectory() as tmp:
        segs = []
        for k in range(tiles):
            segs.append(mosaic_segment(tmp, f"{name}_seg{k:02d}", cuts, tiles, k + 1, k, clock, clock[k],
                                       played[k], speeds[k], spec))
        if closing:
            # the closing clip grows to full screen over the full mosaic and plays at normal speed
            segs.append(mosaic_segment(tmp, f"{name}_closing", cuts, tiles, tiles, None, clock, clock[-1],
                                       played[-1] + tl["hold"], 1.0, spec, closing=True))
        else:
            segs.append(mosaic_segment(tmp, f"{name}_hold", cuts, tiles, tiles, None, clock,
                                       clock[-1] + tl["lengths"][-1], tl["hold"], 1.0, spec))
        lst = Path(tmp) / "mosaic_list.txt"
        lst.write_text("".join(f"file '{p}'\n" for p in segs), encoding="utf-8")
        silent = Path(tmp) / "mosaic_video.mp4"
        run(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", str(lst),
             "-an", "-r", str(FPS), "-c:v", "libx264", "-preset", "veryfast", "-crf", "18", "-pix_fmt", "yuv420p",
             str(silent)])
        sound = mosaic_audio(tmp, name, cuts, starts, speeds, tl["total"], spec)
        mosaic = Path(tmp) / "mosaic.mp4"
        encode(["-i", str(silent), "-i", str(sound), "-map", "0:v", "-map", "1:a", "-t", f"{tl['total']:.3f}"], mosaic)
        parts = ([bumper(tmp, name, *spec["bumper"])] if spec.get("bumper") else []) + [mosaic]
        if spec.get("sting"):
            parts.append(sting(tmp, name))
        out = OUT / f"insert_{name}.mp4"
        join(tmp, parts, out)
        run(["ffmpeg", "-y", "-loglevel", "error", "-i", str(out), "-vn", "-ar", "48000", "-ac", "2",
             str(OUT / f"insert_{name}.wav")])
    print(f"insert {name}: mosaic of {len(cuts)} clips, {tl['end']:.1f} s of clips, {duration(out):.1f} s in all -> {out}")
    for i, c in enumerate(cuts):
        print(f"   {starts[i]:5.1f} s  {played[i]:4.1f} s  speed {speeds[i]:.2f}  {c['who']}")


def join(tmp, parts, out):
    """Join uniform clips with hard cuts."""
    lst = Path(tmp) / (out.stem + "_list.txt")
    lst.write_text("".join(f"file '{p}'\n" for p in parts), encoding="utf-8")
    encode(["-f", "concat", "-safe", "0", "-i", str(lst)], out)


def build(name, spec):
    if not spec["cuts"]:
        raise SystemExit(f"Insert {name} has no cuts.")
    if spec.get("mosaic"):
        return build_mosaic(name, spec)
    with tempfile.TemporaryDirectory() as tmp:
        clips = [cut_clip(tmp, f"{name}{n + 1}", cut, spec["banner"]) for n, cut in enumerate(spec["cuts"])]
        parts = [bumper(tmp, name, *spec["bumper"])] if spec.get("bumper") else []
        swipe = transition(tmp, name, spec["transition"]) if spec.get("transition") else None
        for n, clip in enumerate(clips):
            if n and swipe:
                parts.append(swipe)
            parts.append(clip)
        if spec.get("sting"):
            parts.append(sting(tmp, name))
        out = OUT / f"insert_{name}.mp4"
        join(tmp, parts, out)
        run(["ffmpeg", "-y", "-loglevel", "error", "-i", str(out), "-vn", "-ar", "48000", "-ac", "2",
             str(OUT / f"insert_{name}.wav")])
    total = sum(duration(c) for c in clips)
    print(f"insert {name}: {len(clips)} cuts, {total:.1f} s of clips, {duration(out):.1f} s in all -> {out}")
    for c, cut in zip(clips, spec["cuts"]):
        print(f"   {c.name} {duration(c):4.1f} s  {cut['who']}")


def main():
    inserts = json.loads(Path(need(SPEC)).read_text(encoding="utf-8"))
    names = [a.upper() for a in sys.argv[1:]] or list(inserts)
    for n in names:
        if n not in inserts:
            raise SystemExit(f"Unknown insert {n}. Known inserts are {', '.join(inserts)}.")
        build(n, inserts[n])


if __name__ == "__main__":
    main()
