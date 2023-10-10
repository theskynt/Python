import cv2
import numpy as np
import matplotlib.pyplot as plt

img_1=cv2.imread("/Users/thesky/Desktop/Python/โค้ด/image_processing/lab1/473.png")
RGB_img1 = cv2.cvtColor(img_1, cv2.COLOR_BGR2RGB)
img_2=cv2.imread("/Users/thesky/Desktop/Python/โค้ด/image_processing/lab1/l_slide35-1.jpg")
RGB_img2 = cv2.cvtColor(img_2, cv2.COLOR_BGR2RGB)
resize_img1 = cv2.resize(RGB_img1, (200, 200))
resize_img2 = cv2.resize(RGB_img2, (200, 200))

output_file = "output_file.mp4"
fourcc = cv2.VideoWriter_fourcc(*'mp4v')

fps = 1
frame = 100
trans_duration = 30

out = cv2.VideoWriter(output_file, fourcc, fps, (resize_img1.shape[1], resize_img1.shape[0]))

w = [1.0, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1, 0]


#Move IMG 1 to IMG 2
for w1, w2 in zip(w, w[::-1]):
    image_result = cv2.addWeighted(resize_img1, w1, resize_img2, w2, 0)
    out.write(image_result)
    
#MOVE iMG2 TO IMG1
for w2, w1 in zip(w, w[::-1]):
    image_result = cv2.addWeighted(resize_img1, w1, resize_img2, w2, 0)
    out.write(image_result)


out.release()