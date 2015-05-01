import socket

host = ''
# Symbolic name meaning all available interfaces

port = 5566
# Arbitrary non-privileged port

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(1)

while True:
    conn, addr = s.accept()
    print('Connected by', addr)
    data = conn.recv(1024)

    if not data:
        break

    conn.sendall(data)

conn.close()
