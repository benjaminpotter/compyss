import matplotlib.pyplot as plt
import numpy as np

from compyss.compass import Compass
from compyss.sources.arena_sdk import ArenaSDK
from compyss.decoders.hough import extract_binary, hough_transform

"""
ArenaSDK example implementation.

This example uses the ArenaSDK as an ImageSource and builds a figure using matplotlib.

"""

def main():
    
    cmps = Compass(source=ArenaSDK(streamable_file="res/arena/features.txt"))
    image = cmps.source.get().instrument_to_local()
    
    # apply Hough transform
    bin_image = extract_binary(image)
    print(hough_transform(bin_image) * 180 / np.pi)
    
    image.show()
    
    
if __name__ == "__main__":
    main()
