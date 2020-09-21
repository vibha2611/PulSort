from PIL import Image, ImageOps
import os

def flip_one(path):
    split=os.path.split(path)
    im=Image.open(path)
    im_flip=ImageOps.flip(im)
    im_flip.save(os.path.join(split[0], 'flip_'+str(split[1])), quality=100)
    im_mirror=ImageOps.mirror(im)
    im_mirror.save(os.path.join(split[0],'mirror_'+str(split[1])), quality=100)

def flip_many(path):
    paths=[os.path.join(path, file) for file in os.listdir(path) if os.path.isfile(os.path.join(path, file))==True]
    for path in paths:
        flip_one(path)
