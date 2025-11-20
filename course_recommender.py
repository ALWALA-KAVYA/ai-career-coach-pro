
from googleapiclient.discovery import build
import streamlit as st

def get_youtube_courses(query, max_results=5):
    api_key = st.secrets["api_keys"].get("YOUTUBE_API_KEY")
    if not api_key:
        return "YOUTUBE_API_KEY not set in Streamlit secrets."

    youtube = build("youtube", "v3", developerKey=api_key)

    request = youtube.search().list(
        q=query,
        part="snippet",
        maxResults=max_results,
        type="video"
    )

    response = request.execute()

    results = []
    for item in response.get("items", []):
        results.append({
            "title": item["snippet"]["title"],
            "video_url": f"https://www.youtube.com/watch?v={item['id']['videoId']}",
            "thumbnail": item["snippet"]["thumbnails"]["high"]["url"]
        })

    return results
