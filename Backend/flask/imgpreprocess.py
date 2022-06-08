import json
import tensorflow as tf
import os
import numpy as np
import base64
from PIL import Image
import io


def preproc(data):
    imgdata = base64.decodebytes(data)
    image = Image.open(io.BytesIO(imgdata)).convert('RGB')
    image_new = image.resize((299, 299))
    x = np.array(image_new)
    x = np.expand_dims(x, axis=0)
    x = x / 255.0
    new_x = np.vstack([x])
    return 