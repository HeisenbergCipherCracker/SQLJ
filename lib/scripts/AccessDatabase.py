import sqlite3 
# from database import create_database_for_Captures
import asyncio
from colorama import Fore,init

init()

async def Access_the_data_base():
    # await create_database_for_Captures()
    conn = sqlite3.connect("ResultCap.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM Datas")
    result = cur.fetchall()
    HTMLresult = result[0]
    # print(sorted(HTMLresult))
    useragent = result[1]
    ipaddress = result[2]
    hostname = result[3]
    port = result[4]
    print(ipaddress)
    print(hostname)
    print(port) 
    print(HTMLresult)
    print(useragent)
    
    # print(useragent)
    ask = input("Which data you want to access?(useragent/htmlresult)")
    if ask == "1":
        print(f"the final html response :\n{HTMLresult}")
    
    elif ask == "2":
        print(useragent)
    
asyncio.run(Access_the_data_base())