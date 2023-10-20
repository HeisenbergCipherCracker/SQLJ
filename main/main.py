import sys
import sys
sys.path.append('D:/SQLjj/SQLJ/exploit')
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
        except:
            pass
        # if url == "cls"
        # await auth_SQL_inj(url)
        print(options)
        ch = input(Fore.BLUE+"enter the exploit attack:") #* ASK the attack type of user
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
                

                
            case "--help":
                pass
            case _:
                pass
            
            
            
                
            
    except Exception as e:
        print(Fore.RED+"[ERROR] An error occurred:",e)
        
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
        #     res = Memory_handling()
        #     await res
    
