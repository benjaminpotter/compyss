import cv2 as cv
import numpy as np
import math

from compyss.image import Image

"""
From my research, this method was first documented by Lu et al. in their paper DOI:10.1364/OE.23.007248.
See the paper linked above for more information.
"""


def extract_binary(aolp_image: Image, threshold=0.1) -> np.array:
    """
    Extract a binary image by sampling each pixel in an AoLP image. If pixel is within threshold of 90*,
    mark the pixel as a one in the binary image.
    """

    bin_image = np.empty_like(aolp_image.aolp)
    for y in range(len(aolp_image.aolp)):
        for x in range(len(aolp_image.aolp[y])):
            bin_image[y][x] = 0
            if aolp_image.aolp[y][x] < (-np.pi/2 + threshold) or aolp_image.aolp[y][x] > (np.pi/2 - threshold):
                bin_image[y][x] = 255

    return bin_image


def draw_line_overlay(image, line):
    """
    Draw a line on an image and write it to resources directory.

    TODO Move this to a utility module.
    """

    rho = line[0][0]
    theta = line[0][1] 
    a = math.cos(theta)
    b = math.sin(theta)
    x0 = a * rho
    y0 = b * rho
    pt1 = (int(x0 + 1000*(-b)), int(y0 + 1000*(a)))
    pt2 = (int(x0 - 1000*(-b)), int(y0 - 1000*(a)))
    cv.line(image, pt1, pt2, (0,0,255), 3, cv.LINE_AA)

    cv.imwrite("res/line_overlay.png", image)
    

def hough_transform(bin_image: np.array) -> float:
    """
    Perform Hough transform on a binary image.
    Return an angle.
    """

    line_threshold = 300
    lines = cv.HoughLines(bin_image.astype('uint8'), 1, np.pi / 180, line_threshold, None, 0, 0)

    if lines is None:
        return 0.0
    
    """
    https://stackoverflow.com/questions/36021556/get-rho-and-theta-with-miximum-votes-from-cv2-houghlines

    According to above post, the lines list is sorted by votes. I will pick the first line to use as an angle
    since it has the highest number of votes in accumulator space.
    """

    s_meridian = lines[0]

    line_display = cv.cvtColor(np.float32(bin_image), cv.COLOR_GRAY2BGR)
    draw_line_overlay(line_display, s_meridian)
        
    return s_meridian[0][1]
     
