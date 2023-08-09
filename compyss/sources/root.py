
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
        
    def instrument_to_local(self):
        """
        Transform image reference frame from instrument plane to local meridian.
        """
        
        # transformed_image = deepcopy(image)
        
        # lut_cosbeta = np.genfromtxt("res/LUT/cosbeta.csv", delimiter=",")
        # lut_sinbeta = np.genfromtxt("res/LUT/sinbeta.csv", delimiter=",")
        
        # for x in range(2048):
            # for y in range(2048):
                # q = transformed_image.stokes[x][y][1]
                # u = transformed_image.stokes[x][y][2]
                
                # transformed_image.stokes[x][y][1] = q * lut_cosbeta[x][y] + u * lut_sinbeta[x][y]
                # transformed_image.stokes[x][y][2] = -q * lut_sinbeta[x][y] + u * lut_cosbeta[x][y]
                
        raise NotImplementedError


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

