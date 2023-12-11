import cv2
import matplotlib.pyplot as plt
import numpy as np

# Read the image
I = cv2.imread('test.jpg')

# Get the dimensions of the image
height, width, planes = I.shape

# Reshape the image to a 2D array for visualization
rgb = np.reshape(I, (height, width * planes))

# Display the reshaped image
plt.imshow(rgb)
plt.axis('off')  # Turn off axis labels
plt.show()
