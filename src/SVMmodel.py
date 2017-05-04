from pyspark.mllib.classification import SVMWithSGD, SVMModel
from pyspark.mllib.regression import LabeledPoint

# Load and parse the data
def parsePoint(line):
    values = [float(x) for x in line.split(' ')]
    return LabeledPoint(values[0], values[1:])

def run(inputFile):
    data = sc.textFile(inputFile)
    parsedData = data.map(parsePoint)

    # Build the model
    model = SVMWithSGD.train(parsedData, iterations=100)

    # Evaluating the model on training data
    labelsAndPreds = parsedData.map(lambda p: (p.label, model.predict(p.features)))
    trainErr = labelsAndPreds.filter(lambda (v, p): v != p).count() / float(parsedData.count())
    print("Training Error = " + str(trainErr))

    # Save and load model
    model.save(sc, "target/tmp/pythonSVMWithSGDModel")
    sameModel = SVMModel.load(sc, "target/tmp/pythonSVMWithSGDModel")

if len(sys.argv) > 1:
    run(sys.argv[1])
else:
    print("Usage: python3 TranSVM.py <input-file>")