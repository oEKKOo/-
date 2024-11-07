import cv2
import numpy as np
from matplotlib import pyplot as plt


img = cv2.imread('child.jpg', cv2.IMREAD_COLOR)
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
plt.subplot(221), plt.imshow(img, 'gray'), plt.title('origin')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)   #转换成灰度图片

dft = cv2.dft(np.float32(img), flags=cv2.DFT_COMPLEX_OUTPUT)  #进行傅里叶变化 
#参数说明:img表示输入的图片， cv2.DFT_COMPLEX_OUTPUT表示进行傅里叶变化的方法

fshift = np.fft.fftshift(dft) #将图像中的低频部分移动到图像的中心
rows, cols = img.shape
crow, ccol = int(rows / 2), int(cols / 2)
# 低通滤波器R
mask1 = np.zeros((rows, cols, 2), np.uint8)  #返回来一个给定形状和类型的用0填充的数组；
mask1[crow - 10:crow + 10, ccol - 10:ccol + 10] = 1
# 高通滤波器B
mask2 = np.ones((rows, cols, 2), np.uint8)   #返回一个全1的n维数组
mask2[crow - 40:crow + 40, ccol - 40:ccol + 40] = 0
# 带通滤波器G
mask3 = np.zeros((rows, cols, 2), np.uint8)
mask3[crow - 40:crow + 40, ccol -40:ccol + 40] = 1
mask3[crow - 10:crow + 10, ccol - 10:ccol + 10] = 0
# 掩膜图像和频谱图像乘积
f1 = fshift * mask1
f2 = fshift * mask2
f3 = fshift * mask3

ishift1 = np.fft.ifftshift(f1) #图像的低频和高频部分移动到图像原来的位置
iimg1 = cv2.idft(ishift1)   #傅里叶逆变换
res1 = cv2.magnitude(iimg1[:, :, 0], iimg1[:, :, 1])  #将sqrt(x^2 + y^2) 计算矩阵维度的平方根
ishift2 = np.fft.ifftshift(f2)
iimg2 = cv2.idft(ishift2)
res2 = cv2.magnitude(iimg2[:, :, 0], iimg2[:, :, 1])
ishift3 = np.fft.ifftshift(f3)
iimg3 = cv2.idft(ishift3)
res3 = cv2.magnitude(iimg3[:, :, 0], iimg3[:, :, 1])
res = cv2.merge([res2, res3, res1])   #通道合并

plt.subplot(222), plt.imshow(res1), plt.title('low')
plt.subplot(223), plt.imshow(res2), plt.title('high')
plt.subplot(224), plt.imshow(res3), plt.title('middle')
plt.show()

