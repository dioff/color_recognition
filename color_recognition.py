import cv2
import math
import numpy as np


target_color = {
    'Green' :{
        'min':[35, 43, 46],
        'max':[77, 255, 255]
    },
    'Yellow':{
        'min':[26, 43, 46],
        'max':[34, 255, 150]
    },
    'blue':{
        'min':[100, 43, 46],
        'max':[124, 255, 255]
    }
}




# 打开摄像头
cap = cv2.VideoCapture(0)

while True:
    # 读取每一帧图像
    ret, frame = cap.read()
    
    if not ret:
        break
    
    img_h, img_w = frame.shape[:2]
    frame_gb = cv2.GaussianBlur(frame, (5, 5), 1)
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # lower_color = np.array([100, 43, 46])  # 低阈值（蓝色的范围）
    # upper_color = np.array([124, 255, 255])  # 高阈值 
    for color_name, color in target_color.items():
        
        # 二值化处理
        color_mask = cv2.inRange(hsv_frame, tuple(color['min']), tuple(color['max']))
        
        # 腐蚀膨胀处理
        eroded = cv2.erode(color_mask, cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3)))
        dilated = cv2.dilate(eroded, cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3)))
        
        # 查找轮廓
        contours = cv2.findContours(dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)[-2]
        contour_area = map(lambda c: (c, math.fabs(cv2.contourArea(c))), contours)
        contour_area = list(filter(lambda c: c[1] > 1200, contour_area))

        if len(contour_area) > 0:
                for contour, area in contour_area:  
                    # 获取最小外接圆的坐标和面积
                    (center_x, center_y), r = cv2.minEnclosingCircle(contour)
                    cv2.circle(frame, (int(center_x), int(center_y)), 1, (0, 255, 0), 5)
                    cv2.circle(frame, (int(center_x), int(center_y)), int(r), (0, 255, 0), 2)
                    cv2.putText(frame, color_name.upper(), (int(center_x), int(center_y)), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (255, 255, 255), 2)
        cv2.line(frame, (int(img_w / 2 - 10), int(img_h / 2)), (int(img_w / 2 + 10), int(img_h / 2)), (0, 255, 255), 2)
        cv2.line(frame, (int(img_w / 2), int(img_h / 2 - 10)), (int(img_w / 2), int(img_h / 2 + 10)), (0, 255, 255), 2)
    
    # # 对其进行镜像
    flipped = cv2.flip(frame, 1)
    
    # 进行显示
    cv2.imshow('binary', flipped)
    
    # 退出Esc
    
    key = cv2.waitKey(1)
    if key == 27:
        break
    
cap.release()
cv2.destroyAllWindows()