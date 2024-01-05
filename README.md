# Japanese-OCR
## Overview
汎用OCRをローカルで使えるようにしたかったので、データセットの構築からモデル開発までしています。\
現在は文書に対応したモデルの開発をしています。


## History

2022-11-01:Created test data for vertical writing data.\
2022-10-05:Implemented semi-automated annotation process\
2022-09-29:Registered additional characters. (total: 6574 characters) \
2022-09-28:Registered additional characters. (total:  771 characters) \
2022-09-25:Registered additional characters. (total:  553 characters)  \
2022-09-23:Registered number characters about 0 ~ 9 

## Sample
Update as needed (20221109)
7割以下の予測は青字
![pred_sample](https://user-images.githubusercontent.com/55880071/200763901-ab613c40-bd1d-4114-8fda-93077bf35831.png)






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

