
import fitz  # PyMuPDF

COMMON_SKILLS = [
    'python','sql','pandas','numpy','scikit-learn','tensorflow','pytorch','nlp','machine learning',
    'aws','azure','gcp','docker','kubernetes','powerbi','tableau','excel','deep learning',
    'html','css','javascript','react','node','data analysis','data science'
]

def extract_text_from_pdf(uploaded_file):
    data = uploaded_file.read()
    doc = fitz.open(stream=data, filetype="pdf")
    parts = []
    for page in doc:
        parts.append(page.get_text())
    return "\n".join(parts).strip()

def extract_skills(text):
    if not text:
        return []
    text_l = text.lower()
    found = [s for s in COMMON_SKILLS if s in text_l]
    return list(dict.fromkeys(found))

