import mysql.connector
from prettytable import PrettyTable
import re


class DBMS_mysql:
    def __init__(self, host, user, password, database,tablename=None) -> None:
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
        self.cursor.execute(f"SELECT * FROM {self.tablename}")
        result = self.cursor.fetchall()
        for row in result:
            self.table.add_column(row)
        
        print(self.table)
    
    def drop_data_base(self):
        self.cursor.execute(f"DROP DATABASE IF EXISTS {self.database}")
    
    def create_database(self):
        self.cursor.execute(f"CREATE DATABASE IF NOT EXISTS Your_security_is_fucked_up_and_suck_dicks")
    

# Example usage
obj = DBMS_mysql("localhost", "root", "alimirmohammad", "mysql",tablename="mmd")
obj.create_database()
