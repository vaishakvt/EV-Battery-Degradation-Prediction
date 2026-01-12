import streamlit as st
import pandas as pd
import joblib
import base64

# -----------------------------
# Load trained model
# -----------------------------
model = joblib.load("EV_Battery_Degradation_Model.pkl")

# -----------------------------
# Set background with dark overlay
# -----------------------------
def set_bg_with_overlay(image_file):
    with open(image_file, "rb") as f:
        encoded = base64.b64encode(f.read()).decode()

    st.markdown(
        f"""
        <style>
        /* Background */
        .stApp {{
            background:
                linear-gradient(rgba(0,0,0,0.65), rgba(0,0,0,0.65)),
                url("data:image/png;base64,{encoded}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }}

        /* Labels */
        label, .stMarkdown {{
            color: white !important;
            font-weight: 500;
        }}

        /* Input boxes */
        input, textarea {{
            background-color: rgba(255,255,255,0.92) !important;
            color: #000000 !important;
            border-radius: 8px !important;
            border: 1px solid #ccc !important;
            font-size: 16px !important;
        }}

        /* Sliders text */
        .stSlider span {{
            color: white !important;
            font-weight: 500;
        }}

        /* Center button */
        div.stButton {{
            display: flex;
            justify-content: center;
        }}

        /* Button style */
        div.stButton > button {{
            background-color: #00c896;
            color: black;
            font-size: 18px;
            padding: 10px 30px;
            border-radius: 10px;
            font-weight: bold;
        }}

        div.stButton > button:hover {{
            background-color: #00a87a;
            color: white;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Apply background
set_bg_with_overlay("evcar.png")

# -----------------------------
# App Header
# -----------------------------
st.markdown(
    "<h1 style='text-align:center; color:white;'>🔋 EV Battery Degradation Prediction</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<p style='text-align:center; color:#dddddd;'>Machine Learning model to estimate EV battery health loss</p>",
    unsafe_allow_html=True
)

st.markdown("---")

# -----------------------------
# Input Section
# -----------------------------
col1, col2 = st.columns(2)

with col1:
    vehicle_age = st.number_input("Vehicle Age (Years)", 0.5, 15.0, 5.0)
    battery_capacity = st.number_input("Battery Capacity (kWh)", 30, 100, 50)
    daily_usage = st.number_input("Daily Usage (km)", 10, 200, 60)
    total_distance = st.number_input("Total Distance Driven (km)", 1000, 700000, 90000)

with col2:
    charge_cycles = st.number_input("Charge Cycles", 50, 6000, 800)
    fast_charge = st.slider("Fast Charging Usage (%)", 0, 100, 30)
    avg_temp = st.slider("Average Operating Temperature (°C)", 0, 60, 30)

st.markdown("---")

# -----------------------------
# Prediction
# -----------------------------
if st.button("🚀 Predict Battery Degradation"):
    input_df = pd.DataFrame({
        "Vehicle_Age_Years": [vehicle_age],
        "Battery_Capacity_kWh": [battery_capacity],
        "Daily_Usage_km": [daily_usage],
        "Total_Distance_km": [total_distance],
        "Charge_Cycles": [charge_cycles],
        "Fast_Charge_%": [fast_charge],
        "Avg_Temperature_C": [avg_temp]
    })

    prediction = model.predict(input_df)[0]

    st.markdown(
        f"""
        <h2 style='text-align:center; color:#00ff99;'>
        🔮 Predicted Battery Degradation: {prediction:.2f}%
        </h2>
        """,
        unsafe_allow_html=True
    )

# -----------------------------
# Footer
# -----------------------------
st.markdown(
    "<p style='text-align:center; color:#bbbbbb;'>Built using Machine Learning & Streamlit</p>",
    unsafe_allow_html=True
)
