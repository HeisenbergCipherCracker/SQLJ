import sys
import sys
import sys
import os
from colorama import Style
import threading
import requests
import asyncio
import sys
import os
from lib.scripts.authbypass_inj import htmlpattern
from lib.scripts.Error_based_injection import *
from lib.scripts.genericSQL import *
from lib.scripts.Time_based_Header_inj import *
from lib.scripts.Auth_bypass_inj_with_HEADERS import *
from lib.scripts.Unionselect import *
from lib.scripts.Memmoryerr import *
from lib.scripts.Headers_added_in_used_UNION_SELECT_ATTACK import *
from lib.scripts.Headers_added_in_used_UNION_SELECT_ATTACK import *
from lib.scripts.Generic_SQL_with_header import *
from lib.scripts.Get_host_name import *
from lib.scripts.AccessDatabase import *
from lib.scripts.Backend_language import *
from lib.scripts.Time_based_Header_inj import *
from lib.scripts.database import *
from lib.scripts.Hackgpt import *
from lib.scripts.Backend_language import *
from lib.scripts.authbypass_inj import *
from lib.scripts.Error_based_inj_with_headers import *
from lib.scripts.Timebasedinj import *
from Core.Socketapi.findports import Find_open_ports_of_the_target




"""Tested against: http://testphp.vulnweb.com/disclaimer.php """

init()

Style.BRIGHT


logo = """
   _____ ____    __        __
  / ___// __ \  / /       / /
  \__ \/ / / / / /   __  / / 
 ___/ / /_/ / / /___/ /_/ /  
/____/\___\_\/_____/\____/   
                             

"""

options = """
Pre-release 1.0
1.authbypassSQL
2.ErrorbasedINJection
3.GenericSQL
4.TimebasedSQL
5.UNIONselect

"""

# url = None

async def main():
    global host
    """The main function and the user side of the program."""
    try:
        # while Tr
        global logo,options #*Declare the variables as global
        print(logo)
        await asyncio.sleep(1)
        url = input(Fore.GREEN+"[INFO] enter the url of the target:") #* Asks the user of URL
        try:
            if url == "host":
                await Get_host_name(Host=input("enter the host:"))
                
            elif url == "cls":
                print(logo)
                os.system('cls' if os.name == 'nt' else 'clear')
            
            elif url == "exit":
                sys.exit()
        except:
            pass
        # if url == "cls"
        # await auth_SQL_inj(url)
        print(options)
        ch = input(Fore.BLUE+"[INFO]enter the exploit attack:") #* ASK the attack type of user
        match ch:
            case "1":
                # url = input("enter the target url:")
                await auth_SQL_inj(url) #* Declare the auth bypass injection in case 1
                # asyncio.run(auth_SQL_inj(url))

                
            case "2":
                await Error_based_inj(url) #* Declare the Error_based_injection in case of 2
                # asyncio.run(Error_based_inj(url))
                
                
            case "3":
                await generic_sql_attack(url) #* Declare the generic_sql_injection in case of 3
                # asyncio.run(generic_sql_attack(url))
                
            case "4":
                await Time_based_sql_injection(url) #* Declare the time based SQL injection in case of 4
                
            case "5":
                await union_based_SQL_inj(url) #* Declare the union based injection in case of 5
                
            case "Full":
                await asyncio.gather(
                auth_main(url),
                Error_based_inj(url),
                generic_sql_attack(url),
                Time_based_sql_injection(url),
                Time_based_sql_injection(url),
                union_based_SQL_inj(url))
                
            case "cls": #* Clear the terminal and print the logo
                print(logo)
                os.system('cls' if os.name == 'nt' else 'clear')
                
            case "exit": #* Exit
                exit()
                
            case "show options": #* show options
                print(options)
                
            case "1 --header":
                await auth_SQL_inj_HEADER(url)
            
            case "2 --header":
                await Error_based_inj_HEADER(url)
                
                
            case "3 --header":
                await generic_sql_attack_HEADER(url)
            
            case "4 --header":
                await Time_based_sql_injection_HEADER(url)
        
            
            case "5 --header":
                await union_based_SQL_inj_HEADER(url)
            
            
            case "dbs --access":
                # await Access_the_data_base()
                # import os
                if os.name == 'nt':  #* For Windows
                    os.system('cls')
                else:  # *For Mac and Linux
                    os.system('clear')
                    print(""" 
                      
                      
                      
                       ____  ____                              _      
|  _ \| __ )    ___ ___  _ __  ___  ___ | | ___ 
| | | |  _ \   / __/ _ \| '_ \/ __|/ _ \| |/ _ \
| |_| | |_) | | (_| (_) | | | \__ \ (_) | |  __/
|____/|____/   \___\___/|_| |_|___/\___/|_|\___|
                      
                      
                      """)
                # await create_table()
                # await Display_info_of_the_Datas()
                while True:
                    i = input("**[INFO]Press any key to display the info:**")
                    db = Database()
                    threads = [db.create_table(),db.display_the_info()]
                    for thread in threads:
                        tr = threading.Thread(target=thread)
                        tr.start()
                        tr.join()
                    
                    if i == "q":
                        # raise SystemExit
                        break
                    elif i == "esc":
                        raise SystemExit
                    else:
                        continue
                        
                    
                    
                # await display_table_Attacktype()
                
            
            case "Full --header":
                await asyncio.gather(
                auth_SQL_inj_HEADER(url),
                Error_based_inj_HEADER(url),
                generic_sql_attack_HEADER(url),
                Time_based_sql_injection_HEADER(url),
                union_based_SQL_inj_HEADER(url)
                )
            case "--help":
                pass
            
            case "backend --lang":
                """This is not always indicating the precise backend language of the big websites. """
                # while True:
                await find_backend_language(url)
                i = input("")
                if i == "y":
                    pass
                    # break
                elif i == "q":
                    raise SystemExit
                
                
            case "o":
                pass
            
            case "esc":
                raise SystemExit
            
            case "port -f":
                await Find_open_ports_of_the_target(ipV4=input("Enter the ipV4 of the target:"))
            
            case "auto":
                # while True:
                await Back_end_auto(url)
                a = input("")
                if a == "y":
                    print(Fore.YELLOW+"**[INFO]Testing injection parameters...")
                    await asyncio.gather(
                    auth_SQL_inj(url),
                    Error_based_inj(url),
                    generic_sql_attack(url),
                    Time_based_sql_injection(url),
                    union_based_SQL_inj(url)
                    )
                    threads = [db.create_table(),db.display_the_info()]
                    for thread in threads:
                        print("The final result of the exploitation:\n")
                        tr = threading.Thread(target=thread)
                        tr.start()
                        tr.join()
                    
                # elif "n":
                #     break
                elif a == "q":
                    raise SystemExit
                
                elif a == "n":
                    # break
                    sys.exit(0)
                
                else:
                    # continue
                    pass
            
            
            
            
            
                
            
    except Exception as e:
        print(Fore.RED+"[ERROR] An error occurred:",e)
    
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
        
# if __name__ =
            

            
            
            
            
            
       
if __name__ == "main": 
    while True: 
        try:
            asyncio.run(main())
        except KeyboardInterrupt:
            continue

else:
    
    #TODO: i can remove while True maybe
    while True:
        try:
            asyncio.run(main())
            
        except KeyboardInterrupt:
            continue
        # except MemoryError:
            # p
            # import psutil
            # # Get the system memory information
            # memory = psutil.virtual_memory()

            # # Calculate the threshold for 80% memory usage
            # threshold = memory.total * 0.9

            # # Check if the used memory is greater than the threshold
            # Err =  memory.used <= threshold
            # while not Err:
            #     memory = psutil.virtual_memory()
            #     Err = memory.used <= threshold
            #     print("Please Release you RAM space to continue the application")
            #     await asyncio.sleep(5)
    
