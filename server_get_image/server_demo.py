import base64

from flask import Flask
from flask_cors import CORS, cross_origin
from flask import request
from flask import Response
from PIL import Image
from flask import jsonify, json, render_template
import numpy as np
import cv2
import io
import os , io , sys

from flask_cors import CORS, cross_origin

app = Flask(__name__)

# Apply Flask_CORS
CORS(app)
app.config['CORS_HEADERS'] = 'Content-type'
@cross_origin(origin='*')

##############
@app.route('/maskImage' , methods=['POST'])
def mask_image():
	# print(request.files , file=sys.stderr)
	file = request.files['image'].read() ## byte file
	npimg = np.fromstring(file, np.uint8)
	img = cv2.imdecode(npimg,cv2.IMREAD_COLOR)
	######### Do preprocessing here ################
	# img[img > 150] = 0
	## any random stuff do here
	################################################
	img = Image.fromarray(img.astype("uint8"))
	rawBytes = io.BytesIO()
	img.save(rawBytes, "JPEG")
	rawBytes.seek(0)
	img_base64 = base64.b64encode(rawBytes.read())
	return jsonify({'status':str(img_base64)})

################

@app.route('/test' , methods=['GET','POST'])
def test():
	print("log: got at test" , file=sys.stderr)
	return jsonify({'status':'succces'})

@app.route('/home')
def home():
	#return render_template('index.jinja2')
	return render_template('index.html')


	
@app.after_request
def after_request(response):
    print("log: setting cors" , file = sys.stderr)
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response


if __name__ == '__main__':
    app.run(host='127.0.0.1', port='6868')
	
    


    


