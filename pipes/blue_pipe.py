from pipes.pipe import Pipe


class BoringPipe(Pipe):
    def pipe(self, data):
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        np.array([110, 50, 50])
        np.array([130, 255, 255])
        cv2.inRange(hsv, lo, hi)
        cv2.bitwise_and(img, img, mask=mask)
        return res

    def __enter__(self):
        return self

    def __exit__(self, exit_type, value, traceback):
        pass
