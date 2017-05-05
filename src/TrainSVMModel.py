from pyspark.mllib.classification import SVMWithSGD, SVMModel
from pyspark.mllib.regression import LabeledPoint
from pyspark import SparkContext
import sys

sc = SparkContext()

# Load and parse the data
def parsePoint(line):
	values = [float(x) for x in line.split(' ')]
	return LabeledPoint(values[0], values[1:])

def run(inputFile):
	f = open("TrainingResults.txt", "w")
	data = sc.textFile(inputFile)
	parsedData = data.map(parsePoint)

	# Build the model
	model = SVMWithSGD.train(parsedData, iterations=100)

	# Evaluating the model on training data
	labelsAndPreds = parsedData.map(lambda p: (p.label, model.predict(p.features)))
	trainErr = labelsAndPreds.filter(lambda (v, p): v != p).count() / float(parsedData.count())
	f.write("Training Error = " + str(trainErr))
	f.close()

	# Save and load model
	model.save(sc, "model/pythonSVMWithSGDModel")

if len(sys.argv) > 1:
	run(sys.argv[1])
else:
	print("Usage: path-to-spark-folder/bin/spark-submit TrainSVMModel.py <training-data>")