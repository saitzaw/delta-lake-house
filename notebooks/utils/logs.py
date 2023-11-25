
import os
import logging 

def havester_logger(log_file_name):
    log_file_path = os.path.abspath(os.path.join(os.getcwd(), "../.."))

    # Create a logger
    logger = logging.getLogger(log_file_name)

    # Set the level of the logger
    logger.setLevel(logging.INFO)

    # Create a FileHandler object and specify the file path
    logger_file_name = "onu_olt_data.log"
    file_path = os.path.join(log_file_path, logger_file_name)
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    file_handler = logging.FileHandler(file_path)

    # Set the format for the log messages
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)

    # Logger handler
    logger.addHandler(file_handler)

    return logger