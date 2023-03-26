from PIL import Image
import os

def create_black_and_white_image(image_path, output_path, threshold=256):
    # Load the image
    img = Image.open(image_path).convert("L")

    # Create a new image with the same dimensions
    new_img = Image.new("RGBA", img.size, (0, 0, 0, 0))

    # Iterate through the pixels
    for x in range(img.width):
        for y in range(img.height):
            # Get the pixel value
            value = img.getpixel((x, y))

            # Check if the value is closer to black than the threshold
            if value < threshold:
                # Calculate the transparency of the black pixel
                alpha = int((1 - (value / 255)) * 255)

                # Set the pixel in the new image
                new_img.putpixel((x, y), (0, 0, 0, alpha))

    # Save the new image
    new_img.save(output_path)

# Example usage
input_image = "input.png"
output_image = "output.png"

script_dir = os.path.dirname(os.path.realpath(__file__))
input_image_path = os.path.join(script_dir, input_image)
output_image_path = os.path.join(script_dir, output_image)
create_black_and_white_image(input_image_path, output_image_path , 256)