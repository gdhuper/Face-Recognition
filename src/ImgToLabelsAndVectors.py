import numpy as np
from os import listdir
from PIL import Image
import sys
from ProgressBar import printProgressBar

def loadimages(dir1, dir2, outputFile):
	f = open(outputFile, 'w')

	# Save face images
	imagesOfFaces = listdir(dir1)
	count = 0
	l = len(imagesOfFaces)
	print("Creating " + outputFile + " ...")
	printProgressBar(count, l, prefix=" Transforming Face Images:", suffix = 'Complete', decimals = 3,length=100)
	for faceImage in imagesOfFaces:
		line = "1" # The number is 1 because this is a 'positive' example of a face.
		faceImg = Image.open(dir1 + faceImage)
		imageArray = np.array(faceImg).ravel()
		for pixelValue in imageArray:
			line += " " + str(pixelValue)
		line += "\n"
		f.write(line)
		count += 1
		printProgressBar(count, l, prefix=" Transforming Face Images:", suffix = 'Complete', decimals = 3,length=100)

	# Save non face images
	count = 0
	imagesOfNonFaces = listdir(dir2)
	l = len(imagesOfNonFaces)
	printProgressBar(count, l, prefix=" Transforming NonFace Images:", suffix = 'Complete',decimals = 3,length=100)
	for nonFaceImage in imagesOfNonFaces:
		line = "0" # The number is 0 because this is a 'negative' example of a face.
		nonFaceImg = Image.open(dir2 + nonFaceImage)
		nonFaceImageArray = np.array(nonFaceImg).ravel()
		for pixelValue in nonFaceImageArray:
			line += " " + str(pixelValue)
		line += "\n"
		f.write(line)
		count += 1
		printProgressBar(count, l, prefix=" Transforming NonFace Images:", suffix = 'Complete',decimals = 3,length=100)
	f.close()
	
	
#read and parse command line arguments
if len(sys.argv) > 2:
	loadimages(sys.argv[1], sys.argv[2], sys.argv[3])
else:
	print("usage: python3 ImgToLabelAndVectors.py <pos-img-dir-path> <neg-img-dir-path> <output-file-name.txt>")


