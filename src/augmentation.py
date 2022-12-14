import albumentations as A
from matplotlib import pyplot as plt
import cv2
import os

files = os.listdir('data/train/labels/train')
# print(files)
for file in files[0:5]:
    print(file)
    bboxes = []
    text_path = './data/train/labels/train/' + file
    img_path = './data/train/images/train/' + file[:-4] + '.jpg'
    # print(img_path)
    with open(text_path) as f:    
        box_params = f.readlines()
        for line in box_params:
            params = line.split(' ')
            params.pop(0)
            for i in range(0, len(params)):
                params[i] = float(params[i])
            bboxes.append(params)

    # print(len(bboxes))
    # print(bboxes)

    class_labels = [0]*len(bboxes)
    category_id_to_name = {0: 'pohole'}

    transform = A.Compose([
        A.GlassBlur(sigma=0.7,iterations=2, always_apply=True),
        # A.RandomRain(always_apply=True),
        # A.RandomBrightness(always_apply=True) 
        # A.RandomFog()?
        # A.RandomShadow()
        # A.UnsharpMask()
        # A.RandomCrop(width=256, height=256)
        # A.BBoxSafeRandomCrop()
        # A.SafeRotate(always_apply=True)
        # A.Flip(always_apply=True)
        # A.ShiftScaleRotate(always_apply=True)
        # A.VerticalFlip(always_apply=True)
        # A.VerticalFlip(always_apply=True)
    ], bbox_params=A.BboxParams(format='yolo', label_fields = ['class_labels']))

    # Read an image with OpenCV and convert it to the RGB colorspace
    image = cv2.imread(img_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    transformed = transform(image=image, bboxes=bboxes, class_labels=class_labels)
    transformed_image = transformed['image']
    transformed_bboxes = transformed['bboxes']
    transformed_class_labels = transformed['class_labels']

    new_bboxes = []
    for box in transformed_bboxes:
        n_box = list(box)
        n_box.insert(0, 0)
        new_bboxes.append(n_box)
    print(new_bboxes)
    # cv2.imshow('aug', transformed_image)
    # cv2.waitKey(0)

    dest_text = './data/augmented/labels/' + file[:-4] + '_aug.txt'
    dest_img = './data/augmented/images/' + file[:-4] + '_aug.jpg'
    cv2.imwrite(dest_img, transformed_image)
    with open(dest_text, 'w') as f:
        for line in new_bboxes:
            f.write(f"{line}\n")
