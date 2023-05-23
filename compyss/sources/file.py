from compyss.sources.root import ImageSource, Image
import cv2 as cv
import numpy as np

class FileSource(ImageSource):
    """
    Load image from a file source.
    """

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
        
        self.image = Image()
        
        # TODO update using image encoding
        self.image.aolp = self.raw_image

    def get(self):
        if not self.is_loaded:
            return None

        return self.image 
