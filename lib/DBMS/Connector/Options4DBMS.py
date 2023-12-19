import os
import sys

cur = os.getcwd()
sys.path.append(cur)

from lib.DBMS.Connector.Connection import db_handler
from lib.extra.options import db_options
from lib.DBMS.Connector.Connection import DBMS_mysql


def mysql_dbms_interface(hosturl):
    while True:
        username = input("Enter the possible username of the target website:")
        if username == "":
            pass
        password = input("Enter the possible password of the target website:")
        if password == "":
            pass
        db_name = input("Enter the possible database name of the target website:")
        if db_name == "":
            pass
        tableN = input("Enter the possible table name of the target website:")
        if tableN == "":
            pass
        DB_handler = DBMS_mysql(host=hosturl,user=username if username is not "" else "root",password=password if password is not "" else "alimirmohammad",database=db_name if db_name is not "" else "mysql",tablename=tableN if tableN is not "" else "db")
        print(db_options)
        match input("(sqljng)>>>"):
            case "1":
                DB_handler._show_database_columns_info()
            
            case "2":
                DB_handler.show_all_tables()
            
            case "3":
                DB_handler.drop_table()
            
            case "4":
                DB_handler.alter_table()
            
            case "5":
                DB_handler.show_databases()
            
            case "6":
                DB_handler.show_all_tables()
            
            case "7":
                DB_handler._describe_table()
            
            case "8":
                DB_handler.select_data_from_table()

            case "9":
                DB_handler.drop_data_base()

            case "10":
                DB_handler.create_database()
            
            case "":
                pass

            case "esc":
                break
            case "Exit"|"exit":
                raise SystemExit
            


mysql_dbms_interface("localhost")


