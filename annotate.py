import cv2
import pytesseract
import os
import numpy as np


def get_string(img):
    """
    parameter: img = cv2.imread(img_path)
    Takes an img which has already been read by opencv
    Using pytesseract, get the text inside the Image
    """
    # Convert to gray
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Apply dilation and erosion to remove some noise
    kernel = np.ones((1, 1), np.uint8)
    img = cv2.dilate(img, kernel, iterations=1)
    img = cv2.erode(img, kernel, iterations=1)
    # Recognize text with tesseract for python
    result = pytesseract.image_to_string(img, lang='eng', config='--psm6')
    return result