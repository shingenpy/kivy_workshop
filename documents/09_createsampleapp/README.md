# サンプルアプリを作る
今回,作成するアプリはタイマーアプリです

![timer0](/documents/00_image/timer0.png)

* BoxLayout で上から
    * 時間表示パネル
    * 時間調整のためのスライダー... 左右に動かすことで時間がかわる
    * スタートボタン

## 最初
draw.io などを利用して、インターフェースを試作してみましょう

![timerapp](/documents/00_image/timerapp.png)

## アプリケーションのファイルを作成
* timer.py を作成

** timer.py **
```
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class MainWidget(BoxLayout):
    pass

class TimerApp(App):
    pass

TimerApp().run()
```

## UI の定義
* timer.kv を作成して、ひな形を作成

** timer.kv **
```
#:kivy 1.9.1
MainWidget: 

<MainWidget>:
    orientation: "vertical"

    Label:
        text: "05:00"
        font_size: 60
    Slider:
        min: 10
        max: 600
        step: 1
        value: 300
    Button:
        text: "Start"
        font_size: 60
```

* いったんここで実行してみる
```
> python timer.py
```

まだ、スライダーを動かしても、スタートボタンを押しても意味はありません

## スライダーの動きと時間パネルを連動させる
* まずはスライダーの値にアクセスするために id を指定する
* ついでに on_touch_move を定義して、数値が変更されたことを print してみる

** timer.kv **
```
#:kivy 1.9.1
MainWidget: 

<MainWidget>:
    :
    Slider:
        id: timerval # 追記
        min: 10
        max: 600
        step: 1
        value: 300
        on_touch_move: print(timerval.value) # 追記
    :
```

時間パネルも連動させる

** timer.kv **
```
    :
    Label:
        # text: "05:00" ↓へ変更
        text: "{:0>2}:{:0>2}".format(timerval.value // 60, timerval.value % 60)
    :
```

## 時間経過でタイマーが進むようにする
* Slider に設定した値をそのまま使うと Slider が持っている値に干渉する
    * Slider で数値が変更されたら timer_val 変数に同期するという処理にする

### timer.py へ追記
** timer.py **
```
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import NumericProperty

class MainWidget(BoxLayout):
    # timer_val を定義
    timer_val = NumericProperty(300) # 追記

    # timer_val が変更されたら呼ばれる関数
    def on_change_timerval(self, widget):　# 追記
        self.timer_val = widget.value      # 追記

class TimerApp(App):
    pass

TimerApp().run()
```

### timer.kv を変更し、スライダーの値とカウントダウンのための数値 timer_val が連動するための処理を加える

** timer.kv **
```
#:kivy 1.9.1
MainWidget: 

<MainWidget>:
    :
    Slider:
        id: timerval 
        min: 10
        max: 600
        step: 1
        value: 300
        on_touch_move: root.on_change_timerval(self) # self は Slider のこと
    :
```

## スタートボタンを作りこむ
* ボタンを押したときに押しているという状態を作りたい
* 時間が進んでいる間はボタンの文字列を Stop へ変更し、いつでも止められるようにしたい

### timer.py を編集する
* 時間が経過する状態を保存する timer_state を定義
* ボタンのテキストを保存する timer_button を定義  
* ボタンを押したときに実行されるメソッドを定義

** timer.py **
```
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import NumericProperty
from kivy.properties import BooleanProperty # 追記
from kivy.properties import StringProperty  # 追記

class MainWidget(BoxLayout):
    timer_val = NumericProperty(300)

    # ここから
    timer_state = BooleanProperty(False)
    timer_button = StringProperty("Start")

    def on_press_button(self):
        if self.timer_button == "Start":
            self.timer_button = "Stop"
            self.timer_state = True
        else:
            self.timer_button = "Start"
            self.timer_state = False
    # ここまで追記

    def on_change_timerval(self, widget):
        self.timer_val = widget.value 

class TimerApp(App):
    pass

TimerApp().run()
```

### timer.kv に Button を押したときに実行されるイベントを定義する
* text パラメータに root.timer_button を定義する
* on_release (ボタンをおして話すときにイベントを実行する) に先ほど定義した関数 on_press_button を定義する

** timer.kv **
```
    :
    Button:
        text: root.timer_button 
        on_release: root.on_press_button()
    :
```

## 時間の制御
* kivy の機能の Clock を使う. 

** timer.py **
```
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import NumericProperty
from kivy.properties import BooleanProperty 
from kivy.properties import StringProperty  
from kivy.clock import Clock # 追記

class MainWidget(BoxLayout):
    timer_val = NumericProperty(300)

    timer_state = BooleanProperty(False)
    timer_button = StringProperty("Start")

    def on_press_button(self):
        if self.timer_button == "Start":
            self.timer_button = "Stop"
            self.timer_state = True
        else:
            self.timer_button = "Start"
            self.timer_state = False

    def on_change_timerval(self, widget):
        self.timer_val = widget.value
    
    # 1. ここから
    def update(self, dt):
        if self.timer_state:
            self.timer_val -= 1
    # ここまで追記

class TimerApp(App):
    # pass ← pass をコメント
    # 2. ここから
    def build(self):
        timer = MainWidget()
        Clock.schedule_interval(timer.update, 1.0)
        return timer    
    # ここまで追記

TimerApp().run()
```

### 時間経過で時間パネルの数値も変わるようにする
* timer.kv の Label の text パラメータを修正する

** timer.kv **
```
    Label:
        text: "{:0>2}:{:0>2}".format(root.timer_val // 60, root.timer_val % 60)
```
## 最後の作りこみ
* 指定時間が過ぎたら時間が進まないようにする
* 時間が 0 になったら、文字を赤くする

** timer.py **
```
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import NumericProperty
from kivy.properties import BooleanProperty 
from kivy.properties import StringProperty  
from kivy.properties import ListProperty # 追記
from kivy.clock import Clock

class MainWidget(BoxLayout):
    timer_val = NumericProperty(300)

    timer_state = BooleanProperty(False)
    timer_button = StringProperty("Start")

    bg_color = ListProperty([1,1,1,1]) # 追記

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

    # 0 秒になった際に実行するやつ
    def on_timer_zero(self):
        self.bg_color = [1,0,0,1]
        self.timer_state = False
        self.timer_button = "Start"

    def update(self, dt): # 0 秒になったら時間が経過しないようにする
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
```

** timer.kv ** 
```
#:kivy 1.9.1

MainWidget:

<MainWidget>:
    orientation: "vertical"

    Label:
        text: "{:0>2}:{:0>2}".format(root.timer_val // 60, root.timer_val % 60)
        font_size: 60
        color: root.bg_color # 追記
    
    Slider:
        id: timerval
        min: 10
        max: 600
        step: 1
        value: 300
        on_touch_move: root.on_change_timerval(self)
        disabled: root.timer_state

    Button:
        text: root.timer_button
        font_size: 60
        on_release: root.on_press_button()
```

とりあえず、完成です

![timer_last](/documents/00_image/timer_last.png)

こんな感じでサンプルアプリの作成は終わりです.発展課題も考えてみたので試しにトライしてみてください

## 発展課題
* もっと長めの時間を設定できるようにする
* タイマーがゼロになったときに音を鳴らす
* Android アプリにしてみる

|
[back](/documents/08_screenmanager)
|
[home](https://github.com/shingenpy/kivy_workshop)
|
[next](/documents/10_ends)
|