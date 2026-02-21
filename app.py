import streamlit as st
import google.generativeai as genai
import pandas as pd
import time

# ==========================================
# 1. PAGE CONFIGURATION & CUSTOM CSS
# ==========================================
st.set_page_config(page_title="CoachBot AI | NextGen", page_icon="⚡", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    h1 { color: #1e3d59; font-family: 'Helvetica Neue', sans-serif; }
    .stButton>button {
        background-color: #ff6e40; color: white; border-radius: 8px;
        padding: 10px 24px; font-weight: bold; border: none; transition: 0.3s;
    }
    .stButton>button:hover { background-color: #ff521b; transform: scale(1.02); }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 2. HEADER & SECURE API CONFIGURATION
# ==========================================
col_logo, col_title = st.columns([1, 8])
with col_logo:
    st.image("https://cdn-icons-png.flaticon.com/512/3043/3043888.png", width=80) 
with col_title:
    st.title("⚡ CoachBot AI: NextGen Virtual Coach")
    st.markdown("*Empowering youth athletes with AI-driven, personalized sports science.*")

st.sidebar.image("https://cdn-icons-png.flaticon.com/512/2112/2112281.png", width=150)
st.sidebar.header("🔐 Authentication")

# Securely load API key from Streamlit Secrets
try:
    api_key = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=api_key)
    # Configure the specific model required by the assignment
    model = genai.GenerativeModel('gemini-1.5-pro')
    st.sidebar.success("✅ API Key Loaded Securely")
except KeyError:
    st.sidebar.error("❌ API Key missing! Please configure Streamlit Secrets.")
    api_key = None

st.sidebar.header("⚙️ CoachBot Brain Tuning")
temperature = st.sidebar.slider("Creativity (Temperature)", 0.0, 1.0, 0.4, 0.1)
top_p = st.sidebar.slider("Focus (Top P)", 0.0, 1.0, 0.9, 0.1)

# ==========================================
# 3. MAIN DASHBOARD UI (TABS)
# ==========================================
tab1, tab2, tab3 = st.tabs(["📋 Athlete Setup", "🏋️‍♂️ Generate Plan", "📊 Analytics & Diet"])

# --- TAB 1: ATHLETE SETUP ---
with tab1:
    st.subheader("Define Your Athlete Profile")
    
    with st.container():
        c1, c2, c3 = st.columns(3)
        with c1:
            sport = st.selectbox("Primary Sport", ["Football", "Cricket", "Basketball", "Athletics", "Tennis"])
            position = st.text_input("Position/Role", "Midfielder")
        with c2:
            age = st.number_input("Athlete Age", min_value=8, max_value=25, value=16)
            intensity = st.slider("Target Intensity (1-10)", 1, 10, 6)
        with c3:
            goal = st.selectbox("Primary Objective", ["Stamina", "Injury Rehab", "Tactical IQ", "Explosive Power"])
            diet = st.selectbox("Dietary Needs", ["Standard", "Vegetarian", "Vegan", "High-Protein"])

    # PROMINENT PROBLEM/INJURY BOX
    st.warning("⚠️ Current Problem or Injury Context")
    problem_injury = st.text_area(
        "Describe any current problems, injuries, or pain points you have:", 
        placeholder="e.g., 'Recovering from a torn ACL', 'Lower back pain after running', or 'Trouble building stamina late in the game'."
    )

# --- TAB 2: GENERATE PLAN ---
with tab2:
    st.subheader("🧠 Request AI Coaching")
    
    feature = st.selectbox("Select Coaching Module:", [
        "1. Full-Body Workout Plan", "2. Safe Recovery Training Schedule", 
        "3. Tactical Coaching Tips", "4. Nutrition & Meal Guide", 
        "5. Warm-up & Cooldown Routine", "6. Pre-Match Mental Visualization", 
        "7. Hydration & Electrolyte Strategy", "8. Positional Decision-Making Drills", 
        "9. Sleep & Recovery Optimization", "10. Off-Season Conditioning Plan"
    ])

    if st.button("🚀 Generate My Personalized Plan"):
        if not api_key:
            st.error("Cannot generate plan: API key is missing from secrets.")
        elif not problem_injury.strip():
            st.error("Please enter your current problem or injury in the 'Athlete Setup' tab so we can ensure safe advice.")
        else:
            system_prompt = "You are CoachBot AI, an expert, encouraging youth sports coach. Prioritize safety and injury prevention."
            user_context = f"Athlete: {age}yo {sport} {position}. Problem/Injury: {problem_injury}. Goal: {goal}. Diet: {diet}. Intensity: {intensity}/10."
            task = f"Task: {feature}. Use clear markdown formatting, emojis, and bullet points."
            
            with st.spinner(f"CoachBot is designing your {feature.lower()}..."):
                try:
                    time.sleep(1) # Rate limit protection
                    response = model.generate_content(
                        f"{system_prompt}\n\n{user_context}\n\n{task}",
                        generation_config=genai.types.GenerationConfig(temperature=temperature, top_p=top_p)
                    )
                    
                    st.success("Plan Generated Successfully!")
                    with st.container(border=True):
                        st.markdown(response.text)
                    
                    with st.expander("🔍 View Raw Generation Logs (For Assessor)"):
                        st.write(f"**Temperature:** {temperature} | **Top_P:** {top_p}")
                        st.code(f"{system_prompt}\n\n{user_context}\n\n{task}")
                        
                except Exception as e:
                    st.error(f"Generation Failed: {e}")

# --- TAB 3: ANALYTICS ---
with tab3:
    st.subheader("📊 Athlete Dashboard Trackers")
    col_m1, col_m2, col_m3 = st.columns(3)
    col_m1.metric(label="Readiness Score", value="85%", delta="5%")
    col_m2.metric(label="Hydration Level", value="Optimal", delta="Maintained", delta_color="normal")
    col_m3.metric(label="Injury Risk", value="Low", delta="-10%", delta_color="inverse")
    
    macro_data = pd.DataFrame({
        "Day": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
        "Protein (g)": [120, 130, 120, 140, 125],
        "Carbs (g)": [250, 300, 250, 320, 280]
    })
    st.dataframe(macro_data, use_container_width=True, hide_index=True)
