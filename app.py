
import streamlit as st
from resume_parser import extract_text_from_pdf, extract_skills
from job_recommender import get_jobs
from course_recommender import get_courses
from groq_api import get_career_advice

st.set_page_config(page_title="AI Career Coach — Pro", layout="wide")
st.title("💼 AI Career Coach — Pro (Groq)")

st.markdown(
    "Upload your resume (PDF). The app extracts skills, generates AI career advice, recommends jobs and courses. "
    "Set `GROQ_API_KEY` and `RAPIDAPI_KEY` as Streamlit secrets for full features."
)

with st.sidebar:
    st.header("About")
    st.write("Pro demo: Groq + Streamlit")
    st.write("Add keys in Settings → Secrets: GROQ_API_KEY, RAPIDAPI_KEY")

uploaded = st.file_uploader("Upload your Resume (PDF)", type=["pdf"])
job_text = st.text_area("Optional: paste a Job Description or target job title here")

if uploaded:
    with st.spinner("Parsing resume..."):
        try:
            resume_text = extract_text_from_pdf(uploaded)
        except Exception as e:
            st.error(f"Failed to parse resume: {e}")
            resume_text = ""

    st.subheader("📄 Resume (snippet)")
    st.code(resume_text[:1200] + ("..." if len(resume_text) > 1200 else ""))

    skills = extract_skills(resume_text)
    st.subheader("🔎 Detected skills / keywords")
    if skills:
        st.write(", ".join(skills))
    else:
        st.write("No explicit skills detected. Try adding a short profile paragraph to the resume.")

    if st.button("🎯 Get AI Career Advice"):
        with st.spinner("Calling Groq for personalized advice..."):
            prompt = f"Analyze this resume and the job text (if provided). Provide:\\n1) Match score (0-100)\\n2) Missing or weak skills\\n3) Structured 30-day learning plan with free resources\\n4) Top 3 job roles to apply for and suggested next steps.\\n\\nResume:\\n{resume_text}\\n\\nJob:\\n{job_text}"
            advice = get_career_advice(prompt)
        st.subheader("🧠 Career Advice (AI)")
        st.write(advice)

    if st.button("💼 Find Jobs (sample)"):
        st.subheader("💼 Job Recommendations")
        query = skills[0] if skills else (job_text or "Data Analyst")
        jobs = get_jobs(query)
        for j in jobs:
            st.write(f"- {j}")

    if st.button("🎓 Recommend Courses"):
        st.subheader("🎓 Course Recommendations")
        query = skills[0] if skills else (job_text or "python")
        courses = get_courses(query)
        for c in courses:
            st.write(f"- {c}")
else:
    st.info("Upload a PDF resume (sample included) to begin.")
