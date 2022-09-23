# Japanese-OCR
## 概要
汎用OCRをローカルで使えるようにしたかったので、自作データセットの構築からモデル開発までしています。\
最終的には、ななめ文字やひずみ文字まで認識できるようにします。\
カメラ画像やインターネット上の画像からテキスト情報を抽出し、物体と文字の意味関係を紐づけるデータベースの作成に使う予定です。
## History
2022-09-23:Added 10 number words about 0 ~ 9


## ワークフロー
各ステップごとにデータとモデルの構築を行い、最終的に1つのモデルで対応
![image](https://user-images.githubusercontent.com/55880071/190562237-58485ce9-5d6a-4d00-8596-b61e51196b15.png)

## サンプル
随時更新
![image](https://user-images.githubusercontent.com/55880071/191898993-1cb9f03d-7fa2-4f77-9e2f-96f5f2526477.png)


## データセット構築状況
文字認識のために画像中のテキスト領域を認識するデータセットを4つ作成しています。\
Microsoft社のVoTTを使ってアノテーションをしています。
### テキスト領域データセット
画像から大まかなテキスト領域を抽出するためのデータセット
![image](https://user-images.githubusercontent.com/55880071/190558020-2a186e36-d2f4-4a57-b47f-9270c669a634.png)
### 縦書き文字領域データセット
縦書きテキスト領域から文字を抽出するためのデータセット
![image](https://user-images.githubusercontent.com/55880071/191922409-718f989f-83f7-4d4a-9653-fb34a9cf1384.png)
### 横書き文字領域データセット
横書きテキスト領域から文字を抽出するためのデータセット
![image](https://user-images.githubusercontent.com/55880071/191922493-fa98d89d-579b-459d-b19c-aa3994dc0bd0.png)

### 文字認識データセット
抽出した文字を判定するためのデータセット\
mnistとひらがな73文字に関しては外部データも使用しています。\
現在数字+カタカナ+ひらがな+少量の漢字に対応\
認識可能文字は随時更新

### 引用
mnist [ https://github.com/pytorch ]\
文字画像データセット(平仮名73文字版)[ https://github.com/ndl-lab/hiragana_mojigazo ]
