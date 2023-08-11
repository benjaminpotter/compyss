import numpy as np
import polanalyser as pa

class Image():
    """
    Standard data for an image that can be decoded by compyss.
    """

    def __init__(self, pixels):
    
        # list of pure pixel data for LI images
        self.pixels = pixels
        
        # stokes vectors
        angles = np.deg2rad([0, 45, 90, 135])
        self._stokes = pa.calcStokes(pa.demosaicing(self.pixels, pa.COLOR_PolarMono), angles)
        
        # numpy array holding angles for each pixel
        self._aolp = 0.5 * np.arctan2(self.stokes[..., 2], self.stokes[..., 1]) # [-pi/2, pi/2]

        # numpy array holding fractions of polarized light for each pixel
        self._dolp = pa.cvtStokesToDoLP(self.stokes)  # [0, 1]
        
    
    @property
    def stokes(self):
        return self._stokes
    
    
    @property
    def aolp(self):
        return self._aolp
        
        
    @property
    def dolp(self):
        return self._dolp
 
        
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