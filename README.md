# Japanese-OCR
## Overview
汎用OCRをローカルで使えるようにしたかったので、データセットの構築からモデル開発までしています。\
現在はPC文字に対応したモデルの開発をしています。
最終的には、手書き文字、ななめ文字やひずみ文字まで認識できるようにします。

## History

2022-11-01:Created test data for vertical writing data.\
2022-10-05:Implemented semi-automated annotation process\
2022-09-29:Registered additional characters. (total: 6574 characters) \
2022-09-28:Registered additional characters. (total:  771 characters) \
2022-09-25:Registered additional characters. (total:  553 characters)  \
2022-09-23:Registered number characters about 0 ~ 9 
## Evaluation
Using BLEU score.\
Max score :100
### Vertical writing data Domain

|  System version  |  BLEU  |
| ---- | ---- |
|  2022-1101  |  72.82  |
|  2022-1103  |  85.19  |
|  2022-1105  |  90.28 |
|  2022-1106  |  91.41 |


## Sample
Update as needed (20221103)
![image](https://user-images.githubusercontent.com/55880071/199670812-251bec1d-07a3-48f4-86be-ba7134e3ce49.png)




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
