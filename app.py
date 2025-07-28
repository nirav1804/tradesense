# app.py
import streamlit as st
import pandas as pd
import os

st.title("📈 TradeSense - Nifty Data Viewer")

file_path = "data/latest_data.csv"

if os.path.exists(file_path):
    df = pd.read_csv(file_path)
    st.success("✅ Live data loaded.")
    st.dataframe(df)
else:
    st.warning("⚠️ Data not found. Please wait for auto-update or run the action manually.")
