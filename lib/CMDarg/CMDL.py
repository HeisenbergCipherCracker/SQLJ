import os
import sys


current_directory = os.getcwd()

sys.path.append(current_directory)

from Exceptions.exceptions import SQLJNGInvalidArgumentError
import platform as Osdetection 

class CmdLine:
    def __init__(self,cmd):
        self.cmd = cmd
        self.args = []
        self.options = {}

    def _get_os_info(self):
        return Osdetection.system().lower()
    
    
    
    
        
