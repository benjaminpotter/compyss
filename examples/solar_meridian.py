import compyss.core

"""
Read angle between camera and solar meridian.
"""

def main():
    
    cmps = compyss.core.Compass(cam_sdk=compyss.core.ARENA_SDK)
    angle_to_sm = cmps.read_to_sm()

    print(angle_to_sm)

if __name__ == "__main__":
    main()
