#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 22:10:16 2021

@author: bhaktihegde
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 20:25:20 2021
@author: bhaktihegde
"""
# any methods in this program that doesn't have a specific comments 
# by the author is referenced from Google Teachable Machine


def gen_labels():
        labels = {}
        with open("labels.txt", "r") as label:
            text = label.read()
            lines = text.split("\n")
            print(lines)
            for line in lines[0:-1]:
                    hold = line.split(" ", 1)
                    labels[hold[0]] = hold[1]
        return labels

# Code below written by Bhakti Hegde
# This method provides the frequency corresponding to the animal input

def animal1(marine):
   
    if marine == 'sea turtles':
        print("The device will let out the frequency of 200-400 Hz")
  
    elif marine == 'orcas':
        print("The device will let out the frequency of 18,000-24,000 Hz")
  
    elif marine == 'dolphins':
        print("The device will let out the frequency of 40,000-100,000 Hz ")
    
    elif marine == 'cod fish':
        print("The device will let out the frequency of 60-310 Hz ")
        
    elif marine == 'jellyfish':
        print("The device will let out the frequency of  38,000-120,000 Hz ")
    
    else:
        print("The device will let out the frequency of 10,000 Hz")

# Main method

import tensorflow.keras
import os

from PIL import Image, ImageOps
import numpy as np
# Disable scientific notation for clarity
np.set_printoptions(suppress=True)
# Load the model
model = tensorflow.keras.models.load_model('keras_model.h5')
# Create the array of the right shape to feed into the keras model
# The 'length' or number of images you can put into the array is
# determined by the first position in the shape tuple, in this case 1.
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
labels = gen_labels()
# Replace this with the path to your image
# make a folder called images and copy all the images in that
directory = r'/Users/bhaktihegde/Downloads/converted_keras/animalimages'
for filename in os.listdir(directory):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        print(os.path.join(directory, filename))
        image = Image.open(os.path.join(directory, filename))
        image = image.convert("RGB")
        #resize the image to a 224x224 with the same strategy as in TM2:
        #resizing the image to be at least 224x224 and then cropping from the center
        size = (224, 224)
        image = ImageOps.fit(image, size, Image.ANTIALIAS)
        #turn the image into a numpy array
        image_array = np.asarray(image)
        # display the resized image
        #image.show()
        # Normalize the image
        normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
        # Load the image into the array
        data[0] = normalized_image_array
        # run the inference
        prediction = model.predict(data)
        print(prediction)
        result = np.argmax(prediction[0])
        pred_text = labels[str(result)]
        print(pred_text)
        
        # After identifying the animal, this method is used to identify
        # the corresponding frequency
    
        animal1(pred_text)
    else:
        print('No file found')
        
        
