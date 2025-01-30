import logging
import os
from datetime import datetime

''' Define log file name with timestamp'''
LOG_FILE = f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"
logs_path= os.path.join(os.getcwd(),"log",LOG_FILE)

os.makedirs(logs_path, exist_ok=True)  #Create directory if it doesn't exist
LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)


# Configure logginG
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(levelname)s - %(message)s",
    level=logging.INFO,
)




