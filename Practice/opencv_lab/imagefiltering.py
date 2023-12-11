import cv2
import numpy as np
from matplotlib import pyplot as plt

# Read the image
image_path = 'test.jpg'
I = cv2.imread(image_path)

# Convert image to grayscale
I = cv2.cvtColor(I, cv2.COLOR_BGR2GRAY)

# Define the filter kernel
h = np.ones((3, 3), dtype=np.float32) / 9.0

# Perform image filtering
I2 = cv2.filter2D(I, -1, h)

# Display the original and filtered images
plt.subplot(121), plt.imshow(I, cmap='gray'), plt.title('Original Image')
plt.subplot(122), plt.imshow(I2, cmap='gray'), plt.title('Filtered Image')
plt.show()
