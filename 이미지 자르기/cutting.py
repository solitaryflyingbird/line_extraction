import os
from PIL import Image

def crop_image(image_path, output_folder, crop_height):
    img = Image.open(image_path)
    width, height = img.size

    for i in range(0, height, crop_height):
        cropped_img = img.crop((0, i, width, i + crop_height))
        cropped_img.save(f"{output_folder}/cropped_{i}.png")

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.realpath(__file__))

    image_name = "image.png"
    image_path = os.path.join(script_dir, image_name)

    output_folder = script_dir
    crop_height = 280

    crop_image(image_path, output_folder, crop_height)
