import cv2
import numpy as np

original_image = cv2.imread("/Users/thesky/Desktop/Python/โค้ด/image_processing/lab2/bodhi.jpg")
resize_img1 = cv2.resize(original_image, (200, 200))

a_values = np.linspace(0.5, 2.0, 20)
b_values = np.linspace(-100, 100, 20)
y_values = 2
bit = 8

width, height = resize_img1.shape[1], resize_img1.shape[0]
frame_rate = 1

video_writer = cv2.VideoWriter('output.mp4', cv2.VideoWriter_fourcc(*'mp4v'), frame_rate, (width, height))

# คำนวณค่าสีในภาพใหม่ตามสมการ g(x, y) = af(x, y)^g + b และเขียนภาพลงในไฟล์วิดีโอ
for a in a_values:
    for b in b_values:
        new_image = np.zeros_like(resize_img1)

        # คำนวณค่าสีในภาพใหม่ตามสมการ g(x, y) = af(x, y)^g + b
        for x in range(resize_img1.shape[0]):
            for y in range(resize_img1.shape[1]):
                for c in range(resize_img1.shape[2]):
                    new_value = a * (resize_img1[x, y, c]**y_values) + b

                    if bit >= 8:
                        new_value = (new_value - np.min(new_value)) / (np.max(new_value) - np.min(new_value))
                        new_value = new_value * 255  # Adjusted to normalize to [0, 255]

                    new_image[x, y, c] = new_value

        new_image = np.clip(new_image, 0, 255).astype(np.uint8)  # Ensure values are within [0, 255]
        video_writer.write(new_image)

video_writer.release()
