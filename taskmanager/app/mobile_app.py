""""""

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window

from taskmanager.tcp_protocol import client
from taskmanager.tcp_protocol import message_templates as tmp

Window.size = (300, 537)
Window.title = 'TaskManager'


class Container(FloatLayout):
    """"""

    mobile_client = None

    def update(self):
        """"""
        try:
            self.mobile_client = client.TCPClient()
            self.mobile_client.receiving_messages_from_server()

            self.send_message_button.disabled = False
            self.open_service_button.disabled = False
            self.close_service_button.disabled = False
        except ConnectionRefusedError:
            self.spinner.text = 'No connection'
            self.spinner.values.clear()

    def send_message(self):
        """"""
        try:
            self.mobile_client.send_message(tmp.SEND_MSG+self.text_input.text)
            self.text_input.text = ""
        except BrokenPipeError:
            self.spinner.text = 'No connection'
            self.spinner.values.clear()

            self.send_message_button.disabled = True
            self.open_service_button.disabled = True
            self.close_service_button.disabled = True


class TaskManagerApp(App):
    """"""

    def build(self):
        """"""
        return Container()


TaskManagerApp().run()
