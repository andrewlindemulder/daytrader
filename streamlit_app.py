import streamlit as st
import pandas as pd
import requests

with st.form("my_form"):
    ticker = st.text_input("Enter the stock ticker")
    limit = st.number_input("Enter your age", step="4")
    submit_button = st.form_submit_button("Submit")

if submit_button:
    st.write("Hello,", ticker, "you are", limit, "years old.")