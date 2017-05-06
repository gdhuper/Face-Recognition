

# from PIL import Image
# from os import listdir
# import numpy as np
# import tables
# import sys

# if len(sys.argv) > 1:
# 	# Generate some data
# 	folderPath = sys.argv[1]
# 	folderList = listdir(folderPath)
# 	img = Image.open(folderPath + folderList[0])

# 	x = np.array(img).ravel()

# 	# Store "x" in a chunked array...
# 	f = tables.open_file('test.hdf', 'w')
# 	atom = tables.Atom.from_dtype(x.dtype)
# 	ds = f.createCArray(f.root, 'imageVector', atom, x.shape)
# 	ds[:] = x
# 	f.close()
import os as listdir
import sys
import numpy as np

def splitPerc(l, perc):
	list = listdir(l)
	splits = np.cumsum(perc)/100
	if splits[-1] != 1:
		raise ValueError("percents don't add up to 100")
	return np.split(list, splits[:-1]*len(l))

print(splitPerc(sys.argv[1], sys.argv[2]))

