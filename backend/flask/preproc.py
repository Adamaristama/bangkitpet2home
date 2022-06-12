import tensorflow as tf
from tensorflow import keras
import tensorflow_hub as hub
import numpy as np
import matplotlib.image as mpimg
import os


model_file = './modelXception.h5'
model = keras.models.load_model(model_file, custom_objects={
                                    'KerasLayer': hub.KerasLayer})

def get_category(img):


    img = mpimg.imread(img)
    img = tf.cast(img, tf.float32) / 255
    img = tf.image.resize(img, [299, 299]) #Xception input 299
    img = np.expand_dims(img, axis=0) # expand image dimension from (299,299,3) to (1,299,299,3) for tensor call
    images = np.vstack([img])

    prediction = model(images)
    predict_label = np.argmax(prediction, axis=1)

    persentase = "{:.2f}".format(np.max(prediction)*100) #output Predict numpy * 100
    
    class_names = ['Abyssinian', 'Beagle', 'Bombay', 'British Shorthair',
                    'Chihuahua', 'Persian', 'Pomeranian', 'Pug',
                    'Shiba Inu','Siamese'] 
    #label class
    
    Prediction = class_names[predict_label[0]]

    return Prediction, persentase # return output
