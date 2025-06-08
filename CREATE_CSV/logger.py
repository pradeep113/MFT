# logger.py
import logging

# Configure logging settings
logging.basicConfig(
    filename="logs/streamlit_app.log",  # Log file name
    level=logging.DEBUG,  # Logging level
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)

def get_logger(name):
    """Returns a logger instance."""
    logger = logging.getLogger(name)
    return logger

