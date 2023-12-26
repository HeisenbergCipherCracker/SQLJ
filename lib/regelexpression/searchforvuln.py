import re
import sys
import os
current_directory = os.getcwd()

sys.path.append(current_directory)
from logger.sqljlog import logger as sqljlog

def detect_sql_injection(response_text:str):
    sql_injection_pattern = re.compile(
        r'\b(?:union(?:\s*all)?|select(?:\s+(?:(?:\*)|(?:distinct\s[^;]+)))?'
        r'|\binsert(?:\s+into\s+[^;]+)?|\bupdate(?:\s+set\s+[^;]+)?'
        r'|\bdelete(?:\s+from\s+[^;]+)?|\bdrop\s\w+|\balter\s\w+\b'
        r'|\bexec(?:ute)?|\bor\s*\d+\b|\band\s*\d+\b|\binformation_schema\.)\b', re.IGNORECASE)

    matches = re.findall(sql_injection_pattern, response_text)

    return sqljlog.info(f"[INFO]SQL keyword:{'|'.join(matches)} appears to be injectable.") if len(matches) > 0 else ""

# response_text = "This is a response with a SELECT statement and UNION ALL injection.FROM"
# response_text = ""
# sql_injection_matches = detect_sql_injection(response_text)

# if sql_injection_matches:
#     print(sql_injection_matches)

