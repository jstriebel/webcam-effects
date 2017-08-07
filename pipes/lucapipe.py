from pipes.pipe import Pipe
import numpy as np
import cv2

class LucaPipe(Pipe):
    def pipe(self, data):
        gray = cv2.cvtColor(data, cv2.COLOR_BGR2GRAY)
        
        _, gray = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY)
        #gray = (gray[:,:,] > 128) * 255
        kernel = np.ones((3,3),np.uint8)
        gray = cv2.erode(gray, kernel, iterations = 1)
        gray = cv2.dilate(gray, kernel, iterations = 1)


        return gray

    def __enter__(self):
        return self

    def __exit__(self, exit_type, value, traceback):
        pass
