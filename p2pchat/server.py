import socket
import sys
import time 


# init



s = socket.socket()
host = socket.gethostname()
print("server will start on host; ", host)
port = 8080
s.bind((host,port))

print("")

print("Host and Port working sucessfully. ")
s.listen(1)
conn, addr = s.accept()
print(addr, "has connected to the server and is now online. ")

