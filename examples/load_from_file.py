import matplotlib.pyplot as plt

from compyss.compass import Compass
from compyss.sources.file import FileSource

"""
ArenaSDK example implementation.

This example uses the ArenaSDK as an ImageSource and builds a figure using matplotlib.

"""

def main():
    
    cmps = Compass(source=FileSource(filepath="res/N9_0.0751_0.0000_0.0000_4_43.50_6.3_498_0.11.png")) # PSNS dataset
    image = cmps.source.get()
    
    pos = plt.imshow(image.aolp, cmap="jet")
    plt.colorbar(pos)
    plt.show()
    
if __name__ == "__main__":
    main()
