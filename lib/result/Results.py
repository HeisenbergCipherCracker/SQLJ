import time
import sys,os
current_directory = os.getcwd()


sys.path.append(current_directory)
from logger.logs import logger
from Exceptions.exceptions import SQLJNGStackRangeError
from lib.Stacks.stack import Stack

async def SQLJNG_result_report(arr:Stack):
    try:
        for _ in arr:
            error_cap = arr[0]
            id_cap = arr[1]
            err_cap_html = arr[2]
            id_html = arr[3]
            err_cap_html_2 = arr[4]
            # sig_cap = Significant_captures[0]
            admin_cap = arr[6]
            logger.info("You will see error message captured in 3 seconds")
            time.sleep(3)
            logger.info(error_cap)
            print("You will see id parameter captured in 3 seconds")
            time.sleep(4)
            logger.info(id_cap)
            print("You will see error parameter captured in 5 seconds")
            time.sleep(5)
            logger.info(err_cap_html)
            print("id parameter captured will be shown in the 3 seconds")
            time.sleep(3)
            logger.info(id_html)
            print("id in html captured will be shown after 5 seconds")
            time.sleep(3)
            logger.info(err_cap_html_2)
            print("admin parameter captured will be shown after 7 seconds")
            time.sleep(7)
            # logger.info(sig_cap)
            logger.info(admin_cap)
    
    except IndexError:
        raise SQLJNGStackRangeError
    except KeyboardInterrupt:
        raise SystemExit
    

def safe_SQLJNG_result(array:Stack):
    if array.size() >= 6:
        return array[6],array[5],array[4],array[3],array[2],array[1],array[0]
    else:
        logger.critical("Could not capture enough data.")
    

# from asyncio import run
# e = Stack()
# e.push(3,5)

# run(SQLJNG_result_report(e)

# print(safe_SQLJNG_result(e))
