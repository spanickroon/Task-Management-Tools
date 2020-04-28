"""TCP client module."""

import socket
import threading

import const_tcp


class TCPClient:
    """The class that is responsible for creating the client object."""

    def __init__(self):
        """Connection to tcp server."""
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((const_tcp.TCP_IP, const_tcp.TCP_PORT))

    def sending_messages(self):
        """Sending messages to the server."""
        while True:
            self.sock.send(input().encode('UTF-8'))

        self.sock.close()

    def start(self):
        """"Start a separate thread for client operation."""
        client_thread = threading.Thread(target=self.sending_messages)
        client_thread.start()


if __name__ == "__main__":
    """Testing."""
    test_client = TCPClient()
    test_client.start()
