import socket

host = ''
# Symbolic name meaning all available interfaces

port = 5566
# Arbitrary non-privileged port

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(1)
print '[!] Server is listening client...'
try:
    conn, addr = s.accept()
    client_ip = addr[0]
    print '[!] connected by %s' % client_ip
    while True:
        data = conn.recv(1024)
        if not data:
            break
        print '[!] Received string \'%s\' from cilent %s' % (data, client_ip)
        conn.sendall(data)
    conn.close()
except (KeyboardInterrupt, SystemExit):
    print 'Server Closed..'
except:
    print 'Some unexpected errors..'
