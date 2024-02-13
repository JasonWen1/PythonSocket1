import socket
import threading
import re  # Import the regular expressions module
import random  # Import for generating server number

active_client_sockets = []  # Track active client sockets
server_running = True  # Global flag to control server running
server_name = "Server Alpha"  # Global string for server name

ip = '10.0.0.212'  # IP address to listen on
port = 12345  # Port to listen on

def handle_client(client_socket, client_address):
    global server_running

    try:
        # Receive data from the client
        data = client_socket.recv(1024).decode()
        if not data:
            return

        # Use regular expressions to separate the name and the integer
        match = re.search(r'(.*)\s+(\d+)$', data)
        if match:
            client_name = match.group(1)  # The client's name part
            client_number = int(match.group(2))  # The integer part
            
            # Generate a random number for the server
            server_number = random.randint(1, 100)
            numbers_sum = client_number + server_number

            if client_number < 1 or client_number > 100:
                print(f"Invalid number received from {client_address}. Shutting down the server.")
                server_running = False
                return

            # Print the requested information
            print(f"{server_name} received a message from {client_name}.")
            print(f"Server number: {server_number}, Client number: {client_number}, Sum: {numbers_sum}")

            # Modify the response message format as per the new requirement
            response = f"{server_name} {server_number}"
            client_socket.sendall(response.encode())
        else:
            print(f"Failed to parse name and integer from the message received from {client_address}")
            return

    finally:
        # Close the connection and remove it from the list
        client_socket.close()
        active_client_sockets.remove(client_socket)


def start_server():
    global server_running

    # Create a TCP/IP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to the address and port
    server_socket.bind((ip, port))

    # Start listening for incoming connections
    server_socket.listen()
    print(f"{server_name} started, waiting for connections...")

    try:
        while server_running:
            client_socket, client_address = server_socket.accept()
            if not server_running:
                break
            active_client_sockets.append(client_socket)
            client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
            client_thread.start()

    finally:
        # Close all active client sockets
        for sock in active_client_sockets:
            sock.close()
        # Close the server socket
        server_socket.close()
        print(f"{server_name} has shut down.")

if __name__ == "__main__":
    start_server()
