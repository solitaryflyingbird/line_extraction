import os
from PIL import Image

def merge_images(image_folder, output_image_path):
    image_files = [f for f in os.listdir(image_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]
    image_files = sorted(image_files, key=lambda x: int(os.path.splitext(x)[0]))
    images = [Image.open(os.path.join(image_folder, image_file)) for image_file in image_files]

    total_height = sum(img.height for img in images)
    max_width = max(img.width for img in images)

    merged_image = Image.new("RGBA", (max_width, total_height))

    y_offset = 0
    for img in images:
        merged_image.paste(img, (0, y_offset))
        y_offset += img.height

    merged_image.save(output_image_path)


if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.realpath(__file__))

    image_folder = os.path.join(script_dir, "number_image")
    output_image_path = os.path.join(script_dir, "merged_image.png")

    merge_images(image_folder, output_image_path)
