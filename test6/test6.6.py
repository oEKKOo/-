import cv2
import numpy as np

# Load the noisy image
img = cv2.imread('noisy.tif', 0)

# Apply Gaussian blur
blur = cv2.GaussianBlur(img, (5,5), 0)

# Calculate the normalized histogram
hist = cv2.calcHist([blur], [0], None, [256], [0, 256])
hist_norm = hist.ravel() / hist.max()

# Cumulative sum of the normalized histogram
Q = hist_norm.cumsum()

# Initialize variables for Otsu's method
bins = np.arange(256)
fn_min = np.inf
thresh = -1

# Otsu's threshold calculation
for i in range(1, 256):
    p1, p2 = np.hsplit(hist_norm, [i])  # probabilities
    q1, q2 = Q[i], Q[255] - Q[i]  # cumulative sum of classes
    b1, b2 = np.hsplit(bins, [i])  # class intervals
    
    # Means and variances for each class
    m1, m2 = np.sum(p1 * b1) / q1, np.sum(p2 * b2) / q2
    v1, v2 = np.sum(((b1 - m1) ** 2) * p1) / q1, np.sum(((b2 - m2) ** 2) * p2) / q2
    
    # Minimization function
    fn = v1 * q1 + v2 * q2
    
    # Find the threshold with the minimum value of the function
    if fn < fn_min:
        fn_min = fn
        thresh = i

# Otsu's threshold value using OpenCV
ret, otsu = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# Output the thresholds
print(f"Otsu's threshold (manual): {thresh}")
print(f"Otsu's threshold (OpenCV): {ret}")
