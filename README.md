# text-detection
## 概要
汎用OCRをローカルで使えるようにしたかったので、自作データセットの構築からモデル開発までしています。
将来的には、カメラ画像やインターネット上の画像からテキスト情報を抽出し、画像と文字の意味関係を紐づけるデータベースの作成を目的としている。

## ワークフロー
各ステップごとにデータとモデルの構築を行い、最終的に1つのモデルで対応する。
<img src="https://user-images.githubusercontent.com/55880071/190015890-09991789-70ac-4188-86b4-80516d8ba04a.png" width="820" height="520">

## サンプル
随時更新
![image](https://user-images.githubusercontent.com/55880071/190018719-745a4ad0-b80b-462c-9b34-1a40420410b8.png)


## データセット構築状況
文字認識のために画像中のテキストエリアを認識するデータセットを3つ作成しています。
Microsoft社のVottを使ってアノテーションをしています。
### テキスト領域データセット
画像から大まかなテキスト領域を抽出するためのデータセット
![image](https://user-images.githubusercontent.com/55880071/189475372-91095030-61ed-40a3-a836-661fe82b68cd.png)
### 縦書き文字領域データセット
縦書きテキスト領域から文字を抽出するためのデータセット
### 横書き文字領域データセット
横書きテキスト領域から文字を抽出するためのデータセット
