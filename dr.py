import requests

# OCR.space API endpoint
api_url = 'https://api.ocr.space/parse/image'

# Path to input image
image_path = '2.jpg'

# OCR.space API parameters
payload = {
    'apikey': 'your_api_key',  # Replace with your OCR.space API key
    'isOverlayRequired': False,
    'file': (image_path, open(image_path, 'rb')),
}

# Send the API request
response = requests.post(api_url, files=payload)

# Get the extracted text from the response
extracted_text = response.json()['ParsedResults'][0]['ParsedText']

# Print the extracted text
print(extracted_text)
