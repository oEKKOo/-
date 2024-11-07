# 实现读取视频文件，显示视频文件
# 实现鼠标点击开关字幕
import cv2

cap = cv2.VideoCapture('vtest.avi')     # 打开视频文件

font = cv2.FONT_HERSHEY_SIMPLEX     # 设置字幕字体
flag = True                         # 标识字幕开关与否


# 鼠标处理函数
# 如果监听到按键，则将字幕状态取非
def caption(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        global flag
        flag = not flag


# 创建一个窗口，并将鼠标处理函数绑定到该窗口
cv2.namedWindow('frame')
cv2.setMouseCallback('frame', caption)


while cap.isOpened():
    ret, frame = cap.read()     # 读取一幅图片
    if ret:
        # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # 显示灰度图片
        if flag:        # 根据flag的状态决定是否要显示字幕
            cv2.putText(frame, 'Here are the subtitles', (10, 500), font, 2, (255, 255, 255), 2, cv2.LINE_AA)
            # 参数注释： 窗口    输出字符串                坐标       字体  字号    颜色         粗细   线条类型
        cv2.imshow('frame', frame)
    if cv2.waitKey(50) & 0xFF == ord('q'):
        # 用waitKey调整视频播放速度
        break
    
cap.release()
cv2.destroyAllWindows()

