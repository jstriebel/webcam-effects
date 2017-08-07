from pipes.pipe import Pipe


class BoringPipe(Pipe):
    def pipe(self, data):
        mode = 0
        if mode == 0:
            data[:, 0:426, 2] = data[:, 0:426, 2] + 100
            data[:, 426:852, 1] = data[:, 426:852, 1] + 100
            data[:, 852:1280, 0] = data[:, 852:1280, 0] + 100
        
        elif mode == 1:
            data[355:365, :, 2] = 255
            data[355:365, :, 0:2] = 0
            data[:, 635:645, 2] = 255
            data[:, 635:645, 0:2] = 0
        
        return data

    def __enter__(self):
        return self

    def __exit__(self, exit_type, value, traceback):
        pass
