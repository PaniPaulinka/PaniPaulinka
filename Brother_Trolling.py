from PIL import Image
import numpy as np

im = Image.open("engi_tf2.png", "r")

im = im.convert("L")
im = im.resize((900, 400))

char_map = "@%#*+=-:. "

ascii_image = ""
pixels = np.array(im)
for row in pixels:
    for pixel in row:
        ascii_image += char_map[pixel // 50]
    ascii_image += "\n"

print(ascii_image)

with open("ya_ugly.txt", "w") as text_file:
    text_file.write(ascii_image)```
