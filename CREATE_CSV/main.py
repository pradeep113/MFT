import streamlit as st
import pandas as pd
import os
from auth import login

# Set page config
st.set_page_config(page_title="MFT Developer Tool", layout="centered", initial_sidebar_state="collapsed")

# Session state to manage login
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

if st.session_state["logged_in"]:
    # MFT Developer Tool UI
    st.title("MFT Developer Tool")
    if st.button("Logout"):
            st.session_state["logged_in"] = False


    pattern = st.selectbox("SELECT TRANSFER PATTERN", ["SFTP_PULL_TO_INT_SHARE_TEMPLATE", "SFTP_PULL_TO_INT_SHAREPOINT_TEMPLATE", "SFTP_PULL_TO_INT_BLOB_TEMPLATE", "SHARE_PULL_TO_INT_SHAREPOINT_TEMPLATE"])


    # Create text input fields for six values
    value1 = st.text_input("INTERFACE")
    value2 = st.text_input("SOURCE SYSTEM")
    value3 = st.text_input("TARGET_SYSTEM")
    value4 = st.text_input("SOURCE SERVER")
    value5 = st.text_input("SOURCE PATH")
    value6 = st.text_input("TARGET SERVER")
    value7 = st.text_input("TARGET PATH")

    # Define the CSV file path
    csv_file_path = "output.csv"

    # Button to submit the inputs
    if st.button("Submit"):
        # Check if all inputs are provided
        if all([value1, value2, value3, value4, value5]):
            # Create a DataFrame to write to CSV
            df = pd.DataFrame([
	        ["PATTERN_VALUE", pattern],
                ["INTERFACE_VALUE", value1],
	        ["SOURCESYSTEM_VALUE", value2],
                ["TARGETSYSTEM_VALUE", value3],
                ["SOURCESERVER_VALUE", value4],
                ["SOURCEPATH_VALUE", value5],
                ["TARGETSERVER_VALUE", value6],
                ["TARGETPATH_VALUE", value7]
            ], columns=["Variable", "Value"])

            # Check if the CSV file already exists
            if os.path.isfile(csv_file_path):
                # Append to the existing CSV file
                df.to_csv(csv_file_path, index=False)

            else:
                # Create a new CSV file
                df.to_csv(csv_file_path, index=False)

            st.success("Values saved to CSV!")
        else:
            st.error("Please fill in all fields before submitting.")

else:
    login()

