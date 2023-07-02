import numpy as np
import cv2

import compyss.core
from compyss.sources.arena_sdk import ArenaSDK

"""
ArenaSDK example implementation.

This example uses the ArenaSDK as an ImageSource and the Hough method as a decoder.
It is currently under construction pending the completion of the ArenaSDK source.

"""

def main():
    
    # cmps = compyss.core.Compass(source=ArenaSDK({}))
    # image = cmps.source.get()
    
    # cv2.imwrite("res/arena.png", image.pixels)
    
    image = cv2.imread("res/arena.png")
    cv2.imshow("PolarizedDolpAolp_Mono8", image)
    cv2.waitKey(0)
    
    # angle_to_sm = cmps.read_to_sm()
    # print(angle_to_sm * 180/np.pi)

if __name__ == "__main__":
    main()
