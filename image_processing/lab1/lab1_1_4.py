import cv2
import numpy as np
import matplotlib.pyplot as plt

img=cv2.imread("/Users/thesky/Desktop/Python/โค้ด/image_processing/l_slide35-1.jpg")
RGB_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
gray_img = cv2.cvtColor(RGB_img, cv2.COLOR_BGR2GRAY)
resize_img  = cv2.resize(gray_img, (200, 200))

plt.imshow(resize_img, cmap='gray')
plt.title('2D')
x_coords, y_coords = np.mgrid[0:resize_img.shape[0], 0:resize_img.shape[1]]
# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')


ax.plot_surface(x_coords, y_coords, resize_img, cmap='gray')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('3D')

plt.show()
