
# ⚡ CoachBot AI — AI-Powered Smart Fitness Assistant

**Student Name:** [ZENE SOPHIE ANAND]

**Student ID:** [1000442]

**Course:** Artificial Intelligence - Generative AI

**School:** [ASPEE NUTAN ACADEMY ]

**Assessment Type:** Summative Assessment (Individual)

**Project Title:** Building AI-Powered Web Applications for Real-World Solutions

---

## 🔗 Project Links

| Resource | Link |
| --- | --- |
| 🚀 Live App | [Open Live App Here](https://idai103-1000442-zene-sophie-anand-sa.streamlit.app/) |
| 💻 GitHub Repo | [View Source Code](https://github.com/zeneanand/IDAI103-1000442-ZENE-SOPHIE-ANAND-SA) |

---

## 📋 Project Overview

**CoachBot AI** is a generative AI-powered web assistant built using **Python**, **Streamlit**, and the **Google Gemini 1.5 Pro API**. Designed for NextGen Sports Lab, it acts as a virtual personal coach providing hyper-personalized, safe, and tactical fitness training for youth athletes.

By analyzing specific user inputs—including sport, precise playing position, age, and critical injury history—CoachBot generates tailored workout plans, recovery schedules, nutritional guides, and tactical advice. This project demonstrates the complete deployment of a generative AI solution, moving from prompt engineering and hyperparameter tuning to a fully responsive, visually engaging cloud-deployed web application.

---

## ❗ Problem Statement

Many aspiring youth athletes, especially in under-resourced regions or the early stages of their training, lack access to professional coaches or tailored fitness routines. Traditional fitness apps often provide:

* Generic, "one-size-fits-all" workout plans.
* Advice that ignores specific positional demands (e.g., Goalkeeper vs. Striker).
* Regimens that fail to account for past injuries, leading to unsafe training environments.

**CoachBot AI** bridges this gap by democratizing access to elite-level sports science, ensuring young athletes train safely, efficiently, and tactically based on their unique physical profiles.

---

## 🎯 Project Objectives

* Integrate the **Gemini 1.5 Pro API** to process real-time user data and generate personalized outputs.
* Design **10 diverse, user-focused prompt features** (e.g., tactical tips, recovery, nutrition).
* Implement robust **Hyperparameter Tuning** (Temperature and Top-P) to balance AI creativity with safety and accuracy.
* Build a modular, visually appealing **Streamlit web application** using custom CSS and DataFrames.
* Deploy the completed project via **GitHub** and **Streamlit Cloud** for real-world usability.

---

## ✨ Key Features

### 🛒 Core Functionality

* **Dynamic Athlete Profiling:** Captures sport, position, age, dietary needs, intensity levels, and crucial injury context.
* **10 Specialized Coaching Modules:** From "Full-Body Workouts" to "Positional Decision-Making Drills" and "Pre-Match Mental Visualization."
* **Safety-First AI Guardrails:** System prompts force the AI to prioritize injury prevention and adjust all routines around user-reported pain points.
* **Adjustable AI Brain Tuning:** Sidebar sliders allow users (and assessors) to tweak Model Temperature and Top-P in real-time.

### 📊 Visual Dashboard & Analytics

* **Tab-Based Navigation:** Cleanly separates "Athlete Setup", "Generate Plan", and "Analytics & Diet".
* **Pandas Data Integration:** Renders weekly macro-nutrient tracking in beautiful, readable dataframes.
* **KPI Metric Cards:** Displays vital athlete stats like Readiness Score, Hydration Levels, and Injury Risk.

---

## 🎨 User Interface Design

* **Vibrant CSS Theme:** A modern gradient background (`#e0f2fe` to `#f3e8ff`) giving the app an energetic, premium fitness feel.
* **High-Contrast Typography:** Deep black text for readability, with strictly targeted white text for the navigation tabs and dropdown menus against an Indigo (`#4338ca`) background.
* **Hover Animations:** Custom CSS buttons with gradient fills, shadow-casting, and scale-on-hover effects to create a highly tactile user experience.
* **Emoji Integration:** Strategic use of emojis to guide the user's eye and maintain an encouraging, youth-friendly interface.

---

## 🔧 Technical Architecture

### Technologies Used

* **Python 3.x** — Core application logic and API handling.
* **Streamlit** — Interactive web interface, tab routing, and UI components.
* **Google Gemini API (`google-generativeai`)** — The generative AI reasoning engine (Gemini 1.5 Pro).
* **Pandas** — Structuring and displaying tabular nutritional data.
* **Streamlit Secrets** — Secure environmental variable management for the API key.

### Prompt Engineering Strategy

The app utilizes a **System + Context + Task** prompt structure:

```text
System: You are CoachBot AI, an expert, encouraging youth sports coach. Prioritize safety...
Context: Athlete: 16yo Football Midfielder. Injury: Recovering from torn ACL. Goal: Build Stamina...
Task: Provide a Safe Recovery Training Schedule. Use clear markdown formatting...

```

This strict structure ensures the Gemini model rarely hallucinates and always factors in the athlete's limitations.

---

## 📁 Project Structure

```text
IDAI103-Student_id-studentname/
│
├── app.py                  # Main Streamlit application and UI logic
├── requirements.txt        # Python dependencies (streamlit, google-generativeai, pandas)
├── README.md               # Comprehensive project documentation
│
└── assets/                 # App screenshots for documentation
    ├── app_dashboard.png
    ├── generated_plan.png
    └── analytics_tab.png

```

---

# 🚀 Project Development Stages

### 🧠 Stage 1: Problem Definition & Research

Analyzed the specific needs of youth athletes across various sports. Researched how professional coaches adapt routines for specific positions (e.g., high-impact vs. low-impact) and studied the importance of mental visualization and proper hydration in youth sports.

### 🧮 Stage 2: Model Integration & Tuning

Configured the Google Gemini 1.5 Pro API. Experimented with hyperparameter tuning:

* **Temperature (0.3 - 0.4):** Found to be the optimal sweet spot. It keeps the AI conservative and safe regarding physical exercises while allowing enough creativity for tactical advice.
* **Top P (0.9):** Allows for a natural, encouraging coaching vocabulary.

### 🖥️ Stage 3: UI/UX & Prompt Engineering

Developed the Streamlit interface using `st.tabs` and `st.columns`. Drafted the **10 compulsory prompt features**, ensuring each one dynamically injected the user's custom inputs (Sport, Position, Injury) directly into the API call. Applied custom CSS to elevate the visual appeal.

### 🧪 Stage 4: Testing & Validation

Tested the application with extreme edge cases (e.g., "10-year-old weightlifter with a broken arm") to ensure the AI successfully adjusted its advice to prioritize rest and safety. Implemented `try-except` blocks to handle API rate-limiting gracefully.

### 🌐 Stage 5: Cloud Deployment

Secured the API key using `st.secrets` locally, pushed the repository to GitHub, and successfully deployed the live web application using Streamlit Cloud.

---

## ⚙️ Deployment Instructions

### 💻 Local Deployment

1. Clone the repository:

```bash
git clone https://github.com/YourUsername/IDAI103-Student_id-studentname.git
cd IDAI103-Student_id-studentname

```

2. Install required dependencies:

```bash
pip install -r requirements.txt

```

3. Create a secrets file for your Gemini API key:

```bash
mkdir .streamlit
echo 'GEMINI_API_KEY = "your-api-key-here"' > .streamlit/secrets.toml

```

4. Run the Streamlit application:

```bash
streamlit run app.py

```

### ☁️ Cloud Deployment (Streamlit Cloud)

1. Push your code to a public GitHub repository.
2. Visit [Streamlit Cloud](https://streamlit.io/cloud) and sign in.
3. Click **"New app"** and select your GitHub repository.
4. Set the main file path to: `app.py`.
5. Go to **Advanced settings → Secrets** and paste your API key:
```toml
GEMINI_API_KEY = "your-api-key-here"

```


6. Click **Deploy**.

🌱 Ethical & Social Considerations
Safety & Health: CoachBot AI is programmed to include disclaimers and prioritize safety, but it explicitly states that AI advice should not replace professional medical clearance, especially regarding severe injuries.

Inclusivity: By removing the financial barrier to personalized sports science, this app promotes inclusive sports excellence for youth in low-income or rural areas.

Data Privacy: The application does not utilize a backend database. All user inputs (injuries, ages, diets) are ephemeral and wiped the moment the browser window is closed.

