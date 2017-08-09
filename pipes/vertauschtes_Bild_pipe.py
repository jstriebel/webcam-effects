from pipes.pipe import Pipe
import numpy as np

class VertauschtesBildPipe(Pipe):
    def pipe(self, img):
        ysize = img.shape[0]
        yhalfsize = ysize / 2
        newframe = np.zeros(img.shape, dtype=np.uint8)
        newframe[:yhalfsize, :, :] = img[yhalfsize:ysize, :, :]
        newframe[yhalfsize:ysize, :, :] = img[:yhalfsize, :, :]
        return newframe

    def __enter__(self):
        return self

    def __exit__(self, exit_type, value, traceback):
        pass
