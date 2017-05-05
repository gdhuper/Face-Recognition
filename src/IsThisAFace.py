from pyspark.mllib.classification import SVMWithSGD, SVMModel
from pyspark.mllib.regression import LabeledPoint
from pyspark import SparkContext
import sys
import numpy as np
from os import listdir
from PIL import Image
sc = SparkContext()
if len(sys.argv) > 1:
	image = Image.open(sys.argv[1])
	imageArray = np.array(image).ravel()
	model = SVMModel.load(sc, "model/pythonSVMWithSGDModel")
	print(model.predict(imageArray))
else:
	print("Usage: path-to-spark/bin/spark-submit IsThisAFace.py <path-to-image>")




# # Load and parse the data
# def parsePoint(line):
# 	values = [float(x) for x in line.split(' ')]
# 	return LabeledPoint(values[0], values[1:])

# def run(inputFile):
# 	f = open("TestingResults.txt", "w")

# 	data = sc.textFile(inputFile)
# 	parsedData = data.map(parsePoint)

# 	# Load the model
# 	model = SVMModel.load(sc, "model/pythonSVMWithSGDModel")

# 	# Evaluating the model on training data
# 	labelsAndPreds = parsedData.map(lambda p: (p.label, model.predict(p.features)))
# 	testingErr = labelsAndPreds.filter(lambda (v, p): v != p).count() / float(parsedData.count())
# 	f.write("Testing Error = " + str(testingErr))
# 	f.close()
	

