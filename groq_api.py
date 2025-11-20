
import os
import streamlit as st
try:
    from groq import Groq
except Exception:
    Groq = None

def _get_client():
    key = st.secrets["api_keys"]["GROQ_API_KEY"]

    if not key:
        return None
    if Groq is None:
        return None
    return Groq(api_key=key)

def get_career_advice(prompt_text):
    client = _get_client()
    if not client:
        return "GROQ_API_KEY not found. Add your key in environment variables or Streamlit secrets."
    try:
        resp = client.chat.completions.create(
            messages=[{"role": "user", "content": prompt_text}],
            model="mixtral-8x7b"
        )
        # parse common response structure
        try:
            return resp.choices[0].message.content
        except Exception:
            return str(resp)
    except Exception as e:
        return f"LLM call failed: {e}"
