# Japanese-OCR
## Overview
汎用OCRをローカルで使えるようにしたかったので、自作データセットの構築からモデル開発までしています。\
最終的には、ななめ文字やひずみ文字まで認識できるようにします。\
カメラ画像やインターネット上の画像からテキスト情報を抽出し、物体と文字の意味関係を紐づけるデータベースの作成に使う予定です。
## History
2022-09-23:Added 10 number characters about 0 ~ 9 \
2022-09-25:Registered additional characters. (total: 553 characters) [word_dict.txt](https://github.com/tsutsui-439f340f/Japanese-OCR/files/9640496/word_dict.txt) \
2022-09-28:Registered additional characters. (total: 771 characters) 



## Work Flow

<img src="https://user-images.githubusercontent.com/55880071/192951264-bb3bbba3-0280-4511-ac70-088c51e819c0.png" width=800 height=500 >

## Sample
Update as needed
![image](https://user-images.githubusercontent.com/55880071/192665742-72cb20dc-0b11-422d-83ef-0d7a9577b9cd.png)


## Dataset construction
Four datasets are created to recognize text regions in images for character recognition.\
I am annotating with VoTT from Microsoft.
### Rough Text region dataset
Dataset for extracting rough text regions from a image.
![image](https://user-images.githubusercontent.com/55880071/190558020-2a186e36-d2f4-4a57-b47f-9270c669a634.png)
### Vertical Character region Dataset
Dataset for extracting characters from a vertical text region.
![image](https://user-images.githubusercontent.com/55880071/191922409-718f989f-83f7-4d4a-9653-fb34a9cf1384.png)
### Horizontal character region dataset
Dataset for extracting characters from a horizontal text region.
![image](https://user-images.githubusercontent.com/55880071/191922493-fa98d89d-579b-459d-b19c-aa3994dc0bd0.png)

### Character recognition dataset
Dataset for determining the extracted characters.\
The external data are mnist dataset and character image dataset corresponding to the 73 hiragana characters.\
Currently supports numbers, katakana, hiragana and a few kanji.\
Recognizable characters are updated as needed.
![image](https://user-images.githubusercontent.com/55880071/192106299-52f3f0dc-7d4d-47d0-a143-ddd71bc0a5f0.png)

### Reference
mnist [ https://github.com/pytorch ]\
character image dataset(the 73 hiragana characters version)[ https://github.com/ndl-lab/hiragana_mojigazo ]
