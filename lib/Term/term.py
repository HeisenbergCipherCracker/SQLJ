term = """


Disclaimer: Use of SQLJ SQL Injection Tool

The SQLJ SQL Injection Tool (hereinafter referred to as "SQLJ") is a software application designed exclusively for educational and legitimate security testing purposes. It is intended to be used by cybersecurity professionals, system administrators, and ethical hackers for the explicit purpose of identifying vulnerabilities and strengthening the security of web applications.

Prohibited Use:
SQLJ is strictly prohibited from being used for any malicious, unauthorized, or illegal activities, including any actions that violate applicable laws and regulations. The use of SQLJ for any illegal or unethical purposes, such as unauthorized access or data theft, is strictly against the terms of use.

Compliance with Laws:
Users of SQLJ must adhere to all local, national, and international laws and regulations when utilizing this tool. The onus for ensuring legal and ethical use falls entirely on the user.

Authorization and Consent:
SQLJ may only be used on web applications for which users possess explicit authorization from the owners or administrators of those applications. It is imperative to obtain proper consent before conducting any testing, and users are responsible for ensuring they have the requisite legal rights and permissions.

Educational and Ethical Purposes:
SQLJ is intended solely for educational and security assessment purposes. It is essential to use SQLJ responsibly and for ethical purposes, with the primary objective of enhancing web application security.

Liability:
The creators and maintainers of SQLJ assume no responsibility for any illegal, unauthorized, or unethical use of the tool. Users bear full responsibility for their actions when utilizing SQLJ.

By using SQLJ, you acknowledge that you have read and understood this disclaimer and agree to use the tool exclusively in a legal, ethical, and responsible manner. Any misuse or illegal application of SQLJ may result in severe legal consequences, and the creators and maintainers of SQLJ are not liable for any such actions.






"""

import time
import sys

def Agree():

    print(term)
    while True:
        try:
            time.sleep(5)
            agree = input("Do you agree to the above terms? (y/n): ")
            if agree == "y":
                break

            elif agree == "n":
                raise SystemExit("You have to agree to the above terms.")
        except KeyboardInterrupt:
            sys.exit("\nExiting...")    
                

    
Agree()