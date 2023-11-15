import argparse
import warnings
import logging
import aiohttp
from asyncio import run
from SQLJng import *
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

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
    parser.add_argument("-verbose", action="store_true", help="Enable verbose mode", required=False)
    parser.add_argument("-other", help="Enable other features", required=False)

    # Parse the command line arguments
    args = parser.parse_args()

    # Accessing values
    url = args.url
    headers = args.headers
    port = args.port
    enable_feature = args.enable_feature
    attack_type = args.types

    await Args_UI(url, headers, port, enable_feature, attack_type, args.verbose, args.other)

async def Args_UI(url, headers, port, enable_feature, attack_type, verbose, other):
    if "www.google.com" in url or "https://www.google.com" in url:
        warnings.warn("This attack may encounter you with legal issues. Please check the url and try again.")
        logger.critical("This attack may encounter you with legal issues. Please check the url and try again. You are trying to perform an attack on google.com")
    elif "www.youtube.com" in url or "https://www.youtube.com" in url:
        warnings.warn("This attack may encounter you with legal issues. Please check the url and try again.")
        logger.critical("This attack may encounter you with legal issues. Please check the url and try again. You are trying to perform an attack on youtube.com")
    

    # Add similar checks for other URLs
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
    
    elif attack_type == "Other":
        pass
    



    # Your logic here based on the provided arguments
    await perform_async_request(url, headers)  # You might need to implement this function using aiohttp

async def perform_async_request(url, headers):
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as response:
            response_text = await response.text()
            logger.info(f"Request successful. Response: {response_text}")

if __name__ == "__main__":
    run(Argument_parser())
