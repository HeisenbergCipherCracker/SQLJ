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

    
import itertools

import random
import string

async def generate_random_value():
    length = 10
    random_value = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
    return random_value

import random
import string
import asyncio

async def generate_random_value():
    length = 10
    random_value = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
    return random_value

async def extract_parameter_name(url):
    pattern = r'[?&]([^=]+)='
    Match = re.search(pattern, url)
    if Match:
        parameter_name = Match.group(1)
        return parameter_name, ""
    else:
        return "", ""

async def parameter_injection(url, payload):
    parameter_name, _ = await extract_parameter_name(url)
    random_value = await generate_random_value()
    modified_url = url.replace(parameter_name + "=1", parameter_name + "=" + payload)
    return modified_url

async def main():
    modified_url = await parameter_injection("http://example.com?param=1", "new_value")
    print("Modified URL:", modified_url)

# asyncio.run(main())
