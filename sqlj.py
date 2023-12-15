import sys
import os
cur = os.getcwd()
sys.path.append(cur)


try:
    #these should be the first unusual imports
    __import__("lib")
    __import__("lib.scripts")
    __import__("Exceptions")
    __import__("Exceptions.exceptions")
    __import__("Core")
    __import__("colorama")
    __import__("colorlog")
    __import__("nmap")
    __import__("requests")

except (ImportError,ModuleNotFoundError) as e:
    sys.exit(f"[!]Wrong installation,please visit github page:https://github.com/HeisenbergCipherCracker/SQLJ\n and make sure you have installed the program properly\n[ERROR]:{e}")

except KeyboardInterrupt:
    sys.exit("[!]Aborted")


try:
    import logging
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
    import warnings
    from colorama import Fore,init
    from datetime import datetime
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
    from lib.priority.Priority import PRIORITY,HARMFULL
    from lib.Term.term import term
    from lib.Cookies.cookies import extract_cookies
    from lib.extra.options import OPTIONS
    from lib.ipv6.IPV6 import get_ipv6_address
    from lib.regelexpression.patterns import Remove_https_for_ipv4 as remove_ipv4_and_ipv6_https_http
    from lib.getipv4.getipv4 import get_ipv4_of_host as IPV4
    from SQLJngUI import Argument_parser
    from lib.pversions.versions import version_311
    from Exceptions.sqljngwarnings import SQLJNGPythonInterpreterNotRecommendedWarning
    from Exceptions.sqljngwarnings import SQLJNGPython2IsNotSupportedWarning
    from Exceptions.sqljngwarnings import SQLJNGPythonInterpreterNotFoundWarning
    from lib.regelexpression.ippatterns import find_ipv4type_private as isprivateipv4
    from logger.logs import logger
    from logger.sqljlog import logger as sqljlog
    from lib.OracleSQLinjection.oracleattack import OracleExploit
    from lib.mysqlerrorbased.errorbasedexploits import HTTPErrorReq
    from lib.mysqlblind.blindsqlexploits import BlindSQlExploit


except (ImportError,ModuleNotFoundError) as e:
    sys.exit(f"[!]Wrong installation:{e} \n please visit https://github.com/HeisenbergCipherCracker/SQLJ at github.")

except KeyboardInterrupt:
    print("[!]Aborted")
    sys.exit(0)


try:
    for _ in version_311:
        ver = str(sys.version_info.major) + "." + str(sys.version_info.minor) + "." + str(sys.version_info.micro)
        if ver == version_311[0]:
            continue
        elif ver  == version_311[1]:
            warnings.warn("It is recommended to use python 3.12 or more for the asyncio improvements.",SQLJNGPythonInterpreterNotRecommendedWarning)
            continue

        elif ver  == version_311[2]:
            warnings.warn("It is recommended to use python 3.12 or more for the asyncio improvements.",SQLJNGPythonInterpreterNotRecommendedWarning)
            continue


        elif ver  == version_311[3] or ver == version_311[4] or ver == version_311[5]:
            sys.exit("[!]Your python interpreter does not support this program syntax,you'll need\npython 3.10 or more\n3.10 recommended.")

        elif ver == version_311[6]:
            warnings.warn("python2 is not supported in this sqljng version_311",SQLJNGPython2IsNotSupportedWarning)
            sys.exit("python2 is not supported in this sqljng version_311.")

        else:
            warnings.warn("Could not find significant information about your python interpreter.",SQLJNGPythonInterpreterNotFoundWarning)

except SystemExit:
    raise
        
        




"""Tested against: http://testphp.vulnweb.com/disclaimer.php """

init()

Style.BRIGHT

https_rm = None

logo = ""

logo = main_banner

options = ""
options += OPTIONS


print(logo)

logging.basicConfig(filename="SQLJ.log",level=logging.ERROR)


logger.setLevel(logging.CRITICAL)
sqljlog.setLevel(logging.INFO)


# url = None

#Reference for testing:http://testphp.vulnweb.com/artists.php
print(f"[*]Starting at:{datetime.now()}")

async def main():
    global host
    """The main function and the user side of the program
    See file SQLJ.log for the error has been occurred and program issues.
    Returns : None
    Parameters : None
    """
    try:
        # while Tr
        global logo,options,https_rm
        await asyncio.sleep(1)
        url = input(Fore.GREEN+">>>TARGET URL:") 
        try:
            if url == "host":
                await Get_host_name(Host=input("enter the host:"))
                
            elif url == "cls":
                os.system('cls' if os.name == 'nt' else 'clear')
            
            elif url == "exit":
                sys.exit()
        except:
            pass
        print(options)
        ch = input(Fore.BLUE+">>>") 
        match ch:
            case "01"|"1":
                https_rm = remove_ipv4_and_ipv6_https_http(url)
                get_ipv6_address(https_rm)
                IPV4(https_rm)
                _,ipinfo = isprivateipv4(https_rm)
                print(ipinfo)
                await asyncio.gather(
                extract_cookies(url),
                auth_SQL_inj(url) )

                
            case "02"|"2":
                
                get_ipv6_address(https_rm)
                IPV4(https_rm)
                await asyncio.gather(
                    extract_cookies(url),
                    Error_based_inj(url)
                )
                
                
            case "03"|"3":
                get_ipv6_address(https_rm)
                IPV4(https_rm)
                await asyncio.gather(
                    extract_cookies(url),
                    generic_sql_attack(url)
                )
                
            case "04"|"4":
                get_ipv6_address(https_rm)
                IPV4(https_rm)
                await asyncio.gather(
                    extract_cookies(url),
                    Time_based_sql_injection(url)
                )
                
            case "05"|"5":
                get_ipv6_address(https_rm)
                IPV4(https_rm)
                await asyncio.gather(
                    extract_cookies(url),
                    union_based_SQL_inj(url)
                )
            
            case "06"|"6":
                try:
                    get_ipv6_address(https_rm)
                    IPV4(https_rm)
                    await asyncio.gather(
                        extract_cookies(url),
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
                
            case "07"|"7":
                try:
                    get_ipv6_address(https_rm)
                    IPV4(https_rm)
                    await asyncio.gather(
                    extract_cookies(url),
                    Error_based_inj(url),
                    generic_sql_attack(url),
                    Time_based_sql_injection(url),
                    Time_based_sql_injection(url),
                    union_based_SQL_inj(url))
                
                except (asyncio.TimeoutError,asyncio.CancelledError):
                    logging.error("Error occurred in the main program due to the asyncio errors while performing a full attack.")
                    raise
                
            case "cls": 
                os.system('cls' if os.name == 'nt' else 'clear')
                
            case "exit": 
                raise SystemExit
                
            case "show options": 
                print(options)
                
            case "08"|"8":
                get_ipv6_address(https_rm)
                IPV4(https_rm)
                await asyncio.gather(
                    extract_cookies(url),
                    auth_SQL_inj_HEADER(url)
                )
            
            case "09"|"9":
                get_ipv6_address(https_rm)
                IPV4(https_rm)
                await asyncio.gather(
                    extract_cookies(url),
                    Error_based_inj_HEADER(url)
                )
                
                
            case "10":
                get_ipv6_address(https_rm)
                IPV4(https_rm)
                await asyncio.gather(
                    extract_cookies(url),
                    generic_sql_attack_HEADER(url)
                )
            
            case "11":
                get_ipv6_address(https_rm)
                IPV4(https_rm)
                await asyncio.gather(
                    extract_cookies(url),
                    Time_based_sql_injection_HEADER(url)
                )
        
            
                        
                    
                    
                
            
            case "x":
                try:
                    get_ipv6_address(https_rm)
                    IPV4(https_rm)
                    await asyncio.gather(
                    extract_cookies(url),
                    auth_SQL_inj_HEADER(url),
                    Error_based_inj_HEADER(url),
                    generic_sql_attack_HEADER(url),
                    Time_based_sql_injection_HEADER(url),
                    union_based_SQL_inj_HEADER(url),
                    LIST_COLUMNS_ORACLE(url),
                    )
                
                except (asyncio.CancelledError,asyncio.IncompleteReadError,asyncio.LimitOverrunError,asyncio.SendfileNotAvailableError):
                    logging.error("Error occurred in the main program due to the asyncio errors while performing a full attack.")
                    raise
                
            
            case "12":
                get_ipv6_address(https_rm)
                IPV4(https_rm)
                await asyncio.gather(
                    extract_cookies(url),
                    INVALID_HTTP_REQ(url)
                )
            
            case "13":
                get_ipv6_address(https_rm)
                IPV4(https_rm)
                await asyncio.gather(
                    extract_cookies(url),
                    DUMP_USERNAME_IN_DATABASE(url)
                )

            case "14":
                get_ipv6_address(https_rm)
                IPV4(https_rm)
                await asyncio.gather(
                    extract_cookies(url),
                    Name_const_inj(url)
                )
            
            
            case "15":
                get_ipv6_address(https_rm)
                IPV4(https_rm)
                await Procedure_Attack(url)
            
            case "16":
                """This is not always indicating the precise backend language of the big websites. """
                await find_backend_language(url)
                i = input("")
                if i == "y":
                    pass
                elif i == "q":
                    raise SystemExit
            
            case "17":
                get_ipv6_address(https_rm)
                IPV4(https_rm)
                run_brute_force(url,0,0)
            
            case "18":
                while True:
                    await find_backend_language(url)
                    
                    e = input("")
                    if e == "y":
                        break
                    
                    elif e == "q":
                        raise SystemExit
                await asyncio.gather(
                    extract_cookies(url),
                    ORACLE_SQL_injection(url),
                    HOSTNAME_ORACLE(url),
                    DB_name_ATTACK(url),
                    Database_LISTING(url)
                    )
            
            
                
            
            case "19":
                get_ipv6_address(https_rm)
                IPV4(https_rm)
                await SQL_inj_BASIC(url)
            
            case "Q":
                raise SystemExit
            
            case "20":
                get_ipv6_address(https_rm)
                ipv4 = IPV4(https_rm)
                await Find_open_ports_of_the_target(ipV4=ipv4)

            case "22":
                get_ipv6_address(https_rm)
                ipv4 = IPV4(https_rm)
                await Extract_value_injection(url)
            
            case "A"|"a":
                get_ipv6_address(https_rm)
                IPV4(https_rm)
                await extract_cookies(url)
                await asyncio.gather(
                    OracleExploit.db_column_exploit(url),
                    OracleExploit.db_column_list_exploit(url),
                    OracleExploit.oracle_injection_exploit(url),
                    OracleExploit.oracle_injection_database_list_attack(url),
                    HTTPErrorReq.Extract_value(url),
                    HTTPErrorReq.http_req(url),
                    Error_based_inj(url),
                    Error_based_inj_HEADER(url),
                    Time_based_sql_injection(url),
                    Time_based_sql_injection_HEADER(url),
                    union_based_SQL_inj(url),
                    union_based_SQL_inj_HEADER(url),
                    auth_SQL_inj(url),
                    auth_SQL_inj_HEADER(url),
                    BlindSQlExploit.binary_sql_exploit(url),
                    BlindSQlExploit.conditional_blind_sql_inj_exploit(url),
                    BlindSQlExploit.sub_string_sql_inj_exploit(url)
                )
            
            case "23":
                await asyncio.gather(
                    BlindSQlExploit.binary_sql_exploit(url),
                    BlindSQlExploit.conditional_blind_sql_inj_exploit(url),
                    BlindSQlExploit.sub_string_sql_inj_exploit(url)
                )

            
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
                    
                elif a == "q":
                    raise SystemExit
                
                elif a == "n":
                    sys.exit(0)
                
                else:
                    pass
            
            
            
    except SystemExit:
        sys.exit(Fore.RESET+f"\nEnding at:{datetime.now()}")   
    except Exception as exc:
        excp = str(exc)
        if any(_ in excp for _ in ("MemoryError", "Cannot allocate memory")) or type(exc) == MemoryError:
            errmsg += "Error ocurred:%s"%excp   
            errmsg += "Cannot handel the memory issues"
            sqljlog.critical(errmsg)
            raise SystemExit
        
        elif type(exc) == requests.exceptions.Timeout:
            errmsg = "Connection has been timeout to."
            errmsg +="\nmake sure you have connected to the internet"
            errmsg += "\nor the ISP is working properly."
            sqljlog.critical(errmsg)
            raise SystemExit
        
        elif any(_ in excp for _ in ("No space left", "Disk quota exceeded", "Disk full while accessing")):
            errmsg += "No such enough space left on the disk"
            errmsg += "\n make sure that you have enough space in the disk."
            sqljlog.critical(errmsg)
            raise SystemExit
        
            


    

            
            
       
if __name__ == "main": 
    while True: 
        try:
            asyncio.run(main())
        except KeyboardInterrupt:
            logger.info("Aborted")
            print(Fore.RESET+f"\n[*]Ending at(interruption by user):{datetime.now()}")

            raise SystemExit

elif __name__ == "SQLJngUI":
    pass

else:

    while True: 
        try:
            asyncio.run(main())
        except KeyboardInterrupt:
            logger.info("Aborted")
            print(Fore.RESET+f"\n[*]Ending at(interruption by user):{datetime.now()}")
            raise SystemExit





    