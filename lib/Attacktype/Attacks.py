from enum import Enum
from colorama import Fore,init,Style

init()

class AttackType(Enum):
    GENERIC_SQL_INJECTION = f"{Fore.RESET}{Fore.WHITE}{Style.RESET_ALL}{Style.BRIGHT}generic sql injection (payloads)"
    AUTH_BYPASS_SQL_INJECTION = f"{Fore.RESET}{Fore.WHITE}{Style.RESET_ALL}{Style.BRIGHT}authentication bypass sql injection (payloads)"
    TIME_BASED_SQL_INJECTION = f"{Fore.RESET}{Fore.WHITE}{Style.RESET_ALL}{Style.BRIGHT}time based sql injection (payloads)"
    ERROR_BASED_SQL_INJECTION = f"{Fore.RESET}{Fore.WHITE}{Style.RESET_ALL}{Style.BRIGHT}error based sql injection (payloads)"
    PRIVILLAGE_ESCALATION = f"{Fore.RESET}{Fore.WHITE}{Style.RESET_ALL}{Style.BRIGHT}privilege escalation (payloads)"
    NO_SQL = f"{Fore.RESET}{Fore.WHITE}{Style.RESET_ALL}{Style.BRIGHT}no sql(payloads)"
    MY_SQL = f"{Fore.RESET}{Fore.WHITE}{Style.RESET_ALL}{Style.BRIGHT}MYSQL (payloads)"
    ORACLE = f"{Fore.RESET}{Fore.WHITE}{Style.RESET_ALL}{Style.BRIGHT}ORACLE injection (payloads)"
    INVALIDHTTP_REQ = f"{Fore.RESET}{Fore.WHITE}{Style.RESET_ALL}{Style.BRIGHT}invalid http (payloads)"
    UNION_BASED_SQL_INJECTION = f"{Fore.RESET}{Fore.WHITE}{Style.RESET_ALL}{Style.BRIGHT}UNION ALL SELECT (payloads)"

class HeaderAttacks(Enum):
    GENERIC_SQL_INJECTION_HEADER = f"{Fore.RESET}{Fore.WHITE}{Style.RESET_ALL}{Style.BRIGHT}generic sql injection using headers (payloads)"
    AUTH_BYPASS_SQL_INJECTION_HEADER = f"{Fore.RESET}{Fore.WHITE}{Style.RESET_ALL}{Style.BRIGHT}authentication bypass sql injection using headers (payloads)"
    TIME_BASED_SQL_INJECTION_HEADER = f"{Fore.RESET}{Fore.WHITE}{Style.RESET_ALL}{Style.BRIGHT}time based sql injection using headers (payloads)"
    ERROR_BASED_SQL_INJECTION_HEADER = f"{Fore.RESET}{Fore.WHITE}{Style.RESET_ALL}{Style.BRIGHT}error based sql injection using headers (payloads)"
    PRIVILLAGE_ESCALATION_HEADER = f"{Fore.RESET}{Fore.WHITE}{Style.RESET_ALL}{Style.BRIGHT}privilege escalation using headers (payloads)"
    UNION_BASED_SQL_INJECTION = f"{Fore.RESET}{Fore.WHITE}{Style.RESET_ALL}{Style.BRIGHT}UNION ALL SELECT using headers (payloads)"

class OracleAttacks(Enum):
    DATABASE_COLUMN_LIST =  f"{Fore.RESET}{Fore.WHITE}{Style.RESET_ALL}{Style.BRIGHT}database column list (payloads)"
    DATABASE_LIST = f"{Fore.RESET}{Fore.WHITE}{Style.RESET_ALL}{Style.BRIGHT}database list (payloads)"
    DATABASE_NAME = f"{Fore.RESET}{Fore.WHITE}{Style.RESET_ALL}{Style.BRIGHT}database name (payloads)"
    HOST_NAME_INJECTION = f"{Fore.RESET}{Fore.WHITE}{Style.RESET_ALL}{Style.BRIGHT}host name  (payloads)"
    NORMAL_ORACLE = f"{Fore.RESET}{Fore.WHITE}{Style.RESET_ALL}{Style.BRIGHT}normal oracle(payloads)"

class ErrorBasedSQl(Enum):
    INVALID_HTTP_REQ = f"{Fore.RESET}{Fore.WHITE}{Style.RESET_ALL}{Style.BRIGHT}invalid http request (payloads)"
    BASIC_SQL_Error_Based = f"{Fore.RESET}{Fore.WHITE}{Style.RESET_ALL}{Style.BRIGHT}basic sql (payloads)"
    MYSQL_EXTRACT_VALUE = f"{Fore.RESET}{Fore.WHITE}{Style.RESET_ALL}{Style.BRIGHT}mysql extract value(payloads)"
    MYSQL_NAME_CONST = f"{Fore.RESET}{Fore.WHITE}{Style.RESET_ALL}{Style.BRIGHT}name const(payloads)"






# a = AttackType.GENERIC_SQL_INJECTION

# print(f"using:{a.value}")






    
