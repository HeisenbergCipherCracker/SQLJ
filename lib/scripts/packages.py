import os
import sys
import asyncio
import re
import requests
from colorama import Fore,init,Style
from datetime import datetime
import sqlite3
parent_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(parent_dir)
from headers import *
import logging
add_directory = os.path.abspath(os.path.dirname(__file__))

priority_path = os.path.join(add_directory, '..', 'priority')

sys.path.append(priority_path)

try:
    from Priority import PRIORITY, HARMFULL
except ImportError:
    try:
        PRIORITES = __import__("Priority")
        PRIORITY = PRIORITIES.PRIORITY
        HARMFUL = PRIORITIES.HARMFUL
    except ImportError:
        try:
                
            del PRIORITES,PRIORITY,HARMFUL
            raise
        finally:
            print("[*] wrong installation, you can continue with the installation for now.")




current_directory = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_directory, '..', '..'))

sys.path.append(project_root)

from logger.logs import logger
current_directory = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_directory, '..'))
sys.path.append(project_root)

from regelexpression.patterns import Detect