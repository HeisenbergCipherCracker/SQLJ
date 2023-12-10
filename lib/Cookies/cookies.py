import sys
import os
import requests
from http.cookiejar import CookieJar

current_directory = os.getcwd()
sys.path.append(current_directory)
from Exceptions.exceptions import SQLJNGOptionError
from logger.logs import logger
from logger.sqljlog import logger as sqljlog

try:
    import requests
except ImportError:
    sys.exit("requests library is not installed. Exiting...")

async def extract_cookies(host):
    try:
        # Create a session and cookie jar
        session = requests.Session()
        cookie_jar = CookieJar()

        # Attach the cookie jar to the session
        session.cookies = cookie_jar

        # Make a GET request to the website using the session
        response = session.get(host)

        # Print the cookies with additional information
        for cookie in cookie_jar:
            msg = "Looks like that website: %s" % host
            msg += " is using the cookies below:"
            msg += f"\nName: {cookie.name}"
            msg += f"\nValue: {cookie.value}"
            msg += f"\nDomain: {cookie.domain}"
            msg += f"\nPath: {cookie.path}"
            msg += f"\nExpires: {cookie.expires}"
            msg += f"\nSecure: {cookie.secure}"
            logger.info(msg)
            sqljlog.info(msg)
            con = input("do you want to continue with this cookies(you can use your own cookies)?(y/q)")
            if con == "y":
                pass
            elif con == "q":
                raise SystemExit
            else:
                raise SQLJNGOptionError
            
        return
    
    except SystemExit:
        raise
    except SQLJNGOptionError:
        logger.error("Invalid prompt given.please use y to continue or q to exit.")
        

# Example usage
# extract_cookies("https://www.google.com")
