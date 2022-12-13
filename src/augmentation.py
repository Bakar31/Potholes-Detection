import albumentations as A
import cv2

bboxes = []
with open('data\\train\\labels\\train\\1.txt') as f:    
    box_params = f.readlines()
    for line in box_params:
        params = line.split(' ')
        params[0] = int(params[0])
        for i in range(1, len(params)):
            params[i] = float(params[i])
        bboxes.append(params)
print(bboxes)

transform = A.Compose([
    A.RandomCrop(width=450, height=450),
    A.HorizontalFlip(p=0.5),
    A.RandomBrightnessContrast(p=0.2),
], bbox_params=A.BboxParams(format='yolo'))

# Read an image with OpenCV and convert it to the RGB colorspace
image = cv2.imread("data\\train\\images\\train\\1.jpg")
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

transformed = transform(image=image, bboxes=bboxes)
transformed_image = transformed['image']
transformed_bboxes = transformed['bboxes']