from PIL import Image
import os.path, sys

x=int(input("Enter 1 if GBT plot, 2 if GBNCC plot: "))
if x==1:
        y=(295, 150, 505, 405)
else:
        y=(700, 420, 1110, 950)
path = r"folder" #enter name of folder containing plots
dirs = os.listdir(path)
for item in dirs:
        fullpath = os.path.join(path,item)         
        if os.path.isfile(fullpath):
            im = Image.open(fullpath)
            f, e = os.path.splitext(fullpath)
            imCrop = im.crop(y) 
            imCrop.save(f + ' phase-subband.png', "png", quality=100)
