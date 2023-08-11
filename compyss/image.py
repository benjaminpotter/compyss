import numpy as np
import polanalyser as pa

class Image():
    """
    Standard data for an image that can be decoded by compyss.
    """

    def __init__(self, stokes):
        
        # stokes vectors
        self._stokes = stokes
        
        # numpy array holding angles for each pixel
        self._aolp = 0.5 * np.arctan2(self.stokes[..., 2], self.stokes[..., 1]) # [-pi/2, pi/2]

        # numpy array holding fractions of polarized light for each pixel
        self._dolp = pa.cvtStokesToDoLP(self.stokes)  # [0, 1]
        
        
    @classmethod
    def from_pixels(cls, pixels):
        angles = np.deg2rad([0, 45, 90, 135])
        stokes = pa.calcStokes(pa.demosaicing(pixels, pa.COLOR_PolarMono), angles)
        return cls(stokes)

    
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
        Transform stokes vectors from instrument plane to local meridian.
        """
        
        transformed_stokes = np.copy(self.stokes)
        
        lut_cosbeta = np.genfromtxt("res/LUT/cosbeta.csv", delimiter=",")
        lut_sinbeta = np.genfromtxt("res/LUT/sinbeta.csv", delimiter=",")
        
        for x in range(2048):
            for y in range(2048):
                q = transformed_stokes[x][y][1]
                u = transformed_stokes[x][y][2]
                
                transformed_stokes[x][y][1] = q * lut_cosbeta[x][y] + u * lut_sinbeta[x][y]
                transformed_stokes[x][y][2] = -q * lut_sinbeta[x][y] + u * lut_cosbeta[x][y]
                
        return Image(transformed_stokes)