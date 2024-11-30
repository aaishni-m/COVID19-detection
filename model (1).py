import tensorflow as tf
import numpy as np
import pandas as pd
from matplotlib.pyplot import imshow
from PIL import ImageOps, Image

base = 'C:/Users/Hello/OneDrive/Desktop/project'

model = tf.keras.models.load_model(f'{base}/CovidTest.h5')
model.compile(optimizer=tf.keras.optimizers.Adam(), loss='binary_crossentropy', metrics=['accuracy'])
def image_pre(path):
    try:
        print(path)
        size = (128, 128)
        image = Image.open(path)
        image = ImageOps.grayscale(image)
        image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)
        image_array = np.asarray(image)
        data = image_array.reshape((-1, 128, 128, 1)) / 255.0
        return data
    except Exception as e:
        print(f"Error in processing image: {e}")
        raise e


def predict(data):
    prediction = model.predict(data)
    return np.round(prediction[0][0])


