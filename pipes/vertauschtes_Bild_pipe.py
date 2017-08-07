from pipes.pipe import Pipe
import numpy as np

class VertauschtesBildPipe(Pipe):
    def pipe(self, frame):
        newframe= np.zeros((480,640,3),dtype= np.uint8)
        newframe[0:240,:,:]= frame[240:480,:,:]
        newframe[240:480,:,:] =frame[0:240,:,:]
        return newframe

    def __enter__(self):
        return self

    def __exit__(self, exit_type, value, traceback):
        pass
