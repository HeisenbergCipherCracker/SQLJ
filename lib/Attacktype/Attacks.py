from enum import Enum
from colorama import Fore,init,Style

init()

class AttackType(Enum):
    GENERIC_SQL_INJECTION = f"{Fore.RESET}{Fore.WHITE}{Style.RESET_ALL}{Style.BRIGHT}generic sql injection (payloads)"
    AUTH_BYPASS_SQL_INJECTION = "authentication bypass sql injection (payloads)"
    TIME_BASED_SQL_INJECTION = "time based sql injection (payloads)"
    ERROR_BASED_SQL_INJECTION = "error based sql injection (payloads)"
    PRIVILLAGE_ESCALATION = "privilege escalation (payloads)"
    NO_SQL = "no sql(payloads)"
    MY_SQL = "MYSQL (payloads)"
    ORACLE = "ORACLE injection (payloads)"
    INVALIDHTTP_REQ = "invalid http (payloads)"

a = AttackType.GENERIC_SQL_INJECTION

print(f"using:{a.value}")






    
