"""
looking for the  private ipv4:192.168.x.x

"""

import re

def find_ipv4type_private(ip:str)->bool:
    pattern = re.compile(r"^(?:192\.168|10|172\.(?:1[6-9]|2[0-9]|3[0-1]))\.\d{1,3}\.\d{1,3}$")
    if pattern.match(ip):
        return True,"this ip is private"
    
    return False,"this ip is not private"


def find_ipv4_public_is(ip:str)->bool:
    pattern = re.compile(r"^(?:192\.168|10|172\.(?:1[6-9]|2[0-9]|3[0-1]))\.\d{1,3}\.\d{1,3}$")
    if pattern.match(ip):
        return False,"ip is public"
    
    return True,"ip is not public"
    
print(find_ipv4_public_is("172.217.1.4"))
    