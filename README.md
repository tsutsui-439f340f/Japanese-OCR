# Japanese-OCR
## Overview
汎用OCRをローカルで使えるようにしたかったので、自作データセットの構築からモデル開発までしています。\
最終的には、ななめ文字やひずみ文字まで認識できるようにします。\
カメラ画像やインターネット上の画像からテキスト情報を抽出し、物体と文字の意味関係を紐づけるデータベースの作成に使う予定です。
## History
2022-09-23:Added 10 number words about 0 ~ 9
2022-09-25:Registering additional many words. (total: 553 words) [word_dict.txt](https://github.com/tsutsui-439f340f/Japanese-OCR/files/9640496/word_dict.txt)


## Work Flow
各ステップごとにデータとモデルの構築を行い、最終的に1つのモデルで対応
![image](https://user-images.githubusercontent.com/55880071/190562237-58485ce9-5d6a-4d00-8596-b61e51196b15.png)

## Sample
Update as needed
![image](https://user-images.githubusercontent.com/55880071/191898993-1cb9f03d-7fa2-4f77-9e2f-96f5f2526477.png)


## Dataset construction
Four datasets are created to recognize text regions in images for character recognition.\
I am annotating with VoTT from Microsoft.
### Textarea dataset
Dataset for extracting rough text regions from images.
![image](https://user-images.githubusercontent.com/55880071/190558020-2a186e36-d2f4-4a57-b47f-9270c669a634.png)
### Vertical Character Area Dataset
Dataset for extracting characters from a vertical text area.
![image](https://user-images.githubusercontent.com/55880071/191922409-718f989f-83f7-4d4a-9653-fb34a9cf1384.png)
### Horizontal character domain dataset
Dataset for extracting characters from a horizontal text area
![image](https://user-images.githubusercontent.com/55880071/191922493-fa98d89d-579b-459d-b19c-aa3994dc0bd0.png)

### Character recognition dataset
Dataset for determining the extracted characters.\
The external data are mnist dataset and character image dataset corresponding to the 73 hiragana characters.\
Currently supports numbers + katakana + hiragana + small amount of kanji.\
Recognizable characters are updated as needed.
![image](https://user-images.githubusercontent.com/55880071/192106299-52f3f0dc-7d4d-47d0-a143-ddd71bc0a5f0.png)

### 引用
mnist [ https://github.com/pytorch ]\
character image dataset(the 73 hiragana characters version)[ https://github.com/ndl-lab/hiragana_mojigazo ]
