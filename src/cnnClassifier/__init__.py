import os
import sys
import logging

logging_str = '[%(asctime)s]: - %(filename)s\nAt Module - %(module)s\n%(message)s\nline number - %(lineno)s'


log_dir = 'logs'
log_filepath = os.path.join(log_dir,"saved_logs.log")
os.makedirs(log_dir,exist_ok=True)

logging.basicConfig(
    level= logging.INFO,
    format = logging_str,
    
    handlers= [
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger('cnnClassifier')