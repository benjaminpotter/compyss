from compyss.image import Image

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