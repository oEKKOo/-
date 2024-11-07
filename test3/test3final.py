import cv2
import numpy as np

# 当鼠标按下时变为True
ix1, iy1 = -1, -1
ix2, iy2 = -1, -1
ix3, iy3 = -1, -1
ix4, iy4 = -1, -1


# 创建回调函数
def draw_circle(event, x, y, flags, param):
    global ix1, iy1, ix2, iy2, ix3, iy3, ix4, iy4
    # 当按下左键是返回位置坐标
    if event == cv2.EVENT_LBUTTONDOWN:
        if ix1 == -1:
            ix1, iy1 = x, y
            cv2.circle(img, (x, y), 2, (255, 255, 255), -1)
        elif ix2 == -1:
            ix2, iy2 = x, y
            cv2.circle(img, (x, y), 2, (255, 255, 255), -1)
        elif ix3 == -1:
            ix3, iy3 = x, y
            cv2.circle(img, (x, y), 2, (255, 255, 255), -1)
        elif ix4 == -1:
            ix4, iy4 = x, y
            cv2.circle(img, (x, y), 2, (255, 255, 255), -1)


img = cv2.imread('drawing.png')
cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_circle)
while 1:
    cv2.imshow('image', img)
    k = cv2.waitKey(1) & 0xFF
    if ix4 != -1:
        break
cv2.imshow('image', img)
#cv2.getAffineTransform 会创建一个2x3 的矩阵，最后这个矩阵会被传给函数cv2.warpAffine。
src_point = np.float32([[ix1, iy1], [ix2, iy2], [ix3, iy3], [ix4, iy4]])
dst_point = np.float32([[0, 0], [0, 300], [300, 300], [300, 0]])
h = cv2.getPerspectiveTransform(src_point, dst_point)  #通过一一对应的点，计算映射矩阵，进行变换
res = cv2.warpPerspective(img, h, (300, 300))   
#cv2.warpPerspective(src, M, dsize[, dst[, flags[, borderMode[, borderValue]]]]) → dst
#src：输入图像
# M：变换矩阵 dsize：目标图像shape flags：插值方式，interpolation方法INTER_LINEAR或INTER_NEAREST
#borderMode：边界补偿方式，BORDER_CONSTANT or BORDER_REPLICATE
#borderValue：边界补偿大小，常值，默认为0
cv2.imshow('output', res)
cv2.waitKey(0)
cv2.destroyAllWindows()

