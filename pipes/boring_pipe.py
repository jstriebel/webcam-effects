from pipes.pipe import Pipe


class BoringPipe(Pipe):
    def pipe(self, data):
        return data

    def __enter__(self):
        return self

    def __exit__(self, exit_type, value, traceback):
        pass
