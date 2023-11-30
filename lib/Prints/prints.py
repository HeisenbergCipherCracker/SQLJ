from colorama import *

init()

def print_function_yellow(*args)->None:
    for par in args:
        print(f"{Fore.RESET}{Fore.YELLOW}{par}")


# Print_function_yellow("gg",6,"yy")