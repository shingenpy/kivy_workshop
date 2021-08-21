from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.uix.screenmanager import ScreenManager

class Sub1(Screen):
    pass

class Sub2(Screen):
    pass

class Main(ScreenManager):
    pass

class ScrApp(App):
    pass

ScrApp().run()