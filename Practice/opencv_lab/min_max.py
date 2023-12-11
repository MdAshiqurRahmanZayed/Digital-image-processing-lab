import cv2
import numpy as np

# Read the image
image_path = 'test.jpg'
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Get the size of the image
rows, cols = image.shape

# Initialize variables
min_val = float(image[0, 0])
max_val = float(image[0, 0])
sum_vals = float(image[0, 0])

# Iterate through each pixel
for i in range(rows):
    for j in range(cols):
        pixel_value = float(image[i, j])

        # Update min and max values
        min_val = min(min_val, pixel_value)
        max_val = max(max_val, pixel_value)

        # Accumulate values for average calculation
        sum_vals += pixel_value

# Calculate average value
avg_val = sum_vals / (rows * cols)

# Display the results
print(f'Minimum Value: {min_val}')
print(f'Maximum Value: {max_val}')
print(f'Average Value: {avg_val}')
