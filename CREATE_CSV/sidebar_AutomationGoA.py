import streamlit as st
import pandas as pd
import os
import re
import datetime

from auth import login


# Function to validate email
def validate_email(email):
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email)

#Load all file into Dataframe
def load_file_dataframe():
    # Load the file into a DataFrame
    sftp_res_file_path = "resources/sftp_resource.txt"
    df_sftp_res = pd.read_csv(sftp_res_file_path, header=None, names=["Key", "Value"])

    ftps_res_file_path = "resources/ftps_resource.txt"
    df_ftps_res = pd.read_csv(ftps_res_file_path, header=None, names=["Key", "Value"])

    networkshare_res_file_path = "networkshare_resource.txt"
    df_networkshare_res = pd.read_csv(networkshare_res_file_path, header=None, names=["Key", "Value"])

    azblob_res_file_path = "resources/azblob_resource.txt"
    df_azblob_res = pd.read_csv(azblob_res_file_path, header=None, names=["Key", "Value"])

    sharepoint_res_file_path = "resources/sharepoint_resource.txt"
    df_sharepoint_res = pd.read_csv(sharepoint_res_file_path, header=None, names=["Key", "Value"])

    # Return all the DataFrames
    return df_sftp_res, df_ftps_res, df_networkshare_res, df_azblob_res, df_sharepoint_res

#Load all variables
def load_variables():
    sftp_as_source = ["SFTP_TO_AZ_BLOB_TEMPLATE", "SFTP_TO_SFTP_TEMPLATE", "SFTP_TO_NETWORK_SHARE_TEMPLATE", "SFTP_TO_SHAREPOINT_TEMPLATE", "SFTP_TO_FTPS_TEMPLATE"]
    ftps_as_source = ["FTPS_TO_AZ_BLOB_TEMPLATE", "FTPS_TO_SFTP_TEMPLATE", "FTPS_TO_NETWORK_SHARE_TEMPLATE", "FTPS_TO_SHAREPOINT_TEMPLATE", "FTPS_TO_FTPS_TEMPLATE"]
    azblob_as_source = ["AZ_BLOB_TO_AZ_BLOB_TEMPLATE", "AZ_BLOB_TO_SFTP_TEMPLATE", "AZ_BLOB_TO_NETWORK_SHARE_TEMPLATE", "AZ_BLOB_TO_SHAREPOINT_TEMPLATE", "AZ_BLOB_TO_FTPS_TEMPLATE"]
    sharepoint_as_source = ["SHAREPOINT_TO_AZ_BLOB_TEMPLATE", "SHAREPOINT_TO_SFTP_TEMPLATE", "SHAREPOINT_TO_NETWORK_SHARE_TEMPLATE", "SHAREPOINT_TO_SHAREPOINT_TEMPLATE", "SHAREPOINT_TO_FTPS_TEMPLATE"]
    networkshare_as_source = ["NETWORK_SHARE_TO_AZ_BLOB_TEMPLATE", "NETWORK_SHARE_TO_SFTP_TEMPLATE", "NETWORK_SHARE_TO_NETWORK_SHARE_TEMPLATE", "NETWORK_SHARE_TO_SHAREPOINT_TEMPLATE", "NETWORK_SHARE_TO_FTPS_TEMPLATE"]

    sftp_as_target = ["SFTP_TO_SFTP_TEMPLATE", "AZ_BLOB_TO_SFTP_TEMPLATE", "FTPS_TO_SFTP_TEMPLATE", "SHAREPOINT_TO_SFTP_TEMPLATE", "NETWORK_SHARE_TO_SFTP_TEMPLATE"]
    azblob_as_target = ["SFTP_TO_AZ_BLOB_TEMPLATE", "AZ_BLOB_TO_AZ_BLOB_TEMPLATE", "FTPS_TO_AZ_BLOB_TEMPLATE", "SHAREPOINT_TO_AZ_BLOB_TEMPLATE", "NETWORK_SHARE_TO_AZ_BLOB_TEMPLATE"]
    sharepoint_as_target = ["SFTP_TO_SHAREPOINT_TEMPLATE", "AZ_BLOB_TO_SHAREPOINT_TEMPLATE", "FTPS_TO_SHAREPOINT_TEMPLATE", "SHAREPOINT_TO_SHAREPOINT_TEMPLATE", "NETWORK_SHARE_TO_SHAREPOINT_TEMPLATE"]
    ftps_as_target = ["SFTP_TO_FTPS_TEMPLATE", "AZ_BLOB_TO_FTPS_TEMPLATE", "FTPS_TO_FTPS_TEMPLATE", "SHAREPOINT_TO_FTPS_TEMPLATE", "NETWORK_SHARE_TO_FTPS_TEMPLATE"]
    networkshare_as_target = ["SFTP_TO_NETWORK_SHARE_TEMPLATE", "AZ_BLOB_TO_NETWORK_SHARE_TEMPLATE", "FTPS_TO_NETWORK_SHARE_TEMPLATE", "SHAREPOINT_TO_NETWORK_SHARE_TEMPLATE", "NETWORK_SHARE_TO_NETWORK_SHARE_TEMPLATE"]

    return sftp_as_source, ftps_as_source, azblob_as_source, sharepoint_as_source, networkshare_as_source, sftp_as_target, ftps_as_target, azblob_as_target, sharepoint_as_target, networkshare_as_target



#Action on Submit Button
def on_submit():
    # Define the CSV file path
    csv_file_path = "uidata/flowdata.csv"
    # Ensure all inputs are provided and not empty
    if all([
        bool(value1),
        bool(value2),
        bool(value3),
        bool(str(value4)),
        bool(value5),
        bool(str(value6)),
        bool(value7),
        bool(value8),
        bool(str(value9)),
        bool(value10)
    ]):
        # Ensure email address is proper
        if value8 and validate_email(value8):
            # Create a DataFrame to write to CSV
            df = pd.DataFrame([
                ["INTERFACE_VALUE", value1],
                ["SOURCESYSTEM_VALUE", value2],
                ["TARGETSYSTEM_VALUE", value3],
                ["SOURCESERVER_VALUE", value4],
                ["SOURCEPATH_VALUE", value5],
                ["TARGETSERVER_VALUE", value6],
                ["TARGETPATH_VALUE", value7],
                ["EMAIL_ADDRESS", value8],
                ["PATTERN_VALUE", value9],
                ["DESCRIPTION_VALUE", value10],
                ["ARCHIVE_VALUE", value11],
                ["ARCHIVE_PATH_VALUE", value12]
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



#_____________________________________________________________________________________________________________
def initiate():
    global value1, value2, value3, value3, value4, value5, value5, value6, value7, value8, value9, value10, value11, value12    
# App Title
    st.title("🌟 GoAnywhere MFT Dev Tool")
    st.text("")
    # Load all files and variables
    df_sftp_res, df_ftps_res, df_networkshare_res, df_azblob_res, df_sharepoint_res = load_file_dataframe()
    sftp_as_source, ftps_as_source, azblob_as_source, sharepoint_as_source, networkshare_as_source, sftp_as_target, ftps_as_target, azblob_as_target, sharepoint_as_target, networkshare_as_target = load_variables()

    #Container 1 have Partner type detail and Resource Alias 
    with st.container():
        st.subheader("Select Resource Types")
        col1, col2, col3 = st.columns(3)  # Use three columns for better alignment

        with col1:
            source_type = st.selectbox("SELECT SOURCE TYPE", ["SFTP", "SHAREPOINT", "AZ_BLOB", "NETWORK_SHARE", "FTPS"])
            target_type = st.selectbox("SELECT TARGET TYPE", ["SFTP", "SHAREPOINT", "AZ_BLOB", "NETWORK_SHARE", "FTPS"])
            #source_alias = st.selectbox("Source Resource Alias:", ["EXT_SFTP_Partner1", "EXT_SFTP_Partner2"])
            pattern = f"{source_type}_TO_{target_type}_TEMPLATE"


        with col2:
            #target_alias = st.selectbox("Target Resource Alias:", ["AZ_blob_Partner1", "AZ_blob_Partner2"])
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


        with col3:
            #target_alias = st.selectbox("Target Resource Alias:", ["AZ_blob_Partner1", "AZ_blob_Partner2"])
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


    st.text("")
    #Container 3 have Configuration detail Paths email .
    with st.container():
        st.subheader("Configuration Details")
        # Split inputs into multiple columns for better alignment
        col1, col2, col3 = st.columns(3)
    
        with col1:
            value1 = st.text_input("INTERFACE")
            value8 = st.text_input("EMAIL ADDRESS")

        with col2:
            value2 = st.text_input("SOURCE SYSTEM")
            value5 = st.text_input("SOURCE PATH")
    
        with col3:
            value3 = st.text_input("TARGET SYSTEM")
            value7 = st.text_input("TARGET PATH")

    st.text("")
    #Expander have additional non mandate details
    with st.expander("Advanced Settings"):  # Use expanders for optional settings
        value9 = st.text_input("File Pattern", "*.*")
        value10 = st.text_input("DESCRIPTION", pattern)
    # Checkbox for Archive
        archive_checked = st.checkbox("Archive")  # Checkbox input

    # Store archive value based on user selection
        value11 = "YES" if archive_checked else "NO"

        # If archive is checked, show Archive Path input field
        if value11 == "YES":
            value12 = st.text_input("Enter Archive Path")
        else:
            value12 = "None"  # No archive path required


    # Submit and Logout Buttons
    col1, col2 = st.columns(2)

    with col1:
        # Button to submit the inputs
        if st.button("Submit"):
            on_submit()


    with col2:
        if st.button("Logout"):
           st.session_state["logged_in"] = False



# Footer
    st.markdown("---")
    # Get the current date
    current_date = datetime.date.today().strftime("%B %d, %Y")  # Format as "Month Day, Year"
    st.caption(f"Developed by: Pradeep | Streamlit | Version: 1.0 🚀 | GoAnywhere Developer Tool | Date: {current_date}")

#______CREATE WBUSER________________________________________________________________________________________________
def create_webuser():
    st.write("CRETAE WEBUSER SECTION")
    # App Title
    st.title("WEBUSER CREATION")
    st.text("")    
    webuser_protocol = st.selectbox("PROTOCOL TEMPLATE:", ["SFTP", "FTPS",])
    if webuser_protocol == "SFTP":
        with st.container():
            webuser_name = st.text_input("Webuser Name")
            description = st.text_input("Description")

    with st.expander("Folder Settings"):  # Use expanders for optional settings


        # Step 1: Ask user how many folders to create
        num_folders = st.number_input("How many folders do you want to create?", min_value=1, max_value=20, step=1)

        # Step 2: Initialize session state for folder names and permissions
        if "folder_data" not in st.session_state or len(st.session_state.folder_data) != num_folders:
            st.session_state.folder_data = [
                {"name": "", "read": False, "write": False, "execute": False}
                for _ in range(num_folders)
            ]  

        # Step 3: Dynamically create inputs
        st.markdown("### Enter folder names and set permissions:")
        for i in range(num_folders):
            col1, col2, col3, col4 = st.columns([2, 1, 1, 1])
            with col1:
                st.session_state.folder_data[i]["name"] = st.text_input(f"Folder {i+1}", value=st.session_state.folder_data[i]["name"])
            with col2:
                st.session_state.folder_data[i]["read"] = st.checkbox("Read", key=f"read_{i}", value=st.session_state.folder_data[i]["read"])
            with col3:
                st.session_state.folder_data[i]["write"] = st.checkbox("Write", key=f"write_{i}", value=st.session_state.folder_data[i]["write"])
            with col4:
                st.session_state.folder_data[i]["execute"] = st.checkbox("Execute", key=f"exec_{i}", value=st.session_state.folder_data[i]["execute"])
            with col4:
                st.session_state.folder_data[i]["execute"] = st.checkbox("Execute", key=f"e_{i}", value=st.session_state.folder_data[i]["execute"])
            with col4:
                st.session_state.folder_data[i]["execute"] = st.checkbox("Execute", key=f"exc_{i}", value=st.session_state.folder_data[i]["execute"])
            with col4:
                st.session_state.folder_data[i]["execute"] = st.checkbox("Execute", key=f"exe_{i}", value=st.session_state.folder_data[i]["execute"])
            with col4:
                st.session_state.folder_data[i]["execute"] = st.checkbox("Execute", key=f"exewc_{i}", value=st.session_state.folder_data[i]["execute"])

    

        # Step 4: Display summary
        st.markdown("### 📁 Folder Summary")
        for i, folder in enumerate(st.session_state.folder_data):
            perms = [perm for perm in ["read", "write", "execute"] if folder[perm]]
            st.write(f"{i+1}. **{folder['name']}** → Permissions: {', '.join(perms) if perms else 'None'}")


   
#______CREATE RESOURCE_____________________________________________________________________________________________
def create_resource():
    # App Title
    st.title("RESOURCE CREATION")
    st.text("")

    resource_type_selected = st.selectbox("Select Resource Type:", ["SFTP", "Network Share", "Azure Blob", "FTPS"])

    if resource_type_selected == "SFTP":
        with st.container():
            resource_name = st.text_input("Resource Name")
            description = st.text_input("Description")
            Hostname = st.text_input("Host name")
            Port = st.text_input("Port")
            sftpUsername = st.text_input("User name")
        
#___________________________________________________________________________________________________________________
# Page Configuration
    #st.set_page_config(page_title="GoAnywhere MFT Dev Tool", layout="wide")



# Session state to manage login
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False# Group Inputs into Sections

if st.session_state["logged_in"]:
    #Sidebar title
    st.sidebar.title("Navigation")

    # Sidebar widgets
    workflow_options = st.sidebar.selectbox("Workflow Creation:", ["Create Webuser", "Create Resource", "Create Project"])
   
    # Main content
    if workflow_options == "Create Webuser":
        create_webuser()
    if workflow_options == "Create Resource":
        create_resource()
    if workflow_options == "Create Project":
        initiate()


else:
    login()
