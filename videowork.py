import cv2
import pytesseract
import re

# Path to Tesseract executable (change it according to your system)
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'
myconfig = r"--psm 12 --oem 3"

# Path to input video
video_path = 'm_Trim.mp4'

# Open the video file
video = cv2.VideoCapture(video_path)

# Get the video's frames per second (fps) and frame size
fps = video.get(cv2.CAP_PROP_FPS)
frame_width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Create a VideoWriter object to save the output video
# output_path = 'output_video.mp4'
# output = cv2.VideoWriter(output_path, cv2.VideoWriter_fourcc(*'mp4v'), fps, (frame_width, frame_height))

# Read and process each frame of the video
while True:
    # Read a frame from the video
    ret, frame = video.read()

    # If no frame is read, we have reached the end of the video
    if not ret:
        break

    # Convert frame to grayscale
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Perform text extraction using Tesseract
    extracted_text = pytesseract.image_to_string(frame,config=myconfig)

    # Filter out non-serial number text using regular expressions
    serial_numbers = re.findall(r'[A-Z]{2}\d{8}[A-Z]', extracted_text)

    # Draw rectangles around the serial numbers
    # for serial_number in serial_numbers:
    #     regex_pattern = r'\b' + re.escape(serial_number) + r'\b'
    #     matches = re.finditer(regex_pattern, extracted_text)
    #     for match in matches:
    #         start = match.start()
    #         end = match.end()
    boxes = pytesseract.image_to_boxes(frame,config=myconfig)
    for box in boxes.splitlines():
        box = box.split(' ')
        x, y, w, h = int(box[1]), int(box[2]), int(box[3]), int(box[4])
                # if start < x < end and start < w < end:
        cv2.rectangle(frame, (x, frame_height - y), (w, frame_height - h), (0, 255, 0), 2)

    # Write the processed frame to the output video

    # Display the frame (optional)
    cv2.imshow('Video', frame)

    # Exit the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture and writer objects
video.release()

# Destroy any remaining OpenCV windows
cv2.destroyAllWindows()