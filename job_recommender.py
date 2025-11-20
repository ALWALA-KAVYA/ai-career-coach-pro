
import os, requests
import streamlit as st

def get_jobs(query):
    rapid_key = st.secrets["api_keys"]["RAPIDAPI_KEY"]
    if not rapid_key:
        return ["RAPIDAPI_KEY not set. Add it to enable live job search (optional)."]
    url = "https://jsearch.p.rapidapi.com/search"
    headers = {
        "X-RapidAPI-Key": rapid_key,
        "X-RapidAPI-Host": "jsearch.p.rapidapi.com"
    }
    params = {"query": query, "num_pages":"1"}
    try:
        r = requests.get(url, headers=headers, params=params, timeout=10)
        r.raise_for_status()
        data = r.json()
        items = data.get("data", [])
        jobs = [f"{it.get('job_title','')} at {it.get('employer_name','')}" for it in items]
        return jobs[:8] if jobs else ["No jobs found for this query."]
    except Exception as e:
        return [f"Job API error: {e}"]
