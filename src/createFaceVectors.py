import numpy as np
from os import listdir
from PIL import Image
import sys
import pdb
import glob
import csv
import threading
import time

# temp arrays to store indices
arr1 = []
arr2 = []
arr3 = []
arr4 = []


out1 = open("faces.csv", 'wb')
wr1 = csv.writer(out1, quoting=csv.QUOTE_NONE, escapechar=' ')

out2 = open("nonfaces.csv", 'wb')
wr2 = csv.writer(out2, quoting=csv.QUOTE_NONE, escapechar=' ')



#myfile = open("facevectors.csv", 'wb')
#wr = csv.writer(myfile, quoting=csv.QUOTE_NONE, escapechar=' ')


countPrints = 0
def loadimages(arr, value, wrFile):
	#print("../" + str(dir) + "*.jpg")
	#imagesList = listdir(dir)
	for image in arr:
		img = Image.open(image)
		createVector(value, img, wrFile)
		
		
		


def createVector(value, img, wrFile):
	temp = []

	#print(img)
	arr = np.array(img)

	#make 1-d array
	flat_arr = arr.ravel()

	print(flat_arr)
	#append 
	temp.append(value)
	#for val in flat_arr:
	#	temp.append(val)

	#write record to csv file
	#wrFile.writerow(temp)



def loadTextFile(filePath):
	file = open(filePath, "r").read().splitlines()
	counter = 0
	for f in file:
		if counter < 3308:
			arr1.append(f)
			counter = counter + 1
		elif counter >= 3308 and counter < 6616:
			arr2.append(f)
			counter = counter + 1
		elif counter >= 6616 and counter < 9924:
			arr3.append(f)
			counter = counter + 1
		elif counter >= 9924:
			arr4.append(f)
			counter = counter + 1

	
	spawThreads(arr1, arr2, arr3, arr4)


def spawThreads(a1, a2, a3, a4):
	#loadimages(a1, 1, wr1)
	t1 = threading.Thread(target=loadimages, args=[a1, 1, wr1])
	t2 = threading.Thread(target=loadimages, args=[a2, 1, wr2])
	#t3 = threading.Thread(target=loadimages, args=[a3, 1, wr3])
	#t4 = threading.Thread(target=loadimages, args=[a4, 1, wr4])
	t1.start()
	t2.start()
	#t3.start()
	#opet4.start()

#read and parse command line arguments
if len(sys.argv) > 1:
	#loadimages(sys.argv[1], sys.argv[2])
	loadTextFile(sys.argv[1])
	#wr.close()

else:
		print("usage: python createFaceVectors.py <img folder> <0 or 1>")