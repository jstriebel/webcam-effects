from pipes.pipe import Pipe
import numpy as np

class VertauschtesBildPipe(Pipe):
    def pipe(self, frame):
        ysize = frame.shape[1]
        yhalfsize = ysize / 2
        newframe = np.zeros(frame.shape, dtype=np.uint8)
        newframe[0:yhalfsize, :, :] = frame[240:ysize, :, :]
        newframe[yhalfsize:ysize, :, :] = frame[0:yhalfsize, :, :]
        return newframe

    def __enter__(self):
        return self

    def __exit__(self, exit_type, value, traceback):
        pass
