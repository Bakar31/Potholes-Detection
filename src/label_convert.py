import os
import pandas as pd
import cv2

labels = pd.read_csv('labels.csv')

def yolo_extractor(row):
    label = labels.iloc[row].ImageID[:-4]
    cx = (labels.iloc[row].XMin + labels.iloc[row].XMax)/2
    cy = (labels.iloc[row].YMin + labels.iloc[row].YMax)/2
    w = labels.iloc[row].XMax - labels.iloc[row].XMin
    h = labels.iloc[row].YMax - labels.iloc[row].YMin
    return label, cx, cy, w, h 

for row in range(len(labels) - 1):
    label, cx, cy, w, h = yolo_extractor(row)
    image_path = os.path.join('img',f'{label}.jpg')
    image = cv2.imread(image_path)
    i_h = image.shape[0]
    i_w = image.shape[1]

    w = round((w/i_w), 6)
    h= round((h/i_h), 6)
    cx = round((cx/i_w), 6)
    cy = round((cy/i_h), 6)
    # print(w, h, cx, cy)

    path = './data/labels/'
    label_name = path + label + '.txt'
    if os.path.exists(label_name):
        with open(label_name, 'a') as f:
            text = "\n" + str(0) + ' ' +  str(cx) + ' ' +  str(cy) + ' ' +  str(w) + ' ' +  str(h)
            print(text)
            f.write(text)
    else:
        with open(label_name, 'w') as f:
            text =  str(0) + ' ' +  str(cx) + ' ' +  str(cy) + ' ' +  str(w) + ' ' +  str(h)
            print(text)
            f.write(text)
            
