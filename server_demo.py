import base64

from flask import Flask
from flask_cors import CORS, cross_origin
from flask import request
import numpy as np
import cv2

# Initial Flask server backend
app = Flask(__name__)

# Apply Flask_CORS
CORS(app)
app.config['CORS_HEADERS'] = 'Content-type'


def base64_to_image(imagebase64):
    try:
        imagebase64 = np.fromstring(base64.b64decode(imagebase64), dtype=np.uint8)
        imagebase64 = cv2.imdecode(imagebase64. cv2.IMREAD_ANYCOLOR)
    except:
        return None
    return imagebase64

def convert_and_save(b64_string):
    with open("imageToSave.png", "wb") as fh:
        fh.write(base64.decodebytes(b64_string.encode()))


@app.route('/text_recognition', methods=['GET'])
@cross_origin(origin='*')


def text_recognition():
    text_in_image = ''
    # Read image from client
    imagebase64 = request.form.get('imagebase64')
    # base64 to OpenCV format
    text = base64_to_image(imagebase64)
    # Run model on image

    # Return text from image
    return "Text: "


# Start back-end
if __name__ == '__main__':
    app.run(host='127.0.0.1', port='6868')
