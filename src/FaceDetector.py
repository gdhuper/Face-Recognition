#!/usr/bin/env python
# -*- coding: utf-8 -*- 
from __future__ import print_function
from pyspark.mllib.classification import SVMWithSGD, SVMModel
from pyspark.mllib.regression import LabeledPoint
from PIL import Image, ImageDraw, ImageFilter
from images2gif import writeGif as writeGif
from pyspark import SparkContext
from os import listdir
import imageio, sys
import numpy as np
import threading
import time
import cv2
import sys
import os 



# Draws a rectangle around a 250x250 image
def colorRectangle(im, color):
	draw = ImageDraw.Draw(im)
	for i in range(6):
		draw.line((i, 0,i,250), fill=color)
		draw.line((245 + i, 0,245 + i,250), fill=color)
		draw.line((0, i, 250, i), fill=color)
		draw.line((0, 245 + i, 250,245 + i), fill=color)
	del draw
	return im 

def resize(tempImg):
	new_img = tempImg.resize((250,250))
	return new_img

def crop(img):
	width = img.size[0]
	height = img.size[1]
	left = (width - height) / 2
	new_img = img.crop((left,0,width-left,height))
	return new_img

def sharpen(tempImg):
	new_img = tempImg.filter(ImageFilter.SHARPEN)
	return new_img

def startFaceDetection():
	# Spark Context
	sc = SparkContext()
	# Load the model 
	model = SVMModel.load(sc, "model/pythonSVMWithSGDModel")

	# Rectangle color values
	RED = (255, 0, 0)
	GREEN = (0,255,0)

	if (sys.argv) < 1:
		print("Usage: spark-submit FaceDetector.py <seconds>")
	else:
		seconds = float(sys.argv[1])
		# Create capture object, and set frame to be 250x250 pixels
		cap = cv2.VideoCapture(0)
		
		# Begin capturing frames from the camera
		startTime = time.time()

		while True:
			# Capture a single frame
			ret, frame = cap.read()
			if ret:
				# Change the cv image to pillow image
				frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
				image = Image.fromarray(frame)
				image = resize(crop(sharpen(image)))
				imgVector = np.array(image).ravel()
				 # check if the image is a face using the model
				if model.predict(imgVector) == 1:
					colorRectangle(image, GREEN)
				else:
					colorRectangle(image, RED)

				# convert the image back to a cv image
				image = image.convert('RGB')
				frame = np.array(image)
				frame = frame[:, :, ::-1].copy()  

				# Display the image
				cv2.imshow('frame',frame)

				# Not really sure what this does... lol
				# if cv2.waitKey(1) & 0xFF == ord('q'): break
				if cv2.waitKey(33) == ord('a'):
					break
				
				# Record only for the number of seconds specified
				endTime = time.time()
				if (endTime - startTime) >= seconds:
					break
			else:
				break
		# Release the camera and destroy windows showing images
		cap.release()
		cv2.destroyAllWindows()

startFaceDetection()


