#!/bin/bash
# One NotebookLM round for episode 2: upload the current scripts, generate the long audio and the
# explainer video, wait, download, transcribe with Whisper, check against the brief and place the inserts.
#
# Usage: scripts/episode2_run.sh VERSION          for example  scripts/episode2_run.sh v2
#        scripts/episode2_run.sh VERSION finish   skip upload and generation, and continue a round
#                                                 whose ids are already in runs.json
#
# Reads   docs/episode2/episode_script.md, video_script.md, notebooklm/audio_focus.md, video_focus.md
# Writes  sources/episode2/notebooklm/VERSION/   downloads and a copy of the uploaded texts
#         transcripts/episode2/VERSION/          Whisper transcripts and check reports
#         build/episode2/VERSION_*_with_inserts  narration with the reaction inserts in place
#         docs/episode2/notebooklm/runs.json     notebook, source and artifact ids of every round
set -euo pipefail
V="${1:?version name, for example v2}"
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"
NB="7672caa9-e12e-4761-9f49-d73d14226f73"
NLM="uvx -q --from notebooklm-mcp-cli nlm"
DOC="docs/episode2"
OUT="sources/episode2/notebooklm/$V"
TR="transcripts/episode2/$V"
mkdir -p "$OUT" "$TR" build/episode2

ids() { python3 -c "
import json, sys
r = [r for r in json.load(open('docs/episode2/notebooklm/runs.json'))['runs'] if r['version'] == sys.argv[1]][0]
print(r['audio']['artifact_id'], r['video']['artifact_id'])" "$V"; }

if [ "${2:-}" != "finish" ]; then
for f in "$DOC/notebooklm/audio_focus.md" "$DOC/notebooklm/video_focus.md"; do
  [ "$(wc -c < "$f")" -lt 5000 ] || { echo "$f is over 5000 characters"; exit 1; }
  if grep -n -i -E "do not|don't|never|must not|forbidden" "$f"; then echo "$f has a negative instruction"; exit 1; fi
done
cp "$DOC/episode_script.md" "$DOC/video_script.md" "$DOC/notebooklm/audio_focus.md" "$DOC/notebooklm/video_focus.md" "$OUT/"

$NLM login --check >/dev/null 2>&1 || $NLM login < /dev/null >/dev/null 2>&1

# The id is read from the line that names it, because the same output also prints the notebook id.
id_of() { grep -E "(Source|Artifact) ID" | grep -Eo '[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}' | tail -1; }
SA=$($NLM source add "$NB" --text "$(cat "$DOC/episode_script.md")" --title "episode2_script" --wait 2>&1 | id_of)
SV=$($NLM source add "$NB" --text "$(cat "$DOC/video_script.md")" --title "episode2_video_script" --wait 2>&1 | id_of)
echo "sources audio=$SA video=$SV"
AA=$($NLM audio create "$NB" --format deep_dive --length long --language en --focus "$(cat "$DOC/notebooklm/audio_focus.md")" --source-ids "$SA" --confirm 2>&1 | id_of)
AV=$($NLM video create "$NB" --format explainer --language en --focus "$(cat "$DOC/notebooklm/video_focus.md")" --source-ids "$SV" --confirm 2>&1 | id_of)
echo "artifacts audio=$AA video=$AV"

python3 - "$V" "$NB" "$SA" "$SV" "$AA" "$AV" <<'EOF'
import json, sys, datetime
from pathlib import Path
v, nb, sa, sv, aa, av = sys.argv[1:]
p = Path("docs/episode2/notebooklm/runs.json")
runs = json.loads(p.read_text()) if p.exists() else {"notebook_id": nb, "runs": []}
runs["runs"] = [r for r in runs["runs"] if r["version"] != v]
runs["runs"].append({"version": v, "started": datetime.datetime.now().isoformat(timespec="minutes"),
                     "audio": {"source_id": sa, "artifact_id": aa, "format": "deep_dive", "length": "long"},
                     "video": {"source_id": sv, "artifact_id": av, "format": "explainer"}})
p.write_text(json.dumps(runs, indent=1) + "\n")
EOF

fi

read -r AA AV <<< "$(ids)"
[ "$AA" != "$NB" ] && [ "$AV" != "$NB" ] && [ -n "$AA" ] && [ -n "$AV" ] || { echo "artifact ids for $V are missing in runs.json"; exit 1; }
scripts/nlm_wait_download.sh "$NB" "$AA" "$AV" "$OUT"

whisper() { uvx -q --from mlx-whisper mlx_whisper "$1" --model mlx-community/whisper-large-v3-turbo --language en \
  --word-timestamps True --output-format json --output-dir "$TR" --verbose False >/dev/null 2>&1; }
whisper "$OUT/audio.m4a"
ffmpeg -y -loglevel error -i "$OUT/video.mp4" -vn -ar 16000 -ac 1 "$TR/video.wav"
whisper "$TR/video.wav"; rm -f "$TR/video.wav"

python3 scripts/episode2_check.py audio "$TR/audio.json" "$TR/audio.txt" > "$TR/audio_check.txt"
python3 scripts/episode2_check.py video "$TR/video.json" "$TR/video.txt" > "$TR/video_check.txt"
python3 video/episode2_assemble.py audio "$OUT/audio.m4a" "$TR/audio.json" "build/episode2/${V}_audio_with_inserts.m4a" | tee "$TR/audio_assembly.txt"
python3 video/episode2_assemble.py video "$OUT/video.mp4" "$TR/video.json" "build/episode2/${V}_video_with_inserts.mp4" | tee "$TR/video_assembly.txt"
echo "round $V done"
