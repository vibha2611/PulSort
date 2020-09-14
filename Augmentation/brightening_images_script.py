#Reference: https://pythonexamples.org/python-pillow-adjust-image-brightness/

from PIL import Image, ImageEnhance
from random import random
import os.path, sys

def brighten(directory):
    dirs=os.listdir(directory)
    for img in dirs:
        fullpath=os.path.join(directory, img)
        img=Image.open(fullpath).convert('LA')
        enhancer=ImageEnhance.Brightness(img)
        for i in range(3): #generate 3 brightened/darkened images from original
            factor=random()+0.5 #range is 50% as bright as original to 150% as bright as original
            im=enhancer.enhance(factor) 
            im.save(fullpath+'bright'+str(i)+".png", "png")
            
