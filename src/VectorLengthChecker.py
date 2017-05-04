import sys

def run(inputFile, numOfVectors, Vlen):
	result = ""
	f = open(inputFile)
	for i in range(numOfVectors):
		length = len(f.readline().split(" "))
		if length < Vlen:
			result += "Line " + str(i) + " is " + str(length) + " long.\n"
	if result == "":
		print("All vectors are the correct size!")
	else:
		print(result)
	

if len(sys.argv) < 3:
	print("Usage: python3 <data-file> <number-of-vectors> <vector-length>")
else:
	run(sys.argv[1],int(sys.argv[2]),int(sys.argv[3]))


	