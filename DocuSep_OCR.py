import tkinter
from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
from Functions import *

pytesseract.pytesseract.tesseract_cmd =r'C:\Program Files\Tesseract-OCR\tesseract.exe'

root = Tk()
root.title('DocuSep')

l1 = tkinter.Label(root, text= 'DocuSep', width = 30)
l1.grid(row=1, column=1, columnspan=4)
b1 = tkinter.Button(root, text='Upload Documents',width=20,command = lambda:upload_file())
b1.grid(row = 2, column=1, columnspan=4)

def upload_file():
    file_types = [('Image Files', '*.jpg *.png *.jpeg *.pdf')]
    filename = tkinter.filedialog.askopenfilenames(filetypes=file_types)
    col=1
    row=3

    indexid = 1

    for f in filename:
        loop_img = cropper(f)
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

            cv2.rectangle(loop_img, (int(b[1]), h - int(b[2])), (int(b[3]), h - int(b[4])), (0, 255, 0), 2)

            # Adding the calculated coordinated to their arrays
            bw.append(int(b[3]) - int(b[1]))
            bh.append(int(b[4]) - int(b[2]))

        # cv2.resizeWindow("Result", 1280, 768)


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



        #handling of image
        new_img = Image.fromarray(loop_img)

        img = ImageTk.PhotoImage(new_img)


        #variables for labels
        answer = tkinter.Label(root)
        answer1 = tkinter.Label(root)
        answer2= tkinter.Label(root)
        answer3 = tkinter.Label(root)
        answer4 = tkinter.Label(root)
        answer5= tkinter.Label(root)
        answer6 = tkinter.Label(root)
        answer7 = tkinter.Label(root)

        # Conditionals
        if len(bw) <= 30:
            answer.label = Label(root, text = "This is Unkown").grid(row = 4 , column= indexid, columnspan=4)
        elif match_scr > .5:
           answer1.label = Label(root, text = "This is Machine Printed").grid(row = 4 , column= indexid, columnspan=4)
        elif avg_ratio > .8:
            answer2.label = Label(root, text = "This is Machine Printed").grid(row = 4 , column= indexid, columnspan=4)
        elif avg_ratio < .5:
            answer3.label = Label(root, text = "This is Handwritten").grid(row = 4 , column= indexid, columnspan=4)
        elif avg_ratio > .7 and match_scr > .05:
            answer4.label = Label(root, text = "This is Machine Printed").grid(row = 4 , column= indexid, columnspan=4)
        elif match_scr < .3:
            answer5.label = Label(root, text = "This is Handwritten").grid(row = 4 , column= indexid, columnspan=4)
        elif match_scr > .4:
            answer6.label = Label(root, text = "This is Machine Printed").grid(row = 4 , column= indexid, columnspan=4)
        else:
            answer7.label = Label(root, text = "This is Unknown").grid(row = 4 , column= indexid, columnspan=4)

        indexid+=1

        e1 = tkinter.Label(root)
        e1.grid(row=row, column=col)
        e1.image = img
        e1['image'] = img
        if (col == 3):
            row = row + 1
            col = 1
        else:
            col = col + 1


root.mainloop()