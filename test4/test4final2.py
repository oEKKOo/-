#B、G、R空间逐一做均衡化处理
import cv2
import numpy as np

img = cv2.imread('Fig6.png')
#分离
(b, g, r) = cv2.split(img)
beq = cv2.equalizeHist(b)
geq = cv2.equalizeHist(g)
req = cv2.equalizeHist(r)
# 合并每一个通道
result1 = cv2.merge((beq, g, r))
result2 = cv2.merge((b, geq, r))
result3 = cv2.merge((b, g, req))

cv2.imshow('image', img)
cv2.imshow('image1', result1)
cv2.imshow('image2', result2)
cv2.imshow('image3', result3)
cv2.waitKey(0)

