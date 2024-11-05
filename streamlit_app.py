import streamlit as st
import pandas as pd
import requests
import math
from alpaca.trading.client import TradingClient
from alpaca.trading.requests import LimitOrderRequest
from alpaca.trading.enums import OrderSide, TimeInForce

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
        trading_client = TradingClient(apikey, apisecret, paper=True)
        account = trading_client.get_account()

        purchase_qty = math.floor((float(account.buying_power) / float(limit)) * 100)/100.0

        limit_order_data = LimitOrderRequest(
                    symbol="TSLA",
                    limit_price=100,
                    notional=200,
                    side=OrderSide.BUY,
                    time_in_force=TimeInForce.DAY
                   )

        limit_order = trading_client.submit_order(
                order_data=limit_order_data
              )
        st.write(limit_order)