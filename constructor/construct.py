import asyncio
import os
import sys
import warnings

warnings.warn("This file is outdated!")

class Constructor(object):
    def __init__(self, file):
        self.file = file
    
    def __enter__(self):
        current_directory = os.path.dirname(os.path.abspath(__file__)) 
        file_path = os.path.join(current_directory, self.file) 
        with open(file_path, "r") as file:
            payload = file.read()
            rows = payload.split("\n") 
            sorted_rows = sorted(rows) 
            sorted_payload = "\n".join(sorted_rows) 
            return sorted_payload
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

# Example usage:

