"""Tcp server module."""

import socket
import threading

from taskmanager.tcp_protocol import const_tcp
from taskmanager.tcp_protocol import message_templates as tmp
from taskmanager.process_management import task_manager as tm


class TCPServer:
    """The class that is responsible for creating the server object."""

    def __init__(self):
        """Create a socket and connect to a port."""
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((const_tcp.TCP_IP, const_tcp.TCP_PORT))
        self.sock.listen()
        self.manager = tm.Manager()

    def message_processing(self, connection, data):
        """Method for processing messages."""
        if tmp.START_APP in data:
            self.manager.manage_application(
                data.replace(tmp.START_APP, ''))

        elif tmp.STOP_APP in data:
            self.manager.manage_application(
                data.replace(tmp.STOP_APP, ''), close=True)

        elif tmp.SEND_MSG in data:
            self.manager.sending_messages(
                data.replace(tmp.SEND_MSG, ''))

        elif tmp.UPD_RPOCESS in data:
            connection.send(
                self.manager.get_list_of_applications().encode('UTF-8'))

    def client_listening(self):
        """Waiting for messages from the client."""
        while True:
            connection, address = self.sock.accept()
            data = connection.recv(const_tcp.BUFFER_SIZE)

            self.message_processing(connection, data.decode('UTF-8'))

    def start(self):
        """Start a separate thread for server operation."""
        server_thread = threading.Thread(target=self.client_listening)
        server_thread.start()
