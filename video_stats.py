import requests
import json
import os
from dotenv import load_dotenv

# 1️⃣ Load env FIRST
load_dotenv("./.env")
API_KEY = os.getenv("API_KEY")

CHANNEL_ID = "UCX6OQ3DkcsbYNE6H8uQQuVA"

def get_playlist_id():
    url = "https://youtube.googleapis.com/youtube/v3/channels"

    params = {
        "part": "contentDetails",
        "id": CHANNEL_ID,   # ✅ use channel ID
        "key": API_KEY
    }

    response = requests.get(url, params=params)
    data = response.json()

    print(json.dumps(data, indent=2))  # DEBUG

    if "items" not in data or not data["items"]:
        raise Exception("No items found. Check API key or channel ID")

    channel_items = data["items"][0]
    uploads_playlist_id = (
        channel_items["contentDetails"]["relatedPlaylists"]["uploads"]
    )

    print("Uploads Playlist ID:", uploads_playlist_id)
    return uploads_playlist_id


if __name__ == "__main__":
    get_playlist_id()
