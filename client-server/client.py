import socket

# Define the server address and port to connect to
SERVER_ADDRESS = '127.0.0.1'
SERVER_PORT = 5000

# Create a socket object and connect it to the server address and port
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((SERVER_ADDRESS, SERVER_PORT))

# Get the user's name and send it to the server
name = input('Enter your name: ')
client_socket.send(name.encode())

# Loop to send messages to the server
while True:
    # Get the user's message and send it to the server
    message = input('Enter your message: ')
    client_socket.send(message.encode())

    # If the user sends an empty message, break out of the loop and close the socket
    if message == '':
        break

# Close the socket
client_socket.close()
