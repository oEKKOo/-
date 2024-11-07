import cv2
import numpy as np

# Load the image
img = cv2.imread('flower.jpg')

# Resize the image using scale factors
# None is used for the output size because we are specifying scaling factors (fx, fy)
res = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)

# OR you can directly set the size of the output image
height, width = img.shape[:2]
res = cv2.resize(img, (2 * width, 2 * height), interpolation=cv2.INTER_CUBIC)

# Loop to display the images
while(1):
    cv2.imshow('res', res)
    cv2.imshow('img', img)
    
    # Press 'Esc' (ASCII 27) to exit the loop
    if cv2.waitKey(1) & 0xFF == 27:
        break

# Destroy all windows when finished
cv2.destroyAllWindows()
