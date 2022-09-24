import sys
from collections import Counter
from PIL import Image
import cv2 as cv
import numpy


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


def find_rectangles(image):
    """
    find rectangles and then predominant colours in them.
    """
    img = cv.cvtColor(numpy.array(image), cv.COLOR_RGB2BGR)
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    Blur = cv.GaussianBlur(gray, (5,5), 1)
    Canny = cv.Canny(Blur, 20, 50)
    contours = cv.findContours(Canny,cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)[0]
    cntrRect = []
    for i in contours:
        epsilon = 0.05*cv.arcLength(i,True)
        approx = cv.approxPolyDP(i,epsilon,True)
        if len(approx) == 4:
            cv.drawContours(img,cntrRect,-1,(0,255,0),2)
            cv.imshow('Roi Rect ONLY',img)
            cntrRect.append(approx)

    cv.waitKey(0)
    cv.destroyAllWindows()
    print(contours)


def main():
    with Image.open(sys.argv[1]) as img:
        img.load()
    find_rectangles(img)

    
if __name__ == "__main__":
    main()
