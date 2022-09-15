# text-detection
## 概要
汎用OCRをローカルで使えるようにしたかったので、自作データセットの構築からモデル開発までしています。
最終的には、ななめ文字やひずみ文字まで認識できるようにします。
カメラ画像やインターネット上の画像からテキスト情報を抽出し、物体と文字の意味関係を紐づけるデータベースの作成に使う予定です。

## ワークフロー
各ステップごとにデータとモデルの構築を行い、最終的に1つのモデルで対応
![image](https://user-images.githubusercontent.com/55880071/190018993-67046378-f039-4580-ba4c-294344b63778.png)

## サンプル
随時更新
![image](https://user-images.githubusercontent.com/55880071/190370910-f4e9176d-9429-4cf5-9f04-739a9f24ee01.png)

## データセット構築状況
文字認識のために画像中のテキスト領域を認識するデータセットを3つ作成しています。
Microsoft社のVoTTを使ってアノテーションをしています。
### テキスト領域データセット
画像から大まかなテキスト領域を抽出するためのデータセット
![image](https://user-images.githubusercontent.com/55880071/189475372-91095030-61ed-40a3-a836-661fe82b68cd.png)
### 縦書き文字領域データセット
縦書きテキスト領域から文字を抽出するためのデータセット
### 横書き文字領域データセット
横書きテキスト領域から文字を抽出するためのデータセット
