from PIL import Image

def create_black_and_white_image(image_path, output_path, threshold=128):
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
create_black_and_white_image(input_image, output_image)