import cv2

cap = cv2.VideoCapture(0)  # 摄像头编号
cap2 = cv2.VideoCapture('vtest.avi')

flag = True
font = cv2.FONT_HERSHEY_SIMPLEX
string = ['subtitles 1', 'subtitles 2', 'subtitles 3', '']
num = 0

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

# 创建窗口
cv2.namedWindow('frame2')

def showMessage(event, x, y, flags, param):
    global flag
    if event == cv2.EVENT_LBUTTONDOWN:
        flag = not flag

# 设置鼠标回调函数
cv2.setMouseCallback('frame2', showMessage)

while cap.isOpened() and cap2.isOpened():
    ret, frame = cap.read()
    ret2, frame2 = cap2.read()
    if ret and ret2:
        # 摄像头翻转
        frame = cv2.flip(frame, 1)

        rows1, cols1, channels1 = frame.shape
        rows, cols, channels = frame2.shape
        roi = frame2[0:rows1, 0:cols1]

        # 自身头像的截取
        framegrey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        ret, mask_front = cv2.threshold(framegrey, 110, 255, cv2.THRESH_BINARY)
        mask_inv = cv2.bitwise_not(mask_front)
        frame_fg = cv2.bitwise_and(frame, frame, mask=mask_inv)

        # 背景视频放置
        frame_bg = cv2.bitwise_and(roi, roi, mask=mask_front)
        frame_add = cv2.add(frame_fg, frame_bg)
        frame2[0:rows1, 0:cols1] = frame_add
        frame_last = frame2[0:rows1, 0:cols1]

        # 添加字幕
        num += 200
        if flag:
            num %= 3
        else:
            num = 3
        messageFrame = cv2.putText(frame_last, string[num], (200, 400), font, 1, (0, 0, 255), 2)

        # 展示并保存
        cv2.imshow('frame2', frame_last)
        # out.write(frame_last)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release everything if job is finished
cap.release()
cap2.release()
cv2.destroyAllWindows()

