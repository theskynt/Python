import cv2
import numpy as np
import matplotlib.pyplot as plt

#base img
base_img = cv2.imread('/Users/thesky/Desktop/Python/โค้ด/image_processing/lab2/0mrq2i.jpg')
base_img = cv2.cvtColor(base_img, cv2.COLOR_BGR2RGB)
base_img = cv2.resize(base_img, (200, 200))


#normalize images with cv2.calcHist nbins=256
base_img_hist_red = cv2.calcHist([base_img], [0], None, [256], [0, 256])/(base_img.shape[0]*base_img.shape[1])
base_img_hist_green = cv2.calcHist([base_img], [1], None, [256], [0, 256])/(base_img.shape[0]*base_img.shape[1])
base_img_hist_blue = cv2.calcHist([base_img], [2], None, [256], [0, 256])/(base_img.shape[0]*base_img.shape[1])
#manual
cdf_red=base_img_hist_red.copy()
cdf_green=base_img_hist_green.copy()
cdf_blue=base_img_hist_blue.copy()

for i in range(1,256):
    cdf_red[i]=cdf_red[i]+cdf_red[i-1]
    cdf_green[i]=cdf_green[i]+cdf_green[i-1]
    cdf_blue[i]=cdf_blue[i]+cdf_blue[i-1]

#template
template_img = cv2.imread('/Users/thesky/Desktop/Python/โค้ด/image_processing/lab2/Beach-photography_10.jpg')
template_img = cv2.cvtColor(template_img, cv2.COLOR_BGR2RGB)
template_img = cv2.resize(template_img, (200, 200))

template_img_hist_red = cv2.calcHist([template_img], [0], None, [256], [0, 256])/(template_img.shape[0]*template_img.shape[1])
template_img_hist_green = cv2.calcHist([template_img], [1], None, [256], [0, 256])/(template_img.shape[0]*template_img.shape[1])
template_img_hist_blue = cv2.calcHist([template_img], [2], None, [256], [0, 256])/(template_img.shape[0]*template_img.shape[1])
#manual
cdf_red_temp=template_img_hist_red.copy()
cdf_green_temp=template_img_hist_green.copy()
cdf_blue_temp=template_img_hist_blue.copy()

for i in range(1,256):
    cdf_red_temp[i]=cdf_red_temp[i]+cdf_red_temp[i-1]
    cdf_green_temp[i]=cdf_green_temp[i]+cdf_green_temp[i-1]
    cdf_blue_temp[i]=cdf_blue_temp[i]+cdf_blue_temp[i-1]

#after use template to base img
#create blank numpy array
new_img_r = np.zeros(256)
new_img_g = np.zeros(256)
new_img_b = np.zeros(256)

#manual matching
for i in range(0,256):
    diff = abs(cdf_red[i]-cdf_red_temp)
    new_img_r[i] = np.argmin(diff)
    diff = abs(cdf_green[i]-cdf_green_temp)
    new_img_g[i] = np.argmin(diff)
    diff = abs(cdf_blue[i]-cdf_blue_temp)
    new_img_b[i] = np.argmin(diff)
#cdf in new image
#change the image in new image
new_img = np.zeros(base_img.shape)
for i in range(0,base_img.shape[0]):
    for j in range(0,base_img.shape[1]):
        new_img[i,j,0]=new_img_r[base_img[i,j,0]]
        new_img[i,j,1]=new_img_g[base_img[i,j,1]]
        new_img[i,j,2]=new_img_b[base_img[i,j,2]]

#histogram of new image
new_img= new_img.astype(np.uint8)
new_img_hist_red = cv2.calcHist([new_img], [0], None, [256], [0, 256])/(new_img.shape[0]*new_img.shape[1])
new_img_hist_green = cv2.calcHist([new_img], [1], None, [256], [0, 256])/(new_img.shape[0]*new_img.shape[1])
new_img_hist_blue = cv2.calcHist([new_img], [2], None, [256], [0, 256])/(new_img.shape[0]*new_img.shape[1])
#cdf of new image
cdf_red_new=new_img_hist_red.copy()
cdf_green_new=new_img_hist_green.copy()
cdf_blue_new=new_img_hist_blue.copy()

for i in range(1,256):
    cdf_red_new[i]=cdf_red_new[i]+cdf_red_new[i-1]
    cdf_green_new[i]=cdf_green_new[i]+cdf_green_new[i-1]    
    cdf_blue_new[i]=cdf_blue_new[i]+cdf_blue_new[i-1]

#show the image
plt.figure(figsize=(10,10))
plt.subplot(3,3,1);plt.imshow(base_img);plt.title("base image")
plt.subplot(3,3,2);plt.plot(base_img_hist_red,'r');plt.plot(base_img_hist_green,'g');plt.plot(base_img_hist_blue,'b');plt.title("base image histogram")
plt.subplot(3,3,3);plt.plot(cdf_red,'r');plt.plot(cdf_green,'g');plt.plot(cdf_blue,'b');plt.title("base image cdf")
plt.subplot(3,3,4);plt.imshow(template_img);plt.title("template image")
plt.subplot(3,3,5);plt.plot(template_img_hist_red,'r');plt.plot(template_img_hist_green,'g');plt.plot(template_img_hist_blue,'b');plt.title("template image histogram")
plt.subplot(3,3,6);plt.plot(cdf_red_temp,'r');plt.plot(cdf_green_temp,'g');plt.plot(cdf_blue_temp,'b');plt.title("template image cdf")
plt.subplot(3,3,7);plt.imshow(new_img.astype(np.uint8));plt.title("new image")
plt.subplot(3,3,8);plt.plot(new_img_hist_red,'r');plt.plot(new_img_hist_green,'g');plt.plot(new_img_hist_blue,'b');plt.title("new image histogram")
plt.subplot(3,3,9);plt.plot(cdf_red_new,'r');plt.plot(cdf_green_new,'g');plt.plot(cdf_blue_new,'b');plt.title("new image cdf")
plt.show()
