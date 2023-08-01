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
                if c=='M' or c=='L' or c=='P' or c=='F':
                    flag=1
                    c2  +=1
            elif flag==1:
                if c=='B' or c=='F' or c=='E' or c=='H' or c=='J' or c=='K'or c =='D' or c=='C':
                    flag=2
                    c2=2
                    #print('all my lfie stood by mee')
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


pytesseract.pytesseract.tesseract_cmd= 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
myconfig = r"--psm 11  --oem 3"
count = 0 
f=0
#out = cv2.VideoWriter('result.avi', fourcc, fps, (w, h))
fourcc=0
fps=0
w=0
h=0
serialnumber = ""
text_file = open("serial3.txt", "w")
cap = cv2.VideoCapture('m_Trim.mp4')
k= cv2.waitKey(1)
while(cap.isOpened()):
    ret,frame = cap.read()
    if ret==True:
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        #gray = frame

        #thresh, im_bw = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
        #gray = frame
        h,w= gray.shape
        # print ( "Rows" ,h )
        # print ("colums" ,w )
        #g2 = noise_removal(gray)
        #dilated_image = thick_font(gray)
        cropped_image = gray[ 540:640,740:990]
        cv2.imshow('crop',cropped_image)

        boxes = pytesseract.image_to_data( gray ,config= myconfig)
        for xx,b in enumerate (boxes.splitlines()):
            if xx!=0:
                b = b.split()
                
                if len(b) ==12:
                    
                     x,y,w,h2 = int(float(b[6])),int(float(b[7])),int(float(b[8])),int(float(b[9]))
                     cv2.rectangle( gray ,(x,y),(w+x,h2+y),(0,0,255),1)
                     cv2.imshow('result ', gray )
                     print(b[11])
                     cv2.waitKey(1)
                     #digit,letter = countletterandstring(b[11])
                    #  if letter==2 and digit >4 :
                    #     print(b[11])
          
            # cord= countletterandstring(b[0])
            # if cord ==1 :
            #     if f==2:
            #         serialnumber+=b[0]
            #         count+=1
            #         if count == 9 :
            #             text_file.write(serialnumber)
            #             print(serialnumber)
            #             f=0
            #             count=0
            #             serialnumber=''
            #     else:
            #         serialnumber=''
            #         f=0
            #         count=0
            # elif cord== 2 :
            #     if f==0 :
            #         serialnumber+=b[0]
            #         f+=1
            #     elif f==1:
            #         serialnumber+=b[0]
            #         f+=1




           

    else:
        break 
text_file.close()
cap.release()
cv2.destroyAllWindows()
#[0,1,2,3,4,5,6,8,7,9]
#['0','1','2','3','4','5','6','7','8','9']
