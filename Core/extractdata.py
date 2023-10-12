import sys
sys.path.append(r"D:\SQLjj\SQLJ\Database")
sys.path.append(r"D:\SQLjj\SQLJ\Database\database.py")
# from Database.database import database
from database import activate_the_payload,database
import asyncio
import sqlite3
sys.path.append(r"D:\SQLjj\SQLJ\Database")
from colorama import Fore,init

init()


########################################################################
generic_sql_attack_payload = []
time_based_attack = []
error_based_attack = []
union_attacks = []
auth_bypass_attack = []

#########################################################################





async def run_the_database():
    await database.connect_and_create_database()
    await database.insert_the_payloads_to_the_database_for_generic_SQL_payloads()
    await database.insert_the_time_based_error_to_the_data_base()
    await database.insert_to_auth_bypass()
    await database.insert_into_generic_union_based_SQL()
    
    

