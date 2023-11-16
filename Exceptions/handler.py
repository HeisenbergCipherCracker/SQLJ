import re

def extract_package_name_from_import_error(error_message):
    # Define a regular expression pattern to match import errors
    pattern = r"ImportError: No module named '(.+)'"

    # Use re.search to find the match
    match = re.search(pattern, error_message)

    # Check if a match is found
    if match:
        # Extract the package name from the matched group
        package_name = match.group(1)
        return package_name
    else:
        return None
