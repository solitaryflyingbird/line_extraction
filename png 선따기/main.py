import cv2
import svgwrite
from PIL import Image

def png_to_svg(input_path, output_path, threshold=228):
    # Load the image and convert it to grayscale
    img = cv2.imread(input_path, cv2.IMREAD_UNCHANGED)
    gray = cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY)

    # Threshold the image to create a binary image
    _, binary_img = cv2.threshold(gray, threshold, 255, cv2.THRESH_BINARY)

    # Find contours in the binary image
    contours, _ = cv2.findContours(binary_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Create an SVG file
    dwg = svgwrite.Drawing(output_path, profile='tiny', size=(img.shape[1], img.shape[0]))

    # Add contours as paths to the SVG file
    for contour in contours:
        path_data = 'M'
        for i, point in enumerate(contour):
            path_data += f"{point[0][0]},{point[0][1]}"
            if i < len(contour) - 1:
                path_data += ' L'
        dwg.add(dwg.path(d=path_data, fill='black', stroke='black'))

    # Save the SVG file
    dwg.save()

# Example usage
input_path = "input.png"
output_path = "output.svg"
png_to_svg(input_path, output_path)
