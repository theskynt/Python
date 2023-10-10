import cv2
import numpy as np
import matplotlib.pyplot as plt

img=cv2.imread("/Users/thesky/Desktop/Python/โค้ด/image_processing/lab1/473.png")
RGB_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
RGB_img_xr = RGB_img[:, :, 0]
RGB_img_xg = RGB_img[:, :, 1]
RGB_img_xb = RGB_img[:, :, 2]

plt.subplot(4, 4, 1)
plt.imshow(RGB_img)
plt.title('RGB')

plt.subplot(4, 4, 2)
plt.imshow(RGB_img_xr, cmap= "gray")
plt.title('R')

plt.subplot(4, 4, 3)
plt.imshow(RGB_img_xg, cmap= "gray")
plt.title('G')

plt.subplot(4, 4, 4)
plt.imshow(RGB_img_xb, cmap= "gray")
plt.title('B')

HSV_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
HSV_img_xh = HSV_img[:, :, 0]
HSV_img_xs = HSV_img[:, :, 1]
HSV_img_xv = HSV_img[:, :, 2]

plt.subplot(4, 4, 5)
plt.imshow(HSV_img)
plt.title('HSV')

plt.subplot(4, 4, 6)
plt.imshow(HSV_img_xh, cmap= "gray")
plt.title('H')

plt.subplot(4, 4, 7)
plt.imshow(HSV_img_xs, cmap= "gray")
plt.title('S')

plt.subplot(4, 4, 8)
plt.imshow(HSV_img_xv, cmap= "gray")
plt.title('V')

HLS_img = cv2.cvtColor(img, cv2.COLOR_BGR2HLS)
HLS_img_xh = HLS_img[:, :, 0]
HLS_img_xl = HLS_img[:, :, 1]
HLS_img_xs = HLS_img[:, :, 2]

plt.subplot(4, 4, 9)
plt.imshow(HLS_img)
plt.title('HLS')

plt.subplot(4, 4, 10)
plt.imshow(HLS_img_xh, cmap= "gray")
plt.title('H')

plt.subplot(4, 4, 11)
plt.imshow(HLS_img_xl, cmap= "gray")
plt.title('L')

plt.subplot(4, 4, 12)
plt.imshow(HLS_img_xs, cmap= "gray")
plt.title('S')

YCrCb_img = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)
YCrCb_img_xY = YCrCb_img[:, :, 0]
YCrCb_img_xCr = YCrCb_img[:, :, 1]
YCrCb_img_xCb = YCrCb_img[:, :, 2]

plt.subplot(4, 4, 13)
plt.imshow(YCrCb_img)
plt.title('CrCb')

plt.subplot(4, 4, 14)
plt.imshow(YCrCb_img_xY, cmap= "gray")
plt.title('Y')

plt.subplot(4, 4, 15)
plt.imshow(YCrCb_img_xCr, cmap= "gray")
plt.title('Cr')

plt.subplot(4, 4, 16)
plt.imshow(YCrCb_img_xCb, cmap= "gray")
plt.title('Cb')

plt.show()