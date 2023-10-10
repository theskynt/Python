import cv2
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from keras.models import Model
from tensorflow.keras.applications.vgg16 import VGG16
from keras.applications.vgg16 import preprocess_input
from keras.preprocessing.image import img_to_array
from numpy import expand_dims
from scipy import signal


model = VGG16()
model.summary()
kernels, biases = model.layers[1].get_weights()
model.layers[1].get_config()
image = cv2.imread("/Users/thesky/Desktop/Python/โค้ด/image_processing/lab3/bodhi.jpg")
image = cv2.resize(image, (224, 224))

img = img_to_array(image)
img = np.expand_dims(img, axis=0)
img = preprocess_input(img)

model = Model(inputs=model.inputs, outputs=model.layers[1].output)
model.summary()
feature_map = model.predict(img)


num_channels = feature_map.shape[-1]

rows = int(np.sqrt(num_channels))
cols = int(np.ceil(num_channels / rows))

plt.figure(figsize=(10, 10)) 


for i in range(num_channels):
    plt.subplot(rows, cols, i + 1)
    plt.imshow(feature_map[0, :, :, i], cmap='viridis')
    plt.axis('off')


plt.tight_layout
plt.show()   