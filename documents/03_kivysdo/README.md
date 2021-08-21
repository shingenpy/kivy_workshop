# kivy の仕組みについて

Kivy の仕組みを理解するには以下の 2 点をまず説明します
* Widget 
* イベント駆動型 - オブサーバーパターン

# Widget 
* Widget とは、アプリケーションを構成する部品のことです
* kivy では、この Widget 単位で レイアウトだったり、ボタンだったりを配置していきます

## Example
例えば、以下のような UI を持つアプリケーションがあるとします

![sampleui](/documents/00_image/sampleui.png)

↓で示したように Widget ごとに分類できます

![sampleui2](/documents/00_image/sampleui2.png)

配置をツリーで表示するとこんな感じになっています

![sampleui3](/documents/00_image/sampleui3.png)

# イベント駆動型について

[イベント駆動型](https://wa3.i-3-i.info/word13776.html)とは、特定の条件が満たされた場合に処理が発生するようにプログラムすることです。

* 例
    * 再生ボタンを押す → 音楽が再生される
    * マウスで画像ファイルをクリックする → 画像が表示される
    * 指でタップする → 何か起こる

## kivy はオブサーバーパターン
イベント駆動型にいくつか種類があり、kivy はオブサーバーパターンとなっています

オブサーバーパターンとは、アプリケーション実行時には監視者が特定の変数やユーザインタラクション(クリックやタッチなど）を監視し、事前に用意された条件で動作するプログラムのことです

![observer](/documents/00_image/observer.png)


|
[back](/documents/02_whykivy)
|
[home](https://github.com/shingenpy/kivy_workshop)
|
[next](/documents/04_aboutlayout)
|