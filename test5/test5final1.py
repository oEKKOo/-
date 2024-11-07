import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('lena.bmp')
median3 = cv2.medianBlur(img,5)
median5 = cv2.medianBlur(img,5)
median7 = cv2.medianBlur(img,5)
plt.subplot(221),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(222),plt.imshow(median3),plt.title('median3*3')
plt.xticks([]), plt.yticks([])
plt.subplot(223),plt.imshow(median5),plt.title('median5*5')
plt.xticks([]), plt.yticks([])
plt.subplot(224),plt.imshow(median7),plt.title('median7*7')
plt.xticks([]), plt.yticks([])
plt.show()