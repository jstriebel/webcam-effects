from pipes.pipe import Pipe


class BoringPipe(Pipe):
    def pipe(self, data):
        
        shape = data.shape
        b = shape[1]//3
        data[:, b:2*b, 2] = 200
        data[:, 0:b, 0] = 200
        data[:, 2*b:3*b, 1] = 200
         
        return data

    def __enter__(self):
        return self

    def __exit__(self, exit_type, value, traceback):
        pass
