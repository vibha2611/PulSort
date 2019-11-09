from PIL import Image
import os.path, sys

path = r"folder" #enter name of folder containing plots
dirs = os.listdir(path)
for item in dirs:
        fullpath = os.path.join(path,item)         
        if os.path.isfile(fullpath):
            im = Image.open(fullpath)
            f, e = os.path.splitext(fullpath)
            imCrop = im.crop((295, 150, 505, 405)) 
            imCrop.save(f + ' phase-subband.png', "png", quality=100)
