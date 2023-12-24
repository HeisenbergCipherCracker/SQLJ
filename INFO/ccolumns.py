import os
import sys

def commom_table_naming():
    """
    >>> coln = commom_table_naming()
    >>> for c in coln:
        >>> print(coln if coln is not None else "")
    """
    filename = "commoncolums.txt"
    current_directory = os.path.dirname(os.path.abspath(__file__)) 
    file_path = os.path.join(current_directory, filename) 
    with open(file_path,'r') as file:
        columns = file.read()
        rows = columns.split("\n") 
        sorted_rows = sorted(rows) 
        sorted_payload = "\n".join(sorted_rows) #* 
        return sorted_payload if not sorted_payload.startswith("#") else None
    

