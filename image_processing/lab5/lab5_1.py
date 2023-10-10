import cv2
import numpy as np
from matplotlib import pyplot as plt

from keras import Model, Input
import keras.utils as image
# from keras.wrappers.scikit_learn import KerasRegressor
# from tensorflow.keras.preprocessing.image import ImageDataGenerator
# from tensorflow.keras.layers import Dense, Conv2D, MaxPool2D, UpSampling2D
# from tensorflow.keras.callbacks import EarlyStopping
# from tensorflow.keras import optimizers

# from tensorflow.keras.datasets import fashion_mnist

from sklearn.model_selection import train_test_split

img = plt.imread("/Users/thesky/Desktop/Python/โค้ด/image_processing/lab5/bodhi.jpg")
# Define resize factor
Reduce_factors = [2, 8, 15]
Scale_factors = [1/ Reduce_factors[0], 1/ Reduce_factors[1], 1/ Reduce_factors[2]]

# Define interpolation method
inter_methods = [cv2.INTER_NEAREST,cv2.INTER_LINEAR, cv2.INTER_CUBIC, cv2.INTER_AREA]
inter_title = ["INTER_NEAREST" ,"INTER_LINEAR" ,"INTER_CUBIC" ,"INTER_AREA"]
plt.figure(figsize=(15, 10))
#Display results using each scale_factors & interpolation methods
for i in range(len(Reduce_factors)):
  for j in range(len(inter_methods)):
   img_resized = cv2.resize(img, None, fx=Scale_factors[i], fy=Scale_factors[i], interpolation=inter_methods[j])
   plt.subplot(len(Reduce_factors), len(inter_methods), i*len(inter_methods)+j+1)
   plt.title(f"{Reduce_factors[i]}\n{inter_title[j]}")
   plt.imshow(img_resized)
plt.show()