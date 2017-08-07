from pipes.pipe import Pipe
import numpy as np

class NegativPipe(Pipe):
    def pipe(self, img):
        whiteframe = np.ones(img.shape, sdtype=np.uint8) * 255
        newframe = whiteframe - img                               
        return newframe

    def __enter__(self):
        return self

    def __exit__(self, exit_type, value, traceback):
        pass
