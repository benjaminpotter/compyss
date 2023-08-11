from compyss.sources.image_source import ImageSource
from compyss.image import Image
import cv2 as cv
import numpy as np

class FileSource(ImageSource):
    """
    Load image from a file source.

    Image is expected to be AoLP with hue representing angle with solar principle plane.
    """
    
    @staticmethod
    def _extract_aolp(hsv_image):
        aolp = []
        for row in hsv_image:
            angle_row = []
            for pixel in row:

                # normalize
                norm = pixel[0] / 120.0

                # map to angle range
                mapd = (norm * 2) - 1
                mapd = mapd * -90

                # mask for greyscale
                if pixel[1] < 1:
                    mapd = 0

                angle_row.append( mapd )
            aolp.append(angle_row)

        return aolp


    def __init__(self, filepath):
        super().__init__()

        self.filepath = filepath
        self.raw_image = None
        self.image: Image = None

        self._load_file()

    def _load_file(self):
        self.raw_image = cv.imread(self.filepath, cv.IMREAD_COLOR)
        
        self.is_loaded = False
        if np.any(self.raw_image):
            self.is_loaded = True

        if not self.is_loaded:
            raise Exception("Cannot load from file " + self.filepath)
        
        hsv_image = cv.cvtColor(self.raw_image, cv.COLOR_BGR2HSV)
        aolp_image = FileSource._extract_aolp(hsv_image) 

        self.image = Image()
        self.image.aolp = aolp_image

    def get(self):
        if not self.is_loaded:
            return None

        return self.image 
