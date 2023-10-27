import requests
from colorama import Fore,init
import asyncio

async def find_backend_language(Link):
    init()

    url = Link

    response = requests.head(url)

    if "Server" in response.headers:
        server_header = response.headers["Server"]
        print(Fore.GREEN+"[INFO] looks like the Backend language is with", Fore.RESET+Fore.RED+server_header)
    else:
        print(Fore.RED+f"[INFO]Backend language not found for website:{Fore.RESET+url}")
        
# asyncio.run(find_backend_language())
