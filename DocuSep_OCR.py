from Functions import *
import random
import cv2
import numpy as np
import pytesseract
import glob
import matplotlib.pyplot as plt

cropper()

imgs = []

# we use glob to find files within folder that have png extension

imglist = glob.glob("croppedimg/*")
random.shuffle(imglist)
for img in imglist:
    loop_img = cv2.imread(img)
    imgs.append(loop_img)
    # truncate function
    loop_img = get_grayscale(loop_img)
    loop_img = thresholding(loop_img)
    # loop_img = remove_noise(loop_img)

    h, w = loop_img.shape
    boxes = pytesseract.image_to_boxes(loop_img)
    bw = []
    bh = []

    blkpix = []
    max_hor = []

    # this is for getting all the black pixels on the image for max horizontal run
    for b in boxes.splitlines():
        b = b.split(' ')
        test_img = loop_img[h - int(b[4]): h - int(b[2]), int(b[1]):int(b[3])]
        th, tw = test_img.shape
        max = 0
        for i in range(th):
            count = 0
            for j in range(tw):
                if test_img[i, j] == 0:
                    count += 1
                else:
                    if max < count:
                        max = count
                    count = 0
            if max < count:
                max = count
            count = 0

        num_black_pix = np.sum(test_img == 0)
        blkpix.append(num_black_pix)
        max_hor.append(max)


    for b in boxes.splitlines():
        b = b.split(' ')

        cv2.rectangle(loop_img, (int(b[1]), h-int(b[2])), (int(b[3]), h-int(b[4])), (0, 255, 0), 2)

        # Adding the calculated coordinated to their arrays
        bw.append(int(b[3]) - int(b[1]))
        bh.append(int(b[4]) - int(b[2]))
    cv2.namedWindow("Result", cv2.WINDOW_NORMAL)
    # cv2.resizeWindow("Result", 1280, 768)
    cv2.imshow('Result', loop_img)

    # Prints the amount of boudning boxes
    sums = np.array(blkpix)
    sus_max_hor = np.array(max_hor)
    new_bw = np.array(bw)
    # print(len(bw))

    # Removing sums less than 50 and greater than 5000
    new_sums = np.delete(sums, np.where(sums < 51))
    new_sums = np.delete(new_sums, np.where(new_sums > 5001))
    # print(new_sums)

    # Getting duplicate sums and how many there are
    dupe, counts = np.unique(new_sums, return_counts=True)
    dupe = dupe[counts > 1]
    counts = counts[counts > 1]

    new_max_hor = np.delete(sus_max_hor, np.where(sus_max_hor < 11))

    new_bw = np.delete(new_bw, np.where(sus_max_hor < 11))

    ratio = np.divide(new_max_hor, new_bw)

    avg_ratio = np.average(ratio)

    counts_sums = np.sum(counts)

    match_scr = counts_sums / len(new_sums)

    # print(dupe)
    # print(counts)


    # Histogram
    plt.hist(new_sums, bins=100, edgecolor="red")
    plt.xlabel('Sums')
    plt.ylabel('Num of Occurrences')
    plt.show()

    # Conditionals

    if len(bw) <= 30:
        print("This is Unknown")
    elif match_scr > .5:
        print("This is Machine Printed")
    elif avg_ratio > .8:
        print("This is Machine Printed")
    elif avg_ratio < .5:
        print("This is Handwritten")
    elif avg_ratio > .7 and match_scr > .05:
        print("This is Machine Printed")
    elif match_scr < .3:
        print("This is Handwritten")
    elif match_scr > .4:
        print("This is Machine Printed")
    else:
        print("This is Unknown")

cv2.waitKey(0)




