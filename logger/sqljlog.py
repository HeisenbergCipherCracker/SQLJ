import logging
import colorlog

#Reference:https://stackoverflow.com/questions/39718895/python-multiple-logger-for-multiple-modules
logger = logging.getLogger('sqljnglog')
logger.setLevel(logging.INFO)

formatter = colorlog.ColoredFormatter(
    "[%(asctime)s] [%(log_color)s%(levelname)s%(reset)s] %(log_color)s%(message)s%(reset)s",
    datefmt="%H:%M:%S",
    log_colors={
        'DEBUG': 'cyan',
        'INFO': 'blue,bold',
        'WARNING': 'yellow',
        'ERROR': 'red,bold',
        'CRITICAL': 'red,bg_white,bold',
    },
    style='%'
)


console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)

logger.addHandler(console_handler)

# Log an info message with the default message
# logger.critical('Testing connection to the target URL')
