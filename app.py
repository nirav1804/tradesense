import streamlit as st
import pandas as pd
from ai_logic import generate_signals

st.set_page_config(page_title="TradeSense AI", layout="centered")
st.title("📈 TradeSense - AI Signal Dashboard")

try:
    df = pd.read_csv("data/latest_data.csv")
    result = generate_signals(df)
    st.dataframe(result)
except Exception as e:
    st.error(f"Error loading data: {e}")
