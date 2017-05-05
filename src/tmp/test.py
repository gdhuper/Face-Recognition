import numpy as np
from tables import *

# Generate some data
x = np.random.random((100,100,100))

# Store "x" in a chunked array...
f = tables.openFile('test.hdf', 'w')
atom = tables.Atom.from_dtype(x.dtype)
ds = f.createCArray(f.root, 'somename', atom, x.shape)
ds[:] = x
f.close()

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