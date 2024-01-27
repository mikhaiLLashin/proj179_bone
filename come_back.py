import os
from random import randint
from PIL import Image

path_1 = 'C:\\Users\\lashi\\Desktop\\bones\\'
path_tr = "C:\\Users\\lashi\\Desktop\\bones\\train\\"
path_val = "C:\\Users\\lashi\\Desktop\\bones\\val\\"

directory = os.fsencode(path_tr + "images")
for file in os.listdir(directory):
    filename = os.fsdecode(file)
    os.rename(path_tr + "images\\" + str(filename), path_1 + "images\\" + str(filename))
    os.rename(path_tr + "labels\\" + str(filename[:-4]) + ".txt", path_1 + "labels\\" + str(filename[:-4]) + ".txt")
directory = os.fsencode(path_val + "images")
for file in os.listdir(directory):
    filename = os.fsdecode(file)
    os.rename(path_val + "images\\" + str(filename), path_1 + "images\\" + str(filename))
    os.rename(path_val + "labels\\" + str(filename[:-4]) + ".txt", path_1 + "labels\\" + str(filename[:-4]) + ".txt")
