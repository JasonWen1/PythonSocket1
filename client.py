import socket
import re  # Import the regular expressions module

ip = '10.0.0.212'  # IP address to listen on
port = 12345  # Port to listen on


def start_client(client_name, client_number):
    # Create a TCP/IP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the server
    client_socket.connect((ip, port))

    message = f"{client_name} {client_number}"

    # Send the message to the server
    client_socket.sendall(message.encode())

    # Receive and decode the response from the server
    response = client_socket.recv(1024).decode()

    # Use regular expressions to separate the server's name and the integer
    match = re.search(r'(.*) (\d+)$', response)
    if match:
        server_name = match.group(1)  # The server's name part
        server_number = int(match.group(2))  # The integer part

        # Output the client's name, server's name, client's number, server's number, and the sum of the numbers
        print(f"Client's name: {client_name}")
        print(f"Server's name: {server_name}")
        print(f"Client's number: {client_number}")
        print(f"Server's number: {server_number}")
        print(f"Sum of numbers: {int(client_number) + server_number}")
    else:
        print("Failed to parse the server's name and number from the response.")

    # Close the socket
    client_socket.close()

if __name__ == "__main__":
    # Prompt the user for the client's name and number
    client_name = input("Enter the client's name: ")
    client_number = input("Enter the client's number: ")
    start_client(client_name, client_number)