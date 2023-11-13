import logging
add_directory = os.path.abspath(os.path.dirname(__file__))

priority_path = os.path.join(add_directory, '..', 'priority')

sys.path.append(priority_path)


from Priority import PRIORITY, HARMFULL

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

logger = logging.getLogger('my_logger')

console_handler = logging.StreamHandler()
logger.addHandler(console_handler)