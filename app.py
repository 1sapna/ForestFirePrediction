import streamlit as st
import pandas as pd
import joblib
from sklearn.preprocessing import LabelEncoder

# Load model
model = joblib.load("forest_fire_model.joblib")

# Encoding for 'month' and 'day' (same as in training)
month_encoder = LabelEncoder().fit(['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec'])
day_encoder = LabelEncoder().fit(['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun'])

# Streamlit UI for inputs
st.title("Forest Fire Prediction App")
month = st.selectbox("Select Month", month_encoder.classes_)
day = st.selectbox("Select Day", day_encoder.classes_)

input_data = {
    'X': st.number_input("X Coordinate", min_value=0.0),
    'Y': st.number_input("Y Coordinate", min_value=0.0),
    'FFMC': st.number_input("FFMC", min_value=0.0),
    'DMC': st.number_input("DMC", min_value=0.0),
    'DC': st.number_input("DC", min_value=0.0),
    'ISI': st.number_input("ISI", min_value=0.0),
    'temp': st.number_input("Temperature (°C)", min_value=0.0),
    'RH': st.number_input("Relative Humidity (%)", min_value=0.0),
    'wind': st.number_input("Wind Speed (km/h)", min_value=0.0),
    'rain': st.number_input("Rain (mm)", min_value=0.0),
    'month_encoded': month_encoder.transform([month])[0],
    'day_encoded': day_encoder.transform([day])[0],
}

# Prediction
if st.button("Predict Area"):
    input_df = pd.DataFrame([input_data])
    prediction = model.predict(input_df)
    st.write(f"Predicted Area: {prediction[0]}")

