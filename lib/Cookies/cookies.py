import sys
import os
import requests
from http.cookiejar import CookieJar

current_directory = os.getcwd()
sys.path.append(current_directory)
from Exceptions.exceptions import SQLJNGConnectionError
from logger.logs import logger

try:
    import requests
except ImportError:
    sys.exit("requests library is not installed. Exiting...")

def extract_cookies(host):
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
    except Exception as e:
        # Handle exceptions, log or raise as needed
        logger.error(f"An error occurred: {e}")
        raise

# Example usage
extract_cookies("https://www.google.com")
