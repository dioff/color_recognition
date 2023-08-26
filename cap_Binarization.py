import cv2

# 打开摄像头
cap = cv2.VideoCapture(0)

while True:
    # 读取每一帧图像
    ret, frame = cap.read()
    
    if not ret:
        break
    
    # 将彩色的图像转换成为灰度图像
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # 进行二值化处理（手动选定阈值/Otsu阈值处理）
    ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    # 自定义阈值
    # img2 = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,5,3)
    
    
    # 平滑处理
    blur1 = cv2.blur(binary, (5, 5))
    blur2 = cv2.GaussianBlur(binary, (5, 5), 1)
    blur3 = cv2.medianBlur(binary, 5)
    
    # 对其进行镜像
    flipped = cv2.flip(blur3, 1)
    
    # 进行显示
    cv2.imshow('binary', flipped)
    
    # 退出Esc
    
    key = cv2.waitKey(1)
    if key == 27:
        break
    
cap.release()
cv2.destroyAllWindows()