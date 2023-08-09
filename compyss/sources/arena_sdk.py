from compyss.sources.root import ImageSource, Image

from arena_api.system import system
from arena_api.buffer import BufferFactory

import numpy as np
import polanalyser as pa

class ArenaSDK(ImageSource):

    """
        Source for LUCID Vision Cameras.
        
        Configuration options are loaded from a "streamable" file. This file can be generated using ArenaView GUI software.
        More information: https://support.thinklucid.com/documentation/configuring-the-camera-and-host-system/user-sets-streamables-and-file-access/streamables/
        TODO: Camera supports saving common streamable files to on-board storage.
        
        Loads a light intensity image from the camera using the Mono8 pixel format. This image contains light intensity for 0, 90, 45, 135 angles.
        The Stokes vector is then constructed for each pixel. From the Stokes vector, AoLP and DoLP are computed.
        More information: https://support.thinklucid.com/knowledgebase/pixel-formats/#mono8
        TODO: Eliminate dependency on Polanalyser.
        
        TODO: Fix exposure settings to improve execution time.
    
    """

    def __init__(self, streamable_file):
        
        self.device = None
        self.pixel_format = 'Mono8'
        self.streamable_file = streamable_file
        self.buffer_count = 25
        
        self.device = self._connect_to_device() # on fail, raise exception
        if self.device is None:
            raise Exception("Failed to connect to camera.")
            
        self._configure_active_device()
        self._start_stream()
     
    def __del__(self):
        if self.device is not None:
            self._stop_stream()
            
        system.destroy_device()
        
    def _connect_to_device(self):
        device_list = system.create_device()
            
        print(f"Found {len(device_list)} device(s).")
        if not device_list:
            return None
        
        return device_list[0]
        
    def _configure_active_device(self):
        # apply streamable file
        self.device.nodemap.read_streamable_node_values_from(self.streamable_file)
        
        self.device.tl_stream_nodemap["StreamBufferHandlingMode"].value = "NewestOnly"
        self.device.tl_stream_nodemap['StreamAutoNegotiatePacketSize'].value = True
        self.device.tl_stream_nodemap['StreamPacketResendEnable'].value = True
    
        self.device.nodemap["PixelFormat"].value = self.pixel_format
        
    def _start_stream(self):
        self.device.start_stream(self.buffer_count)
        
    def _stop_stream(self):
        self.device.stop_stream()
        
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
        image.pixels = np.ctypeslib.as_array(buffer_copy.pdata, (buffer_copy.height, buffer_copy.width))
        
        # ensure each pixel is atleast 0000 0001 to prevent divide by zero later
        np.clip(image.pixels, 1, 255, image.pixels) 
        
        # demosaic
        intensity_imgs = pa.demosaicing(image.pixels, pa.COLOR_PolarMono)
        
        # generate stokes
        angles = np.deg2rad([0, 45, 90, 135])
        image.stokes = pa.calcStokes(intensity_imgs, angles)
        
        # generate dolp 
        image.dolp = pa.cvtStokesToDoLP(image.stokes)  # [0, 1]
        
        # convert to aolp
        image.aolp = 0.5 * np.arctan2(image.stokes[..., 2], image.stokes[..., 1]) # [-pi/2, pi/2]
   
        return image
        
       
