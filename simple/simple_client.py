import socket
# Import socket module

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Create a socket object

host = socket.gethostname()
# Get local machine name

port = 7788
# Reserve a port for your service.

s.connect((host, port))
print s.recv(1024)

s.close
# Close the socket when done
