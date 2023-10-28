import sqlite3
import random
import asyncio
from colorama import Fore,init

init()

async def create_table():
    con = sqlite3.connect("Result.db")
    cur = con.cursor()

    # Create the table if it does not exist
    cur.execute("CREATE TABLE IF NOT EXISTS Datas (id INTEGER PRIMARY KEY AUTOINCREMENT, Data TEXT, attacktype TEXT)")

    # Check if the "attacktype" column already exists
    cur.execute("PRAGMA table_info(Datas)")
    columns = cur.fetchall()
    column_names = [column[1] for column in columns]
    if "attacktype" not in column_names:
        try:
            # Add the "attacktype" column
            cur.execute("ALTER TABLE Datas ADD COLUMN attacktype TEXT")
            con.commit()
            print("Added 'attacktype' column to the database table")
        except sqlite3.Error as e:
            print("Error occurred while adding 'attacktype' column:", e)
    else:
        print("'attacktype' column already exists in the database table")

    # Insert random values into the table
    values = []
    for _ in range(5):
        data = random.randint(1, 100)
        attack_type = random.choice(["Type 1", "Type 2", "Type 3"])
        values.append((data, attack_type))

    try:
        cur.executemany("INSERT INTO Datas (Data, attacktype) VALUES (?, ?)", values)
        con.commit()
        print("Inserted values into the database table")

    except sqlite3.Error as e:
        print("Error occurred while inserting values:", e)

    con.close()

async def display_table_Attacktype():
    con = sqlite3.connect("Result.db")
    cur = con.cursor()
    # Display the values in the table
    cur.execute("SELECT attacktype FROM Datas")
    # cur.execute("SELECT Data FROM Datas")
    rows = cur.fetchall()
    print(Fore.GREEN+"Values in the table:")
    for row in rows:
        print(Fore.GREEN+"Type of attack:",row)

    con.close()

async def Display_info_of_the_Datas():
    con = sqlite3.connect("Result.db")
    cur = con.cursor()
    # Display the values in the table
    cur.execute("SELECT Data FROM Datas")
    # cur.execute("SELECT Data FROM Datas")
    rows = cur.fetchall()
    print("Values in the table:")
    for row in rows:
        print(Fore.GREEN+"Data:",row[0])
async def Display_info_of_the_Datas():
    con = sqlite3.connect("Result.db")
    cur = con.cursor()
    # Display the values in the table
    cur.execute("SELECT Data, attacktype FROM Datas")
    rows = cur.fetchall()
    print("Values in the table:")
    for row in rows:
        try:
            print(Fore.GREEN + "Attack Type:", row[1], "Data:", row[0])
        except IndexError:
            print("Error: Unexpected number of columns in the database table")

async def Run_the_create_table_command():
    await create_table()
    # await display_table_Attacktype()
async def Show_the_database_info_for_attacktype():
    await Run_the_create_table_command()
    await display_table_Attacktype()

async def show_database_info_for_datas():
    await Run_the_create_table_command()
    await Display_info_of_the_Datas()
    
# asyncio.run(Display_info_of_the_Datas())

import sqlite3
import asyncio

import sqlite3
import asyncio

class Database:
    def __init__(self, table=None, column=None):
        self.table = table
        self.column = column

    @staticmethod
    def create_table():
        con = sqlite3.connect("SQLJresult.db")
        cur = con.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS Datas (id INTEGER PRIMARY KEY AUTOINCREMENT, Data TEXT, datetime TEXT, attacktype TEXT)")
        con.commit()
        con.close()

    @staticmethod
    def display_the_info():
        con = sqlite3.connect("SQLJresult.db")
        cur = con.cursor()
        cur.execute("SELECT * FROM Datas")
        rows = cur.fetchall()
        print("Values in the table:")
        for row in rows:
            print(Fore.GREEN+"Data:",row[0])
            print(Fore.GREEN+"dateandtime",row[1])
            print(Fore.GREEN+"Attacktype",row[2])
        con.close()

    @staticmethod
    def insert_value():
        con = sqlite3.connect("SQLJresult.db")
        cur = con.cursor()
        cur.execute("INSERT INTO Datas (Data, attacktype) VALUES ('test', 'test')")
        con.commit()
        con.close()

async def Create_table_for_the_captures_datas():
    db = Database
    await db.create_table()
    # await Database.create_table()
    # await Database.insert_value()
    # await Database.display_the_info()
    
async def Display_the_database_info_of_captures():
    db = Database
    await Create_table_for_the_captures_datas()
    await db.display_the_info()
    


# asyncio.run(Database.display_the_info())
    

