import os
import sys
current_directory = os.getcwd()
from dataclasses import dataclass
from abc import ABC,abstractmethod
from functools import total_ordering


sys.path.append(current_directory)
from Exceptions.exceptions import SQLJNGMagicDictKeyMissing
from lib.Stacks.stack import Stack
from Exceptions.exceptions import SQLJNGBasicException as SQLJException

@total_ordering
@dataclass
class MagicDictShape(dict,ABC):
    cap : Stack
    @abstractmethod
    def __missing__(self,key):
        pass

    @abstractmethod
    def insert_captures_to_dict(self):
        pass

    @abstractmethod
    def safe_insert_to_dict(self):
        pass

    @abstractmethod
    def Errors(self,err:SQLJException):
        pass

    @abstractmethod
    def attack_types_used(self):
        pass

class MagicDict(MagicDictShape):
    def __missing__(self, key):
        raise SQLJNGMagicDictKeyMissing
    
    def insert_captures_to_dict(self,capture:str,value:Stack):
        val = self[capture] = value
        return val

    def safe_insert_to_dict(self,keyname):
        val = self[keyname] = self.cap
        return val
    
    def Errors(self,err:SQLJException,keyerr:str = "Kerr"):
        val = self[keyerr] = err
        return val

# d = Stack()
# d.push(3)

# d = MagicDict(3)
# print(d.insert_captures_to_dict("ke",d))
# magic_dict_instance = MagicDict(d)
# result = magic_dict_instance.insert_captures_to_dict("ke", d)

# # Print keys and values of the dictionary
# for key, value in magic_dict_instance.items():
#     print(f"Key: {key}, Value: {value}")
        



