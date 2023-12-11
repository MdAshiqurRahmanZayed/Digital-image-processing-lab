import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read the image
I = cv2.imread('test.jpg', cv2.IMREAD_GRAYSCALE)

# Convert datatype to Double
# (for allowing fractional values)
r = I.astype(np.float64)

# Constant determining the
# nature of the log curve
C = 1

# Performing log transformation
S = C * np.log1p(r)  # np.log1p(x) calculates log(1 + x) for each element of x
T = 255 / (C * np.log(1 + 255))

# Scaling the result to the range [0, 255]
B = (T * S).clip(0, 255).astype(np.uint8)

# Display the original and transformed images
plt.figure()
plt.subplot(121), plt.imshow(cv2.cvtColor(I, cv2.COLOR_BGR2RGB)), plt.title('Original Image')
plt.subplot(122), plt.imshow(B, cmap='gray'), plt.title('Log Transformation')
plt.show()
