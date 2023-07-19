# To log all the executions

import logging
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

#In the current working directory the 'logs' file is created
logs_path = os.path.join(os.getcwd(), "logs", LOG_FILE)

#Make directory and append the files
os.mkdirs(logs_path,exist_ok = True)

LOG_FILE_PATH=os.path.join(logs_path, LOG_FILE)

#overriding the logging function
logging.basicConfig(

    filename = LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s ",
    level=logging.INFO


)