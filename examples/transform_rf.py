import matplotlib.pyplot as plt

from compyss.compass import Compass
from compyss.sources.file import FileSource

"""
Transform reference frame of a sky image.
"""

def main():
    
    cmps = Compass(source=FileSource("res/SkyPattern.png"))
    image = cmps.source.get()

    image.instrument_to_local()

    pos = plt.imshow(image.aolp, cmap="jet")
    plt.colorbar(pos)
    plt.show()

if __name__ == "__main__":
    main()
