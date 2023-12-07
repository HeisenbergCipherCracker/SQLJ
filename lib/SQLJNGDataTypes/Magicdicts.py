import os
import sys
current_directory = os.getcwd()
from dataclasses import dataclass
from abc import ABC,abstractmethod
from functools import total_ordering
import random


sys.path.append(current_directory)
from Exceptions.exceptions import SQLJNGMagicDictKeyMissing
from lib.Stacks.stack import Stack
from Exceptions.exceptions import SQLJNGBasicException as SQLJException
from lib.Attacktype.Attacks import AttackType

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
    def attack_types_used(self,attack):
        pass

class MagicDict(MagicDictShape):
    """
    This class is used to store the stacks data types to the magic dicts to restore the injectable parameters
    >>> d = Stack(value)
    >>> magic_dict_instance = MagicDict(d)
    >>> result = magic_dict_instance.insert_captures_to_dict("ke", d)

    >>> Print keys and values of the dictionary
    >>> for key, value in magic_dict_instance.items():
    >>>  print(f"Key: {key}, Value: {value}")
    """
    def __missing__(self, key):
        raise SQLJNGMagicDictKeyMissing
    
    def insert_captures_to_dict(self,capture:str,value:Stack):
        val = self[capture] = value
        return val

    def safe_insert_to_dict(self,keyname):
        val = self[keyname] = self.cap
        return val
    
    def Errors(self,err:SQLJException,keyerr:str = f"Kerr{str(random.randint(1,1000))}"):
        val = self[keyerr] = err
        return val
    
    def attack_types_used(self,attack):
        val = self["ATTACKS"] = attack
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
        



