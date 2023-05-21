
ARENA_SDK = None

class Compass():

    def __init__(self, cam_sdk=ARENA_SDK):
        self.cam_sdk = cam_sdk

    def read(self):
        """
        Read angle between compass and local meridian.
        """

        return 0.0

    def read_to_sm(self):
        """
        Read angle between compass and solar meridian.
        """

        return 0.0


