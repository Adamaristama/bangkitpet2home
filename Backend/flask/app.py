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
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img , img_to_array

model = tf.keras.models.load_model('./modelXception')

ALLOWED_EXT = set(['jpg' , 'jpeg' , 'png' , 'jfif'])
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXT



class_names = ['Abyssinian', 'Beagle', 'Bombay', 'British Shorthair',
               'Chihuahua', 'Persian', 'Pomeranian', 'Pug',
               'Shiba Inu','Siamese']



def predictpreprocess(filename , model):
    #image preprocess
    img = load_img(filename , target_size = (299 , 299))
    img = img_to_array(img)
    img = img.reshape(1 , 299 ,299 ,3)

    img = img.astype('float32')
    img = img/255.0
    result = model.predict(img)
    
    #predict
    dict_result = {}
    for i in range(10):
        dict_result[result[0][i]] = class_names[i]

    res = result[0]
    res.sort()
    res = res[::-1]
    prob = res[:3]
    
    prob_result = []
    class_result = []
    for i in range(3):
        prob_result.append((prob[i]*100).round(2))
        class_result.append(dict_result[prob[i]])

    return class_result , prob_result

app = Flask(__name__)



@app.route('/predict' , methods = ['POST'])
def predict():
    error = ''
    target_img = os.path.join(os.getcwd() , 'static/images')
    file = request.files['file']
    if file and allowed_file(file.filename):
                file.save(os.path.join(target_img , file.filename))
                img_path = os.path.join(target_img , file.filename)
                img = file.filename

                class_result , prob_result = predict(img_path , model)

                predictions = {
                      "class1":class_result[0],
                        "class2":class_result[1],
                        "class3":class_result[2],
                        "prob1": prob_result[0],
                        "prob2": prob_result[1],
                        "prob3": prob_result[2],
                }

    else:
        error = "Please upload images of jpg , jpeg and png extension only"

    if(len(error) == 0):
        return  error
    
    return predictions

@app.route('/', methods=['GET'])
def index():
    hello_json = {
        'status_code': 200,
        'message': 'Success testing the API!',
        'data': [],
    }
    return jsonify(hello_json)

@app.route('/post', methods=['POST'])
def post():
    data = request.get_json()
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='5000')