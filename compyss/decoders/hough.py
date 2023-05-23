import cv2 as cv

"""
From my research, this method was first documented by Lu et al. in their paper DOI:10.1364/OE.23.007248.
See the paper linked above for more information.
"""

def extract_binary(aolp_image, threshold=0.5):
    """
    Extract a binary image by sampling each pixel in an AoLP image. If |pixel - 90*| < threshold,
    mark the pixel as a one in the binary image.
    """
    pass

def hough_transform(bin_image):
    """
    Perform Hough transform on a binary image.
    Return an angle.
    """
    

    return 0.0
     
