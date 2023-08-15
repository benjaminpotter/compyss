from compyss.sources.image_source import ImageSource
import compyss.decoders.hough

class Compass():
    """
    Parent class for loading and decoding compass data.
    """

    def __init__(self, source: ImageSource = None):
        self.source = source