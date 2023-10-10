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

img = cv2.imread("/Users/thesky/Desktop/Python/โค้ด/image_processing/lab3/bodhi.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img = cv2.resize(img, (224, 224))
img = img.reshape(1,img.shape[0], img.shape[1], 3)
img_mean = [123.68, 116.779, 103.939]
img = img - img_mean

print(img.shape)
plt.imshow(img[0])
plt.title("Image Preparation")
plt.show()   