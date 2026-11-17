"""Transcribe an audio file into timestamped lines with Whisper turbo (sherpa-onnx) and Silero VAD.

Usage:
  python3 scripts/transcribe.py INPUT.wav OUTPUT.txt [--lang en] [--threads 2] [--limit SECONDS]

The input must be 16 kHz mono WAV, for example:
  ffmpeg -i narration.mp4 -ar 16000 -ac 1 narration.wav

Models are read from --models or $ASR_MODELS (default ~/asr_models), with this layout:
  <models>/sherpa-onnx-whisper-turbo/turbo-encoder.int8.onnx, turbo-decoder.int8.onnx, turbo-tokens.txt
  <models>/silero_vad.onnx
"""
import argparse, os, time
from pathlib import Path
import soundfile as sf
import sherpa_onnx as so

ap = argparse.ArgumentParser()
ap.add_argument("input"); ap.add_argument("output")
ap.add_argument("--lang", default="en"); ap.add_argument("--threads", type=int, default=2)
ap.add_argument("--limit", type=float, default=None, help="transcribe only the first N seconds")
ap.add_argument("--models", default=os.environ.get("ASR_MODELS", "~/asr_models"))
a = ap.parse_args()

M = Path(a.models).expanduser()
W = M / "sherpa-onnx-whisper-turbo"
for f in (W / "turbo-encoder.int8.onnx", W / "turbo-decoder.int8.onnx", W / "turbo-tokens.txt", M / "silero_vad.onnx"):
    if not f.exists(): raise SystemExit(f"Missing model file: {f}")
rec = so.OfflineRecognizer.from_whisper(encoder=str(W / "turbo-encoder.int8.onnx"), decoder=str(W / "turbo-decoder.int8.onnx"),
                                        tokens=str(W / "turbo-tokens.txt"), language=a.lang, task="transcribe", num_threads=a.threads)
cfg = so.VadModelConfig(); cfg.silero_vad.model = str(M / "silero_vad.onnx"); cfg.silero_vad.min_silence_duration = 0.35
cfg.silero_vad.max_speech_duration = 25; cfg.sample_rate = 16000
vad = so.VoiceActivityDetector(cfg, buffer_size_in_seconds=120)

x, sr = sf.read(a.input, dtype="float32")
if sr != 16000 or x.ndim != 1: raise SystemExit("Input must be 16 kHz mono WAV (see usage).")
if a.limit: x = x[:int(min(len(x) / sr, a.limit) * sr)]

out = open(a.output, "w"); t0 = time.time(); STEP = 512
def flush():
    while not vad.empty():
        seg = vad.front; s = rec.create_stream()
        lo = max(0, seg.start - int(.2 * sr)); hi = min(len(x), seg.start + len(seg.samples) + int(.5 * sr))
        s.accept_waveform(sr, x[lo:hi]); rec.decode_stream(s)
        m, sc = divmod(int(seg.start / sr), 60)
        out.write(f"[{m:02d}:{sc:02d}] {s.result.text.strip()}\n"); out.flush(); vad.pop()
for i in range(0, len(x), STEP):
    vad.accept_waveform(x[i:i + STEP]); flush()
vad.flush(); flush()
print("done", round(len(x) / sr), "s audio in", round(time.time() - t0), "s")
