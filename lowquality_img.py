import glob, os
from PIL import Image

path = 'C:/test/'
lqPath = path + 'lowquality/'

if not os.path.exists(lqPath):
    os.makedirs(lqPath)
for filepath in glob.glob(path + "*.png"):
    img = Image.open(filepath)
    new_size = int(img.width/2), int(img.height/2)
    img = img.resize(new_size, Image.ANTIALIAS)
    img.save(lqPath + os.path.basename(filepath), "PNG")