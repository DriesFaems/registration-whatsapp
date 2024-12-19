
import streamlit as st
from pyairtable import Table
import datetime

PERSONAL_ACCESS_TOKEN = st.secrets["PERSONAL_ACCESS_TOKEN"]
BASE_ID = st.secrets["BASE_ID"]
TABLE_NAME = st.secrets["TABLE_NAME"]  # Replace with your table name


# set environment variable for GROQ API key

airtable = Table(PERSONAL_ACCESS_TOKEN, BASE_ID, TABLE_NAME)

# Create title for WHU MBA Streamlit App
st.title("Registration WhatsApp Group WHU GenAI Builders Club")

text = ""

# Display initial input form for user details and PDF upload
with st.form("registration_form"):
    name = st.text_input("Please enter your first name and last name")
    phone = st.text_input("Please provide your phone number")
    submit_form = st.form_submit_button("Submit")

# If the form is submitted and phone number is provided, send a message to the user

if submit_form and phone:
    record = {"Name": name, "Phone": phone}
    airtable.create(record)
    st.markdown("**Registration successful. You can now leave the registration.**")
        
else:
    st.error("Please provide your phone number to register for the WhatsApp group.")



