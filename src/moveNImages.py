from os import listdir, remove
from shutil import move
import sys

# Make sure that there are at least 2 arguments
if len(sys.argv) < 4:
	print("Usage: moveNFiles.py <src-folder> <number> <dest-folder>")
	sys.exit(1)

numberOfFiles = int(sys.argv[2])

srcFolderPath = sys.argv[1]
if srcFolderPath[-1] != "/":
	srcFolderPath += "/"
srcFolderFiles = listdir(srcFolderPath)

destFolderPath = sys.argv[3]
if  destFolderPath[-1] != "/":
	destFolderPath += "/"

if ".DS_Store" in srcFolderFiles:
	remove(srcFolderPath + ".DS_Store")
	srcFolderFiles = listdir(srcFolderPath)

# check if the number given is more than the number of files
if len(srcFolderFiles) < numberOfFiles:
	print("You want to move " + str(numberOfFiles) + " files",end=" ")
	print("but there are " + str(len(srcFolderFiles)), end=" ")
	print("files in the directory " + srcFolderPath)
	sys.exit(1)


for i in range(numberOfFiles):
	print("Moved: " + (srcFolderPath + srcFolderFiles[i]))
	move(srcFolderPath + srcFolderFiles[i], destFolderPath)


