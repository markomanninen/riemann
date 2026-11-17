"""Read or update the title, description, tags, category and language of a YouTube video.

Usage:
  python3 scripts/youtube_metadata.py VIDEO_ID                 # show the current metadata
  python3 scripts/youtube_metadata.py VIDEO_ID --apply FILE    # write metadata from a JSON file, then show the result
  python3 scripts/youtube_metadata.py VIDEO_ID --thumbnail IMG # set the custom thumbnail (JPEG or PNG, 1280x720, under 2 MB)
  python3 scripts/youtube_metadata.py --recent                 # list the latest uploads on the channel

The JSON file holds any of: title, description, tags, categoryId, defaultLanguage, defaultAudioLanguage.
Privacy status, made-for-kids and the altered-content setting are left unchanged.
Credentials come from ~/.config/youtube-upload/token.json (the same login the other upload scripts use).
"""
import argparse, json
from pathlib import Path
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

TOKEN = Path.home() / ".config" / "youtube-upload" / "token.json"
FIELDS = ("title", "description", "tags", "categoryId", "defaultLanguage", "defaultAudioLanguage")

ap = argparse.ArgumentParser()
ap.add_argument("video_id", nargs="?"); ap.add_argument("--apply", metavar="FILE")
ap.add_argument("--thumbnail", metavar="IMG"); ap.add_argument("--recent", action="store_true")
a = ap.parse_args()

creds = Credentials.from_authorized_user_file(str(TOKEN))
if creds.expired and creds.refresh_token:
    creds.refresh(Request()); TOKEN.write_text(creds.to_json())
yt = build("youtube", "v3", credentials=creds)

if a.recent:
    ch = yt.channels().list(part="contentDetails", mine=True).execute()["items"][0]
    up = ch["contentDetails"]["relatedPlaylists"]["uploads"]
    for it in yt.playlistItems().list(part="snippet,status", playlistId=up, maxResults=8).execute()["items"]:
        sn = it["snippet"]; print(sn["resourceId"]["videoId"], sn["publishedAt"], it["status"]["privacyStatus"], sn["title"])
    raise SystemExit
if not a.video_id: ap.error("VIDEO_ID is required")

def fetch():
    items = yt.videos().list(part="snippet,contentDetails,status", id=a.video_id).execute()["items"]
    if not items: raise SystemExit(f"No video {a.video_id} on this account")
    return items[0]

def show(v):
    s = v["snippet"]
    print(json.dumps({"title": s["title"], "duration": v["contentDetails"]["duration"], "privacy": v["status"]["privacyStatus"],
                      "madeForKids": v["status"].get("madeForKids"), "categoryId": s["categoryId"], "defaultLanguage": s.get("defaultLanguage"),
                      "defaultAudioLanguage": s.get("defaultAudioLanguage"), "tags": s.get("tags"), "description": s["description"]},
                     indent=1, ensure_ascii=False))

v = fetch()
if a.apply:
    new = json.loads(Path(a.apply).read_text())
    unknown = set(new) - set(FIELDS)
    if unknown: raise SystemExit(f"Unknown fields: {sorted(unknown)}")
    snippet = {k: v["snippet"][k] for k in FIELDS if k in v["snippet"]}
    snippet.update(new)
    yt.videos().update(part="snippet", body={"id": a.video_id, "snippet": snippet}).execute()
    v = fetch()
if a.thumbnail:
    from googleapiclient.http import MediaFileUpload
    r = yt.thumbnails().set(videoId=a.video_id, media_body=MediaFileUpload(a.thumbnail)).execute()
    print("thumbnail set:", r["items"][0]["maxres" if "maxres" in r["items"][0] else "high"]["url"])
show(v)
