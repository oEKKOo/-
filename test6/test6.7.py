import cv2
import numpy as np

# Load the image (using the provided file)
img = cv2.imread('picture1.png')

# Convert the image to HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Define blue color range in HSV
lower_blue = np.array([110, 50, 50])
upper_blue = np.array([130, 255, 255])

# Create a mask to detect blue regions
mask = cv2.inRange(hsv, lower_blue, upper_blue)

# Perform morphological operations to reduce noise
kernel = np.ones((5, 5), np.uint8)
mask = cv2.erode(mask, kernel, iterations=1)
mask = cv2.dilate(mask, kernel, iterations=2)

# Find contours (to detect the object shape)
contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Draw a circle around the largest blue object detected
if len(contours) > 0:
    # Find the largest contour
    max_contour = max(contours, key=cv2.contourArea)
    # Get the center and radius of the minimum enclosing circle
    (x, y), radius = cv2.minEnclosingCircle(max_contour)
    center = (int(x), int(y))
    radius = int(radius)
    # Draw the circle
    cv2.circle(img, center, radius, (0, 255, 0), 2)

# Show the result
cv2.imshow('Original Image', img)
cv2.imshow('Mask', mask)

cv2.waitKey(0)
cv2.destroyAllWindows()
