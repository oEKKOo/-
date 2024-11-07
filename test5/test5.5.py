import cv2
import numpy as np
from matplotlib import pyplot as plt

# Load the image in grayscale
img = cv2.imread('messigray.jpg', 0)

# Perform 2D FFT on the image
f = np.fft.fft2(img)

# Shift the zero frequency component to the center
fshift = np.fft.fftshift(f)

# Get the dimensions of the image
rows, cols = img.shape

# Calculate the center of the image (casting to integers)
crow, ccol = int(rows / 2), int(cols / 2)

# Apply high-pass filter by zeroing out a square region in the center
fshift[crow-30:crow+30, ccol-30:ccol+30] = 0

# Shift the zero frequency component back
f_ishift = np.fft.ifftshift(fshift)

# Perform inverse FFT to get the image back
img_back = np.fft.ifft2(f_ishift)

# Take the absolute value to get the real part of the image
img_back = np.abs(img_back)

# Plot the original and processed images
plt.subplot(131), plt.imshow(img, cmap='gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])

plt.subplot(132), plt.imshow(img_back, cmap='gray')
plt.title('Image after HPF'), plt.xticks([]), plt.yticks([])

plt.subplot(133), plt.imshow(img_back, cmap='jet')
plt.title('Result in JET'), plt.xticks([]), plt.yticks([])

# Show the images
plt.show()
