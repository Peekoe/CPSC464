import socket
import threading

# Define the address and port to listen on
SERVER_ADDRESS = '127.0.0.1'
SERVER_PORT = 5000

# Create a socket object and bind it to the address and port
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((SERVER_ADDRESS, SERVER_PORT))

# Listen for incoming connections
server_socket.listen()

# Define a function to handle communication with a single client
def handle_client(client_socket, client_address):
    # Receive the client's name
    client_name = client_socket.recv(1024).decode()
    print(f'Client {client_name} connected from {client_address}')

    # Loop to receive messages from the client
    while True:
        # Receive the client's message
        message = client_socket.recv(1024).decode()

        # Print the message and client's name
        print(f'{client_name}: {message}')

        # If the client sends an empty message, close the connection
        if message == '':
            print(f'Client {client_name} disconnected')
            break

    # Close the socket
    client_socket.close()

# Loop to handle incoming client connections
while True:
    # Accept an incoming connection
    client_socket, client_address = server_socket.accept()

    # Create a new thread to handle communication with the client
    client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
    client_thread.start()
