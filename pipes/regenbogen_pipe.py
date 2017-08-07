from pipes.pipe import Pipe


class RegenbogenPipe(Pipe):
    def pipe(self, data):
        data *= 5
        return data

    def __enter__(self):
        return self

    def __exit__(self, exit_type, value, traceback):
        pass
