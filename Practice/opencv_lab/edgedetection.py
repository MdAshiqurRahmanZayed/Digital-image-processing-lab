import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read the image
I = cv2.imread('test.jpg')
I = cv2.cvtColor(I, cv2.COLOR_BGR2GRAY)

# Edge detection using different filters
sEdge = cv2.Sobel(I, cv2.CV_64F, 1, 1, ksize=3)
prEdge = cv2.Prewitt(I, cv2.CV_64F)
roEdge = cv2.Roberts(I, cv2.CV_64F)

# Plotting the results
plt.figure(figsize=(10, 8))

plt.subplot(2, 2, 1)
plt.imshow(I, cmap='gray')
plt.title('Original Image')

plt.subplot(2, 2, 2)
plt.imshow(np.abs(sEdge), cmap='gray')
plt.title('Sobel')

plt.subplot(2, 2, 3)
plt.imshow(np.abs(prEdge), cmap='gray')
plt.title('Prewitt')

plt.subplot(2, 2, 4)
plt.imshow(np.abs(roEdge), cmap='gray')
plt.title('Roberts')

plt.show()
