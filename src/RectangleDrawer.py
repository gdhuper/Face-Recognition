from PIL import Image, ImageDraw
from PIL import ImageColor as imc

def colorRectangle(imagePath):
	im = Image.open(imagePath)
	draw = ImageDraw.Draw(im)
	for i in range(6):
		draw.line((i, 0,i,250), fill=(113,202,88))
		draw.line((245 + i, 0,245 + i,250), fill=(113,202,88))
		draw.line((0, i, 250, i), fill=(113,202,88))
		draw.line((0, 245 + i, 250,245 + i), fill=(113,202,88))
	del draw
	return im 

image = colorRectangle("vid_imgs/vid0000.jpg")
image.show()