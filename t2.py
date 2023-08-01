import cv2
import numpy
import pytesseract
import PIL.Image
import time
start_time = time.time()
def countletter(string, ff):
    c2=c1=0
    flag=0
    for c in string:
     
        if c.isalpha():
            
            if ff==0:
                
                if  c=='M':
                    
                    ff=1
                    c2  +=1
            elif ff==1:
                if  c=='B' :
                    ff=2
                    c2=2
                   
                    
            else :
                ff=0
    
    return ff 
def countnum(s,count2):
    
    for c in s:
         
          if c.isdigit():
            count2+=1
            #print(s)
          else :
            count2 = -1
    return count2

class actor:
   def __init__(self, x, y,w,h): 
        self.x = x 
        self.y = y
        self.w=w
        self.h2=h
font = cv2.FONT_HERSHEY_SIMPLEX
strx= "Currency is : USD "
      
pytesseract.pytesseract.tesseract_cmd= 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'
myconfig = r"--psm 12  --oem 3"
#t = pytesseract.image_to_string(PIL.Image.open("2.png"),config=myconfig)
#print(t)
#digit= countletterandstring(t)
img=im2 = cv2.imread("2.jpg")
img = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)
h,w= img.shape
serialnumber = ''
fletter=0
count = 0
f2=f3=0
xl=yl=x=y=h2=0
l=[]
last=''
boxes = pytesseract.image_to_boxes(img,config= myconfig)
red =int(255)  
g= int(0) 
b = int(0)
for b in boxes.splitlines():
    b = b.split(' ')
    
    #print (b[0])
    xl=x
    yl=y
    wl=w
    hl=h2
    x,y,w,h2 = int(b[1]),int(b[2]),int(b[3]),int(b[4])
    if f3==1:
        f3=2
        #serialnumber+=b[0]
        l.append(actor(x,y,w,h2))
        print(serialnumber)
        for i in l:
             cv2.rectangle(img,(int(i.x),h-int(i.y)),(int(i.w),h-int(i.h2)),(0,0,255),1)
             cv2.putText(img,strx,(0,12),font,0.5,(0,0,255),1)

  
    #if x-xl <=19:
    if b[0].isalpha():
        fletter = countletter(last,fletter)
        fletter = countletter(b[0],fletter)
        # if b[0]=='L':
        #     print(fletter)
        #print(b[0]+last)
    if fletter ==2 :
        print(last+b[0])
        if f2==0:
            serialnumber+=last
            serialnumber+=b[0]
            l.append(actor(x,y,w,h2))
            l.append(actor(xl,yl,wl,hl))
            # if x-xl >19 and x-xl<=23:
            #     print(b[0])
            f2=1
        else:
            count = countnum(b[0],count)
        
            if count == -1:
                # print(serialnumber)
                print("not it")
                f2=0
                fletter=0
                count=0
                #print(b[0]+ serialnumber)
                l.clear()
                serialnumber=''
            else:
               # print("INNNNNNNNNNNNNNN")
                l.append(actor(x,y,w,h2))
                serialnumber+=b[0]
                if count ==8:
                    f3=1
   


                    
           # print("finally")
            
        #print("ALL MAAA LIIIFE :"+ last + "    "+ b[0])
  # 

   
    
    last =b[0]
print("--- %s seconds ---" % (time.time() - start_time))
cv2.imshow('result ',img)
cv2.waitKey(0)