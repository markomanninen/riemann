#!/usr/bin/env bash
# Full build: scenes -> interview clips -> assembly with narration -> music and effects mix.
# Inputs come from $RIEMANN_SOURCES (default <repo>/sources), output goes to $RIEMANN_BUILD (default <repo>/build).
set -euo pipefail
cd "$(dirname "$0")"
REPO="$(cd .. && pwd)"
BUILD="${RIEMANN_BUILD:-$REPO/build}"
OUT="${1:-$BUILD/Predicting_Primes.mp4}"
mkdir -p "$BUILD"
python3 render.py main all
python3 render.py ex all
python3 render.py cred all
python3 clips_c.py
python3 assemble.py "$BUILD/base.mp4"
python3 mix.py "$BUILD/base.mp4"
ffmpeg -v error -y -i "$BUILD/base.mp4" -i "$BUILD/audio/bed_music.wav" -i "$BUILD/audio/bed_sfx.wav" \
  -filter_complex "[0:a]aformat=channel_layouts=stereo[n];[n][1:a][2:a]amix=inputs=3:normalize=0,alimiter=limit=0.89[a]" \
  -map 0:v -map "[a]" -c:v copy -c:a aac -b:a 192k -shortest -movflags +faststart "$BUILD/final_tmp.mp4"
mv "$BUILD/final_tmp.mp4" "$OUT"
echo "Done: $OUT"
