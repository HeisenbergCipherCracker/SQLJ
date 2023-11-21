import os
import sys
current_directory = os.getcwd()
sys.path.append(current_directory)
from logger.logs import logger
from Exceptions.exceptions import SQLJNGFatalError
from lib.mysqlerrorbased.OPS.OSY import Operatingsystem
from lib.mysqlerrorbased.OPS.Platforms import Platforms
from Exceptions.exceptions import SQLJNGFatalError
from lib.priority.Priority import PRIORITY
from lib.priority.Priority import HARMFULL
from sqlmap import sqlmap


