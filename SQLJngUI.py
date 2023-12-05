import argparse
import warnings
import logging
from asyncio import run
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
from lib.regelexpression.patterns import Remove_https_for_ipv4 as remove_ipv4_and_ipv6_https_http
from lib.getipv4.getipv4 import get_ipv4_of_host as IPV4
from lib.ipv6.IPV6 import get_ipv6_address
warnings.simplefilter('ignore')
#Reference: https://note.nkmk.me/en/python-warnings-ignore-warning/

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
#python sqljng.py -A auto -u https://example.com --headers "User-Agent: Mozilla/5.0" 

async def Argument_parser():
    parser = argparse.ArgumentParser(description="SQLJng")

    # Adding arguments
    parser.add_argument("-u", "--url", help="Enter the url of the target", required=True)
    parser.add_argument("-H", "--headers", help="Add headers", required=False)

    # Additional arguments can be added as needed
    parser.add_argument("-p", "--port", type=int, help="Specify a port number", required=False)
    parser.add_argument("--enable-feature", action="store_true", help="Enable a specific feature", required=False)
    parser.add_argument("-A", type=str, help="Specify the type of the attack", required=True)
    parser.add_argument("-v", "--version", action="version", version="%(prog)s 1.3.0")
    parser.add_argument("-vv","-verbose", action="store_true", help="Enable verbose mode", required=False)
    parser.add_argument("-other", help="Enable other features", required=False)

    # Parse the command line arguments
    args = parser.parse_args()

    # Accessing values
    url = args.url
    headers = args.headers
    port = args.port
    enable_feature = args.enable_feature
    attack_type = args.A 
    verbose = args.vv


    await Args_UI(url, headers, port, enable_feature, attack_type, args.vv)
    return(url,headers,port,enable_feature,attack_type,verbose)

async def Args_UI(url, headers, port, enable_feature, attack_type, verbose):
    if "www.google.com" in url or "https://www.google.com" in url:
        logger.warn("This attack may encounter you with legal issues. Please check the url and try again. You are trying to perform an attack on google.com")
        raise SystemExit
    elif "www.youtube.com" in url or "https://www.youtube.com" in url:
        logger.warn("This attack may encounter you with legal issues. Please check the url and try again. You are trying to perform an attack on youtube.com")
        raise SystemExit
    elif "www.facebook.com" in url or "https://www.facebook.com" in url:
        logger.warn("This attack may encounter you with legal issues. Please check the url and try again. You are trying to perform an attack on facebook.com")
        raise SystemExit
    elif "www.instagram.com" in url or "https://www.instagram.com" in url:
        logger.warn("This attack may encounter you with legal issues. Please check the url and try again. You are trying to perform an attack on instagram.com")
        raise SystemExit
    elif "www.twitter.com" in url or "https://www.twitter.com" in url:
        logger.warn("This attack may encounter you with legal issues. Please check the url and try again. You are trying to perform an attack on twitter.com")
        raise SystemExit
    elif "www.reddit.com" in url or "https://www.reddit.com" in url:
        logger.warn("This attack may encounter you with legal issues. Please check the url and try again. You are trying to perform an attack on reddit.com")
        raise SystemExit
    elif "www.linkedin.com" in url or "https://www.linkedin.com" in url:
        logger.warn("This attack may encounter you with legal issues. Please check the url and try again. You are trying to perform an attack on linkedin.com")
        raise SystemExit
    elif "www.instagram.com" in url or "https://www.instagram.com" in url:
        logger.warn("This attack may encounter you with legal issues. Please check the url and try again. You are trying to perform an attack on instagram.com")
        raise SystemExit
    elif "www.amazon.com" in url or "https://www.amazon.com" in url:
        logger.warn("This attack may encounter you with legal issues. Please check")
        raise SystemExit
    
    

    else:
        pass

    if verbose:
        logger.setLevel(logging.DEBUG)
    else:
        logger.setLevel(logging.INFO)
    
    if attack_type == "Abypass":
        await auth_SQL_inj_HEADER(url)
    elif attack_type == "Error":
        await Error_based_inj_HEADER(url)
    
    elif attack_type == "Generic":
        await generic_sql_attack_HEADER(url)
    
    elif attack_type == "Time":
        await Time_based_sql_injection_HEADER(url)
    
    elif attack_type == "Union":
        await union_based_SQL_inj_HEADER(url)
    
    elif attack_type == "List":
        await LIST_COLUMNS_ORACLE(url)
    
    elif attack_type == "Dump":
        await DUMP_USERNAME_IN_DATABASE(url)
    
    elif attack_type == "Name":
        await Name_const_inj(url)


    
    elif attack_type == "Procedure":
        await Procedure_Attack(url)
    
    elif attack_type == "auto":
        try:
            https_rm = remove_ipv4_and_ipv6_https_http(url)
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
    

    
    elif attack_type == "Brute":
        run_brute_force(url,0,0)
    
    elif attack_type == "Oracle":
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
    


   
    
    elif attack_type == "O":
        pass

    elif attack_type == "Basic":
        await SQL_inj_BASIC(url)

    elif attack_type == "Esc":
        raise SystemExit
    
    elif attack_type == "Port":
        await Find_open_ports_of_the_target(ipV4=input("Enter the ipV4 of the target:"))
    
    elif attack_type == "Auto":
        # while True:
        await Back_end_auto(url)
        a = input("")
        if a == "y":
            logger.info("Testing injection parameters...")
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
    
    elif attack_type == "Other":
        pass

    elif attack_type == "Generic" and header == "y":
        await generic_sql_attack_HEADER(url)
    elif attack_type == "Time" and header == "y":
        await Time_based_sql_injection_HEADER(url)
    
    elif attack_type == "Union" and header == "y":
        await union_based_SQL_inj_HEADER(url)
    
    elif attack_type == "List" and header == "y":
        await LIST_COLUMNS_ORACLE(url)
    
    elif attack_type == "Dump" and header == "y":
        await DUMP_USERNAME_IN_DATABASE(url)
    
    elif attack_type == "Name" and header == "y":
        await Name_const_inj(url)
    

    
    elif attack_type == "Procedure" and header == "y":
        await Procedure_Attack(url)
    

    
    elif attack_type == "Brute" and header == "y":
        run_brute_force(url,0,0)
    
    elif attack_type == "Oracle" and header == "y":
        pass

    else:
        pass
    



    # Your logic here based on the provided arguments


# if __name__ == "__main__":
#     run(Argument_parser())
