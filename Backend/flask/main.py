from flask import Flask, request
import numpy as np
import os
import json
from predict import do_predict
from imgpreprocess import preproc

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    data = {'status': 200, 'data': 'Hello there'}
    return json.dumps(data)


@app.route('/api/predict', methods=['POST'])
def predict_img():
    item = request.json
    item_dict = json.loads(item)
    jsonResponse = do_predict(item_dict['data'])
    return jsonResponse


@app.route('/api/test', methods=['POST'])
def test_post():
    item = request.json
    jsonResult = {
        'data': item,
    }
    return json.dumps(jsonResult)


@app.route('/api/predict/img', methods=['POST'])
def predict_full_img():
    item = request.json
    item_dict = json.loads(item, strict=False)
    encodedItem = item_dict['data'].encode('utf8')
    img_data = preproc(encodedItem)
    jsonResponse = do_predict(img_data)
    return jsonResponse


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='5000')