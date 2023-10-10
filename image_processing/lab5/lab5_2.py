import matplotlib.pyplot as plt
import numpy as np
import cv2
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# Define Gaussian noise function
def add_gaussian_noise(img):
    mean = 0
    sigma = 25  # You can adjust the standard deviation as needed
    noisy_img = img + np.random.normal(mean, sigma, img.shape)
    noisy_img = np.clip(noisy_img, 0, 255)  # Clip values to stay within [0, 255] range
    noisy_img = noisy_img.astype('uint8')  # Convert back to uint8
    return noisy_img

# Define parameters
Npic = 100  # Number of augmented images to generate
rotation_range = 40
width_shift_range = 0.2
height_shift_range = 0.2
shear_range = 0.2
zoom_range = 0.2
horizontal_flip = True
fill_mode = ['constant', 'nearest', 'reflect', 'wrap']

#import image
img = cv2.imread('/Users/thesky/Desktop/Python/โค้ด/image_processing/lab5/bodhi.jpg')
cv2.resize((cv2.cvtColor((img), cv2.COLOR_BGR2RGB)), (100, 100))


# Create a VideoWriter object to save the images as a video
output_file = 'output_video_3.mp4'
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Video codec (you can change this as needed)
fps = 1.0  # Frames per second
frame_size = (img.shape[1], img.shape[0])  # Use the size of the input image
out = cv2.VideoWriter(output_file, fourcc, fps, frame_size)


# Define ImageDataGenerator with parameters
datagen = ImageDataGenerator(
    rotation_range=rotation_range,
    width_shift_range=width_shift_range,
    height_shift_range=height_shift_range,
    shear_range=shear_range,
    zoom_range=zoom_range,
    horizontal_flip=horizontal_flip,
    preprocessing_function=add_gaussian_noise,
    fill_mode=fill_mode[2]
)

# Creates our batch of one image
img = np.expand_dims(img, axis=0)  # Add batch dimension
pic = datagen.flow(img, batch_size=1)

#Create Folder
# os.makedirs('augmented_images', exist_ok=True)

# Randomly generate transformed images and write them to the video file
for i in range(1, Npic):
    batch = pic.next()
    im_result = batch[0].astype('uint8')
    
    # Write the transformed image to the video file
    out.write(im_result)

# Release the VideoWriter object
out.release()