import json
import tensorflow as tf
import os
import numpy as np
import base64
# from keras.preprocessing import image

model = tf.keras.models.load_model('./mobilenetv2_final')
class_names = ['Abyssinian', 'Beagle', 'Bombay', 'British Shorthair',
               'Chihuahua', 'Persian', 'Pomeranian', 'Pug',
               'Shiba Inu','Siamese']


def do_predict(data):
    prediction = model.predict(data)
    new_prediction = prediction.tolist()
    result = int(np.argmax(prediction))
    class_name = class_names[result]
    percent = float(np.max(prediction * 100))
    jsonDict = {
        'predClass': result,
        'className': class_name,
        'percentage': percent,
        'prediction': new_prediction,
    }
    return json.dumps(jsonDict)