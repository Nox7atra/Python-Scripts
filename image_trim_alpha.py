import glob, os
from PIL import Image, ImageChops

def trim(im):
    bg = Image.new(im.mode, im.size, im.getpixel((0,0)))
    diff = ImageChops.difference(im, bg)
    diff = ImageChops.add(diff, diff, 2.0, -100)
    bbox = diff.getbbox()
    if bbox:
        return im.crop(bbox)

path = 'C:/Users/Grygory/Desktop/spider/'
trimedPath = path + 'trimed/'

if not os.path.exists(trimedPath):
    os.makedirs(trimedPath)
for filepath in glob.glob(path + "*.png"):
    im = Image.open(filepath)
    im = trim(im)
    im.save(trimedPath + os.path.basename(filepath), "PNG")