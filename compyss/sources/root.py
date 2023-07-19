
class Image(): # TODO, move to core.py?
    """
    Standard data for an image that can be decoded by compyss.
    """

    def __init__(self):
    
        # list of pure pixel data
        self.pixels = None

        # numpy array holding angles for each pixel
        self.aolp = None

        # numpy array holding fractions of polarized light for each pixel
        self.dolp = None
        
        # stokes vectors
        self.stokes = None


class ImageSource():
    """
    Compass requires an ImageSource type to load images from.
    Inherit from ImageSource to create new sources.
    """

    def get(self) -> Image:
        """
        Return the next image to be analysed.
        """
        pass

