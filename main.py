import inspect
import sys

import pipes.pipe
from pipes import *
from sensors import Webcam
from writers import VideoServer


def get_pipes():
    classes = inspect.getmembers(sys.modules[__name__], inspect.isclass)
    return [c[1]() for c in classes
            if pipes.pipe.Pipe in c[1].__bases__
            and c[0] != "Pipeline"]


def main():
    pipes = get_pipes()
    with \
        Webcam() as cam, \
        Pipeline(pipes) as pipeline, \
        VideoServer(port=8080) as video_server:
        while True:
            try:
                frame = cam.read()
                frame = pipeline.pipe(frame)
                video_server.write(frame)
            except KeyboardInterrupt:
                break


if __name__ == '__main__':
    main()
