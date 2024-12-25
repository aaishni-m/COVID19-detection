import os
from PIL import Image
import numpy as np
from flask import Flask, render_template, request
from model import image_pre, predict  # Import your functions from model.py

app = Flask(__name__)
UPLOAD_FOLDER = 'C:/Users/Hello/OneDrive/Desktop/project/static'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}  # Set of allowed extensions
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Set the maximum content length for uploads to 32 MB
app.config['MAX_CONTENT_LENGTH'] = 32 * 1024 * 1024  # Limit to 32 MB

@app.route('/')
def home():
    return render_template('index.html', result='Upload an image for prediction')

def allowed_file(filename):
    # Ensure the file has an extension and it's allowed
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['POST'])
def upload_file():
    print("Form submitted!")  # Debug statement
    
    if 'file1' not in request.files:
        return 'There is no file1 in form!'

    file1 = request.files['file1']

    # Check if the file is valid and has a filename
    if file1.filename == '':
        return 'No selected file. Please upload a valid PNG, JPG, or JPEG image.'

    # Debugging: Print the filename for checking
    print(f"Uploaded filename: {file1.filename}")

    # Check if the file is allowed
    if not allowed_file(file1.filename):
        return 'File type not allowed. Please upload a valid PNG, JPG, or JPEG image.'

    path = os.path.join(app.config['UPLOAD_FOLDER'], 'input.png')

    try:
        # Save the uploaded file
        file1.save(path)

        # Verify the saved image file
        with Image.open(path) as img:
            img.verify()  # Verify the image is not corrupted
        print(f"File saved at {path} and verified as a valid image.")

        # Continue processing the image after verification
        data = image_pre(path)  # Preprocess the image
        s = predict(data)  # Get the prediction

    except Exception as e:
        print(f"Error processing file: {e}")
        return f"An error occurred: {e}"

    # Determine the result based on prediction
    if s == 1:
        result = 'No Covid Detected'
    else:
        result = 'Covid Detected'

    # Provide the result and display the image
    return render_template('index.html', result=result, image_path='static/input.png')

if __name__ == '__main__':
    app.run(debug=True, port=8000)
