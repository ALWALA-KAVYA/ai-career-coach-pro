
import fitz  # PyMuPDF
import spacy

# Load model lazily
_nlp = None
def _get_nlp():
    global _nlp
    if _nlp is None:
        try:
            _nlp = spacy.load("en_core_web_sm")
        except Exception as e:
            raise RuntimeError("spaCy model 'en_core_web_sm' not found. Run: python -m spacy download en_core_web_sm") from e
    return _nlp

def extract_text_from_pdf(uploaded_file):
    data = uploaded_file.read()
    doc = fitz.open(stream=data, filetype="pdf")
    parts = []
    for page in doc:
        parts.append(page.get_text())
    return "\\n".join(parts).strip()

COMMON_SKILLS = [
    'python','sql','pandas','numpy','scikit-learn','tensorflow','pytorch','nlp','machine learning',
    'aws','azure','gcp','docker','kubernetes','powerbi','tableau','excel','deep learning'
]

def extract_skills(text):
    if not text:
        return []
    text_l = text.lower()
    found = [s for s in COMMON_SKILLS if s in text_l]
    nlp = _get_nlp()
    doc = nlp(text[:10000])
    ents = [ent.text for ent in doc.ents if len(ent.text) <= 40]
    skills = list(dict.fromkeys(found + ents))
    return skills
