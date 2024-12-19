
import streamlit as st
import os
from PyPDF2 import PdfReader
from pyairtable import Table
import datetime

PERSONAL_ACCESS_TOKEN = st.secrets["PERSONAL_ACCESS_TOKEN"]
BASE_ID = st.secrets["BASE_ID"]
TABLE_NAME = st.secrets["TABLE_NAME"]  # Replace with your table name


# set environment variable for GROQ API key

airtable = Table(PERSONAL_ACCESS_TOKEN, BASE_ID, TABLE_NAME)

# Create title for WHU MBA Streamlit App
st.title("Registration WHU Speed Networking December 4")

text = ""

# Display initial input form for user details and PDF upload
with st.form("registration_form"):
    name = st.text_input("Please enter your first name and last name")
    email = st.text_input("Please enter your email address")
    # create multiple choice question
    education = st.radio("Please indicate in which WHU program you are participating or have participated:", ("PT MBA", "FT MBA", "Global Online MBA", "Executive MBA", "Executive Education"))
    # user needs to indicate with yes or no if they are a student
    uploaded_file = st.file_uploader("Please upload a PDF of your LinkedIn profile. You can find this PDF by going to your LinkedIn profile page, click on Resources, and click on Save PDF. By uploading the file, you agree that we use and store your LinkedIn profile for the purpose of matchig for the speed networking", type="pdf")
    submit_form = st.form_submit_button("Submit")

# If the form is submitted
if submit_form:
    if uploaded_file is not None:
        # Read the pdf file
        pdf_reader = PdfReader(uploaded_file)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()
        st.session_state.profile = text

        
        record = {"Name": name, "Email": email, "LinkedIn Profile": st.session_state.profile, "Date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "Education": education}
        airtable.create(record)
        st.markdown("**Registration successful. You can now leave the registration.**")
        
    else:
        st.error("Please upload a PDF file.")



