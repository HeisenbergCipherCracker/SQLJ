import platform
import sys
import os

cur = os.getcwd()
sys.path.append(cur)


class Platforms:
    @staticmethod
    def get_sys():
        # mac: darwin
        #windows = windows
        #linux = linux
        return str(platform.system().lower())
    
# print(Platforms.get_sys())