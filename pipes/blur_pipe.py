from pipes.pipe import Pipe
import numpy as np
import cv2

radius = 15

class BlurPipe(Pipe):
    def pipe(self, frame):
        return cv2.GaussianBlur(frame, (radius, radius), 0)
    def __enter__(self):
        return self

    def __exit__(self, exit_type, value, traceback):
        pass
