import cv2
import numpy as np
import pylab as pl


im_dst = cv2.imread('dest.jpg')     #读取标准图像
pts_dst = []                        #存储标准图像特征点坐标
pts_src = []                        #存储源图像特征点坐标
a = []                              #暂存鼠标在图像上点击的坐标


def on_EVENT_LBUTTONDOWN(event, x, y, flags, param):   #获取鼠标在图像上点击的坐标
    if event == cv2.EVENT_LBUTTONDOWN:
        xy = "%d,%d" % (x, y)
        cv2.circle(img, (x, y), 1, (0, 0, 255), thickness=-1)
        cv2.putText(img, xy, (x, y), cv2.FONT_HERSHEY_PLAIN,
                    1.0, (0, 0, 0), thickness=1)
        cv2.imshow("Mark feature points", img)
        a.append((x, y))      #貌似on_EVENT_LBUTTONDOWN函数无法返回列表a，故定义全局列表a暂存鼠标点击坐标

def feature_point(pts):   #获取特征点坐标
    cv2.namedWindow("Mark feature points")
    cv2.setMouseCallback("Mark feature points", on_EVENT_LBUTTONDOWN)
    cv2.imshow("Mark feature points", img)
    cv2.waitKey(0)
    pts = np.copy(a)
    pts = np.array(pts)
    return pts

def homograph(pts_src, i):     #计算单应矩阵，并输出投影后的图像
    p, status = cv2.findHomography(pts_src, pts_dst)
    im_out = cv2.warpPerspective(im_src, p, (im_dst.shape[1], im_dst.shape[0]))
    print('\nimg'+str(i)+'的投影矩阵为：\n', p)
    cv2.imshow("Processed img", im_out)
    print('回车计算下一张图片')
    cv2.waitKey(0)



img = im_dst    #貌似上述on_EVENT_LBUTTONDOWN函数无法传参img，只能定义全局变量img
print('请在目标图上至少标出4个特征点')
pts_dst = feature_point(pts_dst)
print('目标图特征点坐标为：\n', pts_dst)

for i in range(6):       #依次计算六张源图片的单应矩阵，并投影
    a.clear()           #清空上次暂存数据
    im_src = cv2.imread('img'+str(i)+'.jpg')
    img = im_src
    print('\n请在源图img'+str(i)+'上按顺序标出对应的特征点')
    pts_src = feature_point(pts_src)
    print('img'+str(i)+'的特征点坐标为：\n', pts_src)
    homograph(pts_src, i)