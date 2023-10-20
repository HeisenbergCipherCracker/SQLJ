from Graphics_input_handler import get_user_input
from tkinter import *
import tkinter as tk 
import sys
import sys
sys.path.append('D:/SQLjj/SQLJ/exploit')
import authbypass_inj
from authbypass_inj import auth_SQL_inj
import asyncio

@get_user_input
async def generic_sql_attack(User_input):
    await auth_SQL_inj(User_input)
    
asyncio.run(generic_sql_attack())