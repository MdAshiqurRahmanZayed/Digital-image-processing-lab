import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read the image
I = cv2.imread('/home/mrzd/Desktop/Study/CSTE42/Digital Image Processing/lab/Practice/opencv_lab/test.jpg')

# Convert the image to grayscale
I_gray = cv2.cvtColor(I, cv2.COLOR_BGR2GRAY)

# Get the histogram using numpy
histogram, bins = np.histogram(I_gray.flatten(), bins=256, range=[0, 256])

# Plot the histogram
plt.figure()
plt.bar(bins[:-1], histogram, width=1)
plt.title('Histogram of Grayscale Image')
plt.xlabel('Pixel Intensity')
plt.ylabel('Frequency')
plt.show()
