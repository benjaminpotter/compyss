import cv2 as cv

def greyscale(img):
    return cv.cvtColor(img, cv.COLOR_BGR2GRAY)

def gblur(img):
    return cv.GaussianBlur(img, (5, 5), 0)

