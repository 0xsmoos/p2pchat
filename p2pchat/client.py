
import socket 

# init

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = input("What port would you like to use?   ")                # Reserve a port for your service.

s.connect((host, int(port)))
print("Connected to server sucessfully.", host)