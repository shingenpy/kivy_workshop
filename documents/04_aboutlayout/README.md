# レイアウト
* 先ほどの章で Widget のなかにはレイアウトという部品があると説明しました
* レイアウトというのは kivy が事前に用意している配置の仕組みのことです
* レイアウトのプリセット群という感覚で覚えてください → 自分でレイアウトを自作もできる

* kivy が用意しているレイアウトは以下の種類があります
    * [Boxlayout](https://kivy.org/doc/stable/api-kivy.uix.boxlayout.html#module-kivy.uix.boxlayout)
    * [AnchorLayout](https://kivy.org/doc/stable/api-kivy.uix.anchorlayout.html#module-kivy.uix.anchorlayout)
    * [GridLayout](https://kivy.org/doc/stable/api-kivy.uix.gridlayout.html#module-kivy.uix.gridlayout)
    * [StackLayout](https://kivy.org/doc/stable/api-kivy.uix.stacklayout.html#module-kivy.uix.stacklayout)
    * [PageLayout](https://kivy.org/doc/stable/api-kivy.uix.pagelayout.html#module-kivy.uix.pagelayout)
    * [ScatterLayout](https://kivy.org/doc/stable/api-kivy.uix.scatterlayout.html#module-kivy.uix.scatterlayout)
    * [FloatLayout](https://kivy.org/doc/stable/api-kivy.uix.floatlayout.html#module-kivy.uix.floatlayout)
    * ..etc

## 実際にコードを書きながら覚える
### まず kivy を書く準備
#### Python のインストール
ご自身の環境に合わせて [Python](https://www.python.org/) をインストールしてください
#### 仮想環境の用意
仮想環境の作成
```
 > python -m venv env
```
仮想環境のアクティベイト
```
 > env\Scripts\activate
```
#### kivy のインストール

```
(env) > pip install kivy
```
### Hello World を実行
まずは、first.py というファイルを作り以下を書きます

** first.py **
```
from kivy.app import App
from kivy.uix.widget import Widget

class FirstApp(App):
    pass

class MainWidget(Widget):
    pass

FirstApp().run()
```

次に UI 定義用のkv ファイルを作ります。名前は必ず first.kv としてください

** first.kv **
```
MainWidget:

<MainWidget>:
    Label:
        text: "Hello World"
        pos: root.center 
```
kv ファイルには命名規則があり、python ファイルから参照するために App を継承したクラス名から App を取った名前が kv ファイルの名前になります

今回でいう所の FirstApp が App を継承しているため、FirstApp から App を取った結果、First のみになり、first.kv となるという話です

```
class FirstApp(App): # ←ここ
    pass
```

first.py と first.kv は同じディレクトリに置くようにしてください。
```
.
└── first.py
└── first.kv
```
では、実行してみます

```
> python first.py
```

画面の真ん中に "Hello World" が表示されていると思います

## いくつかのレイアウトについて紹介
### [Boxlayout](https://kivy.org/doc/stable/api-kivy.uix.boxlayout.html#module-kivy.uix.boxlayout)
縦向きもしくは縦向きに Widget を配置するレイアウトです

以下のコードを first.kv に追記してください

**first.kv**
```
# MainWidget: ← メインインターフェースは BoxSample へ変更する
BoxSample:

# 以下追記。
<BoxSample@BoxLayout>: 
    Button:
        text: "Yes"
    Button:
        text: "No"
# ここまで

<MainWidget>:
    # <略>
```

縦向きか横向きかは以下で設定する
```
    orientation: "horizontal" or "vertical"
```

ちなみに ```<BoxSample@BoxLayout>``` という書き方の意味は、kv言語特有の書き方でレイアウトなどを継承する場合に使用する.
python のクラスで書く ```class BoxSample(Boxlayout):``` と同じ意味合いになる

### [GridLayout](https://kivy.org/doc/stable/api-kivy.uix.gridlayout.html#module-kivy.uix.gridlayout)
* BoxLayout と似ているが列数が増える点では違う
* 縦横の数を rows または cols で設定する

**first.kv**
```
# MainWidget: ← メインインターフェースは GridSample へ変更する
GridSample:

# 以下追記。
<GridSample@GridLayout>:
    rows: 2
    Button:
        text: "Yes"
    Button:
        text: "No"
    Button:
        text: "Even"
# ここまで

<BoxSample@BoxLayout>: 
    # <略>

<MainWidget>:
    # <略>
```
このまま実行しても OK ですが、cols がないパターンなどを試してみてください。

### [StackLayout](https://kivy.org/doc/stable/api-kivy.uix.stacklayout.html#module-kivy.uix.stacklayout)
* StackLayout は Widget を敷き詰めていくレイアウトです
* どの向きで敷き詰めていくかの設定については、公式ドキュメントをご覧ください
    * デフォルトは、左から右へ、上から下に敷き詰めます 
* StackLayout は Widget をリサイズしないので、指定する必要がある
* StackLayout は画面サイズによって配置が変わるので、縦横に画面をリサイズして試してみてください

**first.kv**
```
# MainWidget: ← メインインターフェースは StackSample へ変更する
StackSample:

# 以下追記。
<StackSample@StackLayout>:
    Button:
        text: "1"
        size: dp(100),dp(100)
        size_hint: None, 0.15

    Button:
        text: "2"
        size: dp(100),dp(100)
        size_hint: None, 0.15
    Button:
        text: "3"
        size: dp(100),dp(100)
        size_hint: None, 0.15
    Button:
        text: "4"
        size: dp(100),dp(100)
        size_hint: None, 0.15
    Button:
        text: "5"
        size: dp(100),dp(100)
        size_hint: None, 0.15
    Button:
        text: "6"
        size: dp(100),dp(100)
        size_hint: None, 0.15
# ここまで

<GridSample@GridLayout>:
    # <略>

<BoxSample@BoxLayout>: 
    # <略>

<MainWidget>:
    # <略>
```

### [PageLayout](https://kivy.org/doc/stable/api-kivy.uix.pagelayout.html#module-kivy.uix.pagelayout)
ページレイアウトとは、複数の Widget を重ねて配置し、ページめくりのように重ねた Widget にアクセスできるレイアウトです

※ 注: ```#:set n 1``` を先頭に追記しています。これは n という変数を定義し、1 を初期値に与えるという命令です

**first.kv**
```
#:set n 1
# MainWidget: ← メインインターフェースは PageLayout へ変更する
PageLayout:

# 以下追記。
<PageLayout>:
    BoxLayout:
        Label:
            text: "1"
            canvas.before:
                Color:
                    rgba: 1, 0, 0, n
                Rectangle:
                    pos: self.pos
                    size: self.size            
    BoxLayout:
        Label:
            text: "2"
            canvas.before:
                Color:
                    rgba: 0, 1, 0, n
                Rectangle:
                    pos: self.pos
                    size: self.size        
    BoxLayout:
        Label:
            text: "3"
            canvas.before:
                Color:
                    rgba: 0, 0, 1, n
                Rectangle:
                    pos: self.pos
                    size: self.size      
# ここまで

<StackSample@StackLayout>:
    # <略>

<GridSample@GridLayout>:
    # <略>

<BoxSample@BoxLayout>: 
    # <略>

<MainWidget>:
    # <略>
```

いったん実行してみましょう。右端をドラッグして、ページの切り替えができれば OK です。

これでは、わからないですが、ページレイアウトには問題があります。

先ほど設定しておいた、n を 0.5 へ変更して再度実行して試してください。
```
#:set n 0.5 

# <略>
```
n は各 Widget の色のアルファ値になっており、0.5 にすることで半透明になります。ページをめくるとわかりますが、ほかのWidget が重ねっていきます。

### マルチレイアウト
今まで作成したレイアウトの定義は、自由に組み合わせることが可能です。

**first.kv**
```
#:set n 1
# MainWidget: ← メインインターフェースは AllSample へ変更する
AllSample:

# 以下追記。
<AllSample@BoxLayout>:
    BoxSample:
    GridSample:
    StackSample:
# ここまで

<PageLayout>:
    # <略>     

<StackSample@StackLayout>:
    # <略>

<GridSample@GridLayout>:
    # <略>

<BoxSample@BoxLayout>: 
    # <略>

<MainWidget>:
    # <略>
```
新たに定義した、AllSample (BoxLayout)に今まで作成した、BoxSample/GridSample/StackSample を並べてみました。

以上、レイアウトの説明でした。他にもレイアウトはあり、それぞれに特徴がありますので、ぜひ試してみてください。

|
[back](/documents/03_kivysdo)
|
[home](https://github.com/shingenpy/kivy_workshop)
|
[next](/documents/05_aboutkvlanguage)
|