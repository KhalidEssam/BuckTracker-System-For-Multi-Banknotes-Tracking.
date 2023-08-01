from operator import contains
from sys import flags
import cv2
import numpy
import pytesseract
import re
from pickle import TRUE
import PIL.Image
pytesseract.pytesseract.tesseract_cmd= 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
myconfig = r"--psm 12  --oem 3"
frame=cv2.imread("m22.png")
gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
# boxes = pytesseract.image_to_data( gray ,config= myconfig)
# for xx,b in enumerate (boxes.splitlines()):
#     if xx!=0:
#         b = b.split()
                
#         if len(b) ==12:
                    
#             x,y,w,h2 = int(float(b[6])),int(float(b[7])),int(float(b[8])),int(float(b[9]))
#             cv2.rectangle( frame ,(x,y),(w+x,h2+y),(0,0,255),1)
            
#             print(b[11])
t= pytesseract.image_to_string(frame,config=myconfig)
print(t)
cv2.imshow('result ', frame)
cv2.waitKey(0)
cv2.destroyAllWindows()