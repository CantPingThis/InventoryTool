# Test in Python
from logger import setup_logger

logger = setup_logger('test')
logger.info("This is an info message")
logger.debug("This is a debug message - only in file")
logger.warning("This is a warning")
logger.error("This is an error")