#Download files with same folder structure to local .
#check File Integrity - Size and Checksum

import os
import paramiko
import hashlib
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Configuration
sftp_host = ''
sftp_port = 22  # Default SFTP port
sftp_port = 22  # Default SFTP port
sftp_username = 'test'
sftp_password = 'Test@123'
remote_root = 'test'  # Root directory on SFTP server
local_root = 'test'    # Root directory on your local machine

def calculate_md5(file_path):
    """Calculate MD5 hash of a file."""
    hasher = hashlib.md5()
    with open(file_path, 'rb') as f:
        while chunk := f.read(8192):
            hasher.update(chunk)
    return hasher.hexdigest()

def download_and_verify(sftp, remote_dir, local_dir):
    """
    Recursively download files from the SFTP server while preserving the folder structure.
    Verifies file size and MD5 checksum for integrity.
    """
    if not os.path.exists(local_dir):
        os.makedirs(local_dir)  # Create local directory if it doesn't exist
        logger.info(f"Created directory: {local_dir}")

    # List items in the remote directory
    for item in sftp.listdir_attr(remote_dir):
        remote_path = os.path.join(remote_dir, item.filename)
        local_path = os.path.join(local_dir, item.filename)

        if item.st_mode & 0o40000:  # Check if it's a directory
            logger.info(f"Entering directory: {remote_path}")
            download_and_verify(sftp, remote_path, local_path)  # Recursive call for subdirectories
        else:
            logger.info(f"Downloading file: {remote_path} to {local_path}")
            sftp.get(remote_path, local_path)  # Download the file

            # Verify file size
            remote_file_size = item.st_size
            local_file_size = os.path.getsize(local_path)
            if remote_file_size != local_file_size:
                logger.error(f"File size mismatch for {remote_path}! (Remote: {remote_file_size}, Local: {local_file_size})")
                continue

            # Verify file content (MD5 checksum)
            with sftp.open(remote_path, 'rb') as remote_file:
                remote_md5 = hashlib.md5(remote_file.read()).hexdigest()
            local_md5 = calculate_md5(local_path)
            if remote_md5 != local_md5:
                logger.error(f"File content mismatch for {remote_path}! (Remote MD5: {remote_md5}, Local MD5: {local_md5})")
            else:
                logger.info(f"File integrity verified for {remote_path}.")

try:
    logger.info("Establishing connection to the SFTP server...")
    # Establish SSH connection
    transport = paramiko.Transport((sftp_host, sftp_port))
    transport.connect(username=sftp_username, password=sftp_password)

    # Open SFTP session
    sftp = paramiko.SFTPClient.from_transport(transport)
    logger.info("SFTP connection established.")

    # Start downloading files from the remote root directory
    download_and_verify(sftp, remote_root, local_root)

    # Close the SFTP session
    sftp.close()
    transport.close()
    logger.info("SFTP connection closed. Files downloaded successfully!")

except Exception as e:
    logger.exception(f"An error occurred: {e}")

