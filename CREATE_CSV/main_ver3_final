import streamlit as st
import pandas as pd
import os
import re

from auth import login


# Function to validate email
def validate_email(email):
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email)



# Set page config
st.set_page_config(page_title="MFT Developer Tool", layout="centered", initial_sidebar_state="collapsed")

# Session state to manage login
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

if st.session_state["logged_in"]:
    # MFT Developer Tool UI
    st.title("MFT Developer Tool")
    #if st.button("Logout1"):
    #        st.session_state["logged_in"] = False

    # Load the file into a DataFrame
    sftp_res_file_path = "sftp_resource.txt"
    df_sftp_res = pd.read_csv(sftp_res_file_path, header=None, names=["Key", "Value"])
    
    ftps_res_file_path = "ftps_resource.txt"
    df_ftps_res = pd.read_csv(ftps_res_file_path, header=None, names=["Key", "Value"])

    networkshare_res_file_path = "networkshare_resource.txt"
    df_networkshare_res = pd.read_csv(networkshare_res_file_path, header=None, names=["Key", "Value"])
    
    azblob_res_file_path = "azblob_resource.txt"
    df_azblob_res = pd.read_csv(azblob_res_file_path, header=None, names=["Key", "Value"])

    sharepoint_res_file_path = "sharepoint_resource.txt"
    df_sharepoint_res = pd.read_csv(sharepoint_res_file_path, header=None, names=["Key", "Value"])

    source_type = st.selectbox("SELECT SOURCE TYPE", ["SFTP", "SHAREPOINT", "AZ_BLOB", "NETWORK_SHARE", "FTPS"])
    target_type = st.selectbox("SELECT TARGET TYPE", ["SFTP", "SHAREPOINT", "AZ_BLOB", "NETWORK_SHARE", "FTPS"])
    pattern = f"{source_type}_TO_{target_type}_TEMPLATE"
    st.write(pattern)


    # Create text input fields for six values
    value1 = st.text_input("INTERFACE")
    value2 = st.text_input("SOURCE SYSTEM")
    value3 = st.text_input("TARGET_SYSTEM")
    #value4 = st.text_input("SOURCE SERVER")

    sftp_as_source = ["SFTP_TO_AZ_BLOB_TEMPLATE", "SFTP_TO_SFTP_TEMPLATE", "SFTP_TO_NETWORK_SHARE_TEMPLATE", "SFTP_TO_SHAREPOINT_TEMPLATE", "SFTP_TO_FTPS_TEMPLATE"]
    ftps_as_source = ["FTPS_TO_AZ_BLOB_TEMPLATE", "FTPS_TO_SFTP_TEMPLATE", "FTPS_TO_NETWORK_SHARE_TEMPLATE", "FTPS_TO_SHAREPOINT_TEMPLATE", "FTPS_TO_FTPS_TEMPLATE"]
    azblob_as_source = ["AZ_BLOB_TO_AZ_BLOB_TEMPLATE", "AZ_BLOB_TO_SFTP_TEMPLATE", "AZ_BLOB_TO_NETWORK_SHARE_TEMPLATE", "AZ_BLOB_TO_SHAREPOINT_TEMPLATE", "AZ_BLOB_TO_FTPS_TEMPLATE"]
    sharepoint_as_source = ["SHAREPOINT_TO_AZ_BLOB_TEMPLATE", "SHAREPOINT_TO_SFTP_TEMPLATE", "SHAREPOINT_TO_NETWORK_SHARE_TEMPLATE", "SHAREPOINT_TO_SHAREPOINT_TEMPLATE", "SHAREPOINT_TO_FTPS_TEMPLATE"]
    networkshare_as_source = ["NETWORK_SHARE_TO_AZ_BLOB_TEMPLATE", "NETWORK_SHARE_TO_SFTP_TEMPLATE", "NETWORK_SHARE_TO_NETWORK_SHARE_TEMPLATE", "NETWORK_SHARE_TO_SHAREPOINT_TEMPLATE", "NETWORK_SHARE_TO_FTPS_TEMPLATE"]    

    if pattern in sftp_as_source:
      # Create a dropdown for column 1 (Key)
        selected_key = st.selectbox("Source Resource Alias", df_sftp_res["Key"])
        value4 = selected_key

      # Auto-populate column 2 (Value) based on selected Key
        if selected_key:
            selected_value = df_sftp_res[df_sftp_res["Key"] == selected_key]["Value"].values[0]
            st.selectbox("Source Server", [selected_value])

    elif pattern in ftps_as_source:
        
      # Create a dropdown for column 1 (Key)
        selected_key = st.selectbox("Source Resource Alias", df_ftps_res["Key"])
        value4 = selected_key

      # Auto-populate column 2 (Value) based on selected Key
        if selected_key:
            selected_value = df_ftps_res[df_ftps_res["Key"] == selected_key]["Value"].values[0]
            st.selectbox("Source Server", [selected_value])

    elif pattern in azblob_as_source:

      # Create a dropdown for column 1 (Key)
        selected_key = st.selectbox("Source Resource Alias", df_azblob_res["Key"])
        value4 = selected_key

      # Auto-populate column 2 (Value) based on selected Key
        if selected_key:
            selected_value = df_azblob_res[df_azblob_res["Key"] == selected_key]["Value"].values[0]
            st.selectbox("Source Server", [selected_value])

    elif pattern in sharepoint_as_source:

      # Create a dropdown for column 1 (Key)
        selected_key = st.selectbox("Source Resource Alias", df_sharepoint_res["Key"])
        value4 = selected_key

      # Auto-populate column 2 (Value) based on selected Key
        if selected_key:
            selected_value = df_sharepoint_res[df_sharepoint_res["Key"] == selected_key]["Value"].values[0]
            st.selectbox("Source Server", [selected_value])
    
    elif pattern in networkshare_as_source:

      # Create a dropdown for column 1 (Key)
        selected_key = st.selectbox("Source Resource Alias", df_networkshare_res["Key"])
        value4 = selected_key

      # Auto-populate column 2 (Value) based on selected Key
        if selected_key:
            selected_value = df_networkshare_res[df_networkshare_res["Key"] == selected_key]["Value"].values[0]
            st.selectbox("Source Server", [selected_value])

    else:
        value4 = st.text_input("SOURCE Resource Alias")

    value5 = st.text_input("SOURCE PATH")

    sftp_as_target = ["SFTP_TO_SFTP_TEMPLATE", "AZ_BLOB_TO_SFTP_TEMPLATE", "FTPS_TO_SFTP_TEMPLATE", "SHAREPOINT_TO_SFTP_TEMPLATE", "NETWORK_SHARE_TO_SFTP_TEMPLATE"]
    azblob_as_target = ["SFTP_TO_AZ_BLOB_TEMPLATE", "AZ_BLOB_TO_AZ_BLOB_TEMPLATE", "FTPS_TO_AZ_BLOB_TEMPLATE", "SHAREPOINT_TO_AZ_BLOB_TEMPLATE", "NETWORK_SHARE_TO_AZ_BLOB_TEMPLATE"]
    sharepoint_as_target = ["SFTP_TO_SHAREPOINT_TEMPLATE", "AZ_BLOB_TO_SHAREPOINT_TEMPLATE", "FTPS_TO_SHAREPOINT_TEMPLATE", "SHAREPOINT_TO_SHAREPOINT_TEMPLATE", "NETWORK_SHARE_TO_SHAREPOINT_TEMPLATE"]
    ftps_as_target = ["SFTP_TO_FTPS_TEMPLATE", "AZ_BLOB_TO_FTPS_TEMPLATE", "FTPS_TO_FTPS_TEMPLATE", "SHAREPOINT_TO_FTPS_TEMPLATE", "NETWORK_SHARE_TO_FTPS_TEMPLATE"]
    networkshare_as_target = ["SFTP_TO_NETWORK_SHARE_TEMPLATE", "AZ_BLOB_TO_NETWORK_SHARE_TEMPLATE", "FTPS_TO_NETWORK_SHARE_TEMPLATE", "SHAREPOINT_TO_NETWORK_SHARE_TEMPLATE", "NETWORK_SHARE_TO_NETWORK_SHARE_TEMPLATE"]

    if pattern in sftp_as_target:
      # Create a dropdown for column 1 (Key)
        selected_key = st.selectbox("Target Resource Alias", df_sftp_res["Key"])
        value6 = selected_key

      # Auto-populate column 2 (Value) based on selected Key
        if selected_key:
            selected_value = df_sftp_res[df_sftp_res["Key"] == selected_key]["Value"].values[0]
            st.selectbox("Target Server", [selected_value])

    elif pattern in ftps_as_target:

      # Create a dropdown for column 1 (Key)
        selected_key = st.selectbox("Target Resource Alias", df_ftps_res["Key"])
        value6 = selected_key

      # Auto-populate column 2 (Value) based on selected Key
        if selected_key:
            selected_value = df_ftps_res[df_ftps_res["Key"] == selected_key]["Value"].values[0]
            st.selectbox("Source Server", [selected_value])

    elif pattern in azblob_as_target:

      # Create a dropdown for column 1 (Key)
        selected_key = st.selectbox("Target Resource Alias", df_azblob_res["Key"])
        value6 = selected_key

      # Auto-populate column 2 (Value) based on selected Key
        if selected_key:
            selected_value = df_azblob_res[df_azblob_res["Key"] == selected_key]["Value"].values[0]
            st.selectbox("Source Server", [selected_value])

    elif pattern in sharepoint_as_target:

      # Create a dropdown for column 1 (Key)
        selected_key = st.selectbox("Target Resource Alias", df_sharepoint_res["Key"])
        value6 = selected_key

      # Auto-populate column 2 (Value) based on selected Key
        if selected_key:
            selected_value = df_sharepoint_res[df_sharepoint_res["Key"] == selected_key]["Value"].values[0]
            st.selectbox("Source Server", [selected_value])

    elif pattern in networkshare_as_target:

      # Create a dropdown for column 1 (Key)
        selected_key = st.selectbox("Target Resource Alias", df_networkshare_res["Key"])
        value6 = selected_key

      # Auto-populate column 2 (Value) based on selected Key
        if selected_key:
            selected_value = df_networkshare_res[df_networkshare_res["Key"] == selected_key]["Value"].values[0]
            st.selectbox("Source Server", [selected_value])


    else:
        value6 = st.text_input("TARGET Resource Alias")


    #value6 = st.text_input("TARGET SERVER")
    value7 = st.text_input("TARGET PATH")
    value8 = st.text_input("Enter your email address")

    # Define the CSV file path
    csv_file_path = "output.csv"

    # Button to submit the inputs

    if st.button("Submit"):
    # Ensure all inputs are provided and not empty
        if all([
            bool(str(pattern)), 
            bool(value1), 
            bool(value2), 
            bool(value3), 
            bool(str(value4)), 
            bool(value5), 
            bool(str(value6)), 
            bool(value7),
            bool(value8)
        ]):
            # Ensure email address is proper
            if value8 and validate_email(value8):
                # Create a DataFrame to write to CSV
                df = pd.DataFrame([
                    ["PATTERN_VALUE", pattern],
                    ["INTERFACE_VALUE", value1],
                    ["SOURCESYSTEM_VALUE", value2],
                    ["TARGETSYSTEM_VALUE", value3],
                    ["SOURCESERVER_VALUE", value4],
                    ["SOURCEPATH_VALUE", value5],
                    ["TARGETSERVER_VALUE", value6],
                    ["TARGETPATH_VALUE", value7],
                    ["EMAIL_ADDRESS", value8]
                ], columns=["Variable", "Value"])

                # Check if the CSV file already exists
                if os.path.isfile(csv_file_path):
                    # Append to the existing CSV file (mode='a' for append)
                    df.to_csv(csv_file_path, index=False, header=False)
                else:
                    # Create a new CSV file
                    df.to_csv(csv_file_path, index=False)

                    #st.success("Values saved to CSV!")
               # REST CALL TO EXECUTE PROJECT

                st.success("Project got created, Please check on admin console and validate the Project")
            
            else:
                st.error("Email adress not correct.")
        else:
            st.error("Please fill in all fields before submitting.")

    if st.button("Logout"):
            st.session_state["logged_in"] = False

else:
    login()

