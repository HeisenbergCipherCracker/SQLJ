import socket
import sys
sys.path.append('D:\SQLjj\SQLJ\lib\scripts')

def send_payload(host, port, payload):
    # Create a socket object
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Connect to the website
        s.connect((host, port))

        # Send the payload
        s.send(payload.encode())

        # Receive the response
        response = s.recv(1024)
        
        # Extract the status code from the response headers
        status_code = int(response.decode().split(' ')[1])
        print("Status code:", status_code)
        
        # Print the response body
        print("Response:", response.decode())
        if status_code == 200:
            return response.decode(),True

    finally:
        # Close the connection
        s.close()

# Example usage
host = '65.61.137.117'
port = 80
payload = 'GET / HTTP/1.1\r\nHost: example.com\r\n\r\n'
print(bool(send_payload(host, port, payload)))