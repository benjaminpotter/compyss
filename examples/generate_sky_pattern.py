import numpy as np
import cv2

from compyss.sources.root import Image
from math import cos, sin

"""
Generate a sky pattern from a sun position.
Save the sky pattern to a PNG file.

"""

def main():
    
    image = Image()
    image.aolp = np.empty((2048, 2048))
    
    phi_s, h_s = np.pi/8, np.pi/8
    
    cache_cos_hs = cos(h_s)
    cache_sin_hs = sin(h_s)
    
    for phi_p in np.arange(0, 2 * np.pi, 0.001):
        cache_cos_phip = cos(phi_p)
        cache_sin_phip = sin(phi_p)
        cache_cos = cos(phi_s - phi_p)
        cache_sin = sin(phi_s - phi_p)
        cache_denominator = cache_cos_hs * cache_sin
        for h_p in np.arange(0, np.pi / 2, 0.001):
            aolp = np.mod(np.arctan2( cos(h_p) * cache_sin_hs - sin(h_p) * cache_cos_hs * cache_cos, cache_denominator ), np.pi)
            x = int(cache_cos_phip * cos(h_p) * 1023) + 1024
            y = int(cache_sin_phip * cos(h_p) * 1023) + 1024
            image.aolp[x][y] = aolp
            
    
    hsv = np.empty((2048, 2048, 3), dtype=np.uint8)
    hsv[:,:,0] = image.aolp * 180.0 / np.pi
    hsv[:,:,1] = 255
    hsv[:,:,2] = 255

    cv2.imwrite("res/SkyPattern.png", cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR))

if __name__ == "__main__":
    main()
