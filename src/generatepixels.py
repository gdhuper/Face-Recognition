from PIL import Image
import sys

im = Image.open(sys.argv[1])

pixels = list(im.getdata())
width, height = im.size
pixels = [pixels[i * width:(i + 1) * width] for i in range(height)]

print(pixels)
