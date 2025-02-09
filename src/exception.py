import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.logger import logging

def error_message_details(error, error_detail: sys):
    """Extracts detailed error information including script name, line number, and error message."""
    _, _, exc_tb = error_detail.exc_info()  # Extract traceback info
    file_name = exc_tb.tb_frame.f_code.co_filename  # Get the filename from traceback

    # Correct variable name for error message
    error_message = "Error occurred in python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )
    return error_message  # Return the formatted error message

class CustomException(Exception):
    """Custom exception class to provide detailed error messages."""
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)  # Call the base exception class initializer
        self.error_message = error_message_details(error_message, error_detail)  # Call the function directly
        
    def __str__(self):
        return self.error_message  # Return the detailed error message when the exception is printed

