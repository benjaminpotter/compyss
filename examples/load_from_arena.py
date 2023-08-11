import matplotlib.pyplot as plt

import compyss.core
from compyss.sources.arena_sdk import ArenaSDK

"""
ArenaSDK example implementation.

This example uses the ArenaSDK as an ImageSource and builds a figure using matplotlib.

"""

def main():
    
    cmps = compyss.core.Compass(source=ArenaSDK(streamable_file="res/features.txt"))
    image = cmps.source.get()
    
    pos = plt.imshow(image.aolp, cmap="jet")
    plt.colorbar(pos)
    plt.show()
    
if __name__ == "__main__":
    main()
