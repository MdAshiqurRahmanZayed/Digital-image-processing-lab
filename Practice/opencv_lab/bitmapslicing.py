import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read the image
I = cv2.imread('test.jpg', cv2.IMREAD_GRAYSCALE)

# Get individual bitplanes
G1 = np.uint8(np.bitwise_and(I, 2**0))
G2 = np.uint8(np.bitwise_and(I, 2**1))
G3 = np.uint8(np.bitwise_and(I, 2**2))
G4 = np.uint8(np.bitwise_and(I, 2**3))
G5 = np.uint8(np.bitwise_and(I, 2**4))
G6 = np.uint8(np.bitwise_and(I, 2**5))
G7 = np.uint8(np.bitwise_and(I, 2**6))
G8 = np.uint8(np.bitwise_and(I, 2**7))

# Plot the images
plt.figure(figsize=(10, 8))

# Original Image
plt.subplot(4, 4, 1)
plt.imshow(I, cmap='gray')
plt.title('Original 8-bit Image')

# Bitplanes
for i, bitplane in enumerate([G1, G2, G3, G4, G5, G6, G7, G8], start=2):
    plt.subplot(4, 4, i)
    plt.imshow(bitplane, cmap='gray')
    plt.title(f'Bitplane {i-1}')

plt.tight_layout()
plt.show()
