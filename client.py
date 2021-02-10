import socket

HOST = 'localhost'
PORT = 5555

# Create socket object
# socket.SOCK_STREAM = TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


# Connect to the server
s.connect((HOST, PORT))

running = True
msg = ''
while running:
    msg = input("Please type message or [q]uit: ")
    if msg == 'q':
        break
    else:
        # Send data to server
        s.send(msg.encode('utf-8'))

    # Received data from the server
    data = s.recv(1024).decode('utf-8')
    print('Received: ', data)
