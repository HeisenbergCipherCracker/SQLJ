import argparse
import warnings
import logging
import aiohttp
from asyncio import run
from SQLJng import *
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
#python SQLJngUI.py --types Basic -u https://example.com --headers "User-Agent: Mozilla/5.0" 

async def Argument_parser():
    parser = argparse.ArgumentParser(description="SQLJng")

    # Adding arguments
    parser.add_argument("-u", "--url", help="Enter the url of the target", required=True)
    parser.add_argument("-H", "--headers", help="Add headers", required=False)

    # Additional arguments can be added as needed
    parser.add_argument("-p", "--port", type=int, help="Specify a port number", required=False)
    parser.add_argument("--enable-feature", action="store_true", help="Enable a specific feature", required=False)
    parser.add_argument("--types", type=str, help="Specify the type of the attack", required=True)
    parser.add_argument("-v", "--version", action="version", version="%(prog)s 1.0")
    parser.add_argument("-vv","-verbose", action="store_true", help="Enable verbose mode", required=False)
    parser.add_argument("-other", help="Enable other features", required=False)

    # Parse the command line arguments
    args = parser.parse_args()

    # Accessing values
    url = args.url
    headers = args.headers
    port = args.port
    enable_feature = args.enable_feature
    attack_type = args.types
    verbose = args.vv


    await Args_UI(url, headers, port, enable_feature, attack_type, args.vv)

async def Args_UI(url, headers, port, enable_feature, attack_type, verbose):
    if "www.google.com" in url or "https://www.google.com" in url:
        logger.critical("This attack may encounter you with legal issues. Please check the url and try again. You are trying to perform an attack on google.com")
        raise SystemExit
    elif "www.youtube.com" in url or "https://www.youtube.com" in url:
        logger.critical("This attack may encounter you with legal issues. Please check the url and try again. You are trying to perform an attack on youtube.com")
        raise SystemExit
    elif "www.facebook.com" in url or "https://www.facebook.com" in url:
        logger.critical("This attack may encounter you with legal issues. Please check the url and try again. You are trying to perform an attack on facebook.com")
        raise SystemExit
    elif "www.instagram.com" in url or "https://www.instagram.com" in url:
        logger.critical("This attack may encounter you with legal issues. Please check the url and try again. You are trying to perform an attack on instagram.com")
        raise SystemExit
    elif "www.twitter.com" in url or "https://www.twitter.com" in url:
        logger.critical("This attack may encounter you with legal issues. Please check the url and try again. You are trying to perform an attack on twitter.com")
        raise SystemExit
    elif "www.reddit.com" in url or "https://www.reddit.com" in url:
        logger.critical("This attack may encounter you with legal issues. Please check the url and try again. You are trying to perform an attack on reddit.com")
        raise SystemExit
    elif "www.linkedin.com" in url or "https://www.linkedin.com" in url:
        logger.critical("This attack may encounter you with legal issues. Please check the url and try again. You are trying to perform an attack on linkedin.com")
        raise SystemExit
    elif "www.instagram.com" in url or "https://www.instagram.com" in url:
        logger.critical("This attack may encounter you with legal issues. Please check the url and try again. You are trying to perform an attack on instagram.com")
        raise SystemExit
    elif "www.amazon.com" in url or "https://www.amazon.com" in url:
        logger.critical("This attack may encounter you with legal issues. Please check")
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

    elif attack_type == "Make":
        await make_set_blind_sql_inj(url)
    
    elif attack_type == "Procedure":
        await Procedure_Attack(url)
    
    elif attack_type == "XML":
        await My_sql_XML_attack(url)
    
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
    
    elif attack_type == "Substring":
        await substring_sql_inj(url)

    elif attack_type == "Cond":
        await conditional_SQL_inj(url)
    
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
    
    elif attack_type == "Other":
        pass
    elif attack_type == "Basic" and header == "y":
        await SQL_inj_BASIC_HEADER(url)
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
    
    elif attack_type == "Make" and header == "y":
        await make_set_blind_sql_inj(url)
    
    elif attack_type == "Procedure" and header == "y":
        await Procedure_Attack(url)
    
    elif attack_type == "XML" and header == "y":
        await My_sql_XML_attack(url)
    
    elif attack_type == "Brute" and header == "y":
        run_brute_force(url,0,0)
    
    elif attack_type == "Oracle" and header == "y":
        pass

    else:
        pass
    



    # Your logic here based on the provided arguments


if __name__ == "__main__":
    run(Argument_parser())
