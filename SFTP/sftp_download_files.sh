#With logger
#Check file integrity
#download only files, not folder structure 


import os
import paramiko
import hashlib
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Configuration
sftp_host = '192.168.64.8'
sftp_port = 22  # Default SFTP port
sftp_username = 'test'
sftp_password = 'Test@123'
remote_path = 'test'
local_path = 'test'

def calculate_md5(file_path):
    """Calculate MD5 hash of a file."""
    hasher = hashlib.md5()
    with open(file_path, 'rb') as f:
        while chunk := f.read(8192):
            hasher.update(chunk)
    return hasher.hexdigest()

try:
    logger.info("Establishing connection to the SFTP server...")
    # Establish SSH connection
    transport = paramiko.Transport((sftp_host, sftp_port))
    transport.connect(username=sftp_username, password=sftp_password)

    # Open SFTP session
    sftp = paramiko.SFTPClient.from_transport(transport)
    logger.info("SFTP connection established successfully.")

    logger.debug(f"Changing to remote directory: {remote_path}")
    # List files in the remote directory
    file_list = sftp.listdir(remote_path)
    logger.info(f"Files found in remote directory: {file_list}")

    for file in file_list:
        remote_file = os.path.join(remote_path, file)
        local_file = os.path.join(local_path, file)

        logger.info(f"Downloading file: {file}")
        # Download the file
        sftp.get(remote_file, local_file)
        logger.info(f"Downloaded file: {file} to {local_file}")

        # Check file size
        remote_file_size = sftp.stat(remote_file).st_size
        local_file_size = os.path.getsize(local_file)
        logger.debug(f"Remote file size: {remote_file_size}, Local file size: {local_file_size}")

        if remote_file_size != local_file_size:
            logger.error(f"File size mismatch for {file}! (Remote: {remote_file_size}, Local: {local_file_size})")
            continue

        # Check file content (MD5 hash)
        with sftp.open(remote_file, 'rb') as f:
            remote_md5 = hashlib.md5(f.read()).hexdigest()
        local_md5 = calculate_md5(local_file)
        logger.debug(f"Remote MD5: {remote_md5}, Local MD5: {local_md5}")

        if remote_md5 != local_md5:
            logger.error(f"File content mismatch for {file}!")
        else:
            logger.info(f"File integrity verified for {file}.")

    # Close the SFTP session
    sftp.close()
    transport.close()
    logger.info("SFTP connection closed.")

except Exception as e:
    logger.exception(f"An error occurred: {e}")

