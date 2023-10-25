import sqlite3
import random
import asyncio

async def create_table():
    con = sqlite3.connect("SQLJcap.db")
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

async def display_table():
    con = sqlite3.connect("Result.db")
    cur = con.cursor()

    # Display the values in the table
    cur.execute("SELECT attacktype FROM Datas")
    rows = cur.fetchall()
    print("Values in the table:")
    for row in rows:
        print("Type of attack:",row)

    con.close()

async def Run_the_create_table_command():
    await create_table()
    # await display_table()
async def Show_the_database_info():
    await Run_the_create_table_command()
    await display_table()
    
asyncio.run(display_table())