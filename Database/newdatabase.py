import sys
sys.path.append('D:/SQLjj/SQLJ/exploit')
import authbypass_inj
import sqlite3

async def create_database_and_tables():
    con = sqlite3.connect("Captures.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS payloads (id INTEGER PRIMARY KEY AUTOINCREMENT, payload TEXT)")
    con.commit()
    con.close()
    