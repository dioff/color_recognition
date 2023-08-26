import cv2


image_path = '/home/liu/Desktop/opencv/img.png'
image = cv2.imread(image_path)
'''
使用opencv画线
cv2.line(image, pt1, pt2, color, thickness)
image: 是要在其上绘制线条的图像
pt1: 线的开始坐标，(x,y)
pt2: 线的结束坐标，(x,y)
color:它是要绘制的线条的颜色。对于 BGR,我们通过一个元组。例如：(255，0，
0)为蓝色
thickness:线条的粗细
'''
cv2.line(image, (100, 100), (100, 200), (255, 0, 0), 5)
cv2.imwrite('line.png', image)
'''
画矩形
函数格式：cv2.rectangle(image,pt1,pt2,color,thickness)。
1) image：它是要在其上绘制矩形的图像。
2) pt1：矩形框的一个顶点坐标，是一个包含两个数字的元组，表示(x, y)。
3) pt2：pt1 的对角线顶点坐标，类型同 pt1。
4) color：它是要绘制的矩形的颜色。对于 BGR，我们通过一个元组。例如：(255，0，
0)为蓝色。
5)
thickness：线宽，数值越大表示线宽越宽；如果取值为负数或者 cv2.FILLED，那
么将画一个填充的矩形

'''