import cv2
import numpy as np
import tensorflow as tf
from typing import Union
from fastapi import FastAPI
import uvicorn

#Define Function
labels = ['Jamur Enoki', 'Jamur Shimeji Coklat', 'Jamur Shimeji Putih', 'Tiram']

def predict(img_input):
    loaded_model = tf.keras.models.load_model('YangJamurJamuraja_v2.h5')
    img = cv2.imread(img_input)
    resize = tf.image.resize(img, (224,224))
    color_converted = (cv2.cvtColor(resize.numpy().astype(np.uint8),cv2.COLOR_BGR2RGB))
    color_converted = loaded_model.predict(np.expand_dims(resize/255,0))
    idx = color_converted.argmax()
    return labels[idx]

result = predict(r"C:\Users\Asus\Documents\Luswis Files\Product-Capstone\deploy\images (1).jpg")
print(result)

#FASTAPI
app = FastAPI()

@app.get("/")
def read_root():
    result = predict(r"C:\Users\Asus\Documents\Luswis Files\Product-Capstone\deploy\images (1).jpg")
    print(result)
    return result

uvicorn.run(app, host='0.0.0.0', port=8001)