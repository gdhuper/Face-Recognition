import numpy as np
import cv2
import sys
import time
from PIL import Image
import os 
from os import listdir
import imageio
from images2gif import writeGif as writeGif






def captureFrames(time_secs):
	startTime = time.time() #start time

	cap = cv2.VideoCapture(0)

	success,image = cap.read() #reading frames from video capture

	count = 0
	success = True

	while success:
	  success,image = cap.read()
	  imgName = "capturedImages/frame" + str(count) + ".jpg"
	  cv2.imwrite("capturedImages/frame%d.jpg" % count, image)  # save frame as JPEG file
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

def createGif(dir):
	print("Creating gif file ....")
	imageList = listdir(dir)
	images=[]
	for img in imageList:
		print(dir+"s"+img)
		images.append(imageio.imread(dir+img))
	imageio.mimsave('result.gif', images)
	#writeGif("result.gif",images,duration=0.5,dither=0)



if len(sys.argv) > 1:
	print("Camera starts in 3secs ...")
	time.sleep(3)
	captureFrames(sys.argv[1])
	dir = "capturedImages/"
	commandDetectFaces = '../spark/bin/spark-submit DetectFaces.py capturedImages/ capturedImages/'
	os.system(commandDetectFaces)

	createGif(dir)



else:
	print("usage: python captureVideo.py <duration-in-seconds>")
