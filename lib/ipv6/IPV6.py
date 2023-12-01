import socket

def get_ipv6_address(hostname):
    try:
        # Get IPv6 address information for the given hostname
        result = socket.getaddrinfo(hostname, None, socket.AF_INET6)
        
        # Extract the first IPv6 address from the result
        ipv6_address = result[0][4][0]
        
        return ipv6_address
    except socket.gaierror as e:
        print(f"Error: {e}")
        return None
