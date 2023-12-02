import os
import sys
current_directory = os.getcwd()

sys.path.append(current_directory)
import socket
from Exceptions.exceptions import SQLJNGGetHostNameError
from logger.logs import logger

def get_ipv4_of_host(target,*args):
    try:
        for arg in args:
            return logger.info(f"ipv4 of the target:{socket.gethostbyname(target),socket.gethostbyname(arg)}")
    except socket.error as e:
        errmsg = ""
        errmsg += "Error in getting hostname:"
        errmsg += str(e)
        logger.error(errmsg)
        raise SQLJNGGetHostNameError

# e,t = get_ipv4_of_host("www.google.com","www.youtube.com")

# print(e)
# print(t)

