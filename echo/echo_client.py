import socket

host = socket.gethostname()

port = 5566
# The same port as used by the server
# create a TCP socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((host, port))

while True:
    msg = raw_input('Please say something to server (type :exit to exit)\n')

    if msg == ':exit':
        print('Disconnected from server..')
        break

    s.sendall(msg)
    data = s.recv(1024)
    print '[!] Server says: %s' % data

s.close()
