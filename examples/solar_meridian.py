import numpy as np

import compyss.core
from compyss.sources.file import FileSource

"""
Read angle between camera and solar meridian.
"""

def main():
    
    cmps = compyss.core.Compass(source=FileSource("res/aolp_test3.png"))
    angle_to_sm = cmps.read_to_sm()

    print(angle_to_sm * 180/np.pi)

if __name__ == "__main__":
    main()
