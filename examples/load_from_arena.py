import numpy as np
import cv2

import compyss.core
from compyss.sources.arena_sdk import ArenaSDK

"""
ArenaSDK example implementation.

This example uses the ArenaSDK as an ImageSource and the Hough method as a decoder.
It is currently under construction pending the completion of the ArenaSDK source.

"""

import matplotlib.pyplot as plt

def main():
    
    cmps = compyss.core.Compass(source=ArenaSDK({'Width':2048, 'Height':2048, 'PixelFormat':'PolarizedAolp_Mono8'}))
    image = cmps.source.get()
    
    cv2.imshow("PolarizedAolp_Mono8", image.pixels)
    cv2.waitKey(0)

if __name__ == "__main__":
    main()
