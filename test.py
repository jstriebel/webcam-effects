import cv2
import numpy as np

def show_webcam(mirror=False):
	cam = cv2.VideoCapture(0)
	while True:
		ret_val, img = cam.read()
				
		if mirror: 
			img = cv2.flip(img, 1)
		print (img.shape)
		peter= np.zeros((480,640,3))
		peter[0:240,:,:]=img[240:480,:,:]
		peter[240:480,:,:]=img[0:240,:,:]
		cv2.imshow('my webcam', peter)

		if cv2.waitKey(1) == 27: 
			break  # esc to quit
	cv2.destroyAllWindows()

def main():
	show_webcam(mirror=True)

if __name__ == '__main__':
	main()
#dtype anpassen 
