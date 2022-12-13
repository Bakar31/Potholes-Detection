import albumentations as A
from matplotlib import pyplot as plt
import cv2

BOX_COLOR = (255, 0, 0) # Red
TEXT_COLOR = (255, 255, 255) # White

bboxes = []
with open('./data/train/labels/train/1.txt') as f:    
    box_params = f.readlines()
    for line in box_params:
        params = line.split(' ')
        params.pop(0)
        for i in range(0, len(params)):
            params[i] = float(params[i])
        bboxes.append(params)

print(len(bboxes))
print(bboxes)

class_labels = [0]*len(bboxes)
category_id_to_name = {0: 'pohole'}

transform = A.Compose([
    A.AdvancedBlur (blur_limit=(3, 7)),
    A.HorizontalFlip(p=0.5),
    A.RandomBrightnessContrast(p=0.2),
], bbox_params=A.BboxParams(format='yolo', label_fields = ['class_labels']))

# Read an image with OpenCV and convert it to the RGB colorspace
image = cv2.imread("./data/train/images/train/1.jpg")
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

transformed = transform(image=image, bboxes=bboxes, class_labels=class_labels)
transformed_image = transformed['image']
transformed_bboxes = transformed['bboxes']
transformed_class_labels = transformed['class_labels']
print(transformed_bboxes)
cv2.imshow('aug', transformed_image)
cv2.waitKey(0)
# print(transformed_image)
