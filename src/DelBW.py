import numpy as np
from os import listdir, remove
from PIL import Image
import sys

# Make sure that there are at least 2 arguments
if len(sys.argv) < 2:
	print("Usage: DelBW.py <folder>")
	sys.exit(1)

dir = sys.argv[1]

if dir[-1] != "/":
	dir += "/"

imagesOfFaces = listdir(dir)

if ".DS_Store" in imagesOfFaces:
	remove(dir + ".DS_Store")
	imagesOfFaces = listdir(dir)

count = 0
for image in imagesOfFaces:
	image_path = dir + image
	img = Image.open(image_path)
	img_arr = np.array(img).ravel()
	if len(img_arr) < 187500:
		count += 1
		remove(image_path)
		print("Deleted: " + image_path)
print("==> Deleted " + str(count) + " images!")

