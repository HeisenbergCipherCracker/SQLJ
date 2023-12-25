import os
import sys

def commom_table_naming():
    """
    >>> for num in commom_table_naming():
        >>> print(num)
    """
    filename = "commoncolums.txt"
    current_directory = os.path.dirname(os.path.abspath(__file__)) 
    file_path = os.path.join(current_directory, filename) 
    with open(file_path,'r') as file:
        columns = file.read()
        rows = columns.split("\n") 
        sorted_rows = sorted(rows) 
        sorted_payload = "\n".join(sorted_rows) #* 
        for line in sorted_payload.split("\n"):
            yield line
    

    

