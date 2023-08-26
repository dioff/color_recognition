import cv2
import numpy as np
import math

target_colors = {
    'red': {
        'min': [0, 120, 120],  # 最小阈值 [L_min, A_min, B_min]
        'max': [100, 180, 180]  # 最大阈值 [L_max, A_max, B_max]
    },
    'green': {
        'min': [0, -120, -120],  # 最小阈值 [L_min, A_min, B_min]
        'max': [100, -50, -50]  # 最大阈值 [L_max, A_max, B_max]
    }
}


cap = cv2.VideoCapture(0)


while True:
    ret, frame = cap.read()
    
    if not ret:
        break
    
    '''
    获取输入图像的高度和宽度
    img.shape返回一个包含图像高度、图像宽度以及通道数的元组
    通过切片操作[:2]来获取前两个值，即高度和宽度
    '''
    img_h, img_w = frame.shape[:2]
    # 高斯滤波,这里使用copy对图像进行拷贝
    frame_blur = cv2.GaussianBlur(np.copy(frame), (5, 5), 5)
    # 转换成Lab颜色空间
    frame_lab = cv2.cvtColor(frame_blur, cv2.COLOR_RGB2LAB)
    
    # 遍历所有要检测的颜色及其阈值
    for color_name, color in target_colors.items():
        # 二值化处理
        frame_mask = cv2.inRange(frame_lab, tuple(color['min']), tuple(color['max']))
        # 腐蚀处理
        eroded = cv2.erode(frame_mask, cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3)))
        dilated = cv2.dilate(eroded, cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3)))
        # 找出轮廓的位置
        contours = cv2.findContours(dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)[-2]
        contour_area = map(lambda c: (c, math.fabs(cv2.contourArea(c))), contours)
        contour_area = list(filter(lambda c: c[1] > 1200, contour_area))  # 去除过小的色块

        # 框出颜色的物体
        if len(contour_area) > 0:
            for contour, area in contour_area:  # Loop through all the contours found
                (center_x, center_y), r = cv2.minEnclosingCircle(contour)
                cv2.circle(frame, (int(center_x), int(center_y)), 1, (0, 255, 0), 5)
                cv2.circle(frame, (int(center_x), int(center_y)), int(r), (0, 255, 0), 2)
                
        cv2.line(frame, (int(img_w / 2 - 10), int(img_h / 2)), (int(img_w / 2 + 10), int(img_h / 2)), (0, 255, 255), 2)
        cv2.line(frame, (int(img_w / 2), int(img_h / 2 - 10)), (int(img_w / 2), int(img_h / 2 + 10)), (0, 255, 255), 2)

    cv2.imshow('frame', frame)
    
    key = cv2.waitKey(1)
    if key == 27:
        break
    
cap.release()
cv2.destroyAllWindows()