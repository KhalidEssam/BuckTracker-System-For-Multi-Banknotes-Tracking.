import string
from PIL import Image
import pytesseract
import argparse
import cv2
import os
import pandas as pd

import matplotlib.pyplot as plt
import numpy as np
import re

import time
start_time = time.time()

pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
myconfig = r"--psm 12  --oem 3"
serial=''
source = cv2.VideoCapture("Y-100euro.jpeg")
#text_file = open("data.txt", "w")
mm = 0
#while source.isOpened():
    # ret, image = source.read()
    # if ret == True:
    #     image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # else:
    #     break
    # image = cv2.resize(image, (1280, 558))

    # cv2.imshow("Live", img)
image=cv2.imread("s23.png")
#image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
text = (pytesseract.image_to_string(image)).lower()
print(text)

nonspacetext = text.replace(" ", "")
# print(nonspacetext)
# match = re.findall(r'\D+\d+\D+', text)
# match = re.findall(
#     r'\D{2}\d{8}[a-z]||\D{2}\d{10}||[a-z][a-z]\d{2}\d{6}||[a-z]\d{8}\D{1}', nonspacetext)
flag = 1
match = ''
currency = ''
if re.findall(r'\D{2}\d{8}[a-z]', nonspacetext):
    flag = 100
    match = re.findall(r'\D{2}\d{8}[a-z]', nonspacetext)
    currency = 'USD,'
elif re.findall(r'[a-z]\d{8}[a-z]', nonspacetext) and flag != 100:
    match = re.findall(r'\D{2}\d{8}[a-z]', nonspacetext)
    currency = 'USD,'
elif re.findall(r'\D{2}\d{10}', nonspacetext):
    match = re.findall(r'\D{2}\d{10}', nonspacetext)
   
    currency = 'EURO,'
elif re.findall(r'[a-z][a-z]\d{8}', nonspacetext):
    match = re.findall(r'[a-z][a-z]\d{8}', nonspacetext)
    currency = 'Sterling,'
st = ''
if len(match) > 0:
    st = st.join(match[0])
    serial=st
    print(st)
final = currency + st
final = final.replace(" ", "")
if final != "":
    final += '\n'
    # text_file.write(final)
final = ' '

#key = cv2.waitKey(1)
# if key == ord("q"):
#     break
# if key == ord("f"):
#     cv2.imshow('result ', image)
print(final)
boxes = pytesseract.image_to_boxes(image,config= myconfig)
h,w,_= image.shape
for b in boxes.splitlines():
    b = b.split(' ')
    
    #print (b[0])
   
    x,y,w,h2 = int(b[1]),int(b[2]),int(b[3]),int(b[4])
    for i in st:
        if i ==b[0].lower():
             cv2.rectangle(image,(int(x),h-int(y)),(int(w),h-int(h2)),(0,0,255),1)
        #cv2.putText(img,strx,(80,80),font,1.5,(0,0,255),2)

 
    
   


                    
           # print("finally")
            
        #print("ALL MAAA LIIIFE :"+ last + "    "+ b[0])
  # 

   
    
cv2.imshow("Live", image)
print(currency)
print("--- %s seconds ---" % (time.time() - start_time))
cv2.waitKey(0)
#text_file.close()

# question one
# lets read an image
# image = cv2.imread('50usd.jfif', 0)

# pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
# convert it into text


# if re.findall('^[A-Z]', text):
#     match = re.match('^[A-Z]', text)
#     print(match)
# else:
#     print('ddddddddddddddddddddddddddddddddddddddddddddddd')
# cv2.imshow('image', image)
# cv2.waitKey(0)


# with open('data.txt') as f:
#     hash = {}
#     for line in f:
#         key, value = line.strip().split(',', 1)
#         hash[key] = str(value)

# print(hash['EURO'])