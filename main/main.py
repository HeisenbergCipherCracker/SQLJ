import sys
import sys
sys.path.append('D:/SQLjj/SQLJ/exploit')
import authbypass_inj
from authbypass_inj import auth_SQL_inj
import sys
import os


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


logo = """
   _____ ____    __        __
  / ___// __ \  / /       / /
  \__ \/ / / / / /   __  / / 
 ___/ / /_/ / / /___/ /_/ /  
/____/\___\_\/_____/\____/   
                             

"""

options = """
1.authbypassSQL
2.ErrorbasedINJection
3.GenericSQL
4.TimebasedSQL
5.UNIONselect

"""

# url = None

async def main():
    try:
        # while Tr
        global logo,options
        print(logo)
        await asyncio.sleep(1)
        url = input("[INFO] enter the url of the target:")
        # if url == "cls"
        # await auth_SQL_inj(url)
        print(options)
        ch = input("enter the exploit attack:")
        match ch:
            case "1":
                # url = input("enter the target url:")
                await auth_SQL_inj(url)
                # asyncio.run(auth_SQL_inj(url))
                
            case "2":
                await Error_based_inj(url)
                # asyncio.run(Error_based_inj(url))
                
            case "3":
                await generic_sql_attack(url)
                # asyncio.run(generic_sql_attack(url))
                
            case "4":
                await Time_based_sql_injection(url)
                
            case "5":
                await union_based_SQL_inj(url)
                
            case "cls":
                print(logo)
                os.system('cls' if os.name == 'nt' else 'clear')
                
            case "exit":
                exit()
                
            case "--help":
                pass
            case _:
                pass
            
                
            
    except Exception as e:
        print(e)
        
# if __name__ =
            

            
            
            
            
            
       
if __name__ == "main": 
    while True: 
        asyncio.run(main())

else:
    while True:
        asyncio.run(main())
    
