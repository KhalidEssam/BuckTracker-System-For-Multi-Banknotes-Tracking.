import cv2
import pytesseract

# Path to Tesseract executable (change it according to your system)
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'
myconfig = r"--psm 12  --oem 3"

# Path to input image
image_path = '2.png'

# Read the image
image = cv2.imread(image_path)

# Convert image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Perform text extraction using Tesseract
extracted_text = pytesseract.image_to_string(gray_image)

# Get the text regions from Tesseract
boxes = pytesseract.image_to_boxes(image, config=myconfig)

# Draw rectangles around the text regions
for box in boxes.splitlines():
    box = box.split(' ')
    x, y, w, h = int(box[1]), int(box[2]), int(box[3]), int(box[4])
    if w - x >= 5 and h - y >= 5:
        cv2.rectangle(gray_image, (x, image.shape[0] - y), (w, image.shape[0] - h), (0, 255, 0), 2)

# Write "Currency = USD" on the top right corner
text = "Currency = USD"
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 0.7
text_thickness = 2
text_size = cv2.getTextSize(text, font, font_scale, text_thickness)[0]
text_x = gray_image.shape[1] - text_size[0] - 10
text_y = text_size[1] + 10
cv2.putText(gray_image, text, (text_x, text_y), font, font_scale, (0, 255, 0), text_thickness, cv2.LINE_AA)

# Display the image with text regions
cv2.imshow('Text Detection', gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
