"""
皮肤检测：利用皮肤颜色的HSV范围，去掉其他的区域，实现皮肤检测
"""
import numpy as np
import cv2
import glob
import matplotlib.pyplot as plt

# 定义皮肤的范围，具体自己调整
lower = np.array([0, 50, 100], dtype="uint8")
upper = np.array([25, 255, 255], dtype="uint8")

images = glob.glob("images/*.jpg")

titles = ['im1', 'im2', 'im3', 'skin1', 'skin2', 'skin3']
for i in range(len(images)):
    frame = cv2.imread(images[i], 1)  # 参数0为黑白通道
    frame = cv2.resize(frame, (400, 400))

    plt.subplot(3, 2, 2 * i + 1)
    plt.imshow(frame)
    plt.title(titles[2 * i])

    # 将BGR格式转为HSV颜色空间
    # HSV在用于指定颜色分割时，有比较大的作用
    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # 创建掩码，q低于lower或高于upper的，设置为0，在范围内设置为255
    # 这样便可以得到皮肤的像素范围
    skinMask = cv2.inRange(hsvImage, lower, upper)

    # 将掩码和原图进行“与”运算，这样原图便只保留皮肤区域
    skin = cv2.bitwise_and(frame, frame, mask=skinMask)

    plt.subplot(3, 2, 2 * i + 2)
    plt.imshow(skin)
    plt.title(titles[2 * i + 1])
plt.show()
