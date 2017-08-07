from pipes.pipe import Pipe
import numpy as np


class BlackAndWhitePlusSlicing(Pipe):
    def pipe(self, data):
        BlackAndWhitePlusSlicing = data
        BlackAndWhitePlusSlicing1 = BlackAndWhitePlusSlicing[200:400, :, 1:2]
        BlackAndWhitePlusSlicing2 = BlackAndWhitePlusSlicing[500:700, :, 1:2]
        BlackAndWhitePlusSlicingEnd = np.vstack((BlackAndWhitePlusSlicing1,
                                                 BlackAndWhitePlusSlicing2))
        return BlackAndWhitePlusSlicingEnd

    def __enter__(self):
        return self

    def __exit__(self, exit_type, value, traceback):
        pass
