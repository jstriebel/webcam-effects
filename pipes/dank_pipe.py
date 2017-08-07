from pipes.pipe import Pipe
import numpy as np
import cv2

class DankPipe(Pipe):
    def pipe(self, data):
        
        data = cv2.blur(data, (8, 8))
        
        result = np.ndarray(data.shape)
        
        # define colors
        blue = [255, 0, 0]
        green = [0, 255, 0]
        red = [0, 0, 255]
        
        # replace blue-ish pixels with green
        result[np.logical_and(data[:, :, 0] > data[:, :, 1] + 10,
                              data[:, :, 0] > data[:, :, 2] + 10)] = green
        
        # replace green-ish pixels with red
        result[np.logical_and(data[:, :, 1] > data[:, :, 0] + 10,
                              data[:, :, 1] > data[:, :, 2] + 10)] = red
        
        # replace red-ish pixels with blue
        result[np.logical_and(data[:, :, 2] > data[:, :, 1] + 10,
                              data[:, :, 2] > data[:, :, 0] + 10)] = blue
        
        return result

    def __enter__(self):
        return self

    def __exit__(self, exit_type, value, traceback):
        pass
