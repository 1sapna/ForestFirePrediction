import streamlit as st
import pandas as pd
import joblib
from sklearn.preprocessing import LabelEncoder

# Load the trained model
model = joblib.load("forest_fire_model.joblib")

# Encoding for 'month' and 'day' (same as in training)
month_encoder = LabelEncoder().fit(['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec'])
day_encoder = LabelEncoder().fit(['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun'])

# Custom theme and title
st.markdown(
    """
    <style>
    .title {
        font-size: 35px;
        font-family: 'Helvetica';
        color: #8B0000;
    }
    .emoji { font-size: 40px; }
    .input-box { color: #2E8B57; }
    </style>
    """,
    unsafe_allow_html=True
)

# App title with fire emoji
st.markdown('<p class="title">🔥 Forest Fire Prediction App 🔥</p>', unsafe_allow_html=True)
st.write("Help us predict forest fire area based on environmental conditions. 🌲🔥")

# User input section
st.subheader("Enter the Environmental Conditions 🌲")
st.markdown('<p class="emoji">🌦️ 🌡️ 💨</p>', unsafe_allow_html=True)

# Input fields with a forest theme
month = st.selectbox("Select Month 📅", month_encoder.classes_)
day = st.selectbox("Select Day 🗓️", day_encoder.classes_)

input_data = {
    'X': st.number_input("X Coordinate 🌍", min_value=0.0),
    'Y': st.number_input("Y Coordinate 🌍", min_value=0.0),
    'FFMC': st.number_input("FFMC 🔥", min_value=0.0),
    'DMC': st.number_input("DMC 💧", min_value=0.0),
    'DC': st.number_input("DC 🌞", min_value=0.0),
    'ISI': st.number_input("ISI 🌡️", min_value=0.0),
    'temp': st.number_input("Temperature (°C) 🌡️", min_value=0.0),
    'RH': st.number_input("Relative Humidity (%) 💧", min_value=0.0),
    'wind': st.number_input("Wind Speed (km/h) 💨", min_value=0.0),
    'rain': st.number_input("Rain (mm) 🌧️", min_value=0.0),
    'month_encoded': month_encoder.transform([month])[0],
    'day_encoded': day_encoder.transform([day])[0],
}

# Prediction button and result
if st.button("Predict Fire Area 🔥"):
    input_df = pd.DataFrame([input_data])
    prediction = model.predict(input_df)
    st.markdown(f'<p class="emoji">📏 Predicted Burn Area: {prediction[0]:.2f} ha 🌲🔥</p>', unsafe_allow_html=True)
