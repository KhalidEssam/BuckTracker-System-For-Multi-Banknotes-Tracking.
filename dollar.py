from operator import contains
from sys import flags
import cv2
import numpy
import pytesseract
import re
from pickle import TRUE
import PIL.Image
#c=='M' or c == 'B' or c=='P' or c=='l' or c=='L' or c=='F' or c=='E' or c=='H'
# or c == 'B' or c=='P' or c=='l' or c=='L' or c=='F' or c=='E' or c=='H' or c=='J' or c=='K'or c =='D' or c=='C'
def countletterandstring(string):
    c2=c1=0
    flag=0
    for c in string:
        if c.isdigit():
            c1+=1
            #print(c)
        elif c.isalpha():
            
            if flag==0:
                if c=='M' or c=='L' or c=='P' or c=='F' or c=='W':
                    flag=1
                    c2  +=1
            elif flag==1:
                if c=='B' or c=='F' or c=='E' or c=='H' or c=='J' or c=='K'or c =='D' or c=='C':
                    flag=2
                    c2=2
                    print('all my lfie stood by mee')
            else :
                flag=0
    if c2==2 and c1 > 2 :
        print(string)
    return c2 , c1
def noise_removal(image):
    import numpy as np
    kernel = np.ones((1, 1), np.uint8)
    image = cv2.dilate(image, kernel, iterations=1)
    kernel = np.ones((1, 1), np.uint8)
    image = cv2.erode(image, kernel, iterations=1)
    image = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
    image = cv2.medianBlur(image, 3)
    return (image)


def thick_font(image):
    import numpy as np
    image = cv2.bitwise_not(image)
    kernel = np.ones((2,2),np.uint8)
    image = cv2.dilate(image, kernel, iterations=1)
    image = cv2.bitwise_not(image)
    return (image)

serialnumber = ""
text_file = open("serial3.txt", "w")
pytesseract.pytesseract.tesseract_cmd= 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'
myconfig = r"--psm 11  --oem 3"
text_file = open("serial3.txt", "w")
img = cv2.imread('m1 (2).png')
#h,w= img.shape
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
nn=noise_removal(gray)
h,w= gray.shape
boxes = pytesseract.image_to_boxes( gray ,config= myconfig)
for b in boxes.splitlines():
    b = b.split(' ')
    x,y,w,h2 = int(b[1]),int(b[2]),int(b[3]),int(b[4])
    cv2.rectangle(img,(x,h-y),(w,h-h2),(0,0,255),1)
    digit,letter = countletterandstring(b[0])
    #if letter==2 and digit >4 :
    print(b[0])
# for xx,b in enumerate (boxes.splitlines()):
#     if xx!=0:
#         b = b.split()
                
#         if len(b) ==12:
                    
            # x,y,w,h2 = int(float(b[6])),int(float(b[7])),int(float(b[8])),int(float(b[9]))
    cv2.rectangle( gray ,(x,y),(w+x,h2+y),(0,0,255),1)
    cv2.imshow('result ', gray )
            #print(b[11])
    cv2.waitKey(0)
           
text_file.close()
cv2.imshow('blur',nn)

cv2.waitKey(0)
cv2.destroyAllWindows()
#[0,1,2,3,4,5,6,8,7,9]