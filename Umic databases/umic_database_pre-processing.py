import numpy as np
import glob
import random as rnd
import pickle
import matplotlib.pyplot as plt
from numpy import asarray
from numpy import save
import cv2
import os

num_photos = 100
names = ["Amit", "atharva", "Balasubramanian", "Harshil", "Meghna", "Rihan Aaron", "Ronit", "Saad", "shubham","Siddhant"]
down_size = 112
down_points = (down_size, down_size)

face_database = []
face_names_database = []
Y = [None] * num_photos
i = 0
j = 0
for name in names:
    file_name = "UMIC Members/"+name+"/*.jpg"
    face_shots = []
    for file in glob.glob(file_name):
        photo = cv2.imread(file)
        face_img = cv2.resize(photo, down_points, interpolation= cv2.INTER_LINEAR)
        print(face_img.shape)
        cv2.imshow("meow", face_img)
        cv2.waitKey()
        face_database.append(face_img)
        face_names_database.append(name)
        Y[i] = j
        i+=1
    j+=1

Y = np.array(Y)
print(Y.shape)

database = np.array(face_database[0],dtype=float)
for i in range(1,len(face_database)):
    j = np.array(face_database[i],dtype=float)
    database = np.concatenate((database,j),axis=0)

print(database.shape)
save("umic_members_images.npy",database)
save("umic_members_Y.npy",Y)
file_name = "umic_members_names.pkl"
open_file = open(file_name, "wb")
pickle.dump(face_names_database, open_file)
open_file.close()