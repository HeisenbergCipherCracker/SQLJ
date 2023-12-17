import socket
import os,sys

current_directory = os.getcwd()

sys.path.append(current_directory)

from logger.logs import logger

def get_ipv6_address(hostname):
    """
    Function returns ipv6 of target
    Usage
    >>> var = get_ipv6_address(hostname)
    >>> print(var if var is not None else "")
    """
    try:
        # Get IPv6 address information for the given hostname
        result = socket.getaddrinfo(hostname, None, socket.AF_INET6)
        
        # Extract the first IPv6 address from the result
        ipv6_address = result[0][4][0]
        
        return logger.info(f"the host:{hostname} has an ipv6 address:{ipv6_address}")
    except socket.gaierror as e:
        print(f"Error: {e}")
        return None

