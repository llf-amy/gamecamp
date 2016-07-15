
from kivy.app import App
from kivy.uix.widget import Widget

class PongGame(Widget):
    pass

class PongApp(App):
    def build(self):
        return Widget()
    
if __name__ == '__main__':
    PongApp().run()