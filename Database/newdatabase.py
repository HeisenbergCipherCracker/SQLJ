import sys
sys.path.append('D:/SQLjj/SQLJ/exploit')
import authbypass_inj
import sqlite3

async def create_database_and_tables():
    con = sqlite3.connect("Captures")