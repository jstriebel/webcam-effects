from pipes.pipe import Pipe
import cv2


class BGRtoGRB_pipe(Pipe):
    def pipe(self, data):
        orig = data.copy()
        blur = data.copy()
        height = orig.shape[0]
        width = orig.shape[1]

        cv2.blur(orig, (15,15), blur);
        
        data[:int(height/2),int(width/2):,1] = blur[int(height/2):,:int(width/2),0]
        data[int(height/2):,:int(width/2),:2] = blur[:int(height/2),int(width/2):,:2]
        data[int(height/2):,int(width/2):,2] = blur[:int(height/2),:int(width/2),1]
        data[:int(height/2),:int(width/2),0] = blur[int(height/2):,int(width/2):,2]
        return data

    def __enter__(self):
        return self

    def __exit__(self, exit_type, value, traceback):
        pass
