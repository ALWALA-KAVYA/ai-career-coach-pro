
import requests
import streamlit as st

def get_courses(topic):
    """
    Fetch course recommendations using Udemy Course Scraper API (RapidAPI).
    Uses RAPIDAPI_KEY stored in Streamlit Secrets.
    """

    # Get API key from Streamlit secrets
    api_key = st.secrets["api_keys"].get("RAPIDAPI_KEY")

    if not api_key:
        return "RAPIDAPI_KEY not set. Add it in Streamlit secrets."

    # Udemy Search API endpoint
    url = "https://udemy-course-scrapper.p.rapidapi.com/search"

    query_params = {"query": topic}

    headers = {
        "x-rapidapi-key": api_key,
        "x-rapidapi-host": "udemy-course-scrapper.p.rapidapi.com"
    }

    try:
        response = requests.get(url, headers=headers, params=query_params, timeout=10)
        response.raise_for_status()

        data = response.json()

        # Extract course list
        if "results" in data and len(data["results"]) > 0:
            courses = []
            for item in data["results"][:6]:  # limit to 6 results
                courses.append({
                    "title": item.get("title", "No Title"),
                    "url": item.get("url", "#"),
                    "rating": item.get("rating", "N/A"),
                    "price": item.get("price", "N/A")
                })
            return courses
        else:
            return []

    except Exception as e:
        return f"Course API error: {e}"

