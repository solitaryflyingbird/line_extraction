from PIL import Image, ImageSequence
import os

def split_gif(gif_path, output_folder):
    img = Image.open(gif_path)
    frame_index = 0

    for frame in ImageSequence.Iterator(img):
        frame_path = os.path.join(output_folder, f"{frame_index}.png")
        frame.save(frame_path, "PNG")
        frame_index += 1

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.realpath(__file__))

    gif_name = "aaa.gif"
    gif_path = os.path.join(script_dir, gif_name)

    output_folder_name = "extracted_frames"
    output_folder = os.path.join(script_dir, output_folder_name)

    # Create the output folder if it does not exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    split_gif(gif_path, output_folder)
