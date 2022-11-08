# encoding utf-8

import argparse
import cv2
import os
import shutil
import torch
import warnings

from tqdm import tqdm

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
warnings.filterwarnings('ignore')

def text_extraction(img,objects,rato=[1,1]):
    text_img=[]
    area=[] #area ymin,ymax,xmin,xmax
    for i,j in enumerate(objects.xyxy[0].name):
        if j=="text":
            ymin=int(objects.xyxy[0].ymin[i])
            ymax=int(objects.xyxy[0].ymax[i])
            xmin=int(objects.xyxy[0].xmin[i])
            xmax=int(objects.xyxy[0].xmax[i])
            text_img.append(img[ymin:ymax,xmin:xmax].copy())
            cv2.rectangle(img, (xmin,ymin),(xmax,ymax), (0, 0, 255),thickness=4)
            area.append([ymin*rato[0],ymax*rato[0],xmin*rato[1],xmax*rato[1]])
    return img,text_img,area

if __name__=="__main__":
    parser = argparse.ArgumentParser(description='')   
    parser.add_argument('path',default=False)   
    parser.add_argument('dst',default=False)   
    parser.add_argument('--which',default=1)    #1だとテキストを含む画像を抽出
    parser.add_argument('--duration',default=60)
    args = parser.parse_args()

    if os.path.exists(args.dst):
        shutil.rmtree(args.dst)
    os.mkdir(args.dst)

    are_param_path = "best1.pt" #テキスト検出モデルのパラメータ
    p=os.listdir("param")
    i=1
    while True:
        if are_param_path not in p:
            are_param_path="best"+str(i-1)+".pt"
            break
        i+=1
        are_param_path="best"+str(i)+".pt"

    are_param_path = os.path.join("param",are_param_path)
    print(are_param_path)
    model = torch.hub.load('ultralytics/yolov5', 'custom', path=are_param_path)

    cap = cv2.VideoCapture(args.path)
    fmt = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    #フレームレート取得
    fps = cap.get(cv2.CAP_PROP_FPS)
    writer = cv2.VideoWriter(os.path.join(args.dst,"sample.mp4"), fmt, fps, (width, height))
    #フレーム数
    count = cap.get(cv2.CAP_PROP_FRAME_COUNT)
    for f in tqdm(range(int(count))):
        ret, img = cap.read()
        if ret is False:
            continue
        results = model(img)
        img2,text_img,_=text_extraction(img.copy(),results.pandas())
        if args.which:
            if len(text_img)!=0:
                if f%args.duration==1:
                    cv2.imwrite(os.path.join(args.dst,"img_{}_{}.png".format(os.path.basename(args.path)[:-4],f)),img)
        else:
            if len(text_img)==0:
                if f%args.duration==1:
                    cv2.imwrite(os.path.join(args.dst,"img_{}_{}.png".format(os.path.basename(args.path)[:-4],f)),img)
        writer.write(img2)
    writer.release()
    cap.release()