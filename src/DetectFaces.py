cfrom pyspark.mllib.classification import SVMWithSGD, SVMModel
from pyspark.mllib.regression import LabeledPoint
from PIL import Image, ImageDraw
from pyspark import SparkContext
from os import listdir
import imageio, sys
import numpy as np

# load the model
sc = SparkContext()

RED = (255, 0, 0)
GREEN = (113,202,88)

# Draws a rectangle around a 250x250 image
def colorRectangle(imagePath, (r,g,b)):
	im = Image.open(imagePath)
	draw = ImageDraw.Draw(im)
	for i in range(6):
		draw.line((i, 0,i,250), fill=(r,g,b))
		draw.line((245 + i, 0,245 + i,250), fill=(r,g,b))
		draw.line((0, i, 250, i), fill=(r,g,b))
		draw.line((0, 245 + i, 250,245 + i), fill=(r,g,b))
	del draw
	return im 

if len(sys.argv) > 2:

	
	model = SVMModel.load(sc, "model/pythonSVMWithSGDModel")

	imgFolderPath = sys.argv[1]
	if imgFolderPath[-1] != "/":
		imgFolderPath += "/"

	destFolder = sys.argv[2]
	if destFolder[-1] != "/":
		destFolder += "/"

	imageList = listdir(imgFolderPath)

	for imageName in imageList:
		im = Image.open(imgFolderPath + imageName)
		imgVector = np.array(im).ravel()
		isFace = False
		if model.predict(imgVector) == 1:
			isFace = True
		if isFace:
			im = colorRectangle(imgFolderPath + imageName, GREEN)
		else:
			im = colorRectangle(imgFolderPath + imageName, RED)
		im.save(destFolder + imageName)
else:
	print("Usage: spark-submit DetectFaces.py <img-src-folder> <img-dest-folder>")