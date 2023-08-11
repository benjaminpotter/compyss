from compyss.sources.image_source import ImageSource
import compyss.decoders.hough

class Compass():

    def __init__(self, source: ImageSource = None):
        self.source = source

    def read(self):
        """
        Read angle between compass and local meridian.
        """

        return 0.0

    def read_to_sm(self):
        """
        Read angle between compass and solar meridian.
        """

        img = self.source.get()

        # use the hough method
        # plan to include support for more methods in the future

        bimg = compyss.decoders.hough.extract_binary(img)
        angle = compyss.decoders.hough.hough_transform(bimg)

        return angle