#imports
import keras
import numpy as np
np.random.seed(420)
from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense
from keras import backend as K
from keras.models import load_model
import cv2
import matplotlib.pyplot as plt

#shows image along with class number, also appends it to an array
model = load_model('model.h5')
value=[]

model.compile(loss='categorical_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])
import os
def loop(path):  
    for x in os.listdir(path):
        img = cv2.imread(os.path.join(path,x))
        #cv2.imshow(img)

        img = cv2.resize(img,(128,128))
        plt.imshow(img)
        plt.show()
        img = np.reshape(img,[1,128,128,3])
        classes = model.predict_classes(img)
        print(classes[0]+1)
        value.append(classes[0]+1)
#path to test images
loop("./test")