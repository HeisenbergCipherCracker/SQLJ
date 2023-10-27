import requests
from colorama import Fore,init
import asyncio

async def find_backend_language(Link):
    init()

    # url = Link

    response = requests.head(Link)

    if "Server" in response.headers:
        server_header = response.headers["Server"]
        # print(Fore.GREEN+"[INFO] looks like the Backend language is with", Fore.RESET+Fore.RED+server_header)
        print(f"{Fore.RESET}Looks like the backend language of {Fore.RESET}{Fore.RED}{Link} is with {Fore.RESET}{Fore.GREEN}{server_header}.{Fore.RESET}Do you want to continue?(y/q)")
    else:
        print(f"Could not found any info related to the backend on the website {Link}.")
        
# print(asyncio.run(find_backend_language("")))
# print(type(ask))
