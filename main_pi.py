import inspect
import sys
import time

import pipes.pipe
from pipes import *
from writers import VideoServer
from sensors.pisensor import PiSensor

def get_pipes():
    classes = inspect.getmembers(sys.modules[__name__], inspect.isclass)
    return [c[1]() for c in classes
            if pipes.pipe.Pipe in c[1].__bases__
            and c[0] != "Pipeline"]

using_pipes = []

def main():
    pipes = get_pipes()
    using_pipes.append(pipes[0])
    with \
        PiSensor() as cam, \
        Pipeline(using_pipes) as pipeline, \
        VideoServer(port=8080, pipes=pipes, using_pipes=using_pipes) \
            as video_server:
        while True:
            try:
                frame = cam.read()
                frame = pipeline.pipe(frame)
                video_server.write(frame)
                time.sleep(.05)
            except KeyboardInterrupt:
                break

if __name__ == '__main__':
    main()
