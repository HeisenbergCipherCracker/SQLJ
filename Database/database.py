import sqlite3
import sys
sys.path.append(r"D:\SQLjj\SQLJ\payloads")
sys.path.append(r"D:\SQLjj\SQLJ\exploit")
from payloads import main, auth_bypass_list_ls, generic_error_ls, generic_sql_inj_ls, generic_union_ls
import asyncio
from exploit.authbypass_inj import capturesAUTHBYPASS
from exploit.Error_based_injection import capturesERRBASED
from exploit.genericSQL import generic_capture
from exploit.Timebasedinj import time_based_injection_capture
from exploit.Unionselect import UNIOn_capture

###############################################################################
extraction = []

lists_extracted = []


###############################################################################3



async def database_for_payloads():
    await main()
    con = sqlite3.connect("payLoadsS.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS payload (column1 datatype1, column2 datatype2)")

    # Insert the lists into the table
    payload_data = [(value,) for value in auth_bypass_list_ls] + [(value,) for value in generic_error_ls] + [(value,) for value in generic_sql_inj_ls] + [(value,) for value in generic_union_ls]
    cur.executemany("INSERT INTO payload (column1) VALUES (?)", payload_data)

    # Commit the changes
    con.commit()

    # Close the connection
    con.close()

async def retrieve_data():
    await database_for_payloads()
    con = sqlite3.connect("payLoadsS.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM payload")
    rows = cur.fetchall()
    for row in rows:
        global extraction
        extraction.append(list(row))
    
    return extraction

async def main_prog():
    await database_for_payloads()
    await retrieve_data()

    # asyncio.run(retrieve_data())
#     print(extraction)
# asyncio.run(main_prog())


async def data_base_for_captures():
    pass