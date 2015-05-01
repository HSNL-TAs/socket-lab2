import socket
# Import socket module

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Create a socket object

host = socket.gethostname()
# Get local machine name

port = 7788
# Reserve a port for your service.

s.bind((host, port))
# Bind to the port

s.listen(1)
# Now wait for client connection.

while True:
    client_socket, addr = s.accept()
    # Establish connection with client.

    print 'Got connection from', addr
    client_socket.send('Thank you for connecting')

    client_socket.close()
    # Close the connection
