# Settings
kivy には、設定画面がデフォルトで搭載されています

open_settings() を実行することでアクセスできます

* 設定項目はカスタマイズ可能
* 設定は ini ファイルで保存される

### 設定画面を開くためのコード例
```
<Setting@BoxLayout>:
    Button:
        text: "open setting"
        on_release: app.open_settings() # この関数を実行することで設定画面が開く
```

![settings](/documents/00_image/settings.png)

以上。詳しくは → [Settings](https://kivy.org/doc/stable/api-kivy.uix.settings.html?highlight=setting#module-kivy.uix.settings)

設定画面についてはこの動画が詳しい [Kivy crash course 13: Using Kivy's settings panel](https://www.youtube.com/watch?v=oQdGWeN51EE)

|
[back](/documents/06_parameters)
|
[home](https://github.com/shingenpy/kivy_workshop)
|
[next](/documents/08_screenmanager)
|