import os
import sys
current_directory = os.getcwd()
sys.path.append(current_directory)
from Exceptions.exceptions import SQLJNGFatalError
from Exceptions.exceptions import SQLJNGInstallationError
from Exceptions.exceptions import SQLJNGModuleError
from logger.logs import logger
import subprocess
from lib.mysqlerrorbased.OPS.OSY import Operatingsystem
from lib.mysqlerrorbased.OPS.OSY import Operatingsystem
from lib.mysqlerrorbased.OPS.Platforms import Platforms

from Exceptions.exceptions import SQLJNGOSError

class Metasploit(object):
    @staticmethod
    def Metasploit_installation():
        if Operatingsystem() != Platforms.LINUX:
            raise SQLJNGInstallationError
        elif Operatingsystem() == Platforms.LINUX:
            try:
                process = subprocess.Popen(['msfconsole'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

                # Send commands to Metasploit console
                commands = [
                    'use auxiliary/scanner/http/http_version',
                    'set RHOSTS 192.168.1.1',
                    'run',
                ]
                for command in commands:
                    process.stdin.write(command + '\n')
                    process.stdin.flush()
    
                # Close the Metasploit console
                process.stdin.write('exit\n')
                process.stdin.flush()
                process.wait()

                # Capture the output
                output, error = process.communicate()

                # Print the output and error
                print("Output:")
                print(output)

                print("Error:")
                print(error)

            except KeyboardInterrupt:
                print("Aborted by user.")



# Metasploit.Metasploit_installation()