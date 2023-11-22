import os
import sys
current_directory = os.getcwd()
sys.path.append(current_directory)
from threading import Thread
from logger.logs import logger
from Exceptions.exceptions import SQLJNGFatalError
from lib.mysqlerrorbased.OPS.OSY import Operatingsystem
from lib.mysqlerrorbased.OPS.Platforms import Platforms
from Exceptions.exceptions import SQLJNGFatalError
from lib.priority.Priority import PRIORITY
from lib.priority.Priority import HARMFULL
from Exceptions.exceptions import SQLJNGOSError
import subprocess

#Reference :https://stackoverflow.com/questions/32382793/inheritance-threading-thread-class-does-not-work


class SQLmap(Thread):
    def __init__(self,url,username=False,password=False,dump=False,columns=False,tables=False):
        self.url = url
        self.username = username
        self.password = password
        self.dump = dump
        self.columns = columns
        self.tables = tables
        self.os = Operatingsystem()
        self.platform = Platforms()
        Thread.__init__(self)

    def _Check_SQlmap(self):
        try:
            if self.os != self.platform.LINUX:
                raise SQLJNGOSError
            
            elif self.os == self.platform.LINUX:
                cmd = subprocess.check_output(["sqlmap","--version"])
                msg = "sqlmap version:"
                msg += str(cmd.decode('utf-8') if type(cmd) != int else "")
                logger.info(msg)
                return True

        
        except (subprocess.CalledProcessError,subprocess.SubprocessError) as exc:
            logger.error(exc)
            return False


        except SQLJNGOSError:
            logger.critical("Sqlmap cannot be executed in your system.")
            return False
        
        except KeyboardInterrupt:
            logger.info("Aborted")
            return False
        
    
    def exploit(self):
        if self._Check_SQlmap():
            try:
                #Reference:https://stackoverflow.com/questions/89228/how-do-i-execute-a-program-or-call-a-system-command
                cmd = subprocess.Popen(["sqlmap","-u",str(self.url)])
                cmd.wait()
                print(cmd)
            
            except (subprocess.CalledProcessError,subprocess.SubprocessError) as err:
                logger.error(err)
            
            except KeyboardInterrupt:
                logger.info("Aborted")
            
        else:
            logger.critical("Your system cannot execute sqlmap")
            
            
                

                
            
    
    def run(self):
        pass





obj = SQLmap('http://testfire.net/')
obj.exploit()
