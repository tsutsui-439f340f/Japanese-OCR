# Japanese-OCR
## Overview
汎用OCRをローカルで使えるようにしたかったので、データセットの構築からモデル開発までしています。\
最終的には、ななめ文字やひずみ文字まで認識できるようにします。

## History
2022-09-23:Registered number characters about 0 ~ 9 \
2022-09-25:Registered additional characters. (total:  553 characters)  \
2022-09-28:Registered additional characters. (total:  771 characters) \
2022-09-29:Registered additional characters. (total: 6574 characters) \
2022-10-05:Implementation of semi-automated annotation process
2022-11-01:Created test data for vertical writing data.
## Evaluation
Using BLEU score.\
Max score :100
### vertical writing data Domain

|  System  |  BLEU  |
| ---- | ---- |
|  2022-1101  |  72.82  |


## Work Flow

<img src="https://user-images.githubusercontent.com/55880071/192951264-bb3bbba3-0280-4511-ac70-088c51e819c0.png" width=800 height=500 >


## Sample
Update as needed (20221019)
![image](https://user-images.githubusercontent.com/55880071/196487417-06894afb-1db3-4c83-835b-28316539e8b6.png)
![image](https://user-images.githubusercontent.com/55880071/196489245-a1162725-7b87-43b4-8a80-f26bff98397e.png)




## Dataset construction
Three datasets are created to recognize text regions in images for character recognition.\
I am annotating with VoTT from Microsoft.
### Rough Text region dataset
Dataset for extracting rough text regions from a image.
![image](https://user-images.githubusercontent.com/55880071/195835235-32815e60-ff99-4bc1-abb4-2458a03c671a.png)

### Vertical Character region Dataset
Dataset for extracting characters from a vertical text region.
![image](https://user-images.githubusercontent.com/55880071/195835827-004346dc-a47a-4436-8ec9-d727c9d21803.png)
### Horizontal character region dataset
Dataset for extracting characters from a horizontal text region.
![image](https://user-images.githubusercontent.com/55880071/195836042-17f3563c-1128-4e32-9579-dabfa62b5026.png)


### Reference
mnist [ https://github.com/pytorch ]\
character image dataset(the 73 hiragana characters version)[ https://github.com/ndl-lab/hiragana_mojigazo ]
