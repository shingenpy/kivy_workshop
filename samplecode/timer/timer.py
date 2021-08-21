from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import NumericProperty
from kivy.properties import BooleanProperty 
from kivy.properties import StringProperty  
from kivy.properties import ListProperty
from kivy.clock import Clock

class MainWidget(BoxLayout):
    timer_val = NumericProperty(300)

    timer_state = BooleanProperty(False)
    timer_button = StringProperty("Start")

    bg_color = ListProperty([1,1,1,1])

    def on_press_button(self):
        if self.timer_button == "Start":
            self.timer_button = "Stop"
            self.timer_state = True
        else:
            self.timer_button = "Start"
            self.timer_state = False

    def on_change_timerval(self, widget):
        self.timer_val = widget.value
        if self.bg_color == [1,0,0,1]:
            self.bg_color = [1,1,1,1]    

    def on_timer_zero(self):
        self.bg_color = [1,0,0,1]
        self.timer_state = False
        self.timer_button = "Start"

    def update(self, dt):
        if self.timer_state:
            if self.timer_val > 0:
                self.timer_val -= 1
            else:
                self.on_timer_zero()

class TimerApp(App):
    def build(self):
        timer = MainWidget()
        Clock.schedule_interval(timer.update, 1.0)
        return timer    

TimerApp().run()