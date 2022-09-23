from PIL import Image
from collections import Counter


with Image.open("Green.png") as img:
    img.load()

def colour_histogram(img):
    """
    """
    width, height = img.size

    histogram = Counter()
    for width_ptr in range(0, width):
        for height_ptr in range(0, height):
            pixel_value = dict()
            pixel_value[img.getpixel((width_ptr, height_ptr))] = 1
            histogram.update(pixel_value)
    return histogram


def find_rectangles(img):
    """
    find rectangles and then predominant colours in them.
    """


def main():
    with Image.open("Green.png") as img:
        img.load()
    histo = colour_histogram(img)
    print(histo)

    
if __name__ == "__main__":
    main()
