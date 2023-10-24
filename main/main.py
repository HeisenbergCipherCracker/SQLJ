import sys
import sys
sys.path.append('D:\SQLjj\SQLJ\lib\scripts')
import authbypass_inj
from authbypass_inj import auth_SQL_inj
import sys
import os
from Get_host_name import Get_host_name

################################################################
host = (f"host {int}")

##########################################################################
from authbypass_inj import auth_SQL_inj,auth_main
############################################################
import asyncio
##############################################################
from Error_based_injection import Error_based_inj

#########################################################################
from genericSQL import generic_sql_attack

##############################################################################
from Timebasedinj import Time_based_sql_injection

###############################################################################
from Unionselect import union_based_SQL_inj
#################################################################################
from colorama import Fore,init
######################################################################################################
from Memmoeyerr import Memory_handling
#########################################################################
from Headers_added_in_used_UNION_SELECT_ATTACK import union_based_SQL_inj_HEADER
###############################################################################
from Auth_bypass_inj_with_HEADERS import auth_SQL_inj_HEADER
################################################################################################
from Error_based_inj_with_headers import Error_based_inj_HEADER
################################################################
from Generic_SQL_with_header import generic_sql_attack_HEADER
####################################################################################
from Time_based_Header_inj import Time_based_sql_injection_HEADER
##########################################################################
from database import create_database_for_Captures
##############################################################
from AccessDatabase import Access_the_data_base
###################################################################
from AccessDatabase import Access_the_data_base

init()


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
                await Access_the_data_base()
            
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
            case _:
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
    
