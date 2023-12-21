import subprocess
import os
import sys

cur = os.getcwd()
sys.path.append(cur)

from lib.SQLJNGDataTypes.memlists import Memelist
from lib.systempaths.checkpath import check_path as isvalidpath


def get_databases_path_for_sqlite_exploit():
    """
    >>> gen = Memelist(get_databases_path_for_sqlite_exploit())
    >>> GEN = gen.get_list_as_generator_obj(gen)
    >>> for item in GEN:
    >>> print(item)
    """

    result = subprocess.run(['find', '/', '-iname', '*.db'], capture_output=True, text=True)

    path_list = result.stdout.splitlines()

    db_paths = []

    for path in path_list:
        db_paths.append(path if isvalidpath(path) else None)
    
    return db_paths


