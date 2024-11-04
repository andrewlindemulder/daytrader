import streamlit as st
import pandas as pd
import requests

with st.form("my_form"):
    ticker = st.text_input("Enter the stock ticker")
    submit_button = st.form_submit_button("Submit")

if submit_button:
    st.write("You entered: ", ticker)