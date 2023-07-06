import socket
import threading

# Function to handle client messages
def handle_client(client_socket, client_name):
    while True:
        message = client_socket.recv(1024).decode('utf-8')
        if not message:
            break
        print(f"{client_name}: {message}")
        # Process the message or perform any required actions here

    client_socket.close()

# Function to start the server
def start_server():
    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to a specific address and port
    server_socket.bind(('localhost', 9999))

    # Listen for incoming connections
    server_socket.listen(2)

    print("Server started. Waiting for connections...")

    while True:
        # Accept a client connection
        client_socket, addr = server_socket.accept()

        # Get the client name
        client_name = client_socket.recv(1024).decode('utf-8')

        print(f"Connected: {client_name} - {addr}")

        # Create a thread to handle the client
        client_thread = threading.Thread(target=handle_client, args=(client_socket, client_name))
        client_thread.start()

# Start the server
start_server()
