from compyss.sources.root import ImageSource, Image

from arena_api.system import system
from arena_api.buffer import BufferFactory

import numpy as np

class ArenaSDK(ImageSource):

    """
        Source for LUCID Vision Cameras.
        
        Configuration options map to camera configuration nodes.
        https://support.thinklucid.com/phoenix-phx050-pq-polarized/#2931
        
        Support for streamable file as well. Configuration options will override streamables.
    
    """

    def __init__(self): ## REMOVE config options
        
        self.device = None
        self.config = {'PixelFormat':'PolarizedStokes_S0_S1_S2_S3_Mono8'}
        self.streamable_file = "res/features.txt"
        self.buffer_count = 25
        
        self.device = self._connect_to_device() # on fail, raise exception
        if self.device is None:
            raise Exception("Failed to connect to camera.")
            
        self._configure_active_device(self.device, self.config, self.streamable_file)
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
        
    def _configure_active_device(self, device, config, streamable_file):
        # apply streamable file
        device.nodemap.read_streamable_node_values_from(streamable_file)
        
        device.tl_stream_nodemap["StreamBufferHandlingMode"].value = "NewestOnly"
        device.tl_stream_nodemap['StreamAutoNegotiatePacketSize'].value = True
        device.tl_stream_nodemap['StreamPacketResendEnable'].value = True
    
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
        
    def get(self):
        
        buffers = self.device.get_buffer(self.buffer_count) # adding extra buffers improves exposure?
        
        buffer = buffers[self.buffer_count-1]
        buffer_copy = BufferFactory.copy(buffer)
        
        self.device.requeue_buffer(buffers)
        
        print("Recieved image with: "
            f'Width = {buffer_copy.width} pxl, '
            f'Height = {buffer_copy.height} pxl, '
            f'Pixel Format = {buffer_copy.pixel_format.name}, '
            f'Bpp = {buffer_copy.bits_per_pixel}')
        
        image = Image()
        
        # PolarizedStokes_S0_S1_S2_S3_Mono8 -> 32 bits, 4 bytes per pixel
        # Reference: https://support.thinklucid.com/knowledgebase/pixel-formats
        
        image.pixels = np.ctypeslib.as_array(buffer_copy.pdata, (buffer_copy.height, buffer_copy.width, buffer_copy.bits_per_pixel // 8))
        
        #image.stokes = np.divide(image.pixels, np.stack((image.pixels[:,:,0],image.pixels[:,:,0],image.pixels[:,:,0],image.pixels[:,:,0]), axis=-1))
        #image.stokes = np.copy(image.pixels) # normalize
        image.stokes = np.clip(image.pixels, 1, 255)
       
        s0 = image.stokes[:,:,0]
        s1 = image.stokes[:,:,1]
        s2 = image.stokes[:,:,2]
        
        # Reference: https://en.wikipedia.org/wiki/Stokes_parameters
        image.aolp = np.mod(0.5 * np.arctan2(s2, s1), np.pi)
        image.dolp = np.sqrt(s1**2 + s2**2) / s0 # S_3 == 0 for all pixels.
   
        return image
        
       
