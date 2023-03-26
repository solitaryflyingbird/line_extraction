import cairosvg

input_png = "input.png"
output_svg = "output_image.svg"

# Convert the PNG to SVG
cairosvg.png2svg(url=input_png, write_to=output_svg)