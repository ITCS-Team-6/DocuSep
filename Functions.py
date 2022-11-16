import cv2
import os

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

def get_grayscale(loop_img):
    return cv2.cvtColor(loop_img, cv2.COLOR_BGR2GRAY)


def thresholding(loop_img):
    return cv2.threshold(loop_img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]


def remove_noise(loop_img):
    return cv2.medianBlur(loop_img,5)