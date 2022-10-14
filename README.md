# Japanese-OCR
## Overview
汎用OCRをローカルで使えるようにしたかったので、自作データセットの構築からモデル開発までしています。\
最終的には、ななめ文字やひずみ文字まで認識できるようにします。

## History
2022-09-23:Registered number characters about 0 ~ 9 \
2022-09-25:Registered additional characters. (total:  553 characters)  \
2022-09-28:Registered additional characters. (total:  771 characters) \
2022-09-29:Registered additional characters. (total: 6574 characters) \
2022-10-05:Implementation of semi-automated annotation process





## Work Flow

<img src="https://user-images.githubusercontent.com/55880071/192951264-bb3bbba3-0280-4511-ac70-088c51e819c0.png" width=800 height=500 >

## Sample
Update as needed (0928)
![image](https://user-images.githubusercontent.com/55880071/192665742-72cb20dc-0b11-422d-83ef-0d7a9577b9cd.png)


## Dataset construction
Three datasets are created to recognize text regions in images for character recognition.\
I am annotating with VoTT from Microsoft.
### Rough Text region dataset
Dataset for extracting rough text regions from a image.
![image](https://user-images.githubusercontent.com/55880071/193344042-24a39974-09ec-43a6-910b-90cce9e61dee.png)

### Vertical Character region Dataset
Dataset for extracting characters from a vertical text region.
![image](https://user-images.githubusercontent.com/55880071/191922409-718f989f-83f7-4d4a-9653-fb34a9cf1384.png)
### Horizontal character region dataset
Dataset for extracting characters from a horizontal text region.
![image](https://user-images.githubusercontent.com/55880071/191922493-fa98d89d-579b-459d-b19c-aa3994dc0bd0.png)


### Reference
mnist [ https://github.com/pytorch ]\
character image dataset(the 73 hiragana characters version)[ https://github.com/ndl-lab/hiragana_mojigazo ]
