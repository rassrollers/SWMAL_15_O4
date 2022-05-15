from hashlib import new
import matplotlib.pyplot as plt
import numpy as np
import os
import random
import tensorflow as tf
import keras
from keras.preprocessing.image import ImageDataGenerator, load_img, img_to_array
from PIL import Image
import cv2

# Controlling which things the script should do regarding images.
augmentImg = False
cleanAug = False
renameAug = True

trainDir = 'C:\\Users\\ra\\Desktop\\O4_AugTest\\Data6Classes\\train\\'
augDir = 'C:\\Users\\ra\\Desktop\\O4_AugTest\\Data6Classes\\augment\\'


if augmentImg == True:
    gen = ImageDataGenerator(rotation_range=40, 
                        width_shift_range=0.1, 
                        height_shift_range=0.1,
                        shear_range=0.15, 
                        zoom_range=0.1, 
                        horizontal_flip=True)
                        
    a,b = gen.flow_from_directory(directory=trainDir, target_size=(180,180),color_mode='rgb',batch_size=2743,
                            save_to_dir=augDir, save_prefix="aug_img", save_format='jpg', 
                            classes=['brisket_126','edamame_76','hamburger_164','lobster_food_91',
                                    'omelette_196', 'pizza_183'],
                                    class_mode="binary")

# Augmentation makes 3 copies, therefor only every third is saved.                
if cleanAug == True:
    if os.path.exists(augDir):
        removed = 0
        counter = 0
        os.chdir(augDir)
        for file in os.listdir():
            counter = counter + 1
            if counter < 3:
                os.remove(file)
                removed = removed + 1
            else:
                counter = 0

if renameAug == True:
    # Counter naming the augmented pictures orderly
    brisk_count = 93563
    renameDir = augDir + "brisket_126\\"
    if os.path.exists(renameDir):
        os.chdir(renameDir)
        for file in os.listdir():
            newFilename = "train_0" + str(brisk_count) + ".jpg"
            os.rename(file,newFilename)
            brisk_count = brisk_count + 1
    
    edamame_count = 45561
    renameDir = augDir + "edamame_76\\"
    if os.path.exists(renameDir):
        os.chdir(renameDir)
        for file in os.listdir():
            newFilename = "train_0" + str(edamame_count) + ".jpg"
            os.rename(file,newFilename)
            edamame_count = edamame_count + 1

    hamburger_count = 89346
    renameDir = augDir + "hamburger_164\\"
    if os.path.exists(renameDir):
        os.chdir(renameDir)
        for file in os.listdir():
            newFilename = "train_0" + str(hamburger_count) + ".jpg"
            os.rename(file,newFilename)
            hamburger_count = hamburger_count + 1

    lobster_count = 20405
    renameDir = augDir + "lobster_food_91\\"
    if os.path.exists(renameDir):
        os.chdir(renameDir)
        for file in os.listdir():
            newFilename = "train_0" + str(lobster_count) + ".jpg"
            os.rename(file,newFilename)
            lobster_count = lobster_count + 1

    omelette_count = 14643
    renameDir = augDir + "omelette_196\\"
    if os.path.exists(renameDir):
        os.chdir(renameDir)
        for file in os.listdir():
            newFilename = "train_0" + str(omelette_count) + ".jpg"
            os.rename(file,newFilename)
            omelette_count = omelette_count + 1

    pizza_count = 79496
    renameDir = augDir + "pizza_183\\"
    if os.path.exists(renameDir):
        os.chdir(renameDir)
        for file in os.listdir():
            newFilename = "train_0" + str(pizza_count) + ".jpg"
            os.rename(file,newFilename)
            pizza_count = pizza_count + 1
