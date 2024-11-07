import numpy as np
import cv2
import math
from matplotlib import pyplot as plt


def hisEqulColor(img):
    hls = cv2.cvtColor(img, cv2.COLOR_BGR2HLS)
    channels = cv2.split(hls)
    cv2.equalizeHist(channels[1])
    cv2.merge(channels, hls)
    cv2.cvtColor(hls, cv2.COLOR_HLS2BGR, img)
    return img


img = cv2.imread('Fig6.png')
eq = hisEqulColor(img)
cv2.imshow('image1', img)
cv2.imshow('image2', eq)
cv2.waitKey(0)

