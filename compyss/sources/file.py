from compyss.sources.image_source import ImageSource
from compyss.image import Image

import cv2 as cv
import numpy as np

class FileSource(ImageSource):
    """
    Load image from a file source.

    File is a LI image conforming to the standard of PSNS images.
    """
    
    def __init__(self, filepath):
        super().__init__()

        self.filepath = filepath
        self.image: Image = self._load_file()

    def _load_file(self):
        image = cv.imread(self.filepath, 0)
        
        self.is_loaded = False
        if np.any(image):
            self.is_loaded = True

        if not self.is_loaded:
            raise Exception("Cannot load from file " + self.filepath)
            
        return Image.from_pixels(image)

    def get(self):
        return self.image 
