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

imgs = []
for img in glob.glob("croppedimg/*.png"):
    n = cv2.imread(img)
    imgs.append(n)


def get_grayscale(n):
    return cv2.cvtColor(n, cv2.COLOR_BGR2GRAY)
gray = get_grayscale(n)
Image.fromarray(gray)

def thresholding(n):
    return cv2.threshold(n, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
thresh = thresholding(gray)
Image.fromarray(thresh)

imgs = []
for img in glob.glob("croppedimg/*.png"):
    n = cv2.imread(img)
    imgs.append(n)
    n = get_grayscale(n)
    n = thresholding(n)
    h, w = n.shape
    boxes = pytesseract.image_to_boxes(n)
    for b in boxes.splitlines():
        b = b.split(' ')
        cv2.rectangle(n, (int(b[1]), h - int(b[2])), (int(b[3]), h - int(b[4])), (0, 255, 0), 2)
    cv2.namedWindow("Result", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Result", 1280, 768)
    cv2.imshow('Result', n)
    cv2.waitKey()
