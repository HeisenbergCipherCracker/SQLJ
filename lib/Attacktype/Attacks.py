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

class HeaderAttacks(Enum):
    GENERIC_SQL_INJECTION_HEADER = f"{Fore.RESET}{Fore.WHITE}{Style.RESET_ALL}{Style.BRIGHT}generic sql injection (payloads)"
    AUTH_BYPASS_SQL_INJECTION_HEADER = f"{Fore.RESET}{Fore.WHITE}{Style.RESET_ALL}{Style.BRIGHT}authentication bypass sql injection (payloads)"
    TIME_BASED_SQL_INJECTION_HEADER = f"{Fore.RESET}{Fore.WHITE}{Style.RESET_ALL}{Style.BRIGHT}time based sql injection (payloads)"
    ERROR_BASED_SQL_INJECTION_HEADER = f"{Fore.RESET}{Fore.WHITE}{Style.RESET_ALL}{Style.BRIGHT}error based sql injection (payloads)"
    PRIVILLAGE_ESCALATION_HEADER = f"{Fore.RESET}{Fore.WHITE}{Style.RESET_ALL}{Style.BRIGHT}privilege escalation (payloads)"




# a = AttackType.GENERIC_SQL_INJECTION

# print(f"using:{a.value}")






    
