import socket

HOST = 'localhost'
PORT = 5555

# Create socket object
# socket.SOCK_STREAM = TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
s.connect((HOST, PORT))

# Send data to server
s.sendall(b'Hello world')

# Received data from the server
data = s.recv(1024)
print('Received: ', repr(data))