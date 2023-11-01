import nmap
import asyncio
import logging
from datetime import datetime

logging.basicConfig(filename="SQLJ.log",level=logging.DEBUG)

async def Find_open_ports_of_the_target(ipV4,scan="-p 1-1000",*args, **kwargs):
    """ 
    Note:
    #*The target should be entered as a ipv4 string
    #*User can enter desired scan type
    """
    try:
        # Create a PortScanner object
        scanner = nmap.PortScanner()
        target_host = ipV4
        logging.info(f"Initiated scan with nmap for the ipv4:{ipV4} in the time:{datetime.now()}")

        # Perform the network scan
        scan_result = scanner.scan(target_host, arguments=scan)
        logging.info(f"Scanned target:{ipV4} at the time:{datetime.now()}")
        # Retrieve the scan results
        for host in scanner.all_hosts():
            print("Host:", host)
            for proto in scanner[host].all_protocols():
                print("Protocol:", proto)
                ports = scanner[host][proto].keys()
                for port in ports:
                    state = scanner[host][proto][port]["state"]
                    print("Port:", port, "State:", state)
    except Exception as e:
        print(e)    
asyncio.run(Find_open_ports_of_the_target("65.61.137.117"))