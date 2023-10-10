import cv2
import numpy as np
import matplotlib.pyplot as plt

img=cv2.imread("/Users/thesky/Desktop/Python/โค้ด/image_processing/473.png")
RGB_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
resize_img = cv2.resize(RGB_img, (1000, 1000))
gray_img = cv2.cvtColor(resize_img, cv2.COLOR_RGB2GRAY)

q_levels = 4
quantized_img = np.zeros(gray_img.shape, dtype=np.uint8)

for h in range(gray_img.shape[0]):
    for w in range(gray_img.shape[1]):
        pixel = gray_img[h, w]
        quantized_value = int((pixel / 255) * q_levels)
        quantized_img[h, w] = int(255 / q_levels) * quantized_value

plt.subplot(2, 2, 1)
plt.imshow(gray_img, cmap= "gray")

plt.subplot(2, 2, 2)
plt.imshow(quantized_img, cmap= "gray")

plt.show()