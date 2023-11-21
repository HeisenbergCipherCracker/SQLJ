import os
import sys
current_directory = os.getcwd()
sys.path.append(current_directory)
from Exceptions.exceptions import SQLJNGFatalError
from Exceptions.exceptions import SQLJNGInstallationError
from Exceptions.exceptions import SQLJNGModuleError
from logger.logs import logger

def Operatingsystem():

    try:
        import platform
        plat = platform.system()
        return plat
        

    except ImportError as ex:
        logger.error(str(ex))
        raise SQLJNGModuleError(str(ex))
