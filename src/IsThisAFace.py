from pyspark.mllib.classification import SVMWithSGD, SVMModel
from pyspark.mllib.regression import LabeledPoint
from pyspark import SparkContext
import sys
import numpy as np
from os import listdir
import threading
from PIL import Image

#initializing spark context
sc = SparkContext()
f = open("TestingResults.txt", "w")

def checkImage(dir, numImgs):
	imagesOfFaces = listdir(dir)
	for img in imagesOfFaces[0:int(numImgs)]:
		image = Image.open(dir + img)
		imageArray = np.array(image).ravel()
		model = SVMModel.load(sc, "model/pythonSVMWithSGDModel")
		f.write("Testing "  + dir +  "" + img + ": " + str(model.predict(imageArray)) + "\n")
		print("Testing "  + dir +  "/" + img + ": " + str(model.predict(imageArray)))
	f.close()
	
if len(sys.argv) > 1:
	t1 = threading.Thread(target=checkImage, args=[sys.argv[1], sys.argv[3]])
	t2 = threading.Thread(target=checkImage, args=[sys.argv[2], sys.argv[3]])
	t1.start()
	t2.start()
	
else:
	print("Usage: path-to-spark/bin/spark-submit IsThisAFace.py <path-to-face-image directory> <path-to-non-face-image-directory> <number of images to test>")
