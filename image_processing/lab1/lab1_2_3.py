import cv2
import numpy as np
import matplotlib.pyplot as plt

img=cv2.imread("/Users/thesky/Desktop/Python/โค้ด/image_processing/lab1/473.png")
RGB_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.subplot(1, 3, 1)
plt.imshow(RGB_img)
plt.title('Original')

height, width = RGB_img.shape[:2]

mask = np.zeros((height, width), dtype=np.uint8)

cv2.rectangle(mask, (400, 450), (900, 100), 255, -1)
plt.subplot(1, 3, 2)
plt.imshow(mask)
plt.title('Image Mask')

masked_image = cv2.bitwise_and(RGB_img, RGB_img, mask=mask)
plt.subplot(1, 3, 3)
plt.imshow(masked_image)
plt.title('Bitwise_AND() result')

plt.show()