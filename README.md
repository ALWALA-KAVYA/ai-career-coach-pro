
# AI Career Coach — Pro (Streamlit Cloud ready)

This repository contains a **Streamlit app** (Pro starter) that uses Groq for AI responses.
It is ready for deployment on **Streamlit Cloud** or **Hugging Face Spaces**.

## Quick start (local)
1. Create & activate venv:
   ```bash
   python -m venv venv
   source venv/bin/activate   # macOS/Linux
   venv\\Scripts\\activate    # Windows (PowerShell)
   ```
2. Install deps:
   ```bash
   pip install -r requirements.txt
   python -m spacy download en_core_web_sm
   ```
3. Set secrets locally (example for Linux/macOS):
   ```bash
   export GROQ_API_KEY="your_groq_key_here"
   export RAPIDAPI_KEY="your_rapidapi_key_here"   # optional for jobs
   ```
4. Run:
   ```bash
   streamlit run app.py
   ```

## Deploy to Streamlit Cloud
1. Push this repo to GitHub.
2. Create a new app on Streamlit Cloud and connect your repo.
3. Add secrets in the Streamlit app settings: `GROQ_API_KEY`, `RAPIDAPI_KEY` (optional).
4. Deploy and share the link.

