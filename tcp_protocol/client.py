"""TCP client module."""

import socket
import threading

import const_tcp
import message_templates as tmp


class TCPClient:
    """The class that is responsible for creating the client object."""

    def __init__(self):
        """Connection to tcp server."""
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((const_tcp.TCP_IP, const_tcp.TCP_PORT))
        self.sock.send(tmp.CONNECT.encode('UTF-8'))

    def sending_messages(self):
        """Sending messages to the server."""
        while True:
            self.sock.send(input().encode('UTF-8'))

        self.sock.close()

    def receiving_messages_from_server(self):
        """Receiving device processes from the server"""
        data = self.sock.recv(const_tcp.BUFFER_SIZE)
        # testing
        # print(data.decode('UTF-8'))
        return True if data else False

    def start(self):
        """"Start a separate thread for client operation."""
        client_thread = threading.Thread(
            target=self.sending_messages)
        server_thread = threading.Thread(
            target=self.receiving_messages_from_server)

        client_thread.start()
        server_thread.start()


if __name__ == "__main__":
    """Testing."""
    test_client = TCPClient()
    test_client.start()
