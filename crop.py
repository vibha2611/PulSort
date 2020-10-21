from PIL import Image
import os.path, sys
import numpy as np

option = 0

while option != 1 or option != 2:
        option = int(input("Enter 1 if GBT plot, 2 if GBNCC plot: "))
        if option == 1:
                section = (295, 150, 505, 405)
        elif option == 2:
                section = (700, 420, 1110, 950)
        else:
                print("Invalid option")

path = <filepath> #folder containing downloaded plots

dirs = os.listdir(path)

for item in dirs:
        fullpath = os.path.join(path,item)         
        if os.path.isfile(fullpath):
                im_list = []
                im = Image.open(fullpath)
                f, e = os.path.splitext(fullpath)
                pulse_profile = im.crop((0, 0, 205, 140))
                pulse_profile.save(f + 'pulse profile.png', "png", quality=100)
                phase_subband = im.crop(section)
                phase_subband.save(f + ' phase-subband.png', "png", quality=100)
