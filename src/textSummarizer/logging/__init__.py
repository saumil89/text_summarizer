import os
import sys
import logging

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"
log_dir = 'logs'
log_file = os.path.join(log_dir, 'running_logs.txt')

if not os.path.exists(log_dir):
    os.makedirs(log_file, exist_ok=True)

logging.basicConfig(
    
    level=logging.INFO, 
    format=logging_str,
    handlers=[
        logging.FileHandler(log_file),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger('TextSummerizerLogger')