import sys
sys.path.append('D:/SQLjj/SQLJ/exploit')
import authbypass_inj
import sqlite3
import genericSQL
import Timebasedinj
import Error_based_injection
from Error_based_injection import capturesERRBASED
from genericSQL import generic_capture
from Timebasedinj import time_based_injection_capture
from authbypass_inj import capturesAUTHBYPASS


def create_database_and_tables():
    con = sqlite3.connect("Captures.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS Datas (id INTEGER PRIMARY KEY AUTOINCREMENT, Data TEXT)")
    con.commit()
    con.close()
    
def Insert_the_data_to_the_data_base():
    con = sqlite3.connect("Captures.db")
    cur = con.cursor()
    cur.execute("INSERT INTO Datas (Data) VALUES (?)", (capturesERRBASED,generic_capture))
    con.commit()
    con.close()
    