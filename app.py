import streamlit as st
import pandas as pd
import joblib

# Load the saved model
MODEL_PATH = "forest_fire_model.joblib"
model = joblib.load(MODEL_PATH)

st.title("Forest Fire Prediction App")
st.write("Input values to predict the forest fire area.")

# User input for prediction
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
}

# Prediction button
if st.button("Predict Area"):
    input_df = pd.DataFrame([input_data])
    prediction = model.predict(input_df)
    st.write(f"Predicted Area: {prediction[0]}")
