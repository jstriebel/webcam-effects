from pipes.pipe import Pipe
import numpy as np
from math import sin, pi

# Legt einen Regenbogen-Filter über das Bild
# Von Luca Schimweg (@lucaschimweg)

class RainbowPipe(Pipe):
    def __init__(self):
        self.initialized = False

    def getSinVal(self, x, offset):
        return (sin((((x - offset) * pi)
                / (self.width / 2))) + 1) / 2

    def init_pipe(self, data):
        self.initialized = True
        self.resolution = data.shape
        self.width = data.shape[1]
        self.vals_0 = np.array([[self.getSinVal(x, 0) 
                                for x in range(self.width)]])
        self.vals_1 = np.array([[self.getSinVal(x, self.width / 3) 
                                for x in range(self.width)]])
        self.vals_2 = np.array([[self.getSinVal(x, (self.width / 3) * 2) 
                                for x in range(self.width)]])

    def pipe(self, data):
        if not self.initialized:
            self.init_pipe(data)
        data[:, :, 0] = data[:, :, 0] * self.vals_0
        data[:, :, 1] = data[:, :, 1] * self.vals_1
        data[:, :, 2] = data[:, :, 2] * self.vals_2
        return data

    def __enter__(self):
        return self

    def __exit__(self, exit_type, value, traceback):
        pass
