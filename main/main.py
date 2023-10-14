import sys

from authbypass_inj import auth_SQL_inj

#########################################################################


logo = """
   _____ ____    __        __
  / ___// __ \  / /       / /
  \__ \/ / / / / /   __  / / 
 ___/ / /_/ / / /___/ /_/ /  
/____/\___\_\/_____/\____/   
                             

"""

options = """
1.authbypassSQL
2.ErrorbasedINJection
3.GenericSQL
4.TimebasedSQL
5.UNIONselect

"""

async def main():
    global logo
    print(logo)
    await asyncio.sleep(1)
    url = input("[INFO] enter the url of the target:")
    # await auth_SQL_inj(url)
    ch = int(input("enter the exploit attack:"))
    match ch:
        case "1":
            url = input("enter the target url:")
            await auth_SQL_inj(url)
            
asyncio.run(main())

