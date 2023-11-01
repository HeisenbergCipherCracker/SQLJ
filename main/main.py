import sys
import sys
sys.path.append('D:\SQLjj\SQLJ\lib\scripts') #* for windows
# sys.path.append('/mnt/d/SQLjj/SQLJ/lib/scripts') #* for linux
import authbypass_inj
from authbypass_inj import auth_SQL_inj
import sys
import os
from Get_host_name import Get_host_name
from colorama import Style
import threading
import requests
from database import *
host = (f"host {int}")
from authbypass_inj import auth_SQL_inj,auth_main
import asyncio
from Error_based_injection import Error_based_inj
from genericSQL import generic_sql_attack
from Timebasedinj import Time_based_sql_injection
from Unionselect import union_based_SQL_inj
from colorama import Fore,init
from Memmoeyerr import Memory_handling
from Headers_added_in_used_UNION_SELECT_ATTACK import union_based_SQL_inj_HEADER
from Auth_bypass_inj_with_HEADERS import auth_SQL_inj_HEADER
from Error_based_inj_with_headers import Error_based_inj_HEADER
from Generic_SQL_with_header import generic_sql_attack_HEADER
from Time_based_Header_inj import Time_based_sql_injection_HEADER
from AccessDatabase import Access_the_data_base
from AccessDatabase import Access_the_data_base
from Backend_language import find_backend_language
from database import create_table
from Hackgpt import chat,M_chat
from Backend_language import Back_end_auto
from database import Database,Display_the_database_info_of_captures,Create_table_for_the_captures_datas

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
            
            case "auto":
                while True:
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
                        break
                    
                    else:
                        continue
            
            
            
            
            
                
            
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
    
