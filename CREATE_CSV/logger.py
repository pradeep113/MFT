import logging

# Setup logger
def setup_logger():
    logger = logging.getLogger("auth_logger")
    logger.setLevel(logging.INFO)

    # Prevent adding multiple handlers on rerun
    if not logger.handlers:
        fh = logging.FileHandler("auth.log")
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        logger.addHandler(fh)

    return logger

