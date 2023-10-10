import cv2
import numpy as np

original_image = cv2.imread("/Users/thesky/Desktop/Python/โค้ด/image_processing/lab2/bodhi.jpg")
input_image = cv2.resize(original_image, (200, 200))


# Grammar Var
num_images = 20
a_values = np.linspace(0.1, 2, num_images)
b = 0
bit_depth = 8

output_filename = 'output_video5.mp4'
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(output_filename, fourcc, 1, input_image.shape[:2][::-1])

# Apply gamma adjustments and create the video
for a in a_values:
    gamma_adjusted = (input_image / 255.0) ** a * 255
    gamma_adjusted[gamma_adjusted < 0] = 0
    gamma_adjusted[gamma_adjusted > 255] = 255
    adjusted_image = gamma_adjusted.astype(np.uint8)
    out.write(adjusted_image)


out.release()
