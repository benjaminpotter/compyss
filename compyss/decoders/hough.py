import cv2 as cv
import numpy as np
import math
from compyss.sources.root import Image

"""
From my research, this method was first documented by Lu et al. in their paper DOI:10.1364/OE.23.007248.
See the paper linked above for more information.
"""


def extract_binary(aolp_image: Image, threshold=0.1) -> np.array:
    """
    Extract a binary image by sampling each pixel in an AoLP image. If |pixel - 90*| < threshold,
    mark the pixel as a one in the binary image.
    """

    bin_image = np.empty_like(aolp_image.aolp)
    for y in range(len(aolp_image.aolp)):
        for x in range(len(aolp_image.aolp[y])):
            bin_image[y][x] = 255 if math.fabs(aolp_image.aolp[y][x] - 90) < threshold else 0

    return bin_image
    

def hough_transform(bin_image: np.array) -> float:
    """
    Perform Hough transform on a binary image.
    Return an angle.
    """
    

    return 0.0
     
