import numpy as np
import os
import cv2
import random
import pickle

subplot=int(input("Which network are you training? Enter 1 for frequency vs. phase or 2 for pulse profile: "))
fp_folder=
pp_folder=

def check_file(subplot):
        file_no=0
        #finish function
        if subplot==1:
                folder=fp_folder
                for file in os.listdir(folder):
                        while str(file_no) in file:
                                file_no+=1  #do not overwrite
                categories= ["pulsar", "not_pulsar"]
                image_width=70
                image_height=93
                features_binary="frequency_phase_features"+str(file_no)+".pickle"
                labels_binary="frequency_phase_labels"+str(file_no)+".pickle"

        elif subplot==2:
                folder=pp_folder
                for file in os.listdir(folder):
                        while str(file_no) in file:
                                file_no+=1
                categories=["harmonics", "pulsar", "not_pulsar"]
                image_width, image_height=50
                features_binary="pulse_profile"+str(file_no)+".pickle"
                labels_binary="pulse_profile"+str(file_no)+".pickle"
        else:
                print("Invalid input")

check_file(subplot)

training_data = []

def create_training_data():
	for category in categories:
		path = os.path.join(folder, category)
		class_num = categories.index(category) #associate each category with number
		for img in os.listdir(path):
			try :
				img_array = cv2.imread(os.path.join(path, img), 0) #read in grayscale
				new_array = cv2.resize(img_array, (image_width, image_height))
				training_data.append([new_array, class_num])
			except Exception as e:
				pass
                        

create_training_data()

random.shuffle(training_data)

X = [] #features
y = [] #labels

for features, label in training_data:
	X.append(features)
	y.append(label)

X = np.array(X).reshape(-1, image_width, image_height, 1)

#binary files to store features and labels
pickle_X = open(features_binary, "wb")
pickle.dump(X, pickle_X)
pickle_X.close()
pickle_y = open(labels_binary, "wb")
pickle.dump(y, pickle_y)
pickle_y.close()
