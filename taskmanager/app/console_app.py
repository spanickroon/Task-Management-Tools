"""Console app module."""

from taskmanager.tcp_protocol import server
from taskmanager.tcp_protocol import const_tcp as cnst


class DesktopApp:
    """Desktop app."""

    def start(self):
        """Start messaging server."""
        try:
            app_server = server.TCPServer()
            app_server.start()
        except OSError:
            print(f'The port {cnst.TCP_PORT} is busy waiting a bit')


if __name__ == "__main__":
    """Start."""
    app = DesktopApp()
    app.start()
