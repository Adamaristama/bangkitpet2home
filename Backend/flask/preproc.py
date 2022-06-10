import tensorflow as tf
from tensorflow import keras
import tensorflow_hub as hub
import numpy as np
import matplotlib.image as mpimg


def get_category(img):
    """Write a Function to Predict the Class Name
    Args:
        img [jpg]: image file with 3 color channels
    Returns:
        [str]: Prediction
        [str]: Presentase
    """
    model_file = 'modelXception.h5'
    model = keras.models.load_model(model_file, custom_objects={
                                    'KerasLayer': hub.KerasLayer})

    # Read an image from a file into a numpy array
    img = mpimg.imread(img)
    # Convert to float32
    img = tf.cast(img, tf.float32) / 255
    # Resize to 224x224 (size the model is expecting)
    img = tf.image.resize(img, [224, 224])
    # Expand img dimensions from (224, 224, 3) to (1, 224, 224, 3) for set_tensor method call
    img = np.expand_dims(img, axis=0)
    images = np.vstack([img])

    prediction = model(images)
    predicted_label = np.argmax(prediction, axis=1)

    persentase = "{:.2f}".format(np.max(prediction)*100)
    class_names = ['Abyssinian', 'Beagle', 'Bombay', 'British Shorthair',
               'Chihuahua', 'Persian', 'Pomeranian', 'Pug',
               'Shiba Inu','Siamese']
    Prediction = class_names[predicted_label[0]]

    return Prediction, persentase