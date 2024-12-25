import tensorflow as tf
import numpy as np
from PIL import ImageOps, Image

# Set the base path for model files
base = 'C:/Users/Hello/OneDrive/Desktop/project'

# Load the pre-trained Keras model
model = tf.keras.models.load_model(f'{base}/CovidTest.h5')
model.compile(optimizer=tf.keras.optimizers.Adam(), loss='binary_crossentropy', metrics=['accuracy'])

def image_pre(path):
    try:
        print(path)
        size = (128, 128)  # Set the target size for the images
        image = Image.open(path)  # Open the image
        image = ImageOps.grayscale(image)  # Convert to grayscale
        image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)  # Resize the image
        image_array = np.asarray(image)  # Convert to numpy array
        data = image_array.reshape((-1, 128, 128, 1)) / 255.0  # Reshape and normalize
        return data
    except Exception as e:
        print(f"Error in processing image: {e}")
        raise e

def predict(data):
    prediction = model.predict(data)  # Make prediction
    return np.round(prediction[0][0])  # Round the prediction to get a binary output
