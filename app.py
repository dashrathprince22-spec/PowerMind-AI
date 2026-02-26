import streamlit as st
import pandas as pd
from data_generator import generate_data
from model import train_model
from optimization import detect_waste

st.title("PowerMind AI - Energy Optimization Dashboard")

df = generate_data()
df = train_model(df)
df, total_waste, money_saved, co2_reduced = detect_waste(df)

st.subheader("Actual vs Predicted Energy Usage")
st.line_chart(df[["actual_kwh", "predicted_kwh"]])

st.subheader("Impact Metrics")
st.metric("Total Energy Waste (kWh)", round(total_waste, 2))
st.metric("Money Saved (₹)", round(money_saved, 2))
st.metric("CO₂ Reduced (kg)", round(co2_reduced, 2))

st.subheader("Anomaly Points")
st.write(df[df["anomaly"] == 1][["timestamp", "actual_kwh", "predicted_kwh", "waste_kwh"]])
