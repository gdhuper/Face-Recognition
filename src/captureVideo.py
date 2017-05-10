import numpy as np
import cv2
import sys
import time
from PIL import Image
import os 
from os import listdir
import imageio
from images2gif import writeGif as writeGif
from PIL import ImageFilter
from ProgressBar import printProgressBar


def captureFrames(time_secs):
	startTime = time.time() #start time
	cap = cv2.VideoCapture(0)
	success,image = cap.read() #reading frames from video capture
	count = 0
	success = True
	while success:
	  success,image = cap.read()
	  cv2.imshow('frame',image)
	  if cv2.waitKey(1) & 0xFF == ord('q'):
	  	break
	  imgName = "capturedImages/frame" + str(count).zfill(3) + ".jpg"
	  cv2.imwrite(imgName, image)  # save frame as JPEG file
	  count += 1
	  endTime = time.time() # current time
	  timeLapsed = endTime - startTime # time lapsed
	  if timeLapsed >= float(time_secs):
	  	break
	  else:
	  	continue
	cap.release()
	cv2.destroyAllWindows()

def enhanceImages(dir):
	images = listdir(dir)
	i = 0
	l = len(images) * 3
	printProgressBar(i, l, prefix = ' Preparing frames for SVM:', suffix = 'Done!', length = 50)
	time.sleep(2)
	for img in images:
		imgName = dir + img
		sharpen(imgName)
		i+= 1
		printProgressBar(i, l, prefix = ' Preparing frames for SVM:', suffix = 'Done!', length = 50)
		crop(imgName)
		i+= 1
		printProgressBar(i, l, prefix = ' Preparing frames for SVM:', suffix = 'Done!', length = 50)
		resize(imgName)
		i+= 1
		printProgressBar(i, l, prefix = ' Preparing frames for SVM:', suffix = 'Done!', length = 50)
		


def crop(imagePath):
	img = Image.open(imagePath)
	width = img.size[0]
	height = img.size[1]
	left = (width - height) / 2
	new_img = img.crop((left,0,width-left,height))
	new_img.save(imagePath,'JPEG')

def resize(img):
	tempImg = Image.open(img)
	new_img = tempImg.resize((250,250))
	new_img.save(""+img,'JPEG')

def sharpen(img):
	tempImg = Image.open(img)
	new_img = tempImg.filter(ImageFilter.SHARPEN)
	new_img.save(""+img,'JPEG')

def createGif(dir):
	imageList = listdir(dir)
	images=[]
	i = 0
	l = len(imageList)
	printProgressBar(i, l, prefix = ' Creating GIF image:', suffix = 'Done!', length = 50)
	for img in imageList:
		images.append(imageio.imread(dir+""+img))
		i += 1
		printProgressBar(i, l, prefix = ' Creating GIF image:', suffix = 'Done!', length = 50)
	imageio.mimsave('result.gif', images)
	#writeGif("result.gif",images,duration=0.5,dither=0)

if len(sys.argv) > 1:
	for i in range(3, -1, -1):
		print("  Camera capture starts in: " + str(i), end = '\r')
		time.sleep(1)
	print("                                        ", end = '\r')
	captureFrames(sys.argv[1])
	dir = "capturedImages/"
	enhanceImages(dir)
	print(" Submitting python script to Spark...")
	commandDetectFaces = '../spark/bin/spark-submit DetectFaces.py capturedImages/ capturedImages/'
	os.system(commandDetectFaces)
	createGif(dir)
	print( "Opening GIF image...")
else:
	print("usage: python captureVideo.py <duration-in-seconds>")
