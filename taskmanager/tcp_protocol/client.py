"""TCP client module."""

import socket
import threading

from taskmanager.tcp_protocol import const_tcp
from taskmanager.tcp_protocol import message_templates as tmp


class TCPClient:
    """The class that is responsible for creating the client object."""

    def __init__(self):
        """Connection to tcp server."""
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((const_tcp.TCP_IP, const_tcp.TCP_PORT))

    def send_message(self, message):
        """Sending messages to the server."""
        self.sock.send(message.encode('UTF-8'))

    def update_process(self):
        """Process update"""
        self.send_message(tmp.UPD_RPOCESS)
        data = self.sock.recv(const_tcp.BUFFER_SIZE)
        return data.decode('UTF-8').split(',')

    def receiving_messages_from_server(self):
        """Receiving device processes from the server"""
        self.sock.send(tmp.CONNECT.encode('UTF-8'))
        data = self.sock.recv(const_tcp.BUFFER_SIZE)

        print(data.decode('UTF-8'))
