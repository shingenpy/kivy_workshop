# ScreenManager
スクリーンマネージャーとは、スクリーンという単位で画面を分ける機能です

メニューがあり、画面が切り替わったりなどの見た目に活用できる

## Example
実際にコードを書いて説明します

```scr.py```, ```scr.kv``` を作成してください

以下のように配置する
```
.
└── prop.py
└── prop.kv
```

** scr.py **
```
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
```

** scr.kv **
```
Main:
    Sub1:
    Sub2:

<Sub1>:
    name: "sub1" # ← id ではなくて name、Screen の名前は name でつける
    BoxLayout:            
        Button:
            text: "go sub2"
            on_release: app.root.current = "sub2"
        Button:
            text: "none"

<Sub2>:
    name: "sub2"
    BoxLayout:        
        Button:
            text: "go sub1"
            on_release: app.root.current = "sub1"
        Button:
            text: "none"
```

実行してみます
```
> python scr.py
```

![screen](/documents/00_image/screen.png)

![screen2](/documents/00_image/screen2.png)

app.root.current に現在のスクリーンが保存してあり、それを変更することで Screen を変更することができる

詳しくは → [Screen Manager](https://kivy.org/doc/stable/api-kivy.uix.screenmanager.html)

|
[back](/documents/07_settings)
|
[home](https://github.com/shingenpy/kivy_workshop)
|
[next](/documents/09_createsampleapp)
|