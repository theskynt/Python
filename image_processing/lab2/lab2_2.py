import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("/Users/thesky/Desktop/Python/โค้ด/image_processing/lab2/bodhi.jpg")

#convert to RGB
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

imgEH_R = cv2.equalizeHist(img[:,:,0])
imgEH_G = cv2.equalizeHist(img[:,:,1])
imgEH_B = cv2.equalizeHist(img[:,:,2])

imgEH = cv2.merge((imgEH_R, imgEH_G, imgEH_B))
OGimg_hist_R = (cv2.calcHist([img], [0], None, [256], [0, 256])/(imgEH.shape[0]*imgEH.shape[1]))
OGimg_hist_G = (cv2.calcHist([img], [1], None, [256], [0, 256])/(imgEH.shape[0]*imgEH.shape[1]))
OGimg_hist_B = (cv2.calcHist([img], [2], None, [256], [0, 256])/(imgEH.shape[0]*imgEH.shape[1]))


R_hist = (cv2.calcHist([imgEH], [0], None, [256], [0, 256])/(imgEH.shape[0]*imgEH.shape[1]))
G_hist = (cv2.calcHist([imgEH], [1], None, [256], [0, 256])/(imgEH.shape[0]*imgEH.shape[1]))
B_hist = (cv2.calcHist([imgEH], [2], None, [256], [0, 256])/(imgEH.shape[0]*imgEH.shape[1]))

plt.figure(figsize=(20, 10))
plt.subplot(2, 2, 1)
plt.imshow(img)
plt.title('Original Image')

plt.subplot(2, 2, 2)
plt.plot(OGimg_hist_R, color='r')
plt.plot(OGimg_hist_G, color='g')
plt.plot(OGimg_hist_B, color='b')
plt.title('Original Image Histogram')

plt.subplot(2, 2, 3)
plt.imshow(imgEH)
plt.title('Equalized Image')

plt.subplot(2, 2, 4)
plt.plot(R_hist, color='r')
plt.plot(G_hist, color='g')
plt.plot(B_hist, color='b')
plt.title('Equalized Image Histogram')

plt.show()