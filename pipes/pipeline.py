from pipes.pipe import Pipe


class Pipeline(Pipe):
    def __init__(self, pipes):
        self.pipes = pipes

    def pipe(self, data):
        for pipe in self.pipes:
            data = pipe.pipe(data)
        return data

    def __enter__(self):
        for pipe in self.pipes:
            pipe.__enter__()
        return self

    def __exit__(self, exit_type, value, traceback):
        for pipe in self.pipes:
            pipe.__exit__(exit_type, value, traceback)
