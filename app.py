import streamlit as st
import google.generativeai as genai
import pandas as pd
import time

# ==========================================
# 1. PAGE CONFIGURATION & VIBRANT CSS
# ==========================================
st.set_page_config(page_title="CoachBot AI | NextGen", page_icon="⚡", layout="wide")

# Visual upgrade using Custom CSS
st.markdown("""
    <style>
    /* Vibrant Main Background Gradient */
    .stApp {
        background: linear-gradient(135deg, #e0f2fe 0%, #f3e8ff 100%);
    }
    
    /* Make ALL main app text, sidebar text, and button text BLACK */
    h1, h2, h3, h4, h5, h6, p, span, label, li, div {
        color: black !important;
        font-family: 'Helvetica Neue', sans-serif;
    }
    
    /* Special Header Font */
    h1, h2, h3 {
        font-family: 'Arial Black', sans-serif;
    }
    
    /* Lighten the sidebar so the black text is clearly visible */
    [data-testid="stSidebar"] {
        background-color: #e2e8f0 !important; 
    }
    
    /* Awesome Gradient Button */
    .stButton>button {
        background: linear-gradient(90deg, #f97316 0%, #e11d48 100%);
        border-radius: 30px;
        padding: 12px 28px;
        font-weight: 800;
        font-size: 18px;
        border: none;
        box-shadow: 0 4px 15px rgba(225, 29, 72, 0.4);
        transition: all 0.3s ease;
    }
    .stButton>button:hover { 
        transform: translateY(-2px) scale(1.02);
        box-shadow: 0 6px 20px rgba(225, 29, 72, 0.6);
    }
    
    /* Styled Text Inputs and Text Areas */
    .stTextInput>div>div>input, .stTextArea>div>div>textarea {
        border: 2px solid #8b5cf6 !important;
        border-radius: 10px;
        background-color: white !important;
        color: black !important; /* Black text for normal inputs */
    }
    
    /* =========================================
       THE 10 COACHING MODULES (WHITE TEXT)
       ========================================= */
    /* Target the selectbox wrapper to give it a dark background and white text */
    .stSelectbox>div>div>div {
        border: 2px solid #8b5cf6 !important;
        border-radius: 10px;
        background-color: #4338ca !important; /* Deep indigo background */
        color: white !important; 
    }
    /* Target the text inside the collapsed selectbox */
    .stSelectbox>div>div>div div, .stSelectbox>div>div>div span {
        color: white !important;
    }
    /* Target the expanded dropdown menu and its list items */
    div[data-baseweb="popover"] ul {
        background-color: #4338ca !important; 
    }
    div[data-baseweb="popover"] ul li, div[data-baseweb="popover"] ul li span, div[data-baseweb="popover"] ul li div {
        color: white !important; /* The 10 items will be white */
    }
    
    /* =========================================
       TAB STYLING - WHITE TEXT
       ========================================= */
    .stTabs [data-baseweb="tab"] {
        background-color: #4338ca; 
        border-radius: 8px 8px 0 0;
        margin-right: 5px;
        border: 2px solid #cbd5e1;
        border-bottom: none;
    }
    /* Force the tab text to be white */
    .stTabs [data-baseweb="tab"] span, .stTabs [data-baseweb="tab"] p {
        color: white !important; 
    }
    
    .stTabs [aria-selected="true"] {
        background-color: #000000;
        border-color: #000000;
    }
    .stTabs [aria-selected="true"] span, .stTabs [aria-selected="true"] p {
        color: white !important; 
    }
    
    /* Metric Cards */
    [data-testid="stMetricValue"] {
        font-weight: bold;
    }
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
    # Using your requested model
    model = genai.GenerativeModel('gemini-3-flash-preview')
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
# These tab labels remain white
tab1, tab2, tab3 = st.tabs(["📋 Athlete Setup", "🏋️‍♂️ Generate Plan", "📊 Analytics & Diet"])

# --- TAB 1: ATHLETE SETUP ---
with tab1:
    st.subheader("Define Your Athlete Profile")
    
    with st.container():
        c1, c2, c3 = st.columns(3)
        with c1:
            # Text input for free-form typing
            sport = st.text_input("Primary Sport 🏀", placeholder="e.g., Football, Swimming, Fencing")
            position = st.text_input("Position/Role 🎯", placeholder="e.g., Midfielder, Sprinter")
        with c2:
            age = st.number_input("Athlete Age 🎂", min_value=8, max_value=25, value=16)
            intensity = st.slider("Target Intensity 🔥 (1-10)", 1, 10, 6)
        with c3:
            # Text input for free-form typing
            goal = st.text_input("Primary Objective 🏆", placeholder="e.g., Build Stamina, Improve Agility")
            # Text input for free-form typing
            diet = st.text_input("Dietary Needs 🥗", placeholder="e.g., Vegan, Gluten-Free, No restrictions")

    # PROMINENT PROBLEM/INJURY BOX
    st.error("⚠️ Current Problem or Injury Context")
    problem_injury = st.text_area(
        "Describe any current problems, injuries, or pain points you have:", 
        placeholder="e.g., 'Recovering from a torn ACL', 'Lower back pain after running', or 'Trouble building stamina late in the game'."
    )

# --- TAB 2: GENERATE PLAN ---
with tab2:
    st.subheader("🧠 Request AI Coaching")
    
    # The text inside this selectbox will now be white
    feature = st.selectbox("Select Coaching Module 🛠️:", [
        "1. Full-Body Workout Plan", "2. Safe Recovery Training Schedule", 
        "3. Tactical Coaching Tips", "4. Nutrition & Meal Guide", 
        "5. Warm-up & Cooldown Routine", "6. Pre-Match Mental Visualization", 
        "7. Hydration & Electrolyte Strategy", "8. Positional Decision-Making Drills", 
        "9. Sleep & Recovery Optimization", "10. Off-Season Conditioning Plan"
    ])

    if st.button("🚀 Generate My Personalized Plan"):
        # Added quick validation to ensure they didn't leave the new text boxes entirely blank
        if not api_key:
            st.error("Cannot generate plan: API key is missing from secrets.")
        elif not sport.strip() or not goal.strip() or not diet.strip():
            st.warning("Please fill out your Sport, Objective, and Dietary Needs in the Athlete Setup tab.")
        elif not problem_injury.strip():
            st.warning("Please enter your current problem or injury in the 'Athlete Setup' tab so we can ensure safe advice.")
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
                    
                    st.success("🎉 Plan Generated Successfully!")
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
    col_m2.metric(label="Hydration Level", value="Optimal", delta="Maintained")
    col_m3.metric(label="Injury Risk", value="Low", delta="-10%")
    
    st.markdown("### Weekly Macro Tracker 🍎")
    macro_data = pd.DataFrame({
        "Day": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
        "Protein (g)": [120, 130, 120, 140, 125],
        "Carbs (g)": [250, 300, 250, 320, 280]
    })
    st.dataframe(macro_data, use_container_width=True, hide_index=True)
