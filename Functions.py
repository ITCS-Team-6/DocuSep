import tkinter
import cv2
import numpy as np
import pytesseract
from pdf2image import convert_from_path

pytesseract.pytesseract.tesseract_cmd =r'C:\Program Files\Tesseract-OCR\tesseract.exe'

dir_path= 'images'

def cropper(filename):
    image = None
    if filename.endswith('.pdf'):
        pages = convert_from_path(filename,
                                  poppler_path=r'C:\Program Files\poppler-0.68.0\bin')
        image = np.array(pages[0])
        image = cv2.resize(image, None, fx=0.5, fy=0.5)

    elif filename.endswith(('.jpg', '.jpeg', '.png')):
        image = cv2.imread(filename)
    h,w,c = image.shape
    cropped_img = image
    if h > 1500:
        cropped_img = image[750:1500, :]
    # if filename.endswith('.pdf'):
    return cropped_img
    #     # cv2.imwrite('croppedimg/' + filename + '.png', cropped_img)
    # else:
    #     # cv2.imwrite('croppedimg/' + filename, cropped_img)

def get_grayscale(loop_img):
    return cv2.cvtColor(loop_img, cv2.COLOR_BGR2GRAY)


def thresholding(loop_img):
    return cv2.threshold(loop_img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]


def remove_noise(loop_img):
    return cv2.medianBlur(loop_img,5)

