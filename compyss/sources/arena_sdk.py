from compyss.sources.root import ImageSource, Image

from arena_api.system import system
from arena_api.buffer import BufferFactory

import numpy as np

class ArenaSDK(ImageSource):

    def __init__(self, config): # TODO implement configuration options
        
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
        nodes = device.nodemap.get_node(['Width', 'Height', 'PixelFormat'])

        # Nodes
        print('Setting Width to its maximum value')
        nodes['Width'].value = nodes['Width'].max

        print('Setting Height to its maximum value')
        height = nodes['Height']
        height.value = height.max

        # Set pixel format to PolarizedDolpAolp_Mono8
        pixel_format_name = 'PolarizedDolpAolp_Mono8'
        print(f'Setting Pixel Format to {pixel_format_name}')
        nodes['PixelFormat'].value = pixel_format_name
        
    def _start_stream(self, device, buffer_count):
        device.start_stream(buffer_count)
        
    def _stop_stream(self, device):
        device.stop_stream()

    def get(self):
        
        buffer = self.device.get_buffer()
        buffer_copy = BufferFactory.copy(buffer)
        self.device.requeue_buffer(buffer)
        
        print(
            f'Width = {buffer_copy.width} pxl, '
            f'Height = {buffer_copy.height} pxl, '
            f'Pixel Format = {buffer_copy.pixel_format.name}')
        
        image = Image()
        image.pixels = np.ctypeslib.as_array(buffer_copy.pdata, (buffer_copy.height, buffer_copy.width))
        
        # TODO parse buffer data into DOLP and AOLP for each pixel
   
        return image
        
       
