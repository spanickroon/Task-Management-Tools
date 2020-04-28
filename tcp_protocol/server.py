"""Tcp server module."""

import socket
import threading

import const_tcp


class TCPServer:
    """The class that is responsible for creating the server object."""

    def __init__(self):
        """Create a socket and connect to a port."""
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((const_tcp.TCP_IP, const_tcp.TCP_PORT))
        self.sock.listen()

    def client_listening(self):
        """Waiting for messages from the client."""
        connection, address = self.sock.accept()

        while True:
            data = connection.recv(const_tcp.BUFFER_SIZE)
            if not data:
                break

            print(f'{data.decode("UTF-8")}')

    def start(self):
        """Start a separate thread for server operation."""
        server_thread = threading.Thread(target=self.client_listening)
        server_thread.start()


if __name__ == "__main__":
    """Testing."""
    test_server = TCPServer()
    test_server.start()
