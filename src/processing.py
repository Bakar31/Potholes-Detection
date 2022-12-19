import numpy as np
import cv2
import os

def trasform(path):
    img = cv2.imread(path) 
    gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    kernel = np.ones((3,3), np.uint8)
    erosion = cv2.erode(gray_image, kernel, iterations = 1)
    kernel_sharpening = np.array([[-1,-1,-1], 
                              [-1,9,-1], 
                              [-1,-1,-1]])
    sharpened = cv2.filter2D(erosion, -1, kernel_sharpening)
    kernel_3x3 = np.ones((3, 3), np.float32) / 9
    blurred = cv2.filter2D(sharpened, -1, kernel_3x3)
    # cv2.imshow('blurred', blurred)
    # cv2.waitKey(0) 
    return blurred

path= 'pothole-dataset/train/images/train/'
val_path= 'pothole-dataset/train/images/val/'
test_path = 'pothole-dataset/test/images/'
destination = 'gray_data/train/images/train/'
val_destination = 'gray_data/train/images/val/'
test_destination = 'gray_data/test/images/'

for image in os.listdir(test_path):
    im_path = test_path + image
    cv2.imwrite(test_destination+image, trasform(im_path))