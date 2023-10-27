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
        return f"Looks like the backend language of {Link} is with {server_header}.Do you want to continue?(y/n/q)"
    else:
        return f"Could not found any info related to the backend on the website {Link}"
        
print(asyncio.run(find_backend_language("https://mediawach.com/introducing-the-short-film-modir-e-madrese/")))
# print(type(ask))
