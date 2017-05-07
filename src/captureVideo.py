import numpy as np
import cv2
import sys
import time
from PIL import Image




def captureFrames(time_secs):
	startTime = time.time() #start time

	cap = cv2.VideoCapture(0)

	success,image = cap.read() #reading frames from video capture

	count = 0
	success = True

	while success:
	  success,image = cap.read()
	  imgName = "frame" + str(count) + ".jpg"
	  cv2.imwrite("frame%d.jpg" % count, image)  # save frame as JPEG file
	  resize(imgName)
	  count += 1

	  endTime = time.time() # current time

	  timeLapsed = endTime - startTime # time lapsed
	  if timeLapsed >= float(time_secs):
	  	break
	  else:
	  	continue


	cap.release()
	cv2.destroyAllWindows()

def resize(img):
	tempImg = Image.open(img)
	new_img = tempImg.resize((250,250))
	new_img.save(""+img,'JPEG')


	im = cv2.imread(img)
	height = np.size(im, 0)
	width = np.size(im, 1)

	print(height, width)



if len(sys.argv) > 1:
	print("Camera starts in 3secs ...")
	time.sleep(3)
	captureFrames(sys.argv[1])
else:
	print("usage: python captureVideo.py <duration-in-seconds>")
