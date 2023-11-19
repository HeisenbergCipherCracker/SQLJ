import requests
from colorama import Fore,init,Style
import asyncio
import sys
import os

try:

    # Assuming Backend_language.py is in lib/scripts/backendlanguage directory
    current_directory = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.abspath(os.path.join(current_directory, '..', '..'))

    # Add the project root directory to the Python path
    sys.path.append(project_root)

    # Now you should be able to import logs
    from logger.logs import logger

except ImportError:
    print("[!]Wrong installation,please download the Tool again from the github page")

# Rest of your code...



async def find_backend_language(Link):
    """This is not always indicating the precise backend language of the big websites. """

    init()

    # url = Link

    response = requests.head(Link)

    if "Server" in response.headers:
        server_header = response.headers["Server"]
        # print(Fore.GREEN+"[INFO] looks like the Backend language is with", Fore.RESET+Fore.RED+server_header)
        logger.info(f"**Looks like server is running on: {server_header} do you want to continue?(y/q)**")
    else:
        logger.error(f"Could not found any info related to the backend on the website {Link}.")
asyncio.run(find_backend_language("http://testfire.net/login.jsp"))
# print(type(ask))

async def Find_back_end_auto(Link):
    response = requests.head(Link)

    if "Server" in response.headers:
        server_header = response.headers["Server"]
        # print(Fore.GREEN+"[INFO] looks like the Backend language is with", Fore.RESET+Fore.RED+server_header)
        return f"{Fore.RESET}{Style.BRIGHT}**[INFO]Looks like the server of {Link} is running on: {Fore.RESET}{Fore.RED}{Link} is with {Fore.RESET}{Fore.GREEN}{server_header}.{Fore.RESET}Do you want to continue?(y/q)**"
    else:
        return f"Could not found any info related to the backend on the website {Link}."
    
import asyncio

async def Back_end_auto(URL):
    T = Find_back_end_auto(URL)
    result = await T
    print(result)

# asyncio.run(test())

# asyncio.run(test())