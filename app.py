import streamlit as st
import google.generativeai as genai
import json
import re
from datetime import datetime
from typing import Dict, Any, Optional

# ── PAGE CONFIG ──────────────────────────────────────────────────────────────
st.set_page_config(page_title="AgSaathi — Smart Farming Assistant", page_icon="🌿", layout="wide")

# ── GEMINI SETUP ────────────────────────────────────────────────────────────
# Ensure you have set this in Streamlit Cloud Secrets or .streamlit/secrets.toml
GEMINI_API_KEY = st.secrets.get("GEMINI_API_KEY", None)

if not GEMINI_API_KEY:
    st.error("⚠️ Gemini API key not found. Please add GEMINI_API_KEY to your Streamlit secrets.")
    st.stop()

genai.configure(api_key=GEMINI_API_KEY)
# Using the stable 2.0 Flash model name
MODEL_NAME = "gemini-2.0-flash" 
MODEL_TEMPERATURE = 0.3

@st.cache_resource
def get_model():
    return genai.GenerativeModel(
        model_name=MODEL_NAME, 
        generation_config=genai.GenerationConfig(temperature=MODEL_TEMPERATURE)
    )

# ── GEO DATA ────────────────────────────────────────────────────────────────
GEO = {
    'India 🇮🇳': {'languages': ['English', 'Hindi'], 'states': ['Uttar Pradesh', 'Punjab', 'Bihar', 'Madhya Pradesh', 'Maharashtra', 'Gujarat']},
    'Canada 🇨🇦': {'languages': ['English', 'French'], 'states': ['Ontario', 'Quebec', 'Saskatchewan', 'Alberta']},
    'Ghana 🇬🇭': {'languages': ['English'], 'states': ['Ashanti', 'Northern', 'Greater Accra', 'Volta']},
}

# ── SESSION STATE ───────────────────────────────────────────────────────────
if 'page' not in st.session_state: st.session_state.page = 'hero'
if 'onboarding_complete' not in st.session_state: st.session_state.onboarding_complete = False
if 'stats' not in st.session_state: st.session_state.stats = {'queries': 0}

# ── AI HELPER ───────────────────────────────────────────────────────────────
def call_ai(prompt: str) -> Optional[Dict]:
    try:
        model = get_model()
        resp = model.generate_content(prompt).text
        # Clean potential markdown code blocks from AI response
        text = re.sub(r'```json|```', '', resp).strip()
        start, end = text.find('{'), text.rfind('}') + 1
        if start != -1:
            st.session_state.stats['queries'] += 1
            return json.loads(text[start:end])
    except Exception as e:
        st.error(f"⚠️ AI Error: {str(e)}")
    return None

def render_confidence_bar(score: int):
    color = "#27AE60" if score >= 80 else "#E67E22" if score >= 50 else "#C0392B"
    st.markdown(f"""
    <div style='margin-top:15px;'>
        <div style='display:flex; justify-content:space-between; font-size:0.8rem; margin-bottom:5px; color:#E8C97A;'>
            <span>AI Confidence Score</span><span>{score}%</span>
        </div>
        <div style='width:100%; background:rgba(255,255,255,0.1); border-radius:5px; height:8px;'>
            <div style='width:{score}%; background:{color}; height:100%; border-radius:5px; transition:1s;'></div>
        </div>
    </div>""", unsafe_allow_html=True)

# ── CSS ─────────────────────────────────────────────────────────────────────
def inject_css():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700;900&family=Nunito+Sans:wght@300;400;600;700&display=swap');
    :root { --soil: #1A0F07; --wheat: #E8C97A; --cream: #FDF6E3; --sage: #4A7C59; }
    html, body, [data-testid="stAppViewContainer"] { background: #121212 !important; color: #FDF6E3 !important; font-family: 'Nunito Sans', sans-serif;}
    h1, h2, h3 { font-family: 'Playfair Display', serif !important; color: #E8C97A !important; }
    .card { background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.1); border-radius: 15px; padding: 25px; margin-bottom: 15px; }
    .stButton>button { border: 2px solid #E8C97A !important; color: #E8C97A !important; border-radius: 50px !important; background: transparent; }
    .stButton>button:hover { background: #E8C97A !important; color: #1A0F07 !important; }
    </style>
    """, unsafe_allow_html=True)

# ── PAGES ───────────────────────────────────────────────────────────────────
def page_hero():
    st.markdown("<div style='text-align:center; margin-top:10vh;'><div style='font-size:6rem;'>🌿</div><h1 style='font-size:4rem;'>AgSaathi</h1><p style='font-size:1.5rem; opacity:0.7;'>Smart Farming Assistant</p></div>", unsafe_allow_html=True)
    if st.button("🚀 GET STARTED", use_container_width=True):
        st.session_state.page = 'country'; st.rerun()

def render_dashboard():
    st.sidebar.title("🌿 AgSaathi")
    st.sidebar.info(f"📍 {st.session_state.get('state', 'Unknown')}")
    
    tab1, tab2, tab3 = st.tabs(["🌾 Crop Rec", "🐛 Pest Control", "🧪 Soil Health"])
    
    with tab1:
        st.subheader("Crop Recommendations")
        goal = st.text_input("What is your goal?", key="crop_goal")
        if st.button("Analyze"):
            prompt = f"Provide a JSON crop recommendation for {st.session_state.get('state')} with goal {goal}. Include crop_name, reason, and confidence_score."
            res = call_ai(prompt)
            if res:
                st.write(f"### Suggestion: {res.get('crop_name')}")
                st.write(res.get('reason'))
                render_confidence_bar(res.get('confidence_score', 85))

# ── MAIN ROUTER ─────────────────────────────────────────────────────────────
def main():
    inject_css()
    if not st.session_state.onboarding_complete:
        if st.session_state.page == 'hero':
            page_hero()
        else:
            # Simple onboarding for demo
            st.session_state.state = "Maharashtra"
            if st.button("Complete Setup"):
                st.session_state.onboarding_complete = True
                st.rerun()
    else:
        render_dashboard()

if __name__ == "__main__":
    main()
