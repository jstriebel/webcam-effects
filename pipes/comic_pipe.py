from pipes.pipe import Pipe


class ComicPipe(Pipe):
    def pipe(self, data):
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        blur = cv2.medianBlur(gray, 7)
        ret = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
                                    cv2.THRESH_BINARY, blockSize=9, C=2)
        ret = cv2.cvtColor(ret, cv2.COLOR_GRAY2RGB)
        ret = cv2.bitwise_and(img, ret)
        return ret

    def __enter__(self):
        return self

    def __exit__(self, exit_type, value, traceback):
        pass
