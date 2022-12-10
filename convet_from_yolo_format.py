import os
import cv2
import numpy as np


text_file_path = './data/labels/test'
img_file_path = './data/images/test'


for label in os.listdir(text_file_path):
    label_name = label.split('.')[0]
    ImageID = f'{label_name}.jpg'
    img = cv2.imread(os.path.join(img_file_path,ImageID))
    i_h = img.shape[0]
    i_w = img.shape[1]

    with open(label,'r') as f:
        lines = f.readlines()
        for line in lines:
            line = np.float32(line.split(" "))
            cx = line[1] * i_w
            cy = line[2] * i_h
            w  = line[3] * i_w 
            h  = line[4] * i_h
            Conf = line[5]
            XMin = cx - w/2
            YMin = cy - h/2
            XMax = cx + w/2
            YMax = cy + h/2

            if os.path.exists('test_labels.csv'):
                with open('test_labels.csv', 'a') as f:
                    text = "\n" + str(XMin) + ',' +  str(YMin) + ',' +  str(XMax) + ',' +  str(YMax) + ',' +  str(Conf) + ',' + str('pothole') + ',' + str(ImageID)
                    f.write(text)
            else:
                with open('test_labels.csv', 'w') as f:
                    text =  'XMin' + ',' +  'YMin' + ',' +  'XMax' + ',' +  'YMax' + ',' +  'Conf' + ',' + 'pothole' + ',' + 'ImageID'
                    f.write(text)
                    
