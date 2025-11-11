
import requests

def get_courses(keyword):
    try:
        url = f"https://api.coursera.org/api/courses.v1?q=search&query={keyword}"
        r = requests.get(url, timeout=10)
        r.raise_for_status()
        data = r.json()
        courses = [e.get('name','Unnamed Course') for e in data.get('elements',[])]
        return courses[:8] if courses else ["No courses found."]
    except Exception as e:
        return [f"Course API error: {e}"]
