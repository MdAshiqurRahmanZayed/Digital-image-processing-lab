import cv2
import numpy as np

# Load the image
image_path = 'test.jpg'
original_image = cv2.imread(image_path, 1)

# Display the original image
cv2.imshow('Original Image', original_image)
cv2.waitKey(0)

# Convert datatype to float (for allowing fractional values)
r = original_image.astype(np.float32)

# Define the gamma value
gamma = 0.6

# Applying the Power Law Transformation
S = 255 * (r / 255) ** gamma

# Convert datatype back to uint8 for displaying
output_image = S.astype(np.uint8)

# Display the transformed image
cv2.imshow('Power Law Transformation', output_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
