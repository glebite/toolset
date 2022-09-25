import sys
from collections import Counter
from PIL import Image
import cv2 as cv
import numpy as np


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


def find_rectangles(image, min_thresh, max_thresh, kernel, iterations):
    """
    find rectangles and then predominant colours in them.
    """
    
    image = cv.imread(image)
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    blur = cv.medianBlur(gray, 5)
    sharpen_kernel = np.array([[-1,-1,-1], [-1,kernel,-1], [-1,-1,-1]])
    sharpen = cv.filter2D(blur, -1, sharpen_kernel)

    # Threshold and morph close
    thresh = cv.threshold(sharpen, min_thresh, max_thresh, cv.THRESH_BINARY_INV)[1]
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (5, 5))
    close = cv.morphologyEx(thresh, cv.MORPH_CLOSE, kernel, iterations=iterations)

    # Find contours and filter using threshold area
    cnts = cv.findContours(close, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if len(cnts) == 2 else cnts[1]

    min_area = 100
    max_area = 182
    image_number = 0
    found = 0
    for c in cnts:
        area = cv.contourArea(c)
        x, y, w, h = cv.boundingRect(c)
        
        # if area > min_area and area < max_area:
        #     print(area, c)
        #     found += 1
        if 10 <= w <= 15 and 10 <= h <= 15:
            found += 1
            cv.rectangle(image, (x, y), (x + w, y + h), (36,255,12), 2)
            image_number += 1
    if found >= 4:
        ROI = image[y:y+h, x:x+w]
        cv.imwrite(f'ROI_{min_thresh}_{max_thresh}_{kernel}_{iterations}.png')
    return found
 

def main():
    for iterations in range(0,5):
        for kernel in range(5,15):
            for min in range(0, 255):
                for max in range(255, 0, -1):
                    val = find_rectangles(sys.argv[1], min, max, kernel, iterations)

    
if __name__ == "__main__":
    main()
