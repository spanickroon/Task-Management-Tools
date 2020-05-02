""""""

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window

Window.size = (300, 537)
Window.title = 'TaskManager'


class Container(FloatLayout):
    """"""
    pass


class TaskManagerApp(App):
    """"""

    def build(self):
        """"""
        self.load_kv('taskmanager.kv')
        return Container()


if __name__ == "__main__":
    TaskManagerApp().run()
