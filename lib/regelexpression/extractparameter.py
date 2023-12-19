import re
import sys
import os
current_directory = os.getcwd()

sys.path.append(current_directory)

from Exceptions.exceptions import SQLJNGParameterNotFoundError
from logger.sqljlog import logger as sqljlog
async def extract_parameter_name(url):
    # Define the pattern to Match the parameter name
    pattern = r'[?&]([^=]+)='

    # Search for the pattern in the URL
    Match = re.search(pattern, url)

    # Extract the parameter name
    if Match:
        parameter_name = Match.group(1)
        return parameter_name,""
    else:
        return "",""
    
async def check_parameter_exists(url):
        # Define the pattern to Match the parameter name
    pattern = r'[?&]([^=]+)='

    # Search for the pattern in the URL
    Match = re.search(pattern, url)

    # Extract the parameter name
    if Match:
        pass
    else:
        pass  

    

# parameter = None

# # Sample URL
# url = "http://testphp.vulnweb.com/artists.php?artist=1"

# # Extract the parameter name
# parameter_name,_ = extract_parameter_name(url)

# # Display the result
# if parameter_name:
#     print("Parameter Name:", parameter_name)
# else:
#     print("No parameter found.")
