import streamlit as st
import subprocess
import os

# Streamlit interface
st.title("SFTP FILE PULL")
tabs = st.tabs(["Input Fields", "File States"])

# Initialize session state variables
if "script_output" not in st.session_state:
    st.session_state.script_output = ""
if "script_error" not in st.session_state:
    st.session_state.script_error = ""
if "script_returncode" not in st.session_state:
    st.session_state.script_returncode = None 


with tabs[0]:
    # Input fields
    arg1 = st.text_input("HOSTNAME", placeholder="Hostname")
    arg2 = st.text_input("PORT", placeholder="Port")
    arg3 = st.text_input("USER NAME", placeholder="User name")
    arg4 = st.text_input("PASSWORD", placeholder="Password", type="password")
    arg5 = st.text_input("REMOTE PATH", placeholder="Remote Path")
    arg6 = st.text_input("LOCAL PATH", placeholder="Local Path")

    # Button to trigger backend script
    if st.button("SUBMIT"):
        if arg1 and arg2 and arg3:
            try:
                # Call the backend Python script with arguments
                result = subprocess.run(
                    ["python3", "sftp_dowbload_files_withargs.py", "--sftp_host", arg1,
                     "--sftp_port", arg2, "--sftp_username", arg3, "--sftp_password", arg4,
                     "--remote_path", arg5, "--local_path", arg6],
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    text=True
                )

		# Save the results to session state
                st.session_state.script_output = result.stdout
                st.session_state.script_error = result.stderr
                st.session_state.script_returncode = result.returncode

                # Display the output
                if result.returncode == 0:
                    st.success("Script executed successfully!")
                    st.text(f"Output:\n{result.stdout}")
                else:
                    st.error("An error occurred while executing the script.")
                    #st.text(f"Error:\n{result.stderr}")
            except Exception as e:
                st.error(f"Failed to execute the script: {e}")
        else:
            st.warning("Please fill in all the required fields.")

with tabs[1]:
    st.write(f"Backend Output:\n{st.session_state['script_output']}")
    st.header("Execution Output & File States")

    # Display backend script output
    if st.session_state.script_returncode is not None:
        if st.session_state.script_returncode == 0:
            st.success("Script executed successfully!")
            st.text(f"Output:\n{st.session_state.script_output}")
        elif st.session_state.script_returncode > 0:
            st.error("An error occurred while executing the script.")
            st.text(f"Error:\n{st.session_state.script_error}")
        else:
            st.error(f"Failed to execute the script: {st.session_state.script_error}")

    # Display the files in the local target directory after execution
    if arg6:
        st.subheader("Target Directory Files (After Transfer):")
        if os.path.exists(arg6):
            target_files = os.listdir(arg6)
            st.text("\n".join(target_files) if target_files else "No files found.")
        else:
            st.warning("Target path does not exist!")   

