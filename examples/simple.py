import compyss.core

def main():

    cmps = compyss.core.Compass(cam_sdk=compyss.core.ARENA_SDK)
    angle = cmps.read()

    print(angle)

if __name__ == "__main__":
    main()
