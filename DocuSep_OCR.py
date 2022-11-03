import os
from PIL import Image
import cv2
import pytesseract
import matplotlib.pyplot as plt
import numpy as np
from pytesseract import Output
import re
import glob


pytesseract.pytesseract.tesseract_cmd =r'C:\Program Files\Tesseract-OCR\tesseract.exe'

dir_path= 'images'

def cropper():
    files = [f for f in os.listdir(dir_path)]
    for file in files:
        filename = dir_path + '/' + file
        image = cv2.imread(filename)
        cropped_img = image[750:2800,:]
        cv2.imwrite('croppedimg/' + file, cropped_img)

cropper()

imgs = []
for img in glob.glob("croppedimg/*.png"):
    loop_img= cv2.imread(img)
    imgs.append(loop_img)


def get_grayscale(loop_img):
    return cv2.cvtColor(loop_img, cv2.COLOR_BGR2GRAY)


def thresholding(loop_img):
    return cv2.threshold(loop_img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]


def remove_noise(loop_img):
    return cv2.medianBlur(loop_img,5)

# test
imgs = []
for img in glob.glob("croppedimg/*.png"):
    loop_img = cv2.imread(img)
    imgs.append(loop_img)
    loop_img = get_grayscale(loop_img)
    loop_img= thresholding(loop_img)
    loop_img = remove_noise(loop_img)
    h, w = loop_img.shape
    boxes = pytesseract.image_to_boxes(loop_img)
    bw = []
    bh = []
    for b in boxes.splitlines():
        b = b.split(' ')
        cv2.rectangle(loop_img, (int(b[1]), h - int(b[2])), (int(b[3]), h - int(b[4])), (0, 255, 0), 2)
    cv2.namedWindow("Result", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Result", 1280, 768)
    cv2.imshow('Result', loop_img)
    print(len(bw))
    print(len(bh))
    cv2.waitKey()
