try:

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
    from Dictionaryattack.payloads import run_brute_force
    from lib.mysqlblind.conditionalblindsql import conditional_blind_sql_inj
    from lib.mysqlerrorbased.mysqlerrorbaseBASIC import SQL_inj_BASIC
    from lib.mysqlerrorbased.mysqlexractvalue import Extract_value_injection
    from lib.mysqlerrorbased.mysqlnameconst import Name_const_inj
    from lib.OracleSQLinjection.OracleINJ import ORACLE_SQL_injection
    from lib.OracleSQLinjection.HostnameORC import HOSTNAME_ORACLE
    from lib.OracleSQLinjection.DBname import DB_name_ATTACK
    from lib.OracleSQLinjection.Databasels import Database_LISTING
    from lib.OracleSQLinjection.Database_clmn_ls import LIST_COLUMNS_ORACLE
    from lib.mysqlerrorbased.invalidHTTPREQ import INVALID_HTTP_REQ
    from lib.privillageessscalation.dumpDBA import DUMP_USERNAME_IN_DATABASE
    from lib.privillageessscalation.PrecudureATT import Procedure_Attack
    from lib.privillageessscalation.findDBlink import Find_data_base_link
    from lib.banner.Banner import main_banner
    from lib.priority.Priority import PRIORITY
    from lib.priority.HARMFULL import HARMFULL

except ImportError:
    print("[!] wrong installation please check the installation instructions")

except KeyboardInterrupt:
    print("Aborted")

__priority__ = PRIORITY.HIGH
__hramfull__ = HARMFULL.HIGH


"""Tested against: http://testphp.vulnweb.com/disclaimer.php """

init()

Style.BRIGHT


logo = """"""

logo += main_banner

options = """
Pre-release 1.0
1.authbypassSQL
2.ErrorbasedINJection
3.GenericSQL
4.TimebasedSQL
5.UNIONselect
6.privilege escalation

"""

logging.basicConfig(filename="SQLJ.log",level=logging.ERROR)

# url = None

async def main():
    global host
    """The main function and the user side of the program."""
    try:
        # while Tr
        global logo,options 
        print(logo)
        await asyncio.sleep(1)
        url = input(Fore.GREEN+"[INFO] enter the url of the target:") 
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
        print(options)
        ch = input(Fore.BLUE+"[INFO]enter the exploit attack:") 
        match ch:
            case "1":
                await auth_SQL_inj(url) 

                
            case "2":
                await Error_based_inj(url)
                
                
            case "3":
                await generic_sql_attack(url) 
                
            case "4":
                await Time_based_sql_injection(url) 
                
            case "5":
                await union_based_SQL_inj(url) 
            
            case "6":
                try:
                    await asyncio.gather(
                        Find_data_base_link(url),
                        DUMP_USERNAME_IN_DATABASE(url)
                    )
                
                except (asyncio.TimeoutError,asyncio.InvalidStateError,asyncio.IncompleteReadError):
                    logging.error("Error occurred in the main program due to the asyncio errors while performing a full attack.")
                    raise
                except asyncio.CancelledError:
                    print("Operation canceled")
                    logging.error(f"asyncio operation canceled.")
                    raise
                
            case "Full":
                try:
                    await asyncio.gather(
                    auth_main(url),
                    Error_based_inj(url),
                    generic_sql_attack(url),
                    Time_based_sql_injection(url),
                    Time_based_sql_injection(url),
                    union_based_SQL_inj(url))
                
                except (asyncio.TimeoutError,asyncio.CancelledError):
                    logging.error("Error occurred in the main program due to the asyncio errors while performing a full attack.")
                    raise
                
            case "cls": 
                print(logo)
                os.system('cls' if os.name == 'nt' else 'clear')
                
            case "exit": 
                raise SystemExit
                
            case "show options": 
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
                while True:
                    i = input("**[INFO]Press any key to display the info:**")
                    db = Database()
                    threads = [db.create_table(),db.display_the_info()]
                    for thread in threads:
                        tr = threading.Thread(target=thread)
                        tr.start()
                        tr.join()
                    
                    if i == "q":
                        break
                    elif i == "esc":
                        raise SystemExit
                    else:
                        continue
                        
                    
                    
                
            
            case "Full --header":
                try:
                    await asyncio.gather(
                    auth_SQL_inj_HEADER(url),
                    await asyncio.sleep(5),
                    Error_based_inj_HEADER(url),
                    await asyncio.sleep(5),
                    generic_sql_attack_HEADER(url),
                    await asyncio.sleep(5),
                    Time_based_sql_injection_HEADER(url),
                    await asyncio.sleep(5),
                    union_based_SQL_inj_HEADER(url),
                    await asyncio.sleep(5),
                    LIST_COLUMNS_ORACLE(url),
                    await asyncio.sleep(5)
                    )
                
                except (asyncio.CancelledError,asyncio.IncompleteReadError,asyncio.LimitOverrunError,asyncio.SendfileNotAvailableError):
                    logging.error("Error occurred in the main program due to the asyncio errors while performing a full attack.")
                    raise
                
            case "--help":
                pass
            
            case "http":
                await INVALID_HTTP_REQ(url)
            
            case "--dump":
                await DUMP_USERNAME_IN_DATABASE(url)

            case "name const":
                await Name_const_inj(url)
            
            case "make set inj":
                await make_set_blind_sql_inj(url)
            
            case "prec attack":
                await Procedure_Attack(url)

            case "XML":
                await My_sql_XML_attack(url)
            
            case "backend --lang":
                """This is not always indicating the precise backend language of the big websites. """
                await find_backend_language(url)
                i = input("")
                if i == "y":
                    pass
                elif i == "q":
                    raise SystemExit
            
            case "brute force":
                run_brute_force(url,0,0)
            
            case "Oracle":
                while True:
                    await find_backend_language(url)
                    
                    e = input("")
                    if e == "y":
                        break
                    
                    elif e == "q":
                        raise SystemExit
                await asyncio.gather(
                    ORACLE_SQL_injection(url),
                    HOSTNAME_ORACLE(url),
                    DB_name_ATTACK(url),
                    Database_LISTING(url)
                    )
            

            case "substring":
                await substring_sql_inj(url)
                
            case "cond":
                await conditional_SQL_inj(url)                
                
            case "o":
                pass
            
            case "basic inj":
                await SQL_inj_BASIC(url)
            
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
                    
                elif a == "q":
                    raise SystemExit
                
                elif a == "n":
                    sys.exit(0)
                
                else:
                    pass
            
            
            
            
            
                
            
    except Exception as e:
        print(Fore.RED+"[ERROR] An error occurred:",e)
    
    except ImportError:
        print(Fore.RED+"[!]Installation error,please ensure that the file is downloaded correctly." )
    
    except MemoryError:
        pass
            
            
       
if __name__ == "main": 
    while True: 
        try:
            asyncio.run(main())
        except KeyboardInterrupt:
            continue

else:
    
    while True:
        try:
            asyncio.run(main())
            
        except KeyboardInterrupt:
            continue

    
