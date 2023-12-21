import os
def check_path(path):
    if os.path.exists(path):
        return True
    else:
        return False