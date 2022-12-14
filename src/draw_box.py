'''
useage:
------------------------------
python src/draw_box.py --image 1
-----------------------------
or 
-----------------------------
python src/draw_box.py -i 1
-----------------------------

'''

import cv2
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--image', type=str, required=True, help='Enter The Image Base-Name')
args = parser.parse_args()


image_id = args.image
text_file = './data/augmented/aug_labels/' + str(image_id) + '.txt'
image_file = './data/augmented/images/' + str(image_id )+ '.jpg'

# load the image
img = cv2.imread(image_file)
with open(text_file, 'r') as f:
    points = f.read().rstrip()
points = points.split('\n')

for box in points:
    points = box.split(' ')
    print(points)
    cx = float(points[1])
    cy = float(points[2])
    w = float(points[3])
    h = float(points[4])

    x1 = int(cx * img.shape[1] - w * img.shape[1] / 2)
    y1 = int(cy * img.shape[0] - h * img.shape[0] / 2)
    x2 = int(cx * img.shape[1] + w * img.shape[1] / 2)
    y2 = int(cy * img.shape[0] + h * img.shape[0] / 2)

    cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)

# save the image
cv2.imshow("image_with_box.jpg", img)
cv2.waitKey(0)
