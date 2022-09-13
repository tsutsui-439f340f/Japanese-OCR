# text-detection
## 概要
汎用OCRをローカルで使えるようにしたかったので、自作データセットの構築からモデル開発までしています。
将来的には、カメラ画像やインターネット上の画像からテキスト情報を抽出し、画像と文字の意味関係を紐づけるデータベースの作成を目的としている。

## ワークフロー
各ステップごとにデータとモデルの構築を行い、最終的に1つのモデルで対応する。
<img src="https://user-images.githubusercontent.com/55880071/190015890-09991789-70ac-4188-86b4-80516d8ba04a.png" width="820" height="520">

## サンプル
随時更新
<p>
          
<img src="https://user-images.githubusercontent.com/55880071/188486580-2add2328-f85f-4c45-8b01-a3b5b6f8f926.png" width="420" height="320">
          
<img src="https://user-images.githubusercontent.com/55880071/188486615-a3d800b1-770e-41e8-82b2-82e396d3bb16.png" width="420" height="320">

<img src="https://user-images.githubusercontent.com/55880071/190014896-c167c271-1bd1-4527-a239-13be040e9bc7.png" width="420" height="320">

<img src="https://user-images.githubusercontent.com/55880071/190014902-46eb4216-7375-4595-a131-51a6c640575c.png" width="420" height="320">

</p>

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
