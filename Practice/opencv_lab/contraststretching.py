import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read the image
I = cv2.imread('test.jpg', cv2.IMREAD_GRAYSCALE)

# Make a copy for the result
G = np.copy(I)

# Get the image dimensions
rows, cols = I.shape

# User input for parameters
T1 = float(input('Enter value of t1 (Threshold 1): '))
T2 = float(input('Enter value of t2 (Threshold 2): '))
s1 = float(input('Enter value of slope 1: '))
s2 = float(input('Enter value of slope 2: '))
s3 = float(input('Enter value of slope 3: '))

# Calculate coefficients
coeffT1 = s1 * T1
coeffT2 = s2 * (T2 - T1) + coeffT1

# Contrast stretching
for i in range(rows):
    for j in range(cols):
        if I[i, j] < T1:
            G[i, j] = np.floor(s1 * I[i, j])
        elif T1 <= I[i, j] < T2:
            G[i, j] = np.floor(s2 * (I[i, j] - T1) + coeffT1)
        elif I[i, j] >= T2:
            G[i, j] = np.floor(s3 * (I[i, j] - T2) + coeffT2)

# Display original and stretched images
plt.figure()
plt.subplot(2, 1, 1), plt.imshow(I, cmap='gray'), plt.title('Original Image')
plt.subplot(2, 1, 2), plt.imshow(G, cmap='gray'), plt.title(
    f"Result of Contrast Stretching\nT1={T1}, T2={T2}, s1={s1}, s2={s2}, s3={s3}")
plt.show()

# Display histograms
plt.figure()
plt.subplot(2, 1, 1), plt.hist(I.flatten(), bins=256, range=[0, 256], color='r'), plt.title('Histogram for Original Image')
plt.subplot(2, 1, 2), plt.hist(G.flatten(), bins=256, range=[0, 256], color='b'), plt.title(
    f"Histogram for Contrast Stretching\nT1={T1}, T2={T2}, s1={s1}, s2={s2}, s3={s3}")
plt.show()
