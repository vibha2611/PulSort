from PIL import Image
import os.path, sys
import numpy as np

path = <filepath> #folder containing downloaded plots

dirs = os.listdir(path)

for item in dirs:
        fullpath = os.path.join(path,item)         
        if os.path.isfile(fullpath):
                im_list=[]
                im = Image.open(fullpath)
                f, e = os.path.splitext(fullpath)
                pulse_profile = im.crop((0, 0, 205, 140)) 
                pulse_profile.save(f + 'pulse profile.png', "png", quality=100)
                phase_subband = im.crop((295, 150, 505, 405))
                phase_subband.save(f + ' phase-subband.png', "png", quality=100)
