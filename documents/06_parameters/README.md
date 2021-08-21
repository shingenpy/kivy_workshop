# パラメータ

kivy アプリにおいての監視対象の変数のこと

設定することでアプリケーション全体で使えるようになり、さらにその値が変化することでイベントを起こすことができる

```on_<変数名>``` という形式で使う

定義方法は以下 (例)
```
from kivy.uix.widget import Widget
from kivy.properties import StringProperty

class Sample(Widget):
    sampletext = StringProperty("HelloWorld")
```
```on_sampletext``` というイベントが使えるようになる。sampletext の値が変更した場合にイベントを呼び出すことが可能

## パラメータの種類
* [NumericProperty](https://kivy.org/doc/stable/api-kivy.properties.html#kivy.properties.NumericProperty)
* [StringProperty](https://kivy.org/doc/stable/api-kivy.properties.html#kivy.properties.StringProperty)
* [ListProperty](https://kivy.org/doc/stable/api-kivy.properties.html#kivy.properties.ListProperty)
* [ObjectProperty](https://kivy.org/doc/stable/api-kivy.properties.html#kivy.properties.ObjectProperty)
* [BooleanProperty](https://kivy.org/doc/stable/api-kivy.properties.html#kivy.properties.BooleanProperty)
* [BoundedNumericProperty](https://kivy.org/doc/stable/api-kivy.properties.html#kivy.properties.BoundedNumericProperty)
* [OptionProperty](https://kivy.org/doc/stable/api-kivy.properties.html#kivy.properties.OptionProperty)
* [ReferenceListProperty](https://kivy.org/doc/stable/api-kivy.properties.html#kivy.properties.ReferenceListProperty)
* [AliasProperty](https://kivy.org/doc/stable/api-kivy.properties.html#kivy.properties.AliasProperty)
* [DictProperty](https://kivy.org/doc/stable/api-kivy.properties.html#kivy.properties.DictProperty)

## Example
新たに ```prop.py```, ```prop.kv``` を作成してください

以下のように配置する
```
.
└── prop.py
└── prop.kv
```

** prop.py **
```
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import NumericProperty

class Sample(BoxLayout):
    count = NumericProperty(0)

class PropApp(App):
    pass

PropApp().run()
```

** prop.kv **
```
Sample:
<Sample>:     
    Label:
        text: str(root.count)
    Button:
        text: "on"
        size: 10,10
        pos: root.center
        on_press: root.count += 1
```

まずは、これを実行して、右のボタンを押すことで左の数値がカウントアップしています
```
> python prop.py
```

![prop](/documents/00_image/prop.png)

では、count パラメータが変わったときに、イベントが実行されるかどうか確認しましょう.
prop.kv を以下のように変更します

** prop.kv **
```
Sample:
<Sample>:
    on_count: print("count is up") # ←ここ追記 count パラメータのイベントなので、on_count になる
    Label:
        text: str(root.count) # root.count は root は Sample Widget のことです
    Button:
        text: "on"
        size: 10,10
        pos: root.center
        on_press: root.count += 1
```

再度、アプリケーションを実行し、ボタンを押すことでカウントされ、数値が変わったことで ```print("count is up")``` が実行され、コンソールに ```count is up``` が表示されると思います

以上がパラメータの説明です

パラメータについての詳しい説明は → [Properties](https://kivy.org/doc/stable/api-kivy.properties.html)

|
[back](/documents/05_aboutkvlanguage)
|
[home](https://github.com/shingenpy/kivy_workshop)
|
[next](/documents/07_settings)
|