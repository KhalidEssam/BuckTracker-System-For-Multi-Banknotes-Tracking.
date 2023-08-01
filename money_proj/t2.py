import cv2
import numpy
import pytesseract
import PIL.Image


def countletter(string, ff, fv):
    c2 = c1 = 0
    flag = 0
    for c in string:

        if c.isalpha():
            # c = c.upper()
            if fv != 1:
                if ff == 0:

                    if c == 'M' or c == 'L' or c == 'P' or c == 'F' or c == 'B' or c == 'W':

                        ff = 1
                        c2 = 1
                elif ff == 1:
                    if c == 'B' or c == 'F' or c == 'E' or c == 'H' or c == 'J' or c == 'K' or c == 'D' or c == 'C':
                        ff = 2
                        c2 = 2

                else:
                    ff = 0
            else:
                if c == 'M' or c == 'L' or c == 'P' or c == 'F' or c == 'B' or c == 'W' or c == 'K' or c == 'D' or c == 'C' or c == 'E' or c == 'H' or c == 'J':
                    ff = 3

    return ff


def countnum(s, count2):

    for c in s:

        if c.isdigit():
            count2 += 1

        else:
            count2 = -1
    return count2


class actor:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h2 = h


pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
myconfig = r"--psm 12  --oem 3"

source = cv2.VideoCapture("m_Trim.mp4")

mm = 0
while True:
    ret, img = source.read()
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # cv2.imshow("Live", img)

    h, w = img.shape
    serialnumber = ''
    fletter = 0
    count = 0
    f2 = f3 = 0
    xl = yl = x = y = h2 = 0
    l = []

    red = int(255)
    g = int(0)
    b = int(0)
    boxes = pytesseract.image_to_boxes(img, config=myconfig)
    last = ''
    for b in boxes.splitlines():
        b = b.split(' ')
        # print(b[0] + '********' + last)
        xl = x
        yl = y
        wl = w
        hl = h2
        # print(last)

        x, y, w, h2 = int(b[1]), int(b[2]), int(b[3]), int(b[4])
        if f3 == 1 and b[0].isalpha():

            f3 = countletter(b[0], fletter, f3)
            if f3 == 3:
                serialnumber += b[0]
                l.append(actor(x, y, w, h2))
                print(serialnumber)
                serialnumber = ''
                count = 0
                f3 = 0
                f2 = 0
                fletter = 0
                l.clear()
        if f3 == 1 and not b[0].isalpha():
            print(serialnumber)
            serialnumber = ''
            count = 0
            f3 = 0
            f2 = 0
            fletter = 0
            l.clear()

            for i in l:
                cv2.rectangle(img, (int(i.x), h-int(i.y)),
                              (int(i.w), h-int(i.h2)), (0, 0, 255), 1)

        if b[0].isalpha():
            if x-xl <= 19:
                fletter = countletter(last, fletter, f3)
                fletter = countletter(b[0], fletter, f3)
        if fletter == 2:
            if f2 == 0:
                serialnumber += last
                serialnumber += b[0]
                l.append(actor(x, y, w, h2))
                l.append(actor(xl, yl, wl, hl))

                f2 = 1
            else:
                count = countnum(b[0], count)
                if count == -1:
                    # print("not it")
                    serialnumber = ''
                    count = 0
                    f3 = 0
                    f2 = 0
                    fletter = 0
                    l.clear()
                else:
                    l.append(actor(x, y, w, h2))
                    serialnumber += b[0]
                    if count == 8:
                        f3 = 1
                        count = 0
        # if len(serialnumber) == 11:
        #     serialnumber = ''
        last = b[0]
        mm += 1
    key = cv2.waitKey(1)
    if key == ord("q"):
        break
    if key == ord("f"):
        cv2.imshow('result ', img)
    cv2.imshow("Live", img)

cv2.waitKey(0)
