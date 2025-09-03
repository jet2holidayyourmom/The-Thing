import yaml
import os
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import re

# --- Load config ---
with open("config.yaml", "r") as f:
    config = yaml.safe_load(f)

api_key = config['youtube']['api_key']
channel_id = config['youtube']['channel_id']

# --- Read latest post from index.html ---
with open("index.html", "r") as f:
    content = f.read()

# Extract first paragraph for Short
text_match = re.search(r'<p>(.*?)</p>', content, re.DOTALL)
short_text = text_match.group(1) if text_match else "Daily conspiracy update!"

# --- Create placeholder video ---
video_file = "short.mp4"
if not os.path.exists(video_file):
    os.system(f"ffmpeg -f lavfi -i color=c=black:s=720x1280:d=30 -vf drawtext=\"fontfile=/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf:text='{short_text}':fontcolor=white:x=10:y=H/2\" {video_file}")

# --- Upload to YouTube ---
try:
    youtube = build("youtube", "v3", developerKey=api_key)

    request = youtube.videos().insert(
        part="snippet,status",
        body={
            "snippet": {
                "title": short_text[:100],
                "description": "Automated conspiracy theory short",
                "tags": ["conspiracy", "AI", "Shorts"],
                "categoryId": "27"
            },
            "status": {
                "privacyStatus": "public"
            }
        },
        media_body=video_file
    )
    response = request.execute()
    print("✅ Uploaded YouTube Short:", response["id"])
except HttpError as e:
    print("❌ YouTube upload failed:", e)
