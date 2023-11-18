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
import logging
add_directory = os.path.abspath(os.path.dirname(__file__))

priority_path = os.path.join(add_directory, '..', 'priority')

sys.path.append(priority_path)






current_directory = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_directory, '..', '..','..'))

sys.path.append(project_root)

from logger.logs import logger
current_directory = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_directory, '..','..'))
sys.path.append(project_root)

from regelexpression.patterns import Detect
from scripts import payload4authpypass