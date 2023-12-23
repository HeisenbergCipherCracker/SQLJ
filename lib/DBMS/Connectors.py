# self.connector = pyodbc.connect('Driver={Microsoft Access Driver (*.mdb)};Dbq=%s;Uid=Admin;Pwd=;' % self.db)
import pyodbc
import os
import sys

cur = os.getcwd()
sys.path.append(cur)
from logger.sqljlog import logger as sqljlog
class DBMSConnector:
    def __init__(self,db,username,password,server) -> None:
        self.db = db
        self.server = server
        self.username = username
        self.password = password
    
    def connect(self):
        try:

            conn = pyodbc.connect('DRIVER={MySQL ODBC 8.0 ANSI Driver};SERVER=localhost;DATABASE=mydatabase;USER=myusername;PASSWORD=mypassword')
        
        except (pyodbc.Error,pyodbc.OperationalError) as exc:
            errmsg = str(exc)
            errmsg += "\n the above error message occurred while interacting with database."
            sqljlog.error(errmsg)
    


