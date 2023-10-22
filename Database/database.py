import sys
import sys
sys.path.append('D:/SQLjj/SQLJ/exploit')
import authbypass_inj
from authbypass_inj import auth_SQL_inj
import sys
import os
import sqlite3

def Create_data_base_for_captures():
    con = sqlite3.connect("Captures.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS Datas (id INTEGER PRIMARY KEY AUTOINCREMENT, Data TEXT)")
    con.commit()
    con.close()