# call sequence: ``multiple(path-to-dir)`` or ``single(img-path)``

# imports
import cv2
import tensorflow as tf
import os.path, sys
from PIL import Image

# set model paths
pppath =
fppath =

# load models
pp_model = tf.keras.models.load_model(pppath)
fp_model = tf.keras.models.load_model(fppath)

# which model to use
subplot = int(input('Which model? 1 for frequency vs phase, 2 for pulse profile: '))
if subplot == 1:
    model = fp_model
    width = 70
    height = 93
elif subplot == 2:
    model = pp_model
    width, height = 50
else:
    print("Invalid entry")

categories = ["Pulsar", "Not a pulsar", "Harmonic"]

# reshape file for NN
def prep(file):
    img_array = cv2.imread(file, 0)
    new_array = cv2.resize(img_array, (width, height))
    new_array = new_array.reshape(-1, width, height, 1)
    new_array = new_array / 255.0  #normalise
    return(new_array)

# return predictions for all images in a dir
def multiple(plots_dir):
    positives = []
    dirs = os.listdir(plots_dir)
    for img in dirs:
        path = os.path.join(plots_dir, img)
        img = prep(path)
        prediction = model.predict([img])
        prediction = list(prediction[0])
        print(path, categories[prediction.index(max(prediction))])
    return

# return prediction for single image
def single(path):
    img = prep(path)
    prediction = model.predict([img])
    prediction = list(prediction[0])
    return(categories[prediction.index(max(prediction))])
