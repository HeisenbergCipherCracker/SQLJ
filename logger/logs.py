import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

logger = logging.getLogger('my_logger')

console_handler = logging.StreamHandler()
logger.addHandler(console_handler)