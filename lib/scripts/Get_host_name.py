import socket
import asyncio
import requests
from datetime import datetime
from colorama import Fore,init

init()

async def Get_host_name(Host):

    # Get the hostname
    # hostname = socket.gethostname()
    try:
        # Get the IP address associated with the hostname
        ip_address = socket.gethostbyname(Host)
        check = requests.get(ip_address)
        if check.status_code == 200:
            print(f"[{datetime.now()}]",Fore.GREEN + f"Host:{Host} is up with the ip address of: {ip_address}")
            
        else:
            print(f"[{datetime.now()}]",Fore.RED + f"Host:{Host} is down")
    
    except socket.error as e:
        print(f"[{datetime.now()}]",e)
        
    except KeyboardInterrupt:
        pass
    except ConnectionError:
        print(Fore.RED+f"[ERROR] An Error occurred with the program:"+"connection Error,please check your connection")
        
    
# asyncio.run(Get_host_name("www.google.com"))