# 实现低通滤波
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('test.png', 0)
i = 70

f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)

rows, cols = img.shape
print(rows, cols)
crow, ccol = int(rows/2), int(cols/2)   # 需强制转换为整数
fshift[0:crow-i, 0:cols] = 0
fshift[crow+i:rows, 0:cols] = 0
fshift[crow-i:crow+i, 0:ccol-i] = 0
fshift[crow-i:crow+i, ccol+i:cols] = 0

f_ishift = np.fft.ifftshift(fshift)
img_back = np.fft.ifft2(f_ishift)
img_back = np.abs(img_back)

plt.subplot(121), plt.imshow(img, cmap='gray'), plt.title('Original')
plt.xticks([]), plt.yticks([])

plt.subplot(122), plt.imshow(img_back, cmap='gray'), plt.title('Image after LPF')
plt.xticks([]), plt.yticks([])

plt.show()

