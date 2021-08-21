from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import NumericProperty

class Sample(BoxLayout):
    count = NumericProperty(0)

class PropApp(App):
    pass

PropApp().run()