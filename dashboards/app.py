import streamlit as st
import pandas as pd
import joblib
import os

# Page Configuration
st.set_page_config(page_title="IoT Smoke Detection System", page_icon="🔥", layout="centered")

# Title and Description
st.title("🔥 IoT Fire Alarm Detection System")
st.markdown("This dashboard predicts **Fire Alarm Status** using IoT sensor data based on your Random Forest model.")
st.write("---")

# Sidebar - User Inputs
st.sidebar.header("Sensor Inputs")

def user_input_features():
    # Key Sensors (High Correlation)
    temperature = st.sidebar.slider("Temperature [C]", -10.0, 50.0, 25.0)
    humidity = st.sidebar.slider("Humidity [%]", 0.0, 100.0, 50.0)
    tvoc = st.sidebar.slider("TVOC [ppb] (Volatile Organic Compounds)", 0, 60000, 100)
    eco2 = st.sidebar.slider("eCO2 [ppm]", 400, 60000, 400)
    
    # Other Technical Sensors
    raw_h2 = st.sidebar.number_input("Raw H2", 10000, 15000, 12000)
    raw_ethanol = st.sidebar.number_input("Raw Ethanol", 15000, 22000, 19000)
    pressure = st.sidebar.number_input("Pressure [hPa]", 930.0, 940.0, 939.0)
    
    # Particulate Matter Sensors (Usually increase during fire)
    pm1_0 = st.sidebar.slider("PM1.0", 0.0, 15000.0, 1.0)
    pm2_5 = st.sidebar.slider("PM2.5", 0.0, 15000.0, 1.0)
    nc0_5 = st.sidebar.number_input("NC0.5", 0.0, 50000.0, 10.0)
    nc1_0 = st.sidebar.number_input("NC1.0", 0.0, 50000.0, 2.0)
    nc2_5 = st.sidebar.number_input("NC2.5", 0.0, 50000.0, 0.5)

    # Prepare Data Frame (Matching the model's expected column order)
    data = {
        'Temperature[C]': temperature,
        'Humidity[%]': humidity,
        'TVOC[ppb]': tvoc,
        'eCO2[ppm]': eco2,
        'Raw H2': raw_h2,
        'Raw Ethanol': raw_ethanol,
        'Pressure[hPa]': pressure,
        'PM1.0': pm1_0,
        'PM2.5': pm2_5,
        'NC0.5': nc0_5,
        'NC1.0': nc1_0,
        'NC2.5': nc2_5
    }
    features = pd.DataFrame(data, index=[0])
    return features

# Get User Input
input_df = user_input_features()

# Display Inputs on Main Screen
st.subheader("Current Sensor Readings")
st.dataframe(input_df)

# Model Loading Logic
# Note: The model is in the 'models' directory, one level up from 'dashboards'.
model_path = os.path.join(os.path.dirname(__file__), '..', 'models', 'smoke_detection_model.pkl')

try:
    model = joblib.load(model_path)
    
    # PREDICTION BUTTON
    if st.button("🚨 Analyze Status"):
        prediction = model.predict(input_df)
        probability = model.predict_proba(input_df)
        
        st.write("---")
        st.subheader("Prediction Result:")
        
        if prediction[0] == 1:
            st.error(f"**FIRE DETECTED!** (Confidence: {probability[0][1]*100:.2f}%)")
            st.image("https://media.giphy.com/media/3o6ozh46EbuWRYAcSY/giphy.gif", width=300)
        else:
            st.success(f"**Environment is Safe.** (Confidence: {probability[0][0]*100:.2f}%)")
            st.balloons()
            
except FileNotFoundError:
    st.error("Model file not found! Please ensure 'models/smoke_detection_model.pkl' exists.")
    st.warning(f"Looking at path: {model_path}")
