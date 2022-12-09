import tkinter
from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
from Functions import *

pytesseract.pytesseract.tesseract_cmd =r'C:\Program Files\Tesseract-OCR\tesseract.exe'

root = Tk()
root.title('DocuSep')
root.geometry("1920x1080")

frame = Frame(root, width=1900, height=1000)
frame.pack(fill= BOTH, expand=1)

canvas = Canvas(frame, width=1900, height=1000)
canvas.pack(side=LEFT, fill=BOTH, expand=1)

scndframe = Frame(canvas, width=1900, height=1000)

canvas.create_window((0,0), window=scndframe, anchor="nw")

b1 = tkinter.Button(scndframe, text = "Upload Documents", width= 20 , command= lambda: upload_file())
b1.grid(row=2,column= 1, columnspan= 4 )
b2 = tkinter.Button(scndframe, text = 'Clear', width = 10, command = lambda: delete())
b2.grid(row = 2, column= 10, columnspan= 4 )
l1 = tkinter.Label(scndframe, text = 'DocuSep', width = 30)
l1.grid(row = 1, column = 1, columnspan = 4)


labels = []

answer = None
imgs = None
answer1 = None
answer2 = None
answer3 = None
answer4 = None
answer5 = None
answer6 = None
answer7 = None


def delete():
    for l in labels:
            l.destroy()

def upload_file():
    file_types = [('Image Files', '*.jpg *.png *.jpeg *.pdf')]
    filename = tkinter.filedialog.askopenfilenames(filetypes=file_types)
    col = 1
    row = 3
    indexid = 1


    for f in filename:
        loop_img = cropper(f)
        loop_img = get_grayscale(loop_img)
        loop_img = thresholding(loop_img)

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

            num_black_pix = np.sum(test_img == 0)
            blkpix.append(num_black_pix)
            max_hor.append(max)

        for b in boxes.splitlines():
            b = b.split(' ')

            cv2.rectangle(loop_img, (int(b[1]), h - int(b[2])), (int(b[3]), h - int(b[4])), (0, 255, 0), 2)

            # Adding the calculated coordinated to their arrays
            bw.append(int(b[3]) - int(b[1]))
            bh.append(int(b[4]) - int(b[2]))


        # Prints the amount of boudning boxes
        sums = np.array(blkpix)
        sus_max_hor = np.array(max_hor)
        new_bw = np.array(bw)


        # Removing sums less than 50 and greater than 5000
        new_sums = np.delete(sums, np.where(sums < 51))
        new_sums = np.delete(new_sums, np.where(new_sums > 5001))


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
        resize_img = new_img.resize((400,650))
        img = ImageTk.PhotoImage(resize_img)

        imgs = tkinter.Label(scndframe)
        imgs.grid(row=row, column=col)
        labels.append(imgs)
        imgs.image = img
        imgs['image'] = img

        if (col == 4):
            row = row + 1
            col = 1
        else:
            col = col + 1


        # Conditionals
        if len(bw) <= 30:
            answer = tkinter.Label(scndframe, text = "This is Unkown")
            answer.grid(row = row + 2 , column = indexid, columnspan = 1)
            labels.append(answer)
        elif match_scr > .5:
            answer1 = tkinter.Label(scndframe, text = "This is Machine Printed")
            answer1.grid(row = row + 2 , column = indexid, columnspan = 1)
            labels.append(answer1)
        elif avg_ratio > .8:
            answer2 = tkinter.Label(scndframe, text = "This is Machine Printed")
            answer2.grid(row = row + 2 , column = indexid, columnspan = 1)
            labels.append(answer2)
        elif avg_ratio < .5:
            answer3 =tkinter.Label(scndframe, text = "This is Handwritten")
            answer3.grid(row = row + 2 , column = indexid, columnspan = 1)
            labels.append(answer3)
        elif avg_ratio > .7 and match_scr > .05:
            answer4 =tkinter.Label(scndframe, text = "This is Machine Printed")
            answer4.grid(row = row + 2 , column = indexid, columnspan = 1)
            labels.append(answer4)
        elif match_scr < .3:
            answer5 =tkinter.Label(scndframe, text = "This is Handwritten")
            answer5.grid(row=row + 2, column= indexid, columnspan=1)
            labels.append(answer5)
        elif match_scr > .4:
            answer6 =tkinter.Label(scndframe, text = "This is Machine Printed")
            answer6.grid(row = row + 2 , column = indexid, columnspan = 1)
            labels.append(answer6)
        else:
            answer7 =tkinter.Label(scndframe, text = "This is Unknown")
            answer7.grid(row = row + 2 , column = indexid, columnspan = 1)
            labels.append(answer7)

        indexid+=1




scrl= Scrollbar(frame, orient=VERTICAL)
scrl.pack(side=RIGHT, fill=Y)
scrl.config(command=canvas.yview)
canvas.configure(yscrollcommand=scrl.set)
canvas.bind('<Configure>', lambda e:canvas.configure(scrollregion=canvas.bbox("all")))

root.mainloop()