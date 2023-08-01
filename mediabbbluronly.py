import cv2

def apply_median_blur(image_path, output_path, kernel_size):
    # Load the image
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    
    # Apply median blur
    # blurred_image = cv2.medianBlur(image, kernel_size)
    
    # Save the blurred image
    cv2.imwrite(output_path, image)

# Example usage
input_image_path = "2.jpg"
output_image_path = "yy.jpg"
kernel_size = 5

apply_median_blur(input_image_path, output_image_path, kernel_size)
