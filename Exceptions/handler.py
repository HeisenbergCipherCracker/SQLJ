import re
import sys
import os
parent_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(parent_dir)
current_directory = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_directory, '..'))
sys.path.append(project_root)


add_directory = os.path.abspath(os.path.dirname(__file__))

priority_path = os.path.join(add_directory, '..', 'priority')

sys.path.append(priority_path)




current_directory = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_directory, '..', '..'))

sys.path.append(project_root)

from logger.logs import logger

import re

import re

import re

def extract_package_name_from_import_error(error_message):
    # Convert error_message to a string
    if not isinstance(error_message, str):
        error_message = str(error_message)

    print(f"Debug: error_message: {error_message}")  # Add this line for debugging

    # Define a regular expression pattern to match import errors
    pattern = r"No module named ['\"]?([^'\"]+)['\"]?"

    # Use re.search to find the match
    match = re.search(pattern, error_message)

    print(f"Debug: match: {match}")  # Add this line for debugging

    # Check if a match is found
    if match:
        # Extract the package name from the matched group
        package_name = match.group(1)
        return package_name
    else:
        pass
    


def Install_missing_packages(e):
    msg = str(e)
    logger.error(e)
    ins = extract_package_name_from_import_error(msg)
    match input(f"Do you want to install the dependencies that has been missing? (y/n): "):
        case "y":
            from subprocess import check_call
            import subprocess
            try:
                check_call(["pip","install",str(ins)])
            
            except subprocess.CalledProcessError as expro:
                try:
                    check_call(["pip","install",str(ins), "--upgrade"])
                
                except subprocess.CalledProcessError as expro:
                    try:
                        check_call(["python3", "-m", "pip", "install", str(ins)])
                    
                    except subprocess.CalledProcessError as expro:
                        try:
                            check_call(["python3", "-m", "pip", "install", str(ins)])
                        
                        except subprocess.CalledProcessError as expro:
                            logger.error(expro)
                            raise SystemExit


            
            except PermissionError as experm:
                logger.error(experm)
                raise SystemExit
        
        case "n":
            raise SystemExit
        

