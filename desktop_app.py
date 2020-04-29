"""Desktop app module."""

from tcp_protocol import server


class DesktopApp:
    """Desktop app."""

    def start(self):
        """Start messaging server."""
        app_server = server.TCPServer()
        app_server.start()


if __name__ == "__main__":
    """Start."""
    app = DesktopApp()
    app.start()
