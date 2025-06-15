# app.py
import streamlit as st

st.title("Water Quality Index Dashboard")
st.write("Welcome! This is a simple dashboard for WQI prediction.")

# Example inputs
pH = st.slider("Select pH value", 0.0, 14.0, 7.0)
do = st.number_input("Enter Dissolved Oxygen (mg/L)", value=6.0)

# Dummy WQI calculation
wqi = (pH * 10 + do * 5) / 2
st.metric("Predicted WQI", round(wqi, 2))
