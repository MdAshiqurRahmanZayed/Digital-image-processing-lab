import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
image_path = 'test.jpg'
original_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Calculate the negative image
negative_image = 255 - original_image

# Display the original and negative images using matplotlib
plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB), cmap='gray')
plt.title('Original Image')

plt.subplot(1, 2, 2)
plt.imshow(cv2.cvtColor(negative_image, cv2.COLOR_BGR2RGB), cmap='gray')
plt.title('Negative Image')

plt.show()
