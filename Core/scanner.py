import requests
from bs4 import BeautifulSoup
from colorama import init,Fore,Style
import re
import asyncio

init()

async def scan_for_the_website():

    url = "http://scanme.org/"  # Replace with the URL of the website you want to inspect

    response = requests.get(url)

    server_header = response.headers.get("Server")
    powered_by_header = response.headers.get("X-Powered-By")

    print(Fore.GREEN+"Server:", server_header)
    print(Fore.GREEN+"X-Powered-By:", powered_by_header)

async def find_the_backend_info_php():

    url = "https://bwapp.hakhub.net/sqli_4.php"  # Replace with the URL of the website you want to inspect

    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    # Find the server-side code or programming language mentioned in the HTML source
    backend_language = soup.find("meta", attrs={"name": "generator"})

    if backend_language:
        info = (Fore.RED+"Backend Language:", backend_language["content"])
        print(info)
        if re.search(r"mysql",str(info)):
            print(Fore.GREEN+"Backend Language is with MYSQL.")
            return True
            
        if re.search(r"PHP",str(info)):
            print(Fore.GREEN+"Backend Language is with PHP.")
            global Info_php_url
            
            
    else:
        print(Fore.GREEN+"Backend Language information not found.")
        
        
asyncio.run(find_the_backend_info_php())

