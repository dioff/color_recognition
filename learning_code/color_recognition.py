import cv2
import numpy as np

def color_detection(frame):
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    lower_color = np.array([25, 50, 50])  # 低阈值（蓝色的范围）
    upper_color = np.array([130, 255, 255])  # 高阈值
    
    color_mask = cv2.inRange(hsv_frame, lower_color, upper_color)
    
    contours, _ = cv2.findContours(color_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    
    return frame

# 打开摄像头
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    processed_frame = color_detection(frame)
    
    cv2.imshow("Color Detection", processed_frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
