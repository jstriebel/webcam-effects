import cv2
import io
import time
import picamera
import numpy as np

from sensors.sensor import Sensor


class PiSensor(Sensor):
    def __enter__(self):
        self.camera = picamera.PiCamera()
        self.camera.resolution = (640, 480)
        self.camera.start_preview()
        self.ready = True
        return self

    def __exit__(self, exit_type, value, traceback):
        self.ready = False
        self.camera.stop_preview()

    def read(self):
        if self.ready:
            stream = io.BytesIO()
            self.camera.capture(stream, format="jpeg")
            data = np.fromstring(stream.getvalue(), dtype=np.uint8)
            return cv2.imdecode(data, 1)
        else:
            return None
