import streamlit as st
import pandas as pd
import requests
from alpaca.trading.client import TradingClient

with st.form("my_form"):
    ticker = st.text_input("Enter the stock ticker")
    limit = st.number_input("Enter the buy price")
    submit_button = st.form_submit_button("Submit Order")

if submit_button:
    if not ticker:
        st.write("Ticker is required")
    if not limit:
        st.write("Limit is required")
    else:
        apikey=st.secrets["alpaca_api_key"]
        apisecret=st.secrets["alpaca_api_secret"]
        trading_client = TradingClient(apikey, apisecret, paper=False)
        account = trading_client.get_account()
        st.write(account.buying_power)