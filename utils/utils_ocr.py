import cv2
import os
import torch.nn as nn
import re

from torchvision import models
from torchvision.models import resnet50

class CNNModel(nn.Module):
    def __init__(self,n:int):
        super().__init__()
        self.cnn_encoder = models.vgg16(pretrained=True)
        self.cnn_encoder.classifier = nn.Linear(25088,n)
        
    def forward(self, x):
        return self.cnn_encoder(x)

class CNNModel_ResNet(nn.Module):
    def __init__(self,n):
        super().__init__()
        self.cnn_encoder = resnet50(pretrained=True)
        self.cnn_encoder.fc = nn.Linear(2048,n)
    def forward(self, x):
        return self.cnn_encoder(x)

def word_save(data,path,name):
    if not os.path.exists(path):
        os.mkdir(path)
    for idx,img in enumerate(data):
        cv2.imwrite("{}/{}.png".format(path,name+"_"+str(idx)), img)  


#F=1で横書き用に変換
def build_map(F=0,m="words/word_dict.txt"):
    tategaki_word_map_data=dict()
    yokogaki_word_map_data=dict()
    capital_pattern = '._C'
    with open(m,encoding="utf-8") as f:
        for i in f.readlines():
            b=None
            a=i.replace("\n","").split("\t")
            if a[1]=="縦、":
                a[1]="︑"
                if F:
                    a[1]="、"
            elif a[1]=="縦。":
                a[1]="︒"
                if F:
                    a[1]="。"
            elif a[1]=="縦3点":
                a[1]="⋮"
                if F:
                    a[1]="…"
            elif a[1]=="縦「":
                a[1]="﹁"
                if F:
                    a[1]="「"
            elif a[1]=="縦」":
                a[1]="﹂"
                if F:
                    a[1]="」"
            elif a[1]=="縦【":
                a[1]="︻"
                if F:
                    a[1]="【"
            elif a[1]=="縦】":
                a[1]="︼"
                if F:
                    a[1]="】"
            elif a[1]=="縦ー":
                a[1]="｜"
                if F:
                    a[1]="ー"
            elif a[1]=="縦(":    
                a[1]="︵"
                if F:
                    a[1]="（"
            elif a[1]=="縦)":    
                a[1]="︶"
                if F:
                    a[1]="）"
                    
            elif a[1]=="カンマ":
                a[1]=","
            elif re.match(capital_pattern, a[1]):
                a[1]=a[1][0]
            elif a[1]=="ピリオド":
                a[1]="."
            elif a[1] in list("ぁぃぅぇぉっゃゅょゎ"):
                for i,j in zip(list("ぁぃぅぇぉっゃゅょゎ"),list("あいうえおつやゆよわ")):
                    if a[1]==i:
                        b=j
            elif a[1]=="縦っ":
                a[1]="っ"
            elif a[1]=="縦ぁ":
                a[1]="ぁ"
            elif a[1]=="縦ゎ":
                a[1]="ゎ"
            elif a[1]=="縦ぅ":
                a[1]="ぅ"
            elif a[1]=="縦ぇ":
                a[1]="ぇ"
            elif a[1]=="縦ッ":
                a[1]="ッ"
            elif a[1]=="縦ぃ":
                a[1]="ぃ"
            elif a[1]=="縦ァ":
                a[1]="ァ"
            elif a[1]=="縦ぉ":
                a[1]="ぉ"
            elif a[1]=="縦ォ":
                a[1]="ォ"
            elif a[1]=="縦ィ":
                a[1]="ィ"
            elif a[1]=="縦ゥ":
                a[1]="ゥ"
            elif a[1]=="縦ェ":
                a[1]="ェ"
            elif a[1]=="縦ゃ":
                a[1]="ゃ"
            elif a[1]=="縦ょ":
                a[1]="ょ"
            elif a[1]=="縦ゅ":
                a[1]="ゅ"
            elif a[1]=="縦ョ":
                a[1]="ョ"
            elif a[1]=="縦ャ":
                a[1]="ャ"
            elif a[1]=="縦ュ":
                a[1]="ュ"
            elif a[1]=="縦《":
                a[1]="《"
            elif a[1]=="縦》":
                a[1]="》"
            elif a[1]=="縦『":
                a[1]="﹃"
                if F:
                    a[1]="『"
            elif a[1]=="縦』":
                a[1]="﹄"
                if F:
                    a[1]="』"
            elif a[1]=="背景":
                a[1]=""
            elif a[1]=="縦～":
                a[1]="～"
            elif a[1]=="3点":
                a[1]="…" 
            yokogaki_word_map_data[int(a[0])]=a[1]
            if b is not None:
                tategaki_word_map_data[int(a[0])]=b
            else:
                tategaki_word_map_data[int(a[0])]=a[1]
    return tategaki_word_map_data,yokogaki_word_map_data



