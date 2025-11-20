
import streamlit as st
from resume_parser import extract_text_from_pdf, extract_skills
from job_recommender import get_jobs
from course_recommender import get_courses
from groq_api import get_career_advice

st.set_page_config(page_title="💼 AI Career Coach — Pro", layout="wide")
st.title("💼 AI Career Coach — Pro")

st.markdown(
    "Upload your resume (PDF). The app extracts skills, generates AI career advice, "
    "recommends jobs and courses. "
    
)

with st.sidebar:
    st.header("About")
    st.write("Pro demo: Groq + Streamlit + YouTube courses")
    
    st.write("GitHub: [https://github.com/ALWALA-KAVYA/ai-career-coach-pro]")

uploaded = st.file_uploader("Upload your Resume (PDF)", type=["pdf"])
job_text = st.text_area("Optional: paste a Job Description or target job title here")

if uploaded:
    with st.spinner("Parsing resume..."):
        try:
            resume_text = extract_text_from_pdf(uploaded)
        except Exception as e:
            st.error(f"Failed to parse resume: {e}")
            resume_text = ""

    st.subheader("📄 Resume Snippet")
    st.code(resume_text[:1200] + ("..." if len(resume_text) > 1200 else ""))

    skills = extract_skills(resume_text)
    st.subheader("🔎 Detected Skills / Keywords")
    if skills:
        for skill in skills:
            st.markdown(
                f"<span style='background-color:#90ee90;padding:3px;border-radius:5px'>{skill}</span>",
                unsafe_allow_html=True
            )
    else:
        st.write("No explicit skills detected. Add a short profile paragraph in the resume for better results.")

    # Career Advice
    if st.button("🎯 Get AI Career Advice"):
        with st.spinner("Calling Groq API for personalized advice..."):
            prompt = f"Analyze this resume and job text (if provided). Provide:\n" \
                     f"1) Match score (0-100)\n2) Missing/weak skills\n3) 30-day learning plan with free resources\n" \
                     f"4) Top 3 job roles to apply for\n\nResume:\n{resume_text}\n\nJob:\n{job_text}"
            advice = get_career_advice(prompt)
        with st.expander("🧠 Career Advice"):
            st.write(advice)

    # Job Recommendations
    if st.button("💼 Find Jobs (sample)"):
        st.subheader("💼 Job Recommendations")
        query = skills[0] if skills else (job_text or "Data Analyst")
        jobs = get_jobs(query)
        cols = st.columns(2)
        for idx, j in enumerate(jobs):
            with cols[idx % 2]:
                st.markdown(f"**{j}**")

    # Course Recommendations
    if st.button("🎓 Recommend Courses"):
        st.subheader("🎓 Course Recommendations")
        query = skills[0] if skills else (job_text or "python")
        courses = get_courses(query)
        cols = st.columns(2)
        for idx, c in enumerate(courses):
            with cols[idx % 2]:
                if isinstance(c, dict):
                    st.image(c.get("thumbnail"), width=200)
                    st.markdown(f"[{c.get('title')}]({c.get('video_url')})")
                else:
                    st.markdown(f"- {c}")

else:
    st.info("Upload a PDF resume (sample included) to begin.")
