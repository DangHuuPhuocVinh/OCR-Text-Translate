from flask import Flask
from flask_cors import CORS, cross_origin
from flask import request
from flask import Response
from flask import jsonify
import numpy as np
import cv2
import jsonpickle




# Initial Flask server backend
app = Flask(__name__)


# Apply Flask_CORS
CORS(app)
app.config['CORS_HEADERS'] = 'Content-type'



@app.route('/text_recognition', methods=['POST'])
@cross_origin(origin='*')



def text_recognition():
    r = request
    # convert string of image data to uint8
    nparr = np.fromstring(r.data, np.uint8)
    # decode image
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    # build a response dict to send back to client
    response = {'message': 'image received. size={}x{}'.format(img.shape[1], img.shape[0])
                }
    # encode response using jsonpickle
    response_pickled = jsonpickle.encode(response)
    
    if request.method == 'POST':
        return jsonify(**request.json)

    return Response(response=response_pickled, status=200, mimetype="application/json")

    


# Start back-end
if __name__ == '__main__':
    app.run(host='127.0.0.1', port='6868')
    app.debug = True
