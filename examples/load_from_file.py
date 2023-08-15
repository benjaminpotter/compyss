import matplotlib.pyplot as plt

from compyss.compass import Compass
from compyss.sources.file import FileSource

"""
Load and display LI image from a PNG file.

PNG example is from the PSNS dataset.
More information: H. Liang and H. Bai, “Polarized Skylight Navigation Simulation (PSNS) Dataset”.
"""

def main():
    
    cmps = Compass(source=FileSource(filepath="res/N9_0.0751_0.0000_0.0000_4_43.50_6.3_498_0.11.png")) # PSNS dataset
    image = cmps.source.get()
    
    image.show()
    
if __name__ == "__main__":
    main()
