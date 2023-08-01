import cv2
import numpy
import pytesseract
pytesseract.pytesseract.tesseract_cmd= 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
img = cv2.imread('3.jpeg')
img = cv2.cvtColor(img , cv2.COLOR_BGR2RGB)
# print(pytesseract.image_to_string(img))
#print(pytesseract.image_to_boxes(img))
h,w,_= img.shape
boxes = pytesseract.image_to_boxes(img)
red =int(255)  
g= int(0) 
b = int(0)
for b in boxes.splitlines():
    b = b.split(' ')
    #print (b)
    x,y,w,h2 = int(b[1]),int(b[2]),int(b[3]),int(b[4])
    cv2.rectangle(img,(x,h-y),(w,h-h2),(0,0,255),1)
    cv2.putText(img,b[0],(x,h-h2+50),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,0),1)
   

cv2.imshow('result ',img)
cv2.waitKey(0)