import streamlit as st
import pandas as pd
import requests
from alpaca.trading.client import TradingClient

with st.form("my_form"):
    ticker = st.text_input("Enter the stock ticker")
    limit = st.number_input("Enter the buy price")
    submit_button = st.form_submit_button("Submit Order")

if submit_button:
    apikey=st.secrets["alpaca_api_key"]
    apisecret=st.secrets["alpaca_api_secret"]
    trading_client = TradingClient(apikey, apisecret, paper=False)
    account = trading_client.get_account()
    st.write(account)