from PIL import Image
import cv2
import pytesseract
import matplotlib.pyplot as plt
import numpy as np
from pytesseract import Output
import re


pytesseract.pytesseract.tesseract_cmd =r'C:\Program Files\Tesseract-OCR\tesseract.exe'

filename = f'images/test.png'
image = cv2.imread(filename)
cropped_img = image[750:2800,:]
cv2.imwrite('images/test4.png', cropped_img)
filename = f'images/test4.png'

custom_config = r'-l eng --oem 3 --psm 6'
text = pytesseract.image_to_string(image,config=custom_config)
print(text)

try:
    text=pytesseract.image_to_string(image,lang="eng")
    characters_to_remove = "!()@—*“>+-/,'|£#%$&^_~"
    new_string = text
    for character in characters_to_remove:
        new_string = new_string.replace(character, "")
    print(new_string)
except IOError as e:
    print("Error (%s)." % e)

image = cv2.imread('images/test.png')



def get_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = get_grayscale(image)
Image.fromarray(gray)



def thresholding(image):
# source image,  grayscale image
    return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
thresh = thresholding(gray)
Image.fromarray(thresh)



def match_template(image, template):
    return cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)
match = match_template(gray, gray)
match

img = cv2.imread(filename)
img = get_grayscale(img)
img = thresholding(img)
h, w = img.shape
boxes = pytesseract.image_to_boxes(img)
for b in boxes.splitlines():
    b = b.split(' ')
    img = cv2.rectangle(img, (int(b[1]), h - int(b[2])), (int(b[3]), h - int(b[4])), (0, 255, 0), 2)
Image.fromarray(img)
cv2.imshow('window',img)
cv2.waitKey()

