import numpy as np
import cv2

import compyss.core
from compyss.sources.arena_sdk import ArenaSDK

"""
ArenaSDK example implementation.

This example uses the ArenaSDK as an ImageSource and converts it to HSV displayable format.
It is currently under construction pending the completion of the ArenaSDK source.

"""

import matplotlib.pyplot as plt

def main():
    
    cmps = compyss.core.Compass(source=ArenaSDK())
    image = cmps.source.get()
    
    hsv = np.empty((2048, 2048, 3), dtype=np.uint8)
    hsv[:,:,0] = image.aolp * 180.0 / np.pi
    hsv[:,:,1] = 255 # image.dolp * 255
    hsv[:,:,2] = 255
    
    cv2.imwrite("PolarizedStokes_S0_Mono8.png", image.stokes[:, :, 0])
    cv2.imwrite("PolarizedStokes_S1_Mono8.png", image.stokes[:, :, 1])
    cv2.imwrite("PolarizedStokes_S2_Mono8.png", image.stokes[:, :, 2])
    cv2.imwrite("PolarizedStokes_S3_Mono8.png", image.stokes[:, :, 3])
    cv2.imwrite("AoLP_HSV.png", cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR))

if __name__ == "__main__":
    main()
