import numpy as np
from os import listdir
from PIL import Image
import sys
import threading 
from ProgressBar import printProgressBar

def loadimages(dir1, dir2, outputFile, numImgs):
	outFile1 = ""
	outFile2 = ""
	if outputFile.find(".txt") == -1:		
		f = open("Training"+ "_" + numImgs + "_Imgs_" + outputFile +".txt", 'w') #training data records (70% of total images)
		outFile1 = "Training"+ "_" + numImgs + "_Imgs_" + outputFile +".txt" #setting name of output file
		f1 = open("Testing"+ "_" + numImgs + "_Imgs_" + outputFile +".txt", 'w') # testing data records  (30 % of totla images)
		outFile2 = "Testing"+ "_" + numImgs + "_Imgs_" + outputFile +".txt"
	else:
		f = open("Training_" + numImgs + "_Imgs_" + outputFile, 'w') #training data records (70% of total images)
		outFile1 = "Training_" + numImgs + "_Imgs_" + outputFile
		f1 = open("Testing_" + numImgs + "_Imgs_" + outputFile, 'w') # testing data records  (30 % of totla images)
		outFile2 = "Testing_" + numImgs + "_Imgs_" + outputFile

	# Save face images
	imagesOfFaces = listdir(dir1)
	imagesOfNonFaces = listdir(dir2)

	lFace = len(imagesOfFaces)
	trainingFaceImgs = int((float(70) /float(100)) * float(numImgs))
	testingFaceImgs = int(numImgs) - trainingFaceImgs

	lNonFace = len(imagesOfNonFaces)
	trainingNonFaceImgs = int((float(70) /float(100)) * float(numImgs))
	testingNonFaceImgs = int(numImgs) - trainingNonFaceImgs
	
	#t1 writes 70% training data from face images and t2 writes 30% testing data for face images
	t1 = threading.Thread(target=writeRecords, args=[dir1, 0, int(trainingFaceImgs), "Training face images",f, 1])
	t2 = threading.Thread(target=writeRecords, args=[dir1, int(trainingFaceImgs)+1, int(trainingFaceImgs) + int(testingFaceImgs),"Testing face images", f1, 1])

	t1.start()
	t2.start()

	t3 = threading.Thread(target=writeRecords, args=[dir2, 0, trainingNonFaceImgs, "Training non face images", f, 0])
	t4 = threading.Thread(target=writeRecords, args=[dir2, trainingNonFaceImgs+1, trainingNonFaceImgs +testingNonFaceImgs, "Testing Nonface images",f1, 0])

	#block thread t3 and t4 until t1 and t2 are finished 
	t1.join()
	t2.join()

	t3.start()
	t4.start()





def writeRecords(dir, startIdx, endIdx, message, outputFile, label):
	imagesOfFaces = listdir(dir)
	#print("Creating " + outputFile + " ...")
	printProgressBar(startIdx, endIdx, prefix= " " + message, suffix = 'Complete', decimals = 3,length=100)
	for faceImage in imagesOfFaces[startIdx:endIdx]:
		line = str(label) # The number is 1 because this is a 'positive' example of a face.
		faceImg = Image.open(dir + faceImage)
		imageArray = np.array(faceImg).ravel()
		for pixelValue in imageArray:
			line += " " + str(pixelValue)
		line += "\n"
		outputFile.write(line)
		startIdx += 1
		printProgressBar(startIdx, endIdx, prefix=" " + message, suffix = 'Complete', decimals = 3,length=100)



	
#read and parse command line arguments
if len(sys.argv) > 3:
	loadimages(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
else:
	print("usage: python3 ImgToLabelAndVectors.py <pos-img-dir-path> <neg-img-dir-path> <output-file-name.txt> <num-of-images-to-test>")


