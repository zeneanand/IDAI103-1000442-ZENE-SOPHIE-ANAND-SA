import streamlit as st
from google import genai
from google.genai import types
import pandas as pd

# --- APP CONFIGURATION ---
st.set_page_config(page_title="CoachBot AI | NextGen Sports", layout="wide", page_icon="⚽")
api_key = st.secrets["GEMINI_API_KEY"]# Custom CSS for a professional look
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stButton>button { width: 100%; border-radius: 5px; height: 3em; background-color: #007bff; color: white; }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR: PLAYER PROFILE ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/857/857418.png", width=100)
    st.title("Athlete Profile")
    
    # Fetching the API Key securely from Streamlit Secrets

        
    
        

    sport = st.selectbox("Sport", ["Football", "Cricket", "Basketball", "Athletics", "Swimming"])
    position = st.text_input("Position", placeholder="e.g., Striker, Fast Bowler")
    injury = st.text_input("Injury History", placeholder="e.g., Grade 1 Ankle Sprain, None")
    
    st.divider()
    st.subheader("Model Tuning")
    # Temperature 0.3 for safety/accuracy in recovery; 0.8 for creative drills
    temp = st.slider("Coaching Creativity (Temperature)", 0.0, 1.0, 0.4)
    # Gemini 3 Thinking Level: Low for speed, High for complex tactical planning
    thinking = st.select_slider("Thinking Intensity", options=["low", "medium", "high"], value="medium")

# --- CORE LOGIC ---
def generate_coach_advice(user_prompt):
    if not api_key:
        st.error("API Key is missing from secrets. Please configure it to continue.")
        return None
    
    try:
        client = genai.Client(api_key=api_key)
        config = types.GenerateContentConfig(
            temperature=temp,
            thinking_config=types.ThinkingConfig(thinking_level=thinking)
        )
        
        response = client.models.generate_content(
            model="gemini-3-flash-preview", 
            contents=user_prompt,
            config=config
        )
        return response.text
    except Exception as e:
        st.error(f"API Error: {str(e)}")
        return None

# --- MAIN INTERFACE ---
st.title("🏆 CoachBot AI")
st.info("Empowering young athletes with professional-grade training and tactical intelligence.")

tab1, tab2, tab3 = st.tabs(["🏋️ Custom Workouts", "🥗 Nutrition & Recovery", "📊 Tactical Drills"])

with tab1:
    st.subheader("Position-Specific Physical Training")
    if st.button("Generate My Position-Based Workout"):
        prompt = f"""
        Act as an elite youth coach. Create a 40-minute workout for a {position} in {sport}.
        Constraints: The athlete is recovering from {injury}. 
        Format: Return a table with Exercise, Sets/Reps, and Safety Notes. 
        Focus: Socially inclusive, no expensive equipment needed.
        """
        result = generate_coach_advice(prompt)
        if result: st.markdown(result)

with tab2:
    st.subheader("Nutrition & Injury Management")
    if st.button("Get Recovery & Meal Plan"):
        prompt = f"Provide a daily nutrition guide and recovery stretching routine for a 15-year-old {position} in {sport} dealing with {injury}. Focus on low-cost, high-protein local foods."
        result = generate_coach_advice(prompt)
        if result: st.markdown(result)

with tab3:
    st.subheader("Game Intelligence")
    if st.button("Analyze Tactical Positioning"):
        prompt = f"Explain 3 common tactical mistakes for a {position} in {sport} and provide a mental visualization drill to improve decision-making under pressure."
        result = generate_coach_advice(prompt)
        if result: st.markdown(result)
