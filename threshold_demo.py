import cv2

# 读取照片
img=cv2.imread('test.jpg')

# 将彩色图片转换成灰度图片
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# 使用阈值对灰度图片进行二值化处理
# 阈值是指将灰度值小于阈值的像素设置为0（黑色）
# 灰度值大于等于阈值的像素设置为255（白色）
ret, img2 = cv2.threshold(img_gray, 135, 255, cv2.THRESH_BINARY)

# #这里阈值为127
# #maxval设为255，所以处理后的图像是黑白图像
cv2.imshow("BINARY", img2)
cv2.waitKey(0)    
cv2.destroyAllWindows()
