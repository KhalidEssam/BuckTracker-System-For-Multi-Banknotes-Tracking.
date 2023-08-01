import cv2
img1 = cv2.imread('C:/Users/LENOVO/Pictures/blank-cheque.jpg')

img2 = cv2.imread('C:/Users/LENOVO/Pictures/blank-cheque - Copy (2).jpg')
img1 = cv2.resize(img1, (500, 500))
img2 = cv2.resize(img2, (500, 500))
img3 = img1-img2
cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.imshow('subtracted img', img3)
cv2.waitKey(0)


cv2.destroyAllWindows()

# importing libraries
# import cv2
# import numpy as np

# # Create a VideoCapture object and read from input file
# cap = cv2.VideoCapture('record.flv')

# w = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
# print(w)
# # Check if camera opened successfull
# if (cap.isOpened() == False):
#     print("Error opening video file")
# l = 0
# # Read until video is completed
# while(cap.isOpened()):

#     # Capture frame-by-frame
#     ret, frame = cap.read()
#     if ret == True:

#         # Display the resulting frame

#         cv2.imshow('Frame', frame)

#         if cv2.waitKey(25) & 0xFF == ord('s'):
#             fourc = cv2.VideoWriter_fourcc(*'XVID')
#             out = cv2.VideoWriter('Hi.mp4', fourc, 24.0, (1920, 1080))
#             l = 1
#             # break

#         if l == 1:
#             out.write(frame)

#         # Press Q on keyboard to exit
#         if cv2.waitKey(25) & 0xFF == ord('q'):
#             break

# # Break the loop
#     else:
#         break

# # When everything done, release
# # the video capture object
# cap.release()

# # Closes all the frames
# cv2.destroyAllWindows()
