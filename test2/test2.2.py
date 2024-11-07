import cv2
import numpy as np
iimg=cv2.imread('woman.tif',0)
img1 = cv2.add(img,80)
img2=cv2.subtract(img,80)
cv2.imshow('img',img)
cv2.imshow('img2',img2)
cv2.waitKey(0)
cv2.destroyAllWindows()