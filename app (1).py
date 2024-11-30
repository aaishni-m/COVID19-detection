import os 
from PIL import Image  # Corrected 'Image' import to come from PIL
import numpy as np
import pandas as pd
from model import image_pre, predict  # Ensure this is correct or update based on location
from flask import Flask, render_template, request

app = Flask(__name__)

UPLOAD_FOLDER = 'C:/Users/Hello/OneDrive/Desktop/project/static'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def home():
    return render_template('index.html', result='test result')

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['POST', 'GET'])
def upload_file():
    result = None
    if 'file1' not in request.files:
        return 'There is no file1 in form!'
    
    file1 = request.files['file1']

    if file1.filename == '' or not allowed_file(file1.filename):
        return 'File type not allowed. Please upload a valid PNG, JPG, or JPEG image.'

    path = os.path.join(app.config['UPLOAD_FOLDER'], 'input.png')

    try:
        file1.save(path)

        # Verify the saved image file
        with Image.open(path) as img:
            img.verify()  # Verify the image is not corrupted
        print(f"File saved at {path} and verified as a valid image.")

        # Continue processing the image after verification
        data = image_pre(path)
        s = predict(data)
    
    except (IOError, SyntaxError) as e:
        print(f"Invalid image file: {e}")
        return f"An error occurred: {e}"

    if s == 1:
        result = 'No Covid Detected'
    else:
        result = 'Covid Detected'

    return render_template('index.html', result=result or 'Processing failed.')

if __name__ == '__main__':
    app.run(debug=True, port=8000)
