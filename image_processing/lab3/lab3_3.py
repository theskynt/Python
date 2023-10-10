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
img = cv2.imread("/Users/thesky/Desktop/Python/โค้ด/image_processing/lab3/bodhi.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img = cv2.resize(img, (224, 224))
imgC = img.copy()
img = img.reshape(1,img.shape[0], img.shape[1], 3)
img_mean = [123.68, 116.779, 103.939]
img = img - img_mean

for j in range(64):
    for i in range(3):
        img[0, :, :, i] = signal.convolve2d(imgC[:, :, i], kernels[:, :, i, j], mode='same')
    image_sum = img[0, :, :, 0]+img[0, :, :, 1]+img[0, :, :, 2]
    Relu = np.maximum(image_sum, 0, image_sum)
    plt.subplot(8, 8, j+1)
    plt.imshow(Relu, cmap='viridis')
    plt.axis('off')
plt.show()