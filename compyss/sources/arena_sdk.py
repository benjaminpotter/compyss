from compyss.sources.root import ImageSource, Image

from arena_api.system import system
from arena_api.buffer import BufferFactory

import numpy as np

class ArenaSDK(ImageSource):

    """
        Source for LUCID Vision Cameras.
        
        Configuration options map to camera configuration nodes.
        https://support.thinklucid.com/phoenix-phx050-pq-polarized/#2931
    
    """

    def __init__(self, config):
        
        self.device = None
        self.config = config
        self.buffer_count = 3
        
        self.device = self._connect_to_device() # on fail, raise exception
        if self.device is None:
            raise Exception("Failed to connect to camera.")
            
        self._configure_active_device(self.device, config)
        self._start_stream(self.device, self.buffer_count)
     
    def __del__(self):
        if self.device is not None:
            self._stop_stream(self.device)
            
        system.destroy_device()
        
    def _connect_to_device(self):
        device_list = system.create_device()
            
        print(f"Found {len(device_list)} device(s).")
        if not device_list:
            return None
        
        return device_list[0]
        
    def _configure_active_device(self, device, config):
        # grab required nodes
        nodes = device.nodemap.get_node(list(config))
        
        # set nodes
        for opt in config:
            nodes[opt].value = config[opt]
            print(f"Set {opt} to {config[opt]}")
        
    def _start_stream(self, device, buffer_count):
        device.start_stream(buffer_count)
        
    def _stop_stream(self, device):
        device.stop_stream()
        
    def _extract_aolp_dolp(self, image: Image):
        """
        Currently takes ~15s to run on my machine. This needs work.
        """
        for idx, row in np.ndenumerate(image.pixels):
            image.dolp[idx] = np.right_shift(row, 8)
            image.aolp[idx] = np.bitwise_and(row, 0x00FF)

    def get(self):
        
        buffer = self.device.get_buffer()
        buffer_copy = BufferFactory.copy(buffer)
        self.device.requeue_buffer(buffer)
        
        print("Recieved image with: "
            f'Width = {buffer_copy.width} pxl, '
            f'Height = {buffer_copy.height} pxl, '
            f'Pixel Format = {buffer_copy.pixel_format.name}')
        
        image = Image()
        
        image.pixels = np.ctypeslib.as_array(buffer_copy.pdata, (buffer_copy.height, buffer_copy.width))
        
        # TODO parse buffer data into DOLP and AOLP for each pixel
        # PolarizedDolpAolp_Mono8 -> 16 bits, 2 bytes
        #   TOP 8 bits are DOLP (0-255)
        #   BOTTOM 8 bits are AOLP (0-201)
        # Reference: https://support.thinklucid.com/knowledgebase/pixel-formats/#polarizeddolpaolp_mono8
        # Reference: C Code Samples: Polarization, Color DoLP AoLP
            
        image.aolp = np.empty((buffer_copy.height, buffer_copy.width), dtype=int)
        image.dolp = np.empty((buffer_copy.height, buffer_copy.width), dtype=int)

        #self._extract_aolp_dolp(image)
   
        return image
        
       
