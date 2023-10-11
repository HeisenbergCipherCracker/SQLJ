import re 
import asyncio

#########################################################################################

generic_sql_injection_ls = []

error_based_sql_injection_ls = []

time_based_sql_injection_ls = []

generic_union_sql_injection_ls = []

auth_bypass_injection = []


#######################################################################################




class Singleton(type):
    """Create a singleton class for metaclass preparation """
    _instances = {} #* Create a insinstance null
    
    def __call__(cls, *args, **kwargs): #* using call to when we called the class
        #!only one instance allowed
        if cls not in cls._instances: #* see if there is an instance of class or not 
            instance = super().__call__(*args, **kwargs) #* if it is not the instance it use the super method to give it attributes
            cls._instances[cls] = instance 
        return cls._instances[cls] #* returns the value
    
class Payloads(metaclass=Singleton):
    
    @staticmethod
    async def generic_SQL_injection_payload():
        file_path = r"D:\SQLjj\SQLJ\payloads\generic_sql_ijc.txt"
        # file_path = "path/to/your/file.txt"  # Replace with the path to your file
# Open the file in read mode
        with open(file_path, "r") as file:
            # Read the file line by line
            payload_lines = [line.strip() for line in file.readlines()]

        # Print each line
        for line in payload_lines:
            global generic_sql_injection_ls
            generic_sql_injection_ls.append(line)
    
    @staticmethod   
    async def generic_error_based_SQL_injection():
        file_path = r"D:\SQLjj\SQLJ\payloads\generic_error_based.txt"
        # file_path = "path/to/your/file.txt"  # Replace with the path to your file
        with open(file_path,'r') as file:
            payload_lines = [line.strip() for line in file.readlines()]
            for line in payload_lines:
                global error_based_sql_injection_ls
                error_based_sql_injection_ls.append(line)
                
    @staticmethod
    async def time_based_SQL_injecdtion():
        file_path = r"D:\SQLjj\SQLJ\payloads\time_based_sql.txt"
        # file_path = "path/to/your/file.txt"  # Replace with the path to your file
        with open(file_path,'r') as file:
            payload_lines = [line.strip() for line in file.readlines()]
            for line in payload_lines:
                global time_based_sql_injection_ls
                time_based_sql_injection_ls.append(line)
                
    
    @staticmethod     
    async def generic_union_based_SQL_injection():
        file_path = r"D:\SQLjj\SQLJ\payloads\Generic_union_sqlinj.txt"
        
        with open(file_path,'r') as file:
            payload_lines = [line.strip() for line in file.readlines()]
            for line in payload_lines:
                global generic_sql_injection_ls
                generic_sql_injection_ls.append(line)
                
    @staticmethod      
    async def auth_bypass():
        # file_path = r"D:\SQLjj\SQLJ\payloads\auth_bypass.txt"
        file_path = r"D:\SQLjj\SQLJ\payloads\authBypass.txt"
        # file_path = "path/to/your/file.txt"  # Replace with the path to your file
        with open(file_path,'r') as file:
            payload_lines = [line.strip() for line in file.readlines()]
            for line in payload_lines:
                global auth_bypass_injection
                auth_bypass_injection.append(line)
                
                
payload = Payloads()
asyncio.run(payload.generic_error_based_SQL_injection())
        

