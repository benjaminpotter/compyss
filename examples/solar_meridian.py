import compyss.core
from compyss.sources.file import FileSource

"""
Read angle between camera and solar meridian.
"""

def main():
    
    cmps = compyss.core.Compass(source=FileSource("res/aolp_test.png"))
    angle_to_sm = cmps.read_to_sm()

    print(angle_to_sm)

if __name__ == "__main__":
    main()
