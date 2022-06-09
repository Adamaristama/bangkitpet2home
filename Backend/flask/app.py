import flask
import io
import string
import time
import os
import numpy as np
import tensorflow as tf
import base64
import json
from PIL import Image
from flask import Flask, jsonify, request

model = tf.keras.models.load_model('./modelXception')


def preproc(data):
    imgdata = base64.decodebytes(data)
    image = Image.open(io.BytesIO(imgdata)).convert('RGB')
    image_new = image.resize((299, 299))
    x = np.array(image_new)
    x = np.expand_dims(x, axis=0)
    x = x / 255.0
    new_x = np.vstack([x])
    return 


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

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def infer_image():
    if 'file' not in request.files:
        return "Please try again. The Image doesn't exist"
    
    file = request.files.get('file')

    if not file:
        return

    img_bytes = file.read()
    img = preproc(img_bytes)

    return jsonify(prediction=do_predict(img))
    

@app.route('/', methods=['GET'])
def index():
    return 'api ml'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='5000')