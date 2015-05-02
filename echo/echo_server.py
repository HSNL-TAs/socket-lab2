import socket

host = ''
# Symbolic name meaning all available interfaces

port = 5566
# Arbitrary non-privileged port

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(1)
print '[!] Server is listening client...'
conn, addr = s.accept()

print '[!] connected by %s' % addr[0]

while True:
    data = conn.recv(1024)

    if not data:
        break
    print '[!] Received string "%s" from cilent %s' % (data, addr[0])
    conn.sendall(data)

conn.close()
