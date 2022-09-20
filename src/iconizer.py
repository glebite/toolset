from PIL import Image
import io
import pathlib
from collections import Counter

with Image.open("icon.png") as img:
    img.load()

print(dir(img))
width, height = img.size

c = Counter()
for i in range(0, width):
    for j in range(0, height):
        c.update((img.getpixel((i,j))))

print(c)
