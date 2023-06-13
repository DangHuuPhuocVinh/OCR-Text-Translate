# -*- coding: utf-8 -*-
"""
Created on Fri May  7 22:29:28 2021

@author: Vinh
"""
from flask import Flask, render_template, request
import os, pytesseract
from flask_uploads import UploadSet, configure_uploads, IMAGES
from PIL import Image

# create directory
project_dir = os.path.abspath(__file__)

# get json
app = Flask(__name__,
            static_url_path= '',
            static_folder = 'static',
            template_folder = 'templates')

app.config['DEBUG'] = True
app.config['UPLOAD_FOLDER'] = 'images'

# image to text
class GetText(object):
    
    def __init__(self, file):
        self.file = pytesseract.image_to_string(Image.open(project_dir + '/img/' + file))

# routing        
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        if 'photo' not in request.files:
                return 'there is no photo here'
        name = request.form['img-name'] + '.jpg'
        photo = request.files['photo']
        path = os.path.join(app.config['UPLOAD_FOLDER'], name)
        photo.save(path)
        
        textObject = GetText(name)
        print(textObject.file)
        return textObject.file
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug = True)
        

