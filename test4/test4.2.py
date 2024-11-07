import cv2
import numpy as np
from matplotlib import pyplot as plt

# Load the image
img = cv2.imread('flower3.jpg')

# Define the color channels (blue, green, red)
color = ('b', 'g', 'r')

# Iterate over each color channel using enumerate for index and color
for i, col in enumerate(color):
    # Calculate the histogram for each color channel
    histr = cv2.calcHist([img], [i], None, [256], [0, 256])
    
    # Plot the histogram
    plt.plot(histr, color=col)
    plt.xlim([0, 256])

# Display the plot outside the loop
plt.show()
