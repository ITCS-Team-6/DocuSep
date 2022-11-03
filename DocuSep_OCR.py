import os
import random
import cv2
import numpy as np
import pytesseract
import glob
pytesseract.pytesseract.tesseract_cmd =r'C:\Program Files\Tesseract-OCR\tesseract.exe'

dir_path= 'images'

def cropper():
    files = [f for f in os.listdir(dir_path)]
    for file in files:
        filename = dir_path + '/' + file
        image = cv2.imread(filename)
        h,w,c = image.shape
        cropped_img = image
        if h > 2800:
            cropped_img = image[750:2800, :]

        cv2.imwrite('croppedimg/' + file, cropped_img)

cropper()

def get_grayscale(loop_img):
    return cv2.cvtColor(loop_img, cv2.COLOR_BGR2GRAY)


def thresholding(loop_img):
    return cv2.threshold(loop_img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]


def remove_noise(loop_img):
    return cv2.medianBlur(loop_img,5)


# def erode(loop_img):
#     kernel = np.ones((5,5),np.uint8)
#     return cv2.erode(loop_img, kernel, iterations = 1)
# erode = erode(gray)
# Image.fromarray(erode)

# def opening(loop_img):
#     kernel = np.ones((5,5),np.uint8)
#     return cv2.morphologyEx(loop_img, cv2.MORPH_OPEN, kernel)
# opening = opening(gray)
# Image.fromarray(opening)
#
# def match_template(loop_img, template):
#     return cv2.matchTemplate(loop_img, template, cv2.TM_CCOEFF_NORMED)
# match = match_template(gray, gray)
# match



imgs = []
#we use glob to find files within folder that have png exten
imglist = glob.glob("croppedimg/*")
random.shuffle(imglist)
for img in imglist:
    loop_img = cv2.imread(img)
    imgs.append(loop_img)
    loop_img = get_grayscale(loop_img)
    loop_img = thresholding(loop_img)
    loop_img = remove_noise(loop_img)

    # print(type(loop_img))
    # loop_img = erode[loop_img]
    # loop_img = opening(loop_img)
    # loop_img = match_template(loop_img, template=0)

    h, w = loop_img.shape
    boxes = pytesseract.image_to_boxes(loop_img)
    bw = []
    bh = []
    for b in boxes.splitlines():
        b = b.split(' ')
        cv2.rectangle(loop_img, (int(b[1]), h-int(b[2])), (int(b[3]), h-int(b[4])), (0, 255, 0), 2)

        #adding the calculated cordinated to their arrays
        bw.append(int(b[3]) - int(b[1]))
        bh.append(int(b[4]) - int(b[2]))
    cv2.namedWindow("Result", cv2.WINDOW_NORMAL)
    # cv2.resizeWindow("Result", 1280, 768)
    print(img)
    print(h,w)
    cv2.imshow('Result', loop_img)

    #prints the amount of boudning boxes
    sum = np.multiply(bw, bh)
    print(len(bw))
    print(sum)

    if len(bw) <= 30:
        print("This is unkown")

    cv2.waitKey()
