import cv2
import numpy as np

# Load the image in grayscale
img = cv2.imread('flower1.tif', 0)

# Get the dimensions of the image
rows, cols = img.shape

# Create the rotation matrix: (center of rotation, angle, scale factor)
M = cv2.getRotationMatrix2D((cols / 2, rows / 2), 45, 0.6)

# Apply the affine transformation (rotation)
dst = cv2.warpAffine(img, M, (cols, rows))

# Save the result with a valid file extension (e.g., .jpg or .png)
cv2.imwrite('before.jpg', dst)

# Display the rotated image
cv2.imshow('after', dst)

# Wait for a key press and close the window
cv2.waitKey(0)
cv2.destroyAllWindows()
