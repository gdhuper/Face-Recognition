import numpy as np
from os import listdir
from PIL import Image
import sys
import pdb
import glob





def loadimages(dir1, dir2, outputFile):
	f = open(outputFile, 'w')

	# Save face images
	imagesOfFaces = listdir(dir1)
	for faceImage in imagesOfFaces[0:99]:
		line = ""
		faceImg = Image.open(dir1 + faceImage)
		imageArray = np.array(faceImg).ravel()
		line += "1"
		for pixelValue in imageArray:
			line += " " + str(pixelValue)
		line += "\n"
		f.write(line)

	# Save non face images
	imagesOfNonFaces = listdir(dir2)
	for nonFaceImage in imagesOfNonFaces[0:99]:
		line = ""
		nonFaceImg = Image.open(dir2 + nonFaceImage)
		nonFaceImageArray = np.array(nonFaceImg).ravel()
		line += "0"
		for pixelValue in nonFaceImageArray:
			line += " " + str(pixelValue)
		line += "\n"
		f.write(line)
	f.close()
	
	
#read and parse command line arguments
if len(sys.argv) > 2:
	loadimages(sys.argv[1], sys.argv[2], sys.argv[3])
else:
        print("usage: python3 SVMTrainingInputMaker.py <pos-img-dir-path> <neg-img-dir-path> <output-file-name.txt>")


