"""Desktop app module."""

from taskmanager.tcp_protocol import server


class DesktopApp:
    """Desktop app."""

    def start(self):
        """Start messaging server."""
        try:
            app_server = server.TCPServer()
            app_server.start()
        except OSError:
            # testing
            print('oserr')


if __name__ == "__main__":
    """Start."""
    app = DesktopApp()
    app.start()
