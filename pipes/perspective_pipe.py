from pipes.pipe import Pipe
import numpy as np
import cv2

class PerspectivePipe(Pipe):
    def pipe(self, frame):
        transform = np.array([[0.57459, -0.33107, 133],
                              [0.00156, 0.41593, -1], [0, -0.00107, 1]])
        return cv2.warpPerspective(frame, transform,
                                   (int(frame.shape[0] * 1.5),
                                    frame.shape[1]))
    def __enter__(self):
        return self

    def __exit__(self, exit_type, value, traceback):
        pass
