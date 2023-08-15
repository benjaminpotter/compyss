import matplotlib.pyplot as plt
import numpy as np

from compyss.compass import Compass
from compyss.sources.file import FileSource

"""
Transform reference frame of a sky image.
"""

def main():
    
    cmps = Compass(source=FileSource(filepath="res/N9_0.0751_0.0000_0.0000_4_43.50_6.3_498_0.11.png"))
    image = cmps.source.get()

    image.instrument_to_local().show()
    

if __name__ == "__main__":
    main()
