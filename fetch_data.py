# fetch_data.py
import yfinance as yf
import pandas as pd
from datetime import datetime
import os

def fetch_nifty_data():
    ticker = "^NSEI"
    df = yf.download(ticker, period="5d", interval="1d")
    df.reset_index(inplace=True)

    # Save to data folder
    os.makedirs("data", exist_ok=True)
    df.to_csv("data/latest_data.csv", index=False)
    print("Data saved successfully.")

if __name__ == "__main__":
    fetch_nifty_data()
