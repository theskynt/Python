import cv2
import numpy as np
import matplotlib.pyplot as plt

img=cv2.imread("/Users/thesky/Desktop/Python/โค้ด/image_processing/473.png")
RGB_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_xr = RGB_img[:, :, 0]
img_xg = RGB_img[:, :, 1]
img_xb = RGB_img[:, :, 2]

plt.subplot(2, 2, 1)
plt.imshow(img_xr, cmap= "gray")
plt.title('R')

print(RGB_img.shape)
img_transpose = np.transpose(RGB_img)  
print(img_transpose.shape)
plt.subplot(2, 2, 2)
plt.imshow(img_transpose[0, :, :], cmap= "gray")
plt.title('transpose image')

img_moveaxis = np.moveaxis(RGB_img, 2, 0)
print(img_moveaxis.shape)
plt.subplot(2, 2, 3)
plt.imshow(img_moveaxis[0, :, :], cmap= "gray")
plt.title('moveaxis image')

height, width, channels = RGB_img.shape
img_reshape = np.reshape(RGB_img, (channels, height, width))
print(img_reshape.shape)
plt.subplot(2, 2, 4)
plt.imshow(img_reshape[0, :, :], cmap= "gray")
plt.title('reshape image')

plt.show()