import streamlit as st
import pandas as pd
import requests

with st.form("my_form"):
    name = st.text_input("Enter your name")
    age = st.number_input("Enter your age")
    submit_button = st.form_submit_button("Submit")

if submit_button:
    st.write("Hello,", name, "you are", age, "years old.")