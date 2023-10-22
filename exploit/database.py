import sqlite3 
import asyncio


async def create_database_for_Captures():
    con = sqlite3.connect("ResultCap.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS Datas (id INTEGER PRIMARY KEY AUTOINCREMENT, Data TEXT)")
    con.commit()
    con.close()
    
if __name__ != "__main__":
    asyncio.run(create_database_for_Captures())