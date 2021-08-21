# Kv 言語について
CSS のような言語です (html + css + javascript を yaml 形式のような書式で書く言語)

アプリケーションのレイアウトなどのデザインのための言語です
* シンタックスルールは基本的に Python と同じ
* ファイル名は設定したアプリ名と同じにする
    * App クラスを継承したクラス名から App を取ったファイル名が kv ファイルの名前になる
        * ```class SampleApp(App):``` の場合 → sample.kv
        * ```class Sample(App):``` のように、クラス名に App がない場合でも、sample.kv になる
* パラメータの右辺は Python コード

* kivy のバージョン設定
```
#:kivy 1.0.9
```

* 変数の定義
```
#:set <変数名> <値>
#:set n 100
```

* Python モジュールをインポートする場合
```
#:import <呼び名> <モジュール名>
#:import random random
```

* Widget の配置や各パラメータについて
    * id は各 Widget に名前が必要な場合に使う。id を定義することで、該当の Widget のパラメータに id でアクセスできる
        * id のアクセス範囲は宣言された Widget 内まで有効。
    * Widget か Layout の定義名は頭文字大文字、パラメータは小文字で始まる
```
<MyWidget>: # なにも継承していない MyWidget は Python ファイル側で BoxLayout などのレイアウトまたは Widget クラスを継承しないとエラーになる
    id: “mywidget”
    GridLayout: # レイアウト
        cols: 1 # パラメータ
        Label: 
            text: “hello world”
        Button:
            text: “Push me”
```

以上、kv 言語についてでした。詳しくは → [Kv language](https://kivy.org/doc/stable/guide/lang.html)

|
[back](/documents/04_aboutlayout)
|
[home](https://github.com/shingenpy/kivy_workshop)
|
[next](/documents/06_parameters)
|