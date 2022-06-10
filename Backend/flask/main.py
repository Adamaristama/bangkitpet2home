import logging
from flask import Flask, jsonify, request
from preproc import get_category

app = Flask(__name__)

@app.route("/")
def showHomePage():
    return "This is home page"


@app.route('/Upload', methods=['GET', 'POST'])
def skin_disease():
    if request.method == 'POST':
    # POST method to post the results file
        # Read file from upload
        img = request.files['file']

        if img is None or img.filename == "":
            return jsonify({"error": "no file"})

        # Get category of prediction
        try:
            image_category = get_category(img)

            # make dictionary data and convert the dictionary to json
            data = { "Prediksi" : image_category[0], 
                    "Presentase" : image_category[1] }
            return jsonify(data)

        except Exception as err:
            return jsonify({"error" : str(err)})

    return {}

@app.route('/', methods=['GET'])
def index():
    hello_json = {
        'status_code': 200,
        'message': 'Success testing the API!',
        'data': [],
    }
    return jsonify(hello_json)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)