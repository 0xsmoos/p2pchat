import socket
import sys
import time 


# init



s = socket.socket()
print("server will start on host; ", host)
port = 80
s.bind(('',port))

print("")

print("Host and Port working sucessfully. ")
s.listen(1)
conn, addr = s.accept()
print(addr, "has connected to the server and is now online. ")

