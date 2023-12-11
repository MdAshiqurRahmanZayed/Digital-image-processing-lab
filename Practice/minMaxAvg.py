import cv2
import numpy as np

# Load the image
I = cv2.imread('./image/onion.png')

# Convert to grayscale
I = cv2.cvtColor(I, cv2.COLOR_BGR2GRAY)

# Calculate the minimum, maximum, and average intensity values
min_val = np.min(I)
max_val = np.max(I)
avg_val = np.mean(I)

print(f"Min Value: {min_val}")
print(f"Max Value: {max_val}")
print(f"Average Value: {avg_val}")
