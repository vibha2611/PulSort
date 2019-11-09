from PIL import Image
import os.path, sys

path = r"C:\Users\vibha\Documents\Known pulsar data"
dirs = os.listdir(path)
for item in dirs:
        fullpath = os.path.join(path,item)         
        if os.path.isfile(fullpath):
            im = Image.open(fullpath)
            f, e = os.path.splitext(fullpath)
            imCrop = im.crop((0, 0, 205, 140)) 
            imCrop.save(f + 'pulse profile.png', "png", quality=100)
