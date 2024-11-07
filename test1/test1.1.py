import numpy as np
import cv2
img = cv2.imread('test.png',0) #试着修改 0 为 1.
cv2.imshow('image',img)
k = cv2.waitKey(0)
if k == 27: # wait for ESC key to exit
    cv2.destroyAllWindows()
elif k == ord('s'): # wait for 's' key to save and exit
    cv2.imwrite('test2.jpg',img)
    cv2.destroyAllWindows()