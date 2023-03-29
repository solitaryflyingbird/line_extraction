import cv2
import numpy as np
import os

def process_image(input_image_path):
    # Read the image
    image = cv2.imread(input_image_path)

    # Convert to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Canny edge detection
    edges = cv2.Canny(gray_image, 100, 200)

    # Apply a Gaussian blur to the original image
    smoothed_image = cv2.GaussianBlur(image, (5, 5), 0)

    # Create a mask from the edge map
    mask = cv2.dilate(edges, np.ones((3, 3), np.uint8), iterations=1)

    # Merge the smoothed image with the original image using the mask
    result = cv2.addWeighted(image, 0.7, cv2.bitwise_and(smoothed_image, smoothed_image, mask=mask), 0.3, 0)

    # Save the output image
    output_image_path = os.path.splitext(input_image_path)[0] + "_output" + os.path.splitext(input_image_path)[1]
    cv2.imwrite(output_image_path, result)

# Get a list of files in the current folder
files = os.listdir()

# Find the first image file with '.jpg' or '.png' extension
image_file = None
for file in files:
    if file.lower().endswith(('.jpg', '.png')):
        image_file = file
        break

if image_file:
    # Process the found image file
    process_image(image_file)
else:
    print("No image file with '.jpg' or '.png' extension found in the current folder.")
