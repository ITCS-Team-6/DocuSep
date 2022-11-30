import os
import numpy as np
from pdf2image import convert_from_path
import cv2


# pages = convert_from_path(r'C:\Users\Brenden\DocuSep\images\Technical Resume.pdf', poppler_path=r'C:\Program Files\poppler-0.68.0\bin')
#
# pdf =
#
# img = np.array(pages[0])
#
# img = cv2.resize(img, None, fx=0.5, fy=0.5)
#
# cv2.imshow("img", img)
# cv2.waitKey()

dir_path= 'images'

files = [f for f in os.listdir(dir_path)]
for file in files:
    filename = dir_path + '/' + file
    image = None
    if filename.endswith('.pdf'):
        pages = convert_from_path(r'C:\Users\Brenden\DocuSep\images\Technical Resume.pdf',
                                  poppler_path=r'C:\Program Files\poppler-0.68.0\bin')
        image = np.array(pages[0])
        image = cv2.resize(image, None, fx=0.5, fy=0.5)

    elif filename.endswith(('.jpg','.jpeg','.png')):

        image = cv2.imread(filename)

    cv2.imshow("img", image)
    cv2.waitKey()