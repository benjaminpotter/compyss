from compyss.sources.root import ImageSource
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

        import cv2 
        cv2.imshow("image", img.aolp)
        cv2.waitKey(0)

        # use the hough method
        # plan to include support for more methods in the future

        bimg = compyss.decoders.hough.extract_binary(img)
        angle = compyss.decoders.hough.hough_transform(bimg)

        return angle


