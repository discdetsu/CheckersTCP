import socket

HOST = 'localhost'
PORT = 5555

# Socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Binding
s.bind((HOST, PORT))

# Waiting for 2 players
s.listen(2)

while True:

    # Waiting for client
    print('Waiting for connection')

    # Accept client
    connection, clientAddress = s.accept()
    try:
        print('Connected from: ', clientAddress)

        # Receive data from client
        while True:
            # Determine data buffer size (char)
            data = connection.recv(1024).decode('utf-8')
            print('Received: ', data)

            # If server received data then send it back to client
            if data:
                print('Sending data back to the client')
                connection.send(data.upper().encode('utf-8'))

            # If no data from client then stop waiting
            else:
                print('No more data from', clientAddress)
                break

        # Done receiving data
    finally:
        connection.close()
        print('Closed connection')
