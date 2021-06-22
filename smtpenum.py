#!/usr/bin/python3
import socket 
import sys

if len(sys.argv) != 2:
     print("Usage: vrfy.py users.txt") 
     sys.exit(0)

#open users list
file1 = open(sys.argv[1], 'r')
lines = file1.readlines()

# Create a Socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the Server
connect = s.connect(('10.11.1.231',25))

# Receive the banner 
banner = s.recv(1024)
print(banner)

for line in lines:
    print('Trying ' + line)
    sendbytes = 'VRFY ' + line + '\r'
    s.send(sendbytes.encode())
    result = s.recv(1024)
    print(result)

# Close the socket 
s.close()
