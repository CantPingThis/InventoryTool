import logging
import sys
from pathlib import Path

def setup_logger(name='inventory_tool', level=None):
    if level is None:
        logger = logging.getLogger(name)
        logger.setLevel(logging.INFO)

        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s - %(message)s')

        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(logging.INFO)
        console_handler.setFormatter(formatter)

        # Create log directory if it doesn't exist
        log_dir = Path("logs")
        log_dir.mkdir(exist_ok=True)

        file_handler = logging.FileHandler(filename="logs/inventory.log",mode='a')
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(formatter)

        if not logger.handlers:
            logger.addHandler(console_handler)
            logger.addHandler(file_handler)

        return logger
    else:
        # for futur use to have a specific log level for a specific run of the app or module
        return None