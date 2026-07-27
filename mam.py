import os
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv

# Environment variables load செய்ய
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

# Gemini AI மாடல் செட்டப் (12-வது வரி மாற்றி அமைக்கப்பட்டது)
genai.configure(api_key=api_key)
model = genai.GenerativeModel(model_name="gemini-2.5-flash")

st.title("🏍️ Smart Helmet & Automatic Speed Control System (GenAI Powered)")

st.subheader("1. Helmet Sensor Check")
# Helmet Sensor Simulation
helmet_on = st.checkbox("Is Helmet Sensor Activated / Helmet On?")

if not helmet_on:
    st.error("❌ Helmet NOT detected! Engine Locked. Bike will NOT Start.")
else:
    st.success("✅ Helmet Detected! Engine Started Successfully.")
    
    st.subheader("2. Speed Monitoring & Auto-Control")
    # Speed Input Simulation
    speed = st.slider("Current Bike Speed (km/h)", min_value=0, max_value=120, value=40)
    
    speed_limit = 70  # நிர்ணயிக்கப்பட்ட வேகம்
    
    if speed > speed_limit:
        st.warning(f"⚠️ OVER SPEEDING DETECTED! Speed ({speed} km/h) crossed limit ({speed_limit} km/h).")
        st.info("🔄 Automatic Engine Speed Reduction Triggered! Reducing speed to safe limit...")
        
        # GenAI integration for Driving Analysis Alert
        if st.button("Generate AI Safety Incident Report"):
            prompt = f"""
            The rider was wearing a helmet, but exceeded the speed limit.
            Current Speed: {speed} km/h.
            Allowed Limit: {speed_limit} km/h.
            Action Taken: Engine automatically reduced the speed.
            
            Write a short, polite, yet urgent driving behavior alert message (in Tamil) to the rider explaining why speed was auto-reduced and warning them about safety.
            """
            
            with st.spinner("GenAI is generating safety feedback..."):
                response = model.generate_content(prompt)
                
            st.write("### 🤖 GenAI Generated Safety Alert:")
            st.write(response.text)
    else:
        st.success(f" Safe Speed ({speed} km/h). Keep riding safely!")