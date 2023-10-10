import cv2
import numpy as np
import matplotlib.pyplot as plt

img=cv2.imread("/Users/thesky/Desktop/Python/โค้ด/image_processing/473.png")
img_xr = img[:, :, 2]
img_xg = img[:, :, 1]
img_xb = img[:, :, 0]

plt.subplot(2, 4, 1)
plt.imshow(img)
plt.title('BGR')

plt.subplot(2, 4, 2)
plt.imshow(img_xb, cmap= "gray")
plt.title('B')

plt.subplot(2, 4, 3)
plt.imshow(img_xg, cmap= "gray")
plt.title('G')

plt.subplot(2, 4, 4)
plt.imshow(img_xr, cmap= "gray")
plt.title('R')

RGB_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
RGB_img_xr = RGB_img[:, :, 0]
RGB_img_xg = RGB_img[:, :, 1]
RGB_img_xb = RGB_img[:, :, 2]
plt.subplot(2, 4, 5)
plt.imshow(RGB_img)
plt.title('RGB')

plt.subplot(2, 4, 6)
plt.imshow(RGB_img_xr, cmap= "gray")
plt.title('R')

plt.subplot(2, 4, 7)
plt.imshow(RGB_img_xg, cmap= "gray")
plt.title('G')

plt.subplot(2, 4, 8)
plt.imshow(RGB_img_xb, cmap= "gray")
plt.title('B')

plt.show()