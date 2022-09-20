from PIL import Image
from collections import Counter


with Image.open("icon.png") as img:
    img.load()

def colour_weight(img):
    width, height = img.size
    print(type(img))

    c = Counter()
    for i in range(0, width):
        for j in range(0, height):
            d = dict()
            d[img.getpixel((i,j))] = 1
            c.update(d)
    print(c)


if __name__ == "__main__":
    main()
