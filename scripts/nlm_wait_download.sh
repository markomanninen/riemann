#!/bin/bash
# Wait for one NotebookLM audio artifact and one video artifact to finish, then download both.
# Usage: scripts/nlm_wait_download.sh NOTEBOOK_ID AUDIO_ARTIFACT_ID VIDEO_ARTIFACT_ID OUT_DIR
# Prints one line per state change and exits 0 when both files are on disk, 1 on failure or timeout.
set -u
NB="$1"; AUD="$2"; VID="$3"; OUT="$4"
NLM="uvx -q --from notebooklm-mcp-cli nlm"
mkdir -p "$OUT"
state() { $NLM studio status "$NB" 2>/dev/null | python3 -c "
import json, sys
want = sys.argv[1]
try:
    for a in json.load(sys.stdin):
        if a.get('artifact_id') == want:
            print(a.get('status')); break
    else:
        print('missing')
except Exception as e:
    print('error')
" "$1"; }
last=""
for i in $(seq 1 90); do
  a=$(state "$AUD"); v=$(state "$VID")
  now="audio=$a video=$v"
  [ "$now" != "$last" ] && echo "$(date +%H:%M:%S) $now" && last="$now"
  if [ "$a" = "completed" ] && [ ! -s "$OUT/audio.m4a" ]; then $NLM download audio "$NB" --id "$AUD" -o "$OUT/audio.m4a" >/dev/null 2>&1 && echo "audio downloaded"; fi
  if [ "$v" = "completed" ] && [ ! -s "$OUT/video.mp4" ]; then $NLM download video "$NB" --id "$VID" -o "$OUT/video.mp4" >/dev/null 2>&1 && echo "video downloaded"; fi
  case "$a$v" in *failed*) echo "generation failed"; exit 1;; esac
  if [ -s "$OUT/audio.m4a" ] && [ -s "$OUT/video.mp4" ]; then ls -la "$OUT"; exit 0; fi
  sleep 60
done
echo "timeout"; exit 1
